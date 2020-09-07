from pymongo import MongoClient
from sanitize import connect_to_db
from forecaster import get_train_model

def get_payments_collection():
    db = connect_to_db()
    payments_collection = db.payments
    return payments_collection


def format_predictions():
    model_df = get_train_model()
    model_in_dict = model_df.to_dict()

    prediction_dict = {}
    for key, val in model_in_dict.items():
        for _, value in val.items():
            prediction_dict[key] = value

    return prediction_dict


def insert_predictions_to_db():
    model_predictions = format_predictions()
    print('model in dict', model_predictions)
    payments_collection = get_payments_collection()
    post_id = payments_collection.insert_one(model_predictions).inserted_id
    return post_id


if __name__ == '__main__':
    insert_predictions_to_db()