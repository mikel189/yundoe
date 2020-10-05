# import mongoengine as me
import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from mongoengine import *
from datetime import datetime
from app import db


class Prediction(db.Document):
    year = db.IntField(required=True)
    amount = db.FloatField(required=True)
    upper_bound = db.FloatField(required=True)
    lower_bound = db.FloatField(required=True)
    month_index = db.IntField(required=True)
    estate_id = db.StringField(required=True)
    date = db.DateField(required=True)
    created_at = db.DateField(required=True)

    meta = {
        'ordering': ['-date']
    }


    def to_json(self):
        prediction_dict = {
            'year': self.year,
            'amount': self.amount,
            'upper_bound': self.upper_bound,
            'lower_bound': self.lower_bound,
            'month_index': self.month_index,
            'estate_id': self.estate_id,
            'date': self.date,
            'created_at': self.created_at,
        }
        return prediction_dict


class RawForecastData(db.Document):
    date = db.DateField(required=True)
    lasperr_id = db.StringField(required=True)

    def to_json(self):
        raw_forecast_data_dict = {
            'lasperr_id': self.lasperr_id
        }
        return raw_forecast_data_dict


# prediction = Prediction(
#                 date=datetime.now(),
#                 year=2020, 
#                 upper_bound=20202.2,
#                 lower_bound=20203.1,
#                 amount=2020202.32,
#                 month_index=9,
#                 estate_id='sdheiageh3',
#                 created_at=datetime.now(),
#             ).save()