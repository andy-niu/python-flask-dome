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
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.fields import *
from wtforms.validators import DataRequired, Length, Regexp

sys.path.append('./src')
bp = Blueprint("program", __name__)


@bp.route('/')
def index():
    articles = Article.query.order_by(db.desc(Article.id)).paginate(page=1, per_page=5)
    users = User.query.order_by(db.desc(User.id)).paginate(page=1, per_page=5)
    data = {'articles':articles, 'users':users}
    return render_template('index.html',data=data)

@bp.route('/get')
def get():
    data = Navigation.query.all()
    print(data)
    return jsonify([nav.serialize() for nav in data])

@bp.route('/todo', methods=['POST', 'GET', 'PUT'])
def todo():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return jsonify(data)
    elif request.method == 'PUT':
        data = User.query.all()
        return  jsonify([m.serialize() for m in data])
    else:
        data = User.query.all()
        return  jsonify([m.serialize() for m in data])

@bp.route('/article')
def article():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(db.desc(Article.id)).paginate(page=page, per_page=10)
    article = pagination.items
    titles = [('id', '#'), ('title', 'Title'), ('author', 'Author'), ('created_at', 'Create Time')]
    data = []
    for msg in article:
        data.append({'id': msg.id, 'text': msg.title, 'author': msg.author, 'title': msg.content, 'created_at': msg.created_at})
    return render_template('article/index.html', article=article, titles=titles, Article=Article, data=data, pagination=pagination)

@bp.route('/article/<int:article_id>')
def view_article(article_id):
    article = Article.query.get(article_id)
    if article is None:
        flash('Article not found!')
        return redirect(url_for('program.article'))
    else:
        return render_template('article/view.html', article=article)

@bp.route('/article/create', methods=['GET', 'POST'])
def create_article():
    form = ArticleForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash('Form validated!')
        article = Article(title=form.title.data, content=form.context.data, author=form.author.data)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('program.article'))
    else:
        return render_template('article/create.html', form=form)
    
@bp.route('/article/<int:article_id>/edit', methods=['GET', 'POST'])
def edit_article(article_id):
    article = Article.query.get(article_id)
    if article is None:
        flash('Article not found!')
        return redirect(url_for('program.article'))
    form = ArticleForm()
    if request.method == 'POST' and form.validate_on_submit():
        article.title = form.title.data
        article.content = form.context.data
        article.author = form.author.data
        db.session.commit()
        flash('updated!')
        return redirect(url_for('program.article'))
    else:
        form.id.data = article.id
        form.title.data = article.title
        form.context.data = article.content
        form.author.data = article.author
        return render_template('article/create.html', form=form, article=article)

@bp.route('/article/<int:article_id>/remove', methods=['GET', 'POST'])
def remove_article(article_id):
    article = Article.query.get(article_id)
    if article is None:
        flash('Article not found!')
        return redirect(url_for('program.article'))
    db.session.delete(article)
    db.session.commit()
    flash('deleted!')
    return redirect(url_for('program.article'))

class ArticleForm(FlaskForm):
    id = HiddenField('ID')
    title = StringField('Title', validators=[DataRequired(), Length(1, 128)])
    context = TextAreaField('Context', validators=[DataRequired(), Length(10, 512)])
    author = StringField('Author', validators=[DataRequired(), Length(2, 30)])
    submit = SubmitField()
