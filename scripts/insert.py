from pymongo import MongoClient
from sanitize import connect_to_db
from forecaster import get_train_model
from datetime import datetime

from api.app import app, db
from api.models import Prediction


def get_forecast_collection():
    db = connect_to_db()
    forecast_collection = db.forecast
    return forecast_collection


def format_predictions():
    model_df = get_train_model()
    model_in_dict = model_df.to_dict()

    prediction_dict = {}
    for key, val in model_in_dict.items():
        for _, value in val.items():
            prediction_dict[key] = value
    
    prediction_dict_keys = list(prediction_dict.keys())

    prediction_dict['date'] = prediction_dict.pop(prediction_dict_keys[0])
    print('time stamp', prediction_dict['date'])
    prediction_dict['upperBound'] = prediction_dict.pop(prediction_dict_keys[1])
    prediction_dict['amount'] = prediction_dict.pop(prediction_dict_keys[2])
    prediction_dict['lowerBound'] = prediction_dict.pop(prediction_dict_keys[3])
    prediction_dict['monthIndex'] = prediction_dict['date'].month
    prediction_dict['year'] = prediction_dict['date'].year
    # prediction_dict['createdAt'] = datetime.now()

    return prediction_dict



def insert_predictions_to_db():
    model_output_dict = format_predictions()
    print('model in dict', model_output_dict)
    
    for item in model_output_dict:
        try:
            prediction = Prediction(
                date=item['date'],
                year=item['year'], 
                upper_bound=item['upper_bond'],
                lower_bound=item['lower_bound'],
                amount=item['amount'],
                month_index=item['month_index'],
                estate_id=item['estate_id'],
                created_at=item['created_at']
            )
            
            db.session.add(prediction)
            db.session.commit()
            print('insertion id: {}'.format(prediction.id))
        except Exception as e:
            return(str(e))


# def insert_predictions_to_db():
#     prediction_dict = format_predictions()
#     print('model in dict', prediction_dict)
#     payments_collection = get_forecast_collection()
#     post_id = payments_collection.insert_one(prediction_dict).inserted_id
#     print(post_id)


if __name__ == '__main__':
    insert_predictions_to_db()