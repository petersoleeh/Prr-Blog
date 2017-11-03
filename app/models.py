from . import db
from datetime import date, datetime


class Article(db.Model):

    __tablename__ = 'articles'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    date = db.Column(db.DateTime,default =datetime.utcnow)
    title = db.Column(db.String(255))
    writer_id = db.Column(db.Integer,db.ForeignKey("writers.id"))




class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'user', lazy = "dynamic")


    def __repr__(self):
        return f'User {self.username}'


class Writer(db.Model):

    __tablename__ = 'writers'

    id = db.Column(db.Integer,primary_key = True)
    writername = db.Column(db.String(255))
    articles = db.relationship('Article',backref='writers',lazy = "dynamic")



class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    article_id = db.Column(db.Integer)
    article_title = db.Column(db.String)
    date = db.Column(db.DateTime,default =datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
