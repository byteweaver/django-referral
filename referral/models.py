from django.db import models
from django.utils.translation import ugettext_lazy as _

from .compat import User
from . import settings


class Campaign(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    pattern = models.CharField(_("Referrer pattern"), blank=True, max_length=255,
        help_text="All auto created referrers containing this pattern will be associated with this campaign")

    class Meta:
        ordering = ['name']
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    def count_users(self):
        count = 0
        for referrer in self.referrers.all():
            count += referrer.count_users()
        return count
    count_users.short_description = _("User count")


class Referrer(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    creation_date = models.DateTimeField(_("Creation date"), auto_now_add=True)
    campaign = models.ForeignKey(Campaign, verbose_name=_("Campaign"), related_name='referrers', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = _("Referrer")
        verbose_name_plural = _("Referrers")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    def count_users(self):
        return self.users.count()
    count_users.short_description = _("User count")

    def match_campaign(self):
        for campaign in Campaign.objects.exclude(pattern=""):
            if campaign.pattern in self.name:
                self.campaign = campaign
                self.save()
                break


class UserReferrerManager(models.Manager):
    def apply_referrer(self, user, request):
        try:
            referrer = Referrer.objects.get(pk=request.session.pop(settings.SESSION_KEY))
        except KeyError:
            pass
        else:
            user_referrer = UserReferrer(user=user, referrer=referrer)
            user_referrer.save()


class UserReferrer(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), related_name='user_referrer')
    referrer = models.ForeignKey(Referrer, verbose_name=_("Referrer"), related_name='users')

    objects = UserReferrerManager()

    class Meta:
        ordering = ['referrer__name']
        verbose_name = _("User Referrer")
        verbose_name_plural = _("User Referrers")

    def __unicode__(self):
        return "%s -> %s" % (self.user.username, self.referrer.name)

    def __str__(self):
        return self.__unicode__()
