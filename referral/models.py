from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

import settings


class Campaign(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Referrer(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    creation_date = models.DateTimeField(_("Creation date"), auto_now_add=True)
    campaign = models.ForeignKey(Campaign, verbose_name=_("Campaign"), blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class UserReferrerManager(models.Manager):
    def apply_referrer(self, user, request):
        try:
            referrer = request.session.pop(settings.SESSION_KEY)
        except KeyError:
            pass
        else:
            user_referrer = UserReferrer(user=user, referrer=referrer)
            user_referrer.save()

class UserReferrer(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), related_name='referrer')
    referrer = models.ForeignKey(Referrer, verbose_name=_("Referrer"), related_name='users')

    objects = UserReferrerManager()

    class Meta:
        ordering = ['referrer__name']

    def __unicode__(self):
        return "%s -> %s" % (self.user.username, self.referrer.name)

