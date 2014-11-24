# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('pattern', models.CharField(help_text=b'All auto created referrers containing this pattern will be associated with this campaign', max_length=255, verbose_name='Referrer pattern', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Campaign',
                'verbose_name_plural': 'Campaigns',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Referrer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('campaign', models.ForeignKey(related_name='referrers', verbose_name='Campaign', blank=True, to='referral.Campaign', null=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Referrer',
                'verbose_name_plural': 'Referrers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserReferrer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referrer', models.ForeignKey(related_name='users', verbose_name='Referrer', to='referral.Referrer')),
                ('user', models.OneToOneField(related_name='user_referrer', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['referrer__name'],
                'verbose_name': 'User Referrer',
                'verbose_name_plural': 'User Referrers',
            },
            bases=(models.Model,),
        ),
    ]
