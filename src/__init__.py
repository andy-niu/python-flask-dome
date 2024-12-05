from flask import Flask
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from datetime import datetime
sys.path.append('./src')
import config
#from models import Article
import os


db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
        
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    app.config.from_object(config)
    # # register the database commands
    # from database import init_db
    # init_db()

    db.init_app(app)
    migrate.init_app(app, db)

    # register the blueprint
    from . import program

    app.register_blueprint(program.bp)

    app.add_url_rule('/', endpoint='index')

    return app