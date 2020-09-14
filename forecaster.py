from fbprophet import Prophet
from sanitize import preprocess_data


def build_model():
    df = preprocess_data()
    model = Prophet(daily_seasonality=True, weekly_seasonality=True)
    model.fit(df)
    future = model.make_future_dataframe(periods = 30)
    forecast = model.predict(future)
    return forecast


def predictions():
    forecast = build_model()
    forecast_df = forecast[['ds', 'yhat_upper', 'yhat', 'yhat_lower']]
    return forecast_df.tail(2)


def get_train_model():
    prediction_df = predictions()
    print(prediction_df)
    return prediction_df


if __name__ == '__main__':
    get_train_model()

