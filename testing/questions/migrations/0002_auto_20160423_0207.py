# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.CharField(choices=[(b'Many', b'Many'), (b'TrueFalse', b'TrueFalse'), (b'One', b'One'), (b'Esse', b'Esse')], max_length=20, null=True),
        ),
    ]
