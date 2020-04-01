from flask import Flask 
from myapp import settings
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from myapp import routes