from flask import Flask
from config import config
from celery import Celery
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(app.config.from_object(config['development']))

bootstrap = Bootstrap(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from app import views, forms
