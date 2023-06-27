# Generated by Django 2.2.15 on 2023-06-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='pattern',
            field=models.CharField(blank=True, help_text='All auto created referrers containing this pattern will be associated with this campaign', max_length=255, verbose_name='Referrer pattern'),
        ),
    ]
