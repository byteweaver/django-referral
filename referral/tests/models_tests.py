from django.test import TestCase

from referral.tests.factories import CampaignFactory, ReferrerFactory


class CampaignTestCase(TestCase):
    def test_model(self):
        obj = CampaignFactory()
        self.assertTrue(obj.pk)

    def test_count_users(self):
        obj = CampaignFactory()
        self.assertEqual(obj.count_users(),0)
        ReferrerFactory(campaign=obj)
        self.assertEqual(obj.count_users(),0)

class ReferrerTestCase(TestCase):
    def test_model(self):
        obj = ReferrerFactory()
        self.assertTrue(obj.pk)

    def test_match_campaign(self):
        obj = ReferrerFactory()
        obj.match_campaign()
        CampaignFactory()
        self.assertIsNone(obj.campaign)
        campaign = CampaignFactory(pattern="Test Referrer")
        obj.match_campaign()
        self.assertEqual(obj.campaign, campaign)

