import os
import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

app = Flask(__name__)

app.config['MONGO_DB'] = 'forecast-db'
app.config['MONGODB_HOST'] = 'mongodb://127.0.0.1:27017/'
app.config['MONGODB_CONNECT'] = False

db = MongoEngine(app)

from api import routes
from api import models

if __name__ == '__main__':
    app.run(debug=True)