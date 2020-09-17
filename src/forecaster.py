from fbprophet import Prophet
from sanitize import preprocess_data


def build_model():
    df = preprocess_data()
    model = Prophet(
        growth='linear', 
        seasonality_mode = 'multiplicative', 
        weekly_seasonality=True, 
        daily_seasonality=True,
    )
    model.fit(df)
    future = model.make_future_dataframe(periods = 1, freq='M')
    forecast = model.predict(future)
    return forecast


def predictions():
    forecast = build_model()
    forecast_df = forecast[['ds', 'yhat_upper', 'yhat', 'yhat_lower']]
    return forecast_df.tail(1)


def get_train_model():
    prediction_df = predictions()
    print(prediction_df)
    return prediction_df


if __name__ == '__main__':
    get_train_model()
