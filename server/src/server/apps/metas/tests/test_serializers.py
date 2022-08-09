from django.test import TestCase

from ..api import serializers


class ProviderSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.ProviderSerializer

    def test_contains_expected_fields(self):
        expected_fields = {"code", "name", "country"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )


class ProviderResponseSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.ProviderResponseSerializer

    def test_contains_expected_fields(self):
        expected_fields = {"status", "providers"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )