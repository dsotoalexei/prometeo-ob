from django.apps import apps
from django.test import SimpleTestCase

from .. import InvestmentsAppConfig


class ProvidersAppConfigTestCase(SimpleTestCase):
    def test_apps(self):
        self.assertEqual(InvestmentsAppConfig.name, "investments")
        self.assertEqual(
            apps.get_app_config("investments").name, "server.apps.investments"
        )
