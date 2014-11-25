from django.http import HttpRequest
from django.test import TestCase

from referral.models import UserReferrer
from referral import settings
from referral.tests.factories import CampaignFactory, ReferrerFactory, UserReferrerFactory, UserFactory


class CampaignTestCase(TestCase):
    def test_model(self):
        obj = CampaignFactory()
        self.assertTrue(obj.pk)

    def test_count_users(self):
        obj = CampaignFactory()
        self.assertEqual(obj.count_users(), 0)
        ReferrerFactory(campaign=obj)
        self.assertEqual(obj.count_users(), 0)
        ref = ReferrerFactory(campaign=obj)
        UserReferrerFactory(referrer=ref)
        self.assertEqual(obj.count_users(), 1)


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


class UserReferrerTestCase(TestCase):
    def test_model(self):
        obj = UserReferrerFactory()
        self.assertTrue(obj.pk)

    def test_repr(self):
        obj = UserReferrerFactory()
        self.assertEqual(str(obj), "{} -> {}".format(obj.user.username, obj.referrer.name))

    def test_manager_apply_referrer_no_ref(self):
        user = UserFactory()
        request = HttpRequest()
        request.session = {}
        UserReferrer.objects.apply_referrer(user, request)
        with self.assertRaises(UserReferrer.DoesNotExist):
            user.user_referrer

    def test_manager_apply_referrer(self):
        referrer = ReferrerFactory()
        user = UserFactory()
        request = HttpRequest()
        request.session = {settings.SESSION_KEY: referrer.pk}
        UserReferrer.objects.apply_referrer(user, request)
        self.assertEqual(user.user_referrer.referrer, referrer)
