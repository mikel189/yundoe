# import mongoengine as me
import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from mongoengine import *
from datetime import datetime
from server import db


class Prediction(db.Document):
    year = db.IntField(required=True)
    amount = db.FloatField(required=True)
    upperBound = db.FloatField(required=True)
    lowerBound = db.FloatField(required=True)
    monthIndex = db.IntField(required=True)
    estateId = db.StringField(required=True)
    date = db.DateTimeField(required=True)
    createdAt = db.DateTimeField(required=True)

    meta = {
        'ordering': ['-date']
    }


    def to_json(self):
        prediction_dict = {
            'year': self.year,
            'amount': self.amount,
            'upper_bound': self.upperBound,
            'lower_bound': self.lowerBound,
            'month_index': self.monthIndex,
            'estate_id': self.estateId,
            'date': self.date,
            'created_at': self.createdAt,
        }
        return prediction_dict


class RawForecastData(db.Document):
    date = db.DateTimeField(required=True)
    lasperrId = db.StringField(required=True)

    def to_json(self):
        raw_forecast_data_dict = {
            'lasperr_id': self.lasperrId
        }
        return raw_forecast_data_dict


# prediction = Prediction(
#                 date=datetime.now(),
#                 year=2020, 
#                 amount=2020202.32,
#                 upper_bound=20202.2,
#                 lower_bound=20203.1,
#                 month_index=9,
#                 estate_id='sdheiageh3',
#                 created_at=datetime.now(),
#             ).save()