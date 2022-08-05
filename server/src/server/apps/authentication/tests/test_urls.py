from django.test import TestCase
from django.urls import resolve

from ..api import viewsets


class CountryUrlsTestCase(TestCase):
    def test_country_request_list_resolve(self):
        url_name = "countries-list"
        url_list_resolve = resolve("/api/v1/countries")
        view_class = url_list_resolve.func.__name__
        self.assertEqual(url_name, url_list_resolve.url_name)
        self.assertEqual(viewsets.CountriesViewSet.__name__, view_class)


class CurrencyUrlsTestCase(TestCase):
    def test_country_request_list_resolve(self):
        url_name = "currencies-list"
        url_list_resolve = resolve("/api/v1/currencies")
        view_class = url_list_resolve.func.__name__
        self.assertEqual(url_name, url_list_resolve.url_name)
        self.assertEqual(viewsets.CurrenciesViewSet.__name__, view_class)


class OperationUrlsTestCase(TestCase):
    def test_country_request_list_resolve(self):
        url_name = "operations-list"
        url_list_resolve = resolve("/api/v1/operations")
        view_class = url_list_resolve.func.__name__
        self.assertEqual(url_name, url_list_resolve.url_name)
        self.assertEqual(viewsets.OperationViewSet.__name__, view_class)


class TransactionUrlsTestCase(TestCase):
    def test_country_request_list_resolve(self):
        url_name = "transactions-list"
        url_list_resolve = resolve("/api/v1/transactions")
        view_class = url_list_resolve.func.__name__
        self.assertEqual(url_name, url_list_resolve.url_name)
        self.assertEqual(viewsets.TransactionViewSet.__name__, view_class)


class VariableProfitUrlsTestCase(TestCase):
    def test_country_request_list_resolve(self):
        url_name = "variable-profits-list"
        url_list_resolve = resolve("/api/v1/variable-profits")
        view_class = url_list_resolve.func.__name__
        self.assertEqual(url_name, url_list_resolve.url_name)
        self.assertEqual(viewsets.VariableProfitViewSet.__name__, view_class)
