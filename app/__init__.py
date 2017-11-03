from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager


# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
# db = SQLAlchemy()

def create_app(config_name):


    #initialize the application
    app = Flask(__name__)


    #set up the app configuration
    app.config.from_object(config_options[config_name])


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # initialize flask extensions
    bootstrap.init_app(app)




    return app