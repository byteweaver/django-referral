from django.test import TestCase
from django.http import HttpRequest

from referral.middleware import ReferrerMiddleware
from referral.models import Referrer 


class ReferrerMiddlewareTest(TestCase):
    def setUp(self):
        self.ref_middleware = ReferrerMiddleware()
        self.request = HttpRequest()
        self.request.session = {}

    def test_process_request_no_ref(self):
        self.ref_middleware.process_request(self.request)
        self.assertEqual(Referrer.objects.all().count(), 0)

