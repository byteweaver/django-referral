import factory

from referral.models import Campaign, Referrer


class CampaignFactory(factory.Factory):
    FACTORY_FOR = Campaign

    name = "Test Campaign"
    description = "Some long test description"

class ReferrerFactory(factory.Factory):
    FACTORY_FOR = Referrer

    name = "Test Referrer"
    description = "Some long test description"

