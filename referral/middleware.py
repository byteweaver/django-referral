import settings
from models import Referrer


class ReferrerMiddleware():
    def process_request(self, request):
        if settings.GET_PARAMETER in request.GET:
            referrer = None
            referrer_name = request.GET[settings.GET_PARAMETER]
            try:
                referrer = Referrer.objects.get(name=referrer_name)
            except Referrer.DoesNotExist:
                if settings.AUTO_CREATE:
                    referrer = Referrer(name=referrer_name)
                    referrer.save()
                if settings.AUTO_ASSOCIATE:
                    referrer.match_campaign()
            finally:
                if not referrer is None:
                    request.session[settings.SESSION_KEY] = referrer

