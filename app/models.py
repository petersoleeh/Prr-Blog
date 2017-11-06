from . import db
from datetime import datetime


class Article(db.Model):

    __tablename__ = 'articles'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    date = db.Column(db.DateTime,default =datetime.utcnow)
    title = db.Column(db.String(255))
    writer_id = db.Column(db.Integer,db.ForeignKey("writers.id"))

    def save_article(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_articles(cls):
        articles = Article.query.all()
        return articles




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

    def __repr__(self):
        return f'Writer {self.writername}'



class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    article_id = db.Column(db.Integer)
    article_title = db.Column(db.String)
    date = db.Column(db.DateTime,default =datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(article_id = id).all()
        return comments
