from django.db import models
from django.utils.translation import ugettext_lazy as _


class Campaign(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        ordering['name']

    def __unicode__(self):
        return self.name

class Referrer(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description models.TextField(_("Description"), blank=True, null=True)
    creation_date = models.DateTimeField(_("Creation date"), auto_now_add=True)
    campaign = models.ForeignKey(_("Campaign"), blank=True, null=True)

    class Meta:
        ordering['name']

    def __unicode__(self):
        return self.name

