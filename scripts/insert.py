import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from pymongo import MongoClient
from scripts.sanitize import connect_to_db
from scripts.forecaster import get_train_model
from datetime import datetime

from  import Prediction
from scripts.sanitize import get_estates


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
    prediction_dict['upper_bound'] = prediction_dict.pop(prediction_dict_keys[1])
    prediction_dict['amount'] = prediction_dict.pop(prediction_dict_keys[2])
    prediction_dict['lower_bound'] = prediction_dict.pop(prediction_dict_keys[3])
    prediction_dict['month_index'] = prediction_dict['date'].month
    prediction_dict['year'] = prediction_dict['date'].year
    prediction_dict['created_at'] = datetime.now()

    return prediction_dict



def insert_predictions_to_db():
    model_output_dict = format_predictions()
    print('model in dict', model_output_dict)
    
    estates = get_estates()
    for estate in estates:
        estate_id = estate['_id']

    for item in model_output_dict:
        try:
            prediction = Prediction(
                date=item['date'],
                year=item['year'], 
                upper_bound=item['upper_bond'],
                lower_bound=item['lower_bound'],
                amount=item['amount'],
                month_index=item['month_index'],
                estate_id=estate_id,
                created_at=item['created_at']
            ).save()
            

            print('insertion id: {}'.format(prediction.id))
        except Exception as e:
            return(str(e))


if __name__ == '__main__':
    insert_predictions_to_db()