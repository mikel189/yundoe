# import mongoengine as me
import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from flask_mongoengine import *
from api.app import db

class Prediction(db.Document):
    __tablename__ = 'test'
    year = db.IntField(required=True)
    amount = db.FloatField(required=True)
    upper_bound = db.FloatField(required=True)
    lower_bound = db.FloatField(required=True)
    month_index = db.IntField(required=True)
    estate_id = db.StringField(required=True)
    date = db.DateTimeField(required=True)
    created_at = db.DateTimeField(required=True)

    meta = {
        'ordering': ['-date']
    }


    def __str__(self):
        return f'amount: {self.amount}'


class RawForecastData(db.Document):
    date = db.DateTimeField(required=True)
    amount = db.DateTimeField(required=True)