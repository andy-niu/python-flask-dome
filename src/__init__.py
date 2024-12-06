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
    init_app(app)
    # db.init_app(app)
    # from models import Article,User,Navigation,NavigationPosition
    # migrate.init_app(app, db)
    # with app.app_context():
    #     migrate.db.metadata.create_all(bind=db.engine)
    init_data(app)

    # register the blueprint
    from . import program
    app.register_blueprint(program.bp)

    app.add_url_rule('/', endpoint='index')

    return app

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    from models import Article,User,Navigation,NavigationPosition
    with app.app_context():
        migrate.db.metadata.create_all(bind=db.engine)

def init_data(app):
    from models import User, Navigation, NavigationPosition
    from config import ADMIN_EMAIL, ADMIN_PASSWORD
    with app.app_context():
        user = User.query.filter_by(email=ADMIN_EMAIL).first()
        if not user:
            user = User(email=ADMIN_EMAIL, password=ADMIN_PASSWORD,name='admin', is_admin=True)
            db.session.add(user)
            user = User(email='andy@andy.cc', password='pass@1',name='Andy', is_admin=False)
            db.session.add(user)
            db.session.commit()
        navs = Navigation.query.all()
        if not navs:
            nav = Navigation(title='首页', position=NavigationPosition.Home.name, url='/')
            db.session.add(nav)
            nav = Navigation(title='文章', position=NavigationPosition.Home.name, url='/article')
            db.session.add(nav)
            db.session.commit()