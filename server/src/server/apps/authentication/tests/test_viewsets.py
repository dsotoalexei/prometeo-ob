import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class LoginAPIViewTestCase(APITestCase):
    def setUp(self):

        self.url = "/api/v1/authentication/login/"
        self.client = APIClient()

    def test_login(self):
        payload = json.dumps({'username': '12345', 'password': 'gfdsa', 'provider': 'test'})
        response = self.client.post(self.url, payload, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
