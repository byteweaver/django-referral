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

