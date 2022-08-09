from django.test import TestCase
from django.urls import resolve

from ..api import viewsets


class UserUrlsTestCase(TestCase):

    def test_user_me_request_resolve(self):
        url_name = "me"
        url_list_resolve = resolve("/api/v1/user/me/")
        view_class = url_list_resolve.func.__name__
        self.assertEqual(url_name, url_list_resolve.url_name)
        self.assertEqual(viewsets.UserMeAPIView.__name__, view_class)
