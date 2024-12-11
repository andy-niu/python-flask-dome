import sys
from flask import Blueprint, jsonify, request
from src import db
from models import Navigation,User,Article,NavigationPosition
import json
sys.path.append('./src')
bp = Blueprint("webapi", __name__)


@bp.route('/api/article')
def article_list():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(db.desc(Article.id)).paginate(page=page, per_page=10)
    data = pagination.items
    msg = ResponseMsg(code=200, message='success', data=([m.serialize() for m in data]))
    return jsonify(msg.serialize())

@bp.route('/api/article/<int:id>', methods=['GET','PUT', 'DELETE'])
def article_id(id):
    if request.method == 'GET':
        data = Article.query.get(id)
        msg = ResponseMsg(code=200, message='success', data=data.serialize())
        return  jsonify(msg.serialize())
    elif request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        db.session.add(Article(title=title, content=content, author=author))
        db.session.commit()
        msg = ResponseMsg(code=200, message='success', data=[])
        return jsonify(msg.serialize())
    elif request.method == 'PUT':
        id = request.form.get('id')
        article = Article.query.get(id)
        article.title = request.form.get('title')
        article.content = request.form.get('content')
        article.author = request.form.get('author')
        db.session.commit()
        responses = ResponseMsg(code=200, message='success', data=[])
        return jsonify(responses.serialize())
    elif request.method == 'DELETE':
        id = request.form.get('id')
        article = Article.query.get(id)
        db.session.delete(article)
        db.session.commit()
        responses = ResponseMsg(code=200, message='success', data=[])
        return jsonify(responses.serialize())
    return jsonify({'message': 'Invalid request method'}), 400


class ResponseMsg:
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data

    def serialize(self):
        return {
            'code': self.code,
            'message': self.message,
            'data': self.data
        }