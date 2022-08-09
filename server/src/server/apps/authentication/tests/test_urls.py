from django.test import TestCase
from django.urls import resolve

from ..api import viewsets


class AuthenticationUrlsTestCase(TestCase):

    def test_authentication_login_request_resolve(self):
        url_name = "login"
        url_list_resolve = resolve("/api/v1/authentication/login/")
        view_class = url_list_resolve.func.__name__
        self.assertEqual(url_name, url_list_resolve.url_name)
        self.assertEqual(viewsets.LoginAPIView.__name__, view_class)

    def test_authentication_logout_request_resolve(self):
        url_name = "logout"
        url_list_resolve = resolve("/api/v1/authentication/logout/")
        view_class = url_list_resolve.func.__name__
        self.assertEqual(url_name, url_list_resolve.url_name)
        self.assertEqual(viewsets.LogoutAPIView.__name__, view_class)
