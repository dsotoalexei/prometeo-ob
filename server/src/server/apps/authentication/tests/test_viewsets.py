from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class CountryViewSetTestCase(APITestCase):
    def setUp(self):

        self.url = "/api/v1/countries"
        self.client = APIClient()

    def test_list(self):

        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CurrencyViewSetTestCase(APITestCase):
    def setUp(self):

        self.url = "/api/v1/currencies"
        self.client = APIClient()

    def test_list(self):

        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OperationViewSetTestCase(APITestCase):
    def setUp(self):

        self.url = "/api/v1/operations"
        self.client = APIClient()

    def test_list(self):

        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TransactionViewSetTestCase(APITestCase):
    def setUp(self):

        self.url = "/api/v1/transactions"
        self.client = APIClient()

    def test_list(self):

        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class VariableProfitViewSetTestCase(APITestCase):
    def setUp(self):

        self.url = "/api/v1/variable-profits"
        self.client = APIClient()

    def test_list(self):

        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
