from django.test import TestCase
from django.http import HttpRequest

from referral.middleware import ReferrerMiddleware
from referral.models import Referrer
from referral import settings


class ReferrerMiddlewareTest(TestCase):
    def setUp(self):
        self.ref_middleware = ReferrerMiddleware()
        self.request = HttpRequest()
        self.request.session = {}

    def test_process_request_no_ref(self):
        self.ref_middleware.process_request(self.request)
        self.assertEqual(Referrer.objects.all().count(), 0)

    def test_process_request_new_ref(self):
        self.request.GET[settings.GET_PARAMETER] = "new_ref"
        self.ref_middleware.process_request(self.request)
        self.assertEqual(Referrer.objects.all()[0].name, "new_ref")

    def test_process_request_new_ref_no_autocreate(self):
        settings.AUTO_CREATE = False
        self.request.GET[settings.GET_PARAMETER] = "new_ref"
        self.ref_middleware.process_request(self.request)
        self.assertEqual(Referrer.objects.count(), 0)
        settings.AUTO_CREATE = True

    def test_referral_case_sensitive(self):
        settings.CASE_SENSITIVE = True
        self.request.GET[settings.GET_PARAMETER] = "new_ref"
        self.ref_middleware.process_request(self.request)
        self.assertEqual(Referrer.objects.count(), 1)

        self.request.GET[settings.GET_PARAMETER] = "NEW_REF"
        self.ref_middleware.process_request(self.request)
        self.assertEqual(Referrer.objects.count(), 2)

        self.assertEqual(Referrer.objects.filter(name='new_ref').count(), 1)
        self.assertEqual(Referrer.objects.filter(name='NEW_REF').count(), 1)
        settings.CASE_SENSITIVE = False

    def test_referral_case_insensitive(self):
        self.request.GET[settings.GET_PARAMETER] = "new_ref"
        self.ref_middleware.process_request(self.request)
        self.assertEqual(Referrer.objects.count(), 1)

        self.request.GET[settings.GET_PARAMETER] = "NEW_REF"
        self.ref_middleware.process_request(self.request)
        self.assertEqual(Referrer.objects.count(), 1)
