# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20160423_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
    ]
