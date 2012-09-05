from django.test import TestCase

from referral.tests.factories import CampaignFactory


class CampaignTestCase(TestCase):
    def test_model(self):
        obj = CampaignFactory()
        self.assertTrue(obj.pk)

    def test_count_users(self):
        obj = CampaignFactory()
        self.assertEqual(obj.count_users(),0)

