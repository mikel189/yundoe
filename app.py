from pymongo import MongoClient
from sanitize import get_payments_collection

def format_predictions(df):
    json_df = df.to_json(date_format='iso')
    return json_df


def insert_predictions_to_db(json_df):
    payments_collection = get_payments_collection()
    post_id = payments_collection.insert_one({json_df}).inserted_id
    return post_id
