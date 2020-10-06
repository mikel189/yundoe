import sys
sys.path.append('/home/ibrahim/assutech/Yundoo/')

from server import app
import unittest
import os


class FlaskTest(unittest.TestCase):

    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type, "application/json")

    
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertTrue(b'hello' in response.data)


    def test_public_endpoint(self):
        tester = app.test_client(self)
        response = tester.get('/api/public')
        status_code = response.status_code
        self.assertEqual(status_code, 200)


    def test_public_endpoint_content_type(self):
        tester = app.test_client(self)
        response = tester.get('/api/public')
        status_code = response.status_code
        self.assertEqual(response.content_type, "application/json")


    def test_public_endpoint_data(self):
        tester = app.test_client(self)
        response = tester.get('/api/public')
        self.assertTrue(b'Hello from a public endpoint!' in response.data)


    def test_private_endpoint(self):
        payload = '{"estate_id": "5f07154f8676eb0008153f14", "year": 2020}'
        headers = { "Content-Type": "application/json", "authorization": "Bearer {}".format(os.environ.get('ACCESS_TOKEN')) }

        tester = app.test_client(self)
        response = tester.post('/api/private', data=payload, headers=headers)
        self.assertEqual(int, type(response.json['year']))
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
