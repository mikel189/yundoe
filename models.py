# import time
# import numpy as np
# import pandas as pd

# import datetime
# from datetime import timedelta

from fbprophet import Prophet

import sanitize


def build_model():
    df = sanitize.preprocess_data()
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods = 4, freq = 'W')
    forecast = model.predict(future)
    return forecast

def predictions():
    forecast = build_model()
    forecast_df = forecast[['ds', 'yhat_upper', 'yhat', 'yhat_lower']]
    return forecast_df.tail()



