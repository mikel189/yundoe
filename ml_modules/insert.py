import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

import json
from datetime import datetime

from ml_modules.sanitize import connect_to_db, get_estates, process_and_save_raw_data
from ml_modules.forecaster import get_train_model
from api_modules.models import Prediction


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
    prediction_dict['upper_bound'] = prediction_dict.pop(prediction_dict_keys[1])
    prediction_dict['amount'] = prediction_dict.pop(prediction_dict_keys[2])
    prediction_dict['lower_bound'] = prediction_dict.pop(prediction_dict_keys[3])
    prediction_dict['month_index'] = prediction_dict['date'].month
    prediction_dict['year'] = prediction_dict['date'].year
    prediction_dict['created_at'] = datetime.now()

    return prediction_dict


def insert_predictions_to_db():
    model_output_dict = format_predictions()
    print('type of model output dict is ', type(model_output_dict))
    print('model in dict', model_output_dict)

    estates = get_estates()
    estate_id = [estate['_id'] for estate in estates]

    print('before insertion')
    prediction = Prediction(year=model_output_dict['year'], amount=model_output_dict['amount'], \
        upperBound=model_output_dict['upper_bound'], lowerBound=model_output_dict['lower_bound'], \
        monthIndex=model_output_dict['month_index'], estateId=str(estate_id[0]), date=model_output_dict['date'],\
        createdAt=datetime.now()).save()
        
    print('after prediction insertion')
    print('insertion id: {}'.format(prediction))
    # except Exception as e:
    #     return(str(e))


if __name__ == '__main__':
    process_and_save_raw_data()
    insert_predictions_to_db()