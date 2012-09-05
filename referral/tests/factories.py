from django.contrib.auth.models import User
import factory

from referral.models import Campaign, Referrer, UserReferrer

class UserFactory(factory.Factory):
    FACTORY_FOR = User

class CampaignFactory(factory.Factory):
    FACTORY_FOR = Campaign

    name = factory.Sequence(lambda n: "Test Campaign %s" % n)
    description = "Some long test description"

class ReferrerFactory(factory.Factory):
    FACTORY_FOR = Referrer

    name = factory.Sequence(lambda n: "Test Referrer %s" % n)
    description = "Some long test description"

class UserReferrerFactory(factory.Factory):
    FACTORY_FOR = UserReferrer

    user = factory.LazyAttribute(lambda a: UserFactory())
    referrer = factory.LazyAttribute(lambda a: ReferrerFactory())

