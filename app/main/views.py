from flask import render_template
from . import main
from .. import db
from ..models import Article, Comment, User, Writer



@main.route('/')
def index():
    '''
    landing page
    '''
    # get the articles/blogs title and date posted

    article = Article.get_articles()

    title = 'Prr-Blog'

    return render_template('index.html',title = title,article=article)


@main.route('/article/<int:id>')
def article(id):

    # article = Article.query.get(id)
    # comments = Comment.get_comments(article.id)
    # title = f' {article.title}'

    return render_template('article-detail.html',id=id)
