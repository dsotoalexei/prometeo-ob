import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class UserAPIViewTestCase(APITestCase):
    def setUp(self):
        
        login = "/api/v1/authentication/login/"
        self.client = APIClient()
        payload = json.dumps({'username': '12345', 'password': 'gfdsa', 'provider': 'test'})
        response = self.client.post(login, payload, content_type='application/json')
        key = response.json().get('key')
        self.url = f"/api/v1/user/me/?key={key}"

    def test_get_user_me(self):
        response = self.client.get(self.url, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
