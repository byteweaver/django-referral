# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'Campaign.start_date'
        db.add_column(
            "referral_campaign",
            "start_date",
            self.gf("django.db.models.fields.DateTimeField")(null=True, blank=True),
            keep_default=False,
        )

        # Adding field 'Campaign.end_date'
        db.add_column(
            "referral_campaign",
            "end_date",
            self.gf("django.db.models.fields.DateTimeField")(null=True, blank=True),
            keep_default=False,
        )

        # Adding field 'Referrer.display_name'
        db.add_column(
            "referral_referrer",
            "display_name",
            self.gf("django.db.models.fields.CharField")(
                max_length=255, null=True, blank=True
            ),
            keep_default=False,
        )

        # Adding field 'Referrer.campaign_only'
        db.add_column(
            "referral_referrer",
            "campaign_only",
            self.gf("django.db.models.fields.BooleanField")(default=False),
            keep_default=False,
        )

    def backwards(self, orm):
        # Deleting field 'Campaign.start_date'
        db.delete_column("referral_campaign", "start_date")

        # Deleting field 'Campaign.end_date'
        db.delete_column("referral_campaign", "end_date")

        # Deleting field 'Referrer.display_name'
        db.delete_column("referral_referrer", "display_name")

        # Deleting field 'Referrer.campaign_only'
        db.delete_column("referral_referrer", "campaign_only")

    models = {
        "auth.group": {
            "Meta": {"object_name": "Group"},
            "id": ("django.db.models.fields.AutoField", [], {"primary_key": "True"}),
            "name": (
                "django.db.models.fields.CharField",
                [],
                {"unique": "True", "max_length": "80"},
            ),
            "permissions": (
                "django.db.models.fields.related.ManyToManyField",
                [],
                {
                    "to": "orm['auth.Permission']",
                    "symmetrical": "False",
                    "blank": "True",
                },
            ),
        },
        "auth.permission": {
            "Meta": {
                "ordering": "(u'content_type__app_label', u'content_type__model', u'codename')",
                "unique_together": "((u'content_type', u'codename'),)",
                "object_name": "Permission",
            },
            "codename": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "content_type": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {"to": "orm['contenttypes.ContentType']"},
            ),
            "id": ("django.db.models.fields.AutoField", [], {"primary_key": "True"}),
            "name": ("django.db.models.fields.CharField", [], {"max_length": "50"}),
        },
        "auth.user": {
            "Meta": {"object_name": "User"},
            "date_joined": (
                "django.db.models.fields.DateTimeField",
                [],
                {"default": "datetime.datetime.now"},
            ),
            "email": (
                "django.db.models.fields.EmailField",
                [],
                {"max_length": "75", "blank": "True"},
            ),
            "first_name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "30", "blank": "True"},
            ),
            "groups": (
                "django.db.models.fields.related.ManyToManyField",
                [],
                {"to": "orm['auth.Group']", "symmetrical": "False", "blank": "True"},
            ),
            "id": ("django.db.models.fields.AutoField", [], {"primary_key": "True"}),
            "is_active": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "True"},
            ),
            "is_staff": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "False"},
            ),
            "is_superuser": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "False"},
            ),
            "last_login": (
                "django.db.models.fields.DateTimeField",
                [],
                {"default": "datetime.datetime.now"},
            ),
            "last_name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "30", "blank": "True"},
            ),
            "password": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "128"},
            ),
            "user_permissions": (
                "django.db.models.fields.related.ManyToManyField",
                [],
                {
                    "to": "orm['auth.Permission']",
                    "symmetrical": "False",
                    "blank": "True",
                },
            ),
            "username": (
                "django.db.models.fields.CharField",
                [],
                {"unique": "True", "max_length": "30"},
            ),
        },
        "contenttypes.contenttype": {
            "Meta": {
                "ordering": "('name',)",
                "unique_together": "(('app_label', 'model'),)",
                "object_name": "ContentType",
                "db_table": "'django_content_type'",
            },
            "app_label": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "id": ("django.db.models.fields.AutoField", [], {"primary_key": "True"}),
            "model": ("django.db.models.fields.CharField", [], {"max_length": "100"}),
            "name": ("django.db.models.fields.CharField", [], {"max_length": "100"}),
        },
        "referral.campaign": {
            "Meta": {"ordering": "['name']", "object_name": "Campaign"},
            "description": (
                "django.db.models.fields.TextField",
                [],
                {"null": "True", "blank": "True"},
            ),
            "end_date": (
                "django.db.models.fields.DateTimeField",
                [],
                {"null": "True", "blank": "True"},
            ),
            "id": ("django.db.models.fields.AutoField", [], {"primary_key": "True"}),
            "name": (
                "django.db.models.fields.CharField",
                [],
                {"unique": "True", "max_length": "255"},
            ),
            "pattern": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "255", "blank": "True"},
            ),
            "start_date": (
                "django.db.models.fields.DateTimeField",
                [],
                {"null": "True", "blank": "True"},
            ),
        },
        "referral.referrer": {
            "Meta": {"ordering": "['name']", "object_name": "Referrer"},
            "campaign": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {
                    "blank": "True",
                    "related_name": "'referrers'",
                    "null": "True",
                    "to": "orm['referral.Campaign']",
                },
            ),
            "campaign_only": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "False"},
            ),
            "creation_date": (
                "django.db.models.fields.DateTimeField",
                [],
                {"auto_now_add": "True", "blank": "True"},
            ),
            "description": (
                "django.db.models.fields.TextField",
                [],
                {"null": "True", "blank": "True"},
            ),
            "display_name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "255", "null": "True", "blank": "True"},
            ),
            "id": ("django.db.models.fields.AutoField", [], {"primary_key": "True"}),
            "name": (
                "django.db.models.fields.CharField",
                [],
                {"unique": "True", "max_length": "255"},
            ),
        },
        "referral.userreferrer": {
            "Meta": {"ordering": "['referrer__name']", "object_name": "UserReferrer"},
            "id": ("django.db.models.fields.AutoField", [], {"primary_key": "True"}),
            "referrer": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {"related_name": "'users'", "to": "orm['referral.Referrer']"},
            ),
            "user": (
                "django.db.models.fields.related.OneToOneField",
                [],
                {
                    "related_name": "'user_referrer'",
                    "unique": "True",
                    "to": "orm['auth.User']",
                },
            ),
        },
    }

    complete_apps = ["referral"]
