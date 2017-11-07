from flask import render_template
from . import main
from .. import db
from ..models import Article, Comment, User, Writer


#landing page
@main.route('/')
def index():
    '''
    landing page
    '''
    # get the articles/blogs title and date posted

    article = Article.get_articles()

    title = 'Prr-Blog'

    return render_template('index.html',title = title,article=article)

#details article
@main.route('/article/<int:id>')
def article(id):




    articles = Article.query.get(id)
    comments = Comment.get_comments(articles.id)
    title = f' {articles.title}'

    return render_template('article-detail.html',id=id,articles=articles,comments=comments,title=title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



# #comment section
# @main.route('/article/comment/new/<int:id>')
# def new_comment(id):
#
#     form = CommentForm()
#     articles = Article.query.get(id)
#
#     if form.validate_on_submit():
#
