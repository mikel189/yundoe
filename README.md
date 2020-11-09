# yundoo


# Requirements
- [Pip](https://pip.pypa.io/en/stable/installing/)

## Create a .env file in the root folder like so
```
    AUTH0_DOMAIN=
    API_IDENTIFIER=
    MONGODB_PROD_URI=""
```    


## Scripts

```
.
├── notebooks                # Jupyter notebooks
│   └── TAG...               # Forecast model experimentations
│   └── Golden...            # Data analysis for Golden Camel Dashboard
├── api                      # models.py
│   └── process_request.py   # process api request
|   └── models.py            # Python classes modeling the database
├── scripts                  # data cleaning and model training code
│   ├── sanitize.py          # Reads db and sanitize the data before modelling
│   ├── forecaster.py        # Time series-based forecasting model 
│   └── insert.py            # Contains routines for inserting raw data and trained model into db
└── test                     # Unit tests source code
    ├── test_endpoints.py    # test api endpoints
    ├── test.py              # unitTest for api endpoints
├── config.py                # Project configuration settings
└── server.py                # Project entry point
```

## How to use
```
run
- pip install -r requirements.txt
- python server.py

```