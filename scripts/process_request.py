import os
import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

def fetch_forecast_data(estate_id, year):
    from api.models import Prediction
    
    prediction = Prediction.objects.filter(estateId=estate_id, year=year).order_by('-createdAt').first()
    return prediction
