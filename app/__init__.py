from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initialize application
app = Flask(__name__,instance_relative_config = True)

#setting up configuraions
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initialize flask extensions
bootstrap = Bootstrap(app)

from app import views
