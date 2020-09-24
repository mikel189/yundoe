import os
import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

app = Flask(__name__)

# app.config.from_pyfile('config.py')
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'test',
#     'host': 'ibrahim',
#     'port': 27017,
# }
app.config['MONGODB_HOST'] = 'mongodb://127.0.0.1:27017/test'

db = MongoEngine(app)

# app.session_interface = MongoEngineSessionInterface(app)

from api import routes
# from scripts import insert

if __name__ == '__main__':
    app.run()