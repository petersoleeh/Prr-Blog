from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class ArticleForm(FlaskForm):
    title = StringField('Article title', validators=[Required()])
    content = TextAreaField('Article content')
    # comment = TextAreaField('New Pitch')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    title = StringField('Comment title', validators=[Required()])
    comment = TextAreaField('New Comment')
    submit = SubmitField('Submit')
