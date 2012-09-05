from django.test import TestCase

from referral.tests.factories import CampaignFactory


class CampaignTestCase(TestCase):
    def test_model(self):
        obj = CampaignFactory()
        self.assertTrue(obj.pk)

