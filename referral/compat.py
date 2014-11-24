from django.conf import settings
import django

__all__ = ['User', 'AUTH_USER_MODEL']

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.USER')

# Django 1.5+ compatibility
if django.VERSION >= (1, 5):
    User = settings.AUTH_USER_MODEL
else:
    from django.contrib.auth.models import User
