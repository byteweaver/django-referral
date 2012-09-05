import factory

from referral.models import Campaign


class CampaignFactory(factory.Factory):
    FACTORY_FOR = Campaign

    name = "Test Campaign"
    description = "Some long test description"

