from flask import Flask
from markupsafe import escape
from flask import Blueprint
from flask import request, jsonify
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
from flask import g
from werkzeug.exceptions import abort
from database import db_session
from models import Navigation,User,Article,NavigationPosition
from src import db


app = Flask(__name__)
bp = Blueprint("program", __name__)


@bp.route('/')
def index():
    model = Navigation(title="Home", url="/",position=NavigationPosition.Home.name)
    db_session.add(model)
    db_session.commit()
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)