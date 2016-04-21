# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f ')),
                ('first_name', models.CharField(max_length=100, verbose_name='\u0418\u043c\u044f ')),
                ('last_name', models.CharField(max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f ')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=profiles.models.user_avatar_upload, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440 ')),
                ('is_active', models.BooleanField(default=False, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0439 ')),
                ('is_admin', models.BooleanField(default=False, verbose_name='\u0421\u0443\u043f\u0435\u0440\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c ')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='\u0423\u0447\u0438\u0442\u0435\u043b\u044c ')),
                ('is_student', models.BooleanField(default=True, verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442 ')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 ')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
            },
        ),
    ]
