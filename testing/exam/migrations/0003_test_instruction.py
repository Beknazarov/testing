# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_remove_test_instruction'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='instruction',
            field=models.TextField(null=True, blank=True),
        ),
    ]
