import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from fbprophet import Prophet
from ml_modules.sanitize import preprocess_data
# from api.models import RawForecastData


def build_model():
    df = preprocess_data()
    model = Prophet(
        growth='linear', 
        seasonality_mode='multiplicative', 
        seasonality_prior_scale=15,
        weekly_seasonality=False, 
        daily_seasonality=False,
    ).add_seasonality(
        name='daily',
        period=1,
        fourier_order=15
    ).add_seasonality(
        name='monthly', 
        period=30.5,
        fourier_order=20
    )
    model.fit(df)
    future = model.make_future_dataframe(periods = 1, freq='M')
    forecast = model.predict(future)
    return forecast


def get_forecast_df():
    forecast = build_model()
    forecast_df = forecast[['ds', 'yhat_upper', 'yhat', 'yhat_lower']]
    return forecast_df.tail(1)


def get_train_model():
    prediction_df = get_forecast_df()
    print('this is prediction df', prediction_df)
    return prediction_df


if __name__ == '__main__':
    get_train_model()

