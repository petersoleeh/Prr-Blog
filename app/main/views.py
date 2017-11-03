from flask import render_template
from . import main


@main.route('/')
def index():
    '''
    landing page
    '''

    title = 'Prr-Blog'
    return render_template('index.html',title = title)
