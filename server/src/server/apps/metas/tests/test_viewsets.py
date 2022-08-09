import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class MetasAPIViewTestCase(APITestCase):
    def setUp(self):

        self.url = "/api/v1/metas/provider/"
        self.client = APIClient()

    def test_get_providers(self):
        response = self.client.get(self.url, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
