import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

import pymongo
import pandas as pd
from os import environ as env
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from api.models import RawForecastData

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    
mongo_uri = env.get("MONGO_URI")


def connect_to_db():
    client = MongoClient(host=mongo_uri)
    db = client.lasperrlive
    return db


def get_estates():
    db = connect_to_db()
    estates_collection = db.estates
    estates = estates_collection.find({})
    return estates


def get_payments_collection():
    db = connect_to_db()
    payments_collection = db.payments
    estates = get_estates()
    
    for estate in estates:
        payments_per_estate = payments_collection.find({'estateId': estate['_id']})
        return payments_per_estate


def create_payments_df():
    payments_collection = get_payments_collection()
    payments_df = pd.DataFrame(payments_collection)
    return payments_df


def load_and_generate_clean_data(df):
    payments_df = df.copy()
    payments_df[['date', 'time']] = payments_df['date'].astype(str).str.split(' ', expand = True)
    clean_df = payments_df[['date', 'amountInGMD']]
    clean_df = clean_df.rename(columns={'date': 'ds', 'amountInGMD': 'y'})
    return clean_df


def format_and_sort_date_values(clean_df):
    df = clean_df.copy()
    df['ds'] = pd.to_datetime(df['ds'])
    sorted_df_dates = df.sort_values('ds', ascending=True)
    return sorted_df_dates


def aggregate_to_weekly(sorted_df):
    sorted_df.set_index('ds', inplace=True)
    sorted_df.index = pd.to_datetime(sorted_df.index)
    monthly_df = sorted_df.resample('1M').sum()
    monthly_df.reset_index(inplace=True)
    return monthly_df


def save_clean_data(forecast_df):
    clean_forecast_df = forecast_df
    date = clean_forecast_df['ds']
    amount = clean_forecast_df['y']
    inserted_data = RawForecastData(date = date, amount = amount).save()
    print('raw forecast df successfully inserted', inserted_data)


def preprocess_data():
    df = create_payments_df()
    clean_data = load_and_generate_clean_data(df)
    formatted_df = format_and_sort_date_values(clean_data)
    sanitized_df = aggregate_to_weekly(formatted_df)
    save_clean_data(sanitized_df)
    print('sanitized payments df', sanitized_df)
    return sanitized_df


if __name__ == '__main__':
    print('preprocessing data......')
    preprocess_data()