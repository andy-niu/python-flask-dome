from flask import jsonify
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
from models import Navigation,User,Article,NavigationPosition
import sys
from src import db
import json

sys.path.append('./src')
bp = Blueprint("program", __name__)

@bp.route('/')
def index():
    # model = Navigation(title="Home", url="/",position=NavigationPosition.Home.name)
    data = Navigation.query.all()
    print(data)
    return jsonify([nav.serialize() for nav in data])