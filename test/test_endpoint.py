import http.client
import json
import requests

def get_access_token():
    conn = http.client.HTTPSConnection("dev-1nkx3tfz.us.auth0.com")

    payload = "{\"client_id\":\"Bh5rk9gYU7ubSp1eeX7mAGVDHy8UDjQ0\",\"client_secret\":\"0mpzhJp3OgI0dBfP61cKpIXFK2KgH6bqckf2dLpM64TMEwuCvHe6y60k8VE5wVnc\",\"audience\":\"yundoe\",\"grant_type\":\"client_credentials\"}"

    headers = { 'content-type': "application/json" }

    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


def access_api_with_auth():
    token_dict = json.loads(get_access_token())
    access_token = token_dict['access_token']

    # url = "http://localhost:9400/api/prediction"
    # url = 'http://0.0.0.0:9400/api/prediction'
    url = 'https://yundoe.herokuapp.com/api/prediction'

    headers = { "authorization": "Bearer {}".format(access_token) }

    payload = '{"estate_id": "5f07154f8676eb0008153f14", "year": 2020}'

    response = requests.post(url, payload, headers = headers)

    print(response.text)

def test_endpoint_with_get():
    token_dict = json.loads(get_access_token())
    access_token = token_dict['access_token']

    # url = "http://localhost:9400/api/train_model"
    # url = 'http://0.0.0.0:9400/api/train_model'
    url = 'https://yundoe.herokuapp.com/api/train_model'

    headers = { "authorization": "Bearer {}".format(access_token) }

    response = requests.get(url, headers = headers)
    print(response.text)

if __name__ == '__main__':
    # test_endpoint_with_get()
    access_api_with_auth()
