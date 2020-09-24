import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

# from app import Prediction

def fetch_forecast_data(estate_id, year):
    prediction = Prediction.objects.filter(estate_id = estate_id, year=year).order_by('-date')
    return prediction

