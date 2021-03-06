from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initialising the application
app = Flask(__name__,instance_relative_config=True)

#setting up configration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing Flask Extentions
bootstrap = Bootstrap(app)

from app import views
from app import error