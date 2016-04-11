from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserActivationKey(models.Model):
    user = models.OneToOneField(User, related_name='saveuser')
    activation_key = models.CharField(max_length=100)
    key_expires = models.DateTimeField()
