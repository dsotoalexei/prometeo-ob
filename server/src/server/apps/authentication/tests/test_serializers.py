from django.test import TestCase

from ..api import serializers


class LoginRequestSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.LoginRequestSerializer

    def test_contains_expected_fields(self):
        expected_fields = {"provider", "username", "password", "type"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )
