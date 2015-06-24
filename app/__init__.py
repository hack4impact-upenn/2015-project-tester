from flask import Flask
from config import config
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(app.config.from_object(config['development']))

bootstrap = Bootstrap(app)

from app import views, forms
