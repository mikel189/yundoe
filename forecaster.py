from fbprophet import Prophet
from sanitize import preprocess_data


def build_model():
    df = preprocess_data()
    model = Prophet(
        growth='linear',
        daily_seasonality=True,
        weekly_seasonality=False,
        yearly_seasonality=True,
        # seasonality_mode='multiplicative',
    ).add_seasonality(
        name = 'monthly',
        period = 30.5,
        fourier_order = 55
    ).add_seasonality(
        name = 'weekly', 
        period = 7,
        fourier_order = 20
    ).add_seasonality(
        name = 'daily',
        period = 1,
        fourier_order = 15
    )
    model.fit(df)
    future = model.make_future_dataframe(periods = 3, freq = 'D')
    forecast = model.predict(future)
    return forecast


def predictions():
    forecast = build_model()
    forecast_df = forecast[['ds', 'yhat_upper', 'yhat', 'yhat_lower']]
    return forecast_df.tail(5)


def get_train_model():
    prediction_df = predictions()
    print(prediction_df)
    return prediction_df


if __name__ == '__main__':
    get_train_model()

