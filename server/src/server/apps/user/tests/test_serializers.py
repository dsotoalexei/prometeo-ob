from django.test import TestCase

from ..api import serializers


class UserSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.UserSerializer

    def test_contains_expected_fields(self):
        expected_fields = {"name", "document", "email"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )


class InfoResponseSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.InfoResponseSerializer

    def test_contains_expected_fields(self):
        expected_fields = {"status", "info"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )