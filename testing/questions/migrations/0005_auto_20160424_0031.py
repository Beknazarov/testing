# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20160423_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compositionanswer',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.CharField(choices=[(b'Many', b'Many'), (b'TrueFalse', b'TrueFalse'), (b'Esse', b'Esse')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='truefalseanswer',
            name='false',
            field=models.BooleanField(default=False),
        ),
    ]
