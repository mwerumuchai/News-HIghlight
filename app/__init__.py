from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument

    Args:
        config_name : name of the configuration used    
    '''
    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initialize flask extensions
    bootstrap.init_app(app)

    #registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)
    # We'll add the views and forms
    return app
