import pymongo
# import numpy as np
import pandas as pd
from pymongo import MongoClient

mongo_uri = 'mongodb://localhost:27017/'
client = MongoClient(mongo_uri)

# client.list_database_names()
# client.list_collection_names()

# db = client['lasperr-live']
# collection = db['payments']


def connect_to_db():
    client = MongoClient(mongo_uri)
    db = client.lasperrlive
    payments_collection = db.payments
    return payments_collection


def read_from_db():
    payments_collection = connect_to_db()
    payments_collection_data = payments_collection.find().sort(('date', pymongo.DESCENDING))[:100]
    payments_df = pd.DataFrame(payments_collection_data)
    return payments_df


def load_and_generate_clean_data(df):
    # raw_df = pd.read_csv('data/lassperr_payments.csv')
    payments_df = df.copy()
    # df = raw_df.copy()
    df[['date', 'time']] = payments_df['date'].str.split('T', expand = True)
    clean_df = df[['date', 'amountInGMD']]
    clean_df = clean_df.rename(columns={'date': 'ds', 'amountInGMD': 'y'}, inplace = True)
    return clean_df


def format_and_sort_date_values(df):
    df['ds'] = pd.to_datetime(df['ds'])
    sorted_df_dates = df.sort_values('ds', ascending=True)
    return sorted_df_dates


def preprocess_data():
    df = read_from_db()
    clean_data = load_and_generate_clean_data(df)
    sanitized_df = format_and_sort_date_values(clean_data)
    return sanitized_df
