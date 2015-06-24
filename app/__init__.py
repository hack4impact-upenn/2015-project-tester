from flask import Flask
from config import config


app = Flask(__name__)
app.config.from_object(app.config.from_object(config['development']))
