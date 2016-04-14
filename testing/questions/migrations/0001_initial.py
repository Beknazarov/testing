# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompositionAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', redactor.fields.RedactorField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
            ],
        ),
        migrations.CreateModel(
            name='ManyChoiceAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('variation', models.CharField(max_length=100, null=True, blank=True)),
                ('text', redactor.fields.RedactorField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
                ('right', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', redactor.fields.RedactorField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('point', models.IntegerField()),
                ('answer_type', models.CharField(max_length=20, null=True, choices=[(b'Many', b'Many'), (b'TrueFalse', b'TrueFalse'), (b'SelfAnswer', b'SelfAnswer'), (b'Esse', b'Esse')])),
                ('test', models.ForeignKey(to='exam.Test')),
            ],
        ),
        migrations.CreateModel(
            name='TrueFalseAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('true', models.BooleanField(default=False)),
                ('false', models.BooleanField()),
                ('question', models.ForeignKey(to='questions.Question')),
            ],
        ),
        migrations.AddField(
            model_name='manychoiceanswer',
            name='question',
            field=models.ForeignKey(to='questions.Question'),
        ),
        migrations.AddField(
            model_name='compositionanswer',
            name='question',
            field=models.ForeignKey(to='questions.Question'),
        ),
    ]
