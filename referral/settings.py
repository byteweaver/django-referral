from django.conf import settings

# Name of the referrer's get parameter name
GET_PARAMETER = getattr(settings, 'REFERRAL_GET_PARAMETER', 'ref')

# Name of the session variable storing the detected referrer
SESSION_KEY = getattr(settings, 'REFERRAL_SESSION_KEY', 'referrer')

# Should unknown referrers be auto created? Default: True
AUTO_CREATE = getattr(settings, 'REFERRAL_AUTO_CREATE', True)

# If this is set auto created referrers will be associated to a campaign that defines a matching pattern. Default: True
AUTO_ASSOCIATE = getattr(settings, 'REFERRAL_AUTO_ASSOCIATE', True)

# If this is set to True, referral names will be case-sensitive.
CASE_SENSITIVE = getattr(settings, 'REFERRAL_CASE_SENSITIVE', False)
