from django.test import TestCase

from ..api import serializers


class CountrySerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.CountrySerializer

    def test_contains_expected_fields(self):
        expected_fields = {"id", "name", "active"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )


class CurrencySerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.CurrencySerializer

    def test_contains_expected_fields(self):
        expected_fields = {"id", "name", "active", "default_provider"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )


class OperationSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.OperationSerializer

    def test_contains_expected_fields(self):
        expected_fields = {"id", "investment", "type", "state", "amount", "currency"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )


class TransactionSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.TransactionSerializer

    def test_contains_expected_fields(self):
        expected_fields = {"id", "investment", "type", "state", "refer_id"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )


class VariableProfitSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.serializer = serializers.VariableProfitSerializer

    def test_contains_expected_fields(self):
        expected_fields = {"id", "investment", "rate", "profit"}
        result_fields = {item for item in self.serializer().get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            "Expected: {expected} Got: {result}".format(
                expected=expected_fields, result=result_fields
            ),
        )
