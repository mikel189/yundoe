from pymongo import MongoClient

mongo_uri = 'mongodb://localhost:27017/'


def format_predictions(df):
    json_df = df.to_json(date_format='iso')
    return json_df


def insert_predictions_to_db(json_df):
    client = MongoClient(mongo_uri)
    collection = client.lasperrlive
    post_id = collection.insert_one({json_df}).inserted_id
    return post_id
