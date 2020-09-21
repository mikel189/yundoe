from flask_sqlalchemy import SQLAlchemy
from api.app import app, db


class Prediction(db.Model):
    __tablename__ = 'predictions'

    id = db.Column(db.Integer, primary_key=True)
    upper_bound = db.Column(db.Integer, nullable=False)
    lower_bound = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    month_index = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    estate_id = db.Column(db.Integer, nullable=False)

    def __init__(self, date, upper_bound, amount, lower_bound, created_at, month_index, estate_id, year):
        self.date = date
        self.upper_bound = upper_bound
        self.amount = amount
        self.lower_bound = lower_bound
        self.created_at = created_at
        self.month_index = month_index
        self.estate_id = estate_id
        self.year = year

    def __repr__(self):
        return '<Date: {}, Upper Bound: {}, Amount: {}, Lower Bound: {}, Month Index: {}, Estate Id: {}, Year: {}>'\
            .format(self.Date, self.upper_bound, self.amount, self.lower_bound, self.month_index, self.estate_id, self.year)

    # def serialize(self):
    #     return {
    #         'Date': self.Date, 
    #         'upper_bound': self.upper_bound,
    #         'amount': self.amount,
    #         'lower_bound':self.lower_bound,
    #         'month_index':self.month_index,
    #         'year': self.year,
    #         'estate_id': self.estate_id,
    #     }
