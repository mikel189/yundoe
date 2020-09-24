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
    date = db.DateTimeField(required=True)
    created_at = db.DateTimeField(required=True)

    meta = {
        'ordering': ['-date']
    }


    def to_json(self):
        prediction_dict = {
            'year': year,
            'amount': amount,
            'upper_bound': upper_bound,
            'lower_bound': lower_bound,
            'month_index': month_index,
            'estate_id': estate_id,
            'date': date,
            'created_at': created_at,
        }
        return prediction_dict


class RawForecastData(db.Document):
    date = db.DateTimeField(required=True)
    amount = db.FloatField(required=True)

    def to_json(self):
        raw_forecast_data_dict = {
            'date': date,
            'amount': amount,
        }
        return raw_forecast_data_dict

