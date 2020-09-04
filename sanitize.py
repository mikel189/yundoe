import pymongo
# import numpy as np
import pandas as pd
from os import environ as env
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
mongo_uri = env.get("MONGO_URI")


def connect_to_db():
    client = MongoClient(host=mongo_uri)
    db = client.lasperrlive
    return db

def get_payments_collection():
    db = connect_to_db()
    payments_collection = db.payments
    return payments_collection


def read_from_db():
    payments_collection = get_payments_collection()
    payments_collection_data = payments_collection.find({}).sort(('date'))
    payments_df = pd.DataFrame(payments_collection_data)
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


def preprocess_data():
    df = read_from_db()
    clean_data = load_and_generate_clean_data(df)
    sanitized_df = format_and_sort_date_values(clean_data)
    print('sanitized payments df', sanitized_df)
    return sanitized_df


if __name__ == '__main__':
    print('preprocessing data......')
    preprocess_data()