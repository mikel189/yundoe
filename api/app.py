import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from flask import Flask, request, jsonify, _request_ctx_stack
from flask_debugtoolbar import DebugToolbarExtension
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
import os

app = Flask(__name__)
db = MongoEngine(app)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/test',
    'connect': False,
}


app.session_interface = MongoEngineSessionInterface(app)
# DebugToolbarExtension(db)
if __name__ == '__main__':
    app.run()