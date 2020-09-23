import os
import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

app = Flask(__name__)

app.config.from_pyfile('config.py')
db = MongoEngine(app)

app.session_interface = MongoEngineSessionInterface(app)

from api import routes
from scripts import insert

if __name__ == '__main__':
    app.run()