# from sqlalchemy import Column, DateTime, Integer, String
# from datetime import datetime
# from database import Base
# from enum import Enum

# class Article(Base):
#     """
#     Article class
#     """
#     __tablename__ = 'articles'

#     id = Column(Integer, primary_key=True)
#     title = Column(String(100))
#     content = Column(String(500))
#     author = Column(String(50))
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now)

#     def __init__(self, id, title, content, author=None):
#         self.id = id
#         self.title = title
#         self.content = content
#         self.author = author

#     def __repr__(self): 
#         return f"<Article {self.title}>"
    
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     email = Column(String(120), unique=True)
#     password = Column(String(120))
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now)

#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     def __repr__(self):
#         return f'<User {self.name!r}>'

# class Navigation(Base):
#     __tablename__ = 'navigations'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(50), unique=True)
#     url = Column(String(120), unique=True)
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now)
#     status = Column(Integer, default=1)
#     position = Column(String(50))

#     def __init__(self,title, url, status=1, position=None):
#         self.title = title
#         self.url = url
#         self.status = status
#         self.position = position

#     def __repr__(self):
#         return f'<Navigation {self.title!r}>'

# class NavigationPosition(Enum):
#     Home = 1
#     Other = 2