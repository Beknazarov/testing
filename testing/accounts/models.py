from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class UserActivationKey(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saveuser')
    activation_key = models.CharField(max_length=100)
    key_expires = models.DateTimeField()
