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
    # print(data.decode("utf-8"))


def access_api():
    token_dict = json.loads(get_access_token())
    access_token = token_dict['access_token']

    # url = "http://127.0.0.1:5000/api/prediction/"
    url = "http://127.0.0.1:5000/api/public/"


    headers = { 'authorization': "Bearer " + access_token }
    body = '{"estate_id": "1234325", "year": 1994}'
    # print('this is headers', headers)

    # response = requests.post(url, data=body, headers = headers)
    response = requests.get(url)

    print(response.text)

if __name__ == '__main__':
    # get_token()
    access_api()


# curl --request POST \
#   --url http://127.0.0.1:5000/api/private \
#   --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhBdWEtenVUT184U1JkbWRCOXFEdiJ9.eyJpc3MiOiJodHRwczovL2Rldi0xbmt4M3Rmei51cy5hdXRoMC5jb20vIiwic3ViIjoiQmg1cms5Z1lVN3ViU3AxZWVYN21BR1ZESHk4VURqUTBAY2xpZW50cyIsImF1ZCI6Inl1bmRvZSIsImlhdCI6MTYwMDY4ODk1MywiZXhwIjoxNjAwNzc1MzUzLCJhenAiOiJCaDVyazlnWVU3dWJTcDFlZVg3bUFHVkRIeThVRGpRMCIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.ol4YvEPql6SNrB2dbB2N503Ts25PKYYPz5MJvO8WeNbnf5IqXYQNdrXc2jQR8bgmIm7Y-wBKDwrIZ1I9sQrFRG4NWC-vWyzFBjBb4pSYoFR6WZrQzchSuz6UQ2ZNifIiq8NQW_3GLRR3J_GU3vqBrDKUfYzkx4Whlot5X-KZkqa5Qey3qB3wKdi0yXCTmT7Jav9EiVmWuC_ib46H1hLkfhejaLzPqvA8cJKSA6bcqLhgHeY96h2XI4xS4kXy-PwMT69bFpZHxGCGCkBRsAOYAwueH3R5Rjjlm0MSVZnhlNd9tjhJGyt5-cgINQKPVKqe608V9LeVRO1MHDeMDCL6Wg' \
#   --data '{"estate_id": "1234325", "year": 1994}'

