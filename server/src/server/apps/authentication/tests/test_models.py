from django.test import TestCase

from server.apps.investments import models


class InvestmentTescase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = models.Investment

    def test_expected_fields(self):
        expected_fields = {
            'variableprofit', 'operation', 'account', 'user', 'currency', 'amount', 'uuid', 'log_state', 'state', 'id', 'country', 'updated_at', 'market', 'transaction', 'created_at'
        }

        result_fields = {item.name for item in self.model()._meta.get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            f"Expected: {expected_fields} Got: {result_fields}",
        )


class UserInformationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = models.UserInformation

    def test_expected_fields(self):
        expected_fields = {
            "date_created",
            "date_updated",
            "email",
            "first_name",
            "id",
            "investment",
            "last_name",
        }
        result_fields = {item.name for item in self.model()._meta.get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            f"Expected: {expected_fields} Got: {result_fields}",
        )


class CountryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = models.Country

    def test_expected_fields(self):
        expected_fields = {"active", "id", "investment", "name"}
        result_fields = {item.name for item in self.model()._meta.get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            f"Expected: {expected_fields} Got: {result_fields}",
        )


class CurrencyTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = models.Currency

    def test_expected_fields(self):
        expected_fields = {
            "active",
            "market",
            "id",
            "investment",
            "name",
            "operation",
        }
        result_fields = {item.name for item in self.model()._meta.get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            f"Expected: {expected_fields} Got: {result_fields}",
        )


class VariableProfitTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = models.VariableProfit

    def test_expected_fields(self):
        expected_fields = {"date_created", "id", "investment", "profit", "rate"}
        result_fields = {item.name for item in self.model()._meta.get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            f"Expected: {expected_fields} Got: {result_fields}",
        )


class OperationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = models.Operation

    def test_expected_fields(self):
        expected_fields = {
            "investment",
            "amount",
            "currency",
            "date_created",
            "id",
            "state",
            "type",
        }
        result_fields = {item.name for item in self.model()._meta.get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            f"Expected: {expected_fields} Got: {result_fields}",
        )


class TransactionTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = models.Transaction

    def test_expected_fields(self):
        expected_fields = {
            "investment",
            "date_created",
            "id",
            "refer_id",
            "state",
            "type",
        }
        result_fields = {item.name for item in self.model()._meta.get_fields()}

        self.assertEqual(
            expected_fields,
            result_fields,
            f"Expected: {expected_fields} Got: {result_fields}",
        )
