import http.client
import json
import requests
from os import environ as env
from dotenv import load_dotenv, find_dotenv


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

AUTH0_DOMAIN = env.get('AUTH0_DOMAIN')
PAYLOAD = env.get('PAYLOAD')


def get_access_token():
    conn = http.client.HTTPSConnection(AUTH0_DOMAIN)

    payload = PAYLOAD

    headers = { 'content-type': "application/json" }

    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


def access_api_with_auth():
    token_dict = json.loads(get_access_token())
    access_token = token_dict['access_token']

    # url = "http://localhost:9500/api/prediction"
    url = 'https://yundoe.vercel.app/api/prediction'

    headers = { "authorization": "Bearer {}".format(access_token) }

    payload = '{"estate_id": "5f07154f8676eb0008153f14", "year": 2020}'

    response = requests.post(url, payload, headers = headers)

    print(response.text)

def test_endpoint_with_post():
    token_dict = json.loads(get_access_token())
    access_token = token_dict['access_token']

    # url = "http://localhost:9500/api/train_model"
    url = 'https://yundoe.vercel.app/api/train_model'

    headers = { "authorization": "Bearer {}".format(access_token) }

    response = requests.post(url, headers = headers)
    print(response.text)

if __name__ == '__main__':
    test_endpoint_with_post()
    access_api_with_auth()
