import factory

from referral.compat import User
from referral.models import Campaign, Referrer, UserReferrer

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

class CampaignFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Campaign

    name = factory.Sequence(lambda n: "Test Campaign %s" % n)
    description = "Some long test description"

class ReferrerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Referrer

    name = factory.Sequence(lambda n: "Test Referrer %s" % n)
    description = "Some long test description"

class UserReferrerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserReferrer

    user = factory.LazyAttribute(lambda a: UserFactory())
    referrer = factory.LazyAttribute(lambda a: ReferrerFactory())

