from datetime import datetime
from src import db
from enum import Enum

class Article(db.Model):
    """
    Article class
    """
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(500))
    author = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, id, title, content, author=None):
        self.id = id
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self): 
        return f"<Article {self.title}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, email, password, is_admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f'<User {self.name!r}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'is_admin': self.is_admin
        }

class Navigation(db.Model):
    __tablename__ = 'navigations'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    url = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Integer, default=1)
    position = db.Column(db.String(50))

    def __init__(self,title, url, status=1, position=None):
        self.title = title
        self.url = url
        self.status = status
        self.position = position

    def __repr__(self):
        return f'<Navigation {self.title!r}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'status': self.status,
            'position': self.position,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }   

class NavigationPosition(Enum):
    Home = 1
    Other = 2