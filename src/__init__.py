from flask import Flask
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
sys.path.append('./src')
#import config
from flask_wtf import FlaskForm, CSRFProtect
import os

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

# app = Flask(__name__)
# app.config.from_object(config)
# db = SQLAlchemy(app)
# from models import Article,User,Navigation,NavigationPosition
# migrate = Migrate(app, db)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # load the config
    app.config.from_object('config')
    #print('SQLALCHEMY_DATABASE_URI: ',app.config['SQLALCHEMY_DATABASE_URI'])
    csrf.init_app(app)
    Bootstrap5(app)

    # init the database
    init_db(app)
    # db.init_app(app)
    # from models import Article,User,Navigation,NavigationPosition
    # migrate.init_app(app, db)
    # with app.app_context():
    #     migrate.db.metadata.create_all(bind=db.engine)
    init_data(app)

    # register the blueprint
    from . import program
    from . import webapi
    app.register_blueprint(program.bp)
    app.register_blueprint(webapi.bp)

    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/article', endpoint='article')
    app.add_url_rule('/article/<int:article_id>', endpoint='view_article')
    app.add_url_rule('/article/create', endpoint='create_article')
    app.add_url_rule('/article/<int:article_id>/edit', endpoint='edit_article')
    app.add_url_rule('/article/<int:article_id>/remove', endpoint='remove_article')

    return app

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)
    from models import Article,User,Navigation,NavigationPosition
    with app.app_context():
        migrate.db.metadata.create_all(bind=db.engine)

def init_data(app):
    from models import User, Navigation, NavigationPosition, Article
    from config import ADMIN_EMAIL, ADMIN_PASSWORD
    with app.app_context():
        user = User.query.filter_by(email=ADMIN_EMAIL).first()
        if not user:
            db.session.add(User(email=ADMIN_EMAIL, password=ADMIN_PASSWORD,name='admin', is_admin=True))
            db.session.add(User(email='andy@andy.cc', password='pass@1',name='Andy', is_admin=False))
            db.session.commit()
        navs = Navigation.query.all()
        if not navs:
            db.session.add(Navigation(title='首页', position=NavigationPosition.Home.name, url='/'))
            db.session.add(Navigation(title='文章', position=NavigationPosition.Home.name, url='/article'))
            db.session.commit()
        navs = Article.query.all()
        if not navs:
            db.session.add(Article(title='Hello World', content='this is test context!', author="andy"))
            for i in range(10):
                db.session.add(Article(title='This is Test'+str(i), content='this is test context!', author="test"+str(i)))
            db.session.commit()
            