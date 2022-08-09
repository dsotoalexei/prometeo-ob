from django.test import TestCase
from django.urls import resolve

from ..api import viewsets


class MetasUrlsTestCase(TestCase):

    def test_metas_providers_request_resolve(self):
        url_name = "provider"
        url_list_resolve = resolve("/api/v1/metas/provider/")
        view_class = url_list_resolve.func.__name__
        self.assertEqual(url_name, url_list_resolve.url_name)
        self.assertEqual(viewsets.ProviderAPIView.__name__, view_class)
