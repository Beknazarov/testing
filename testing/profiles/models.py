# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):  # !!!!!!
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, password=password, username=username,)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


def user_avatar_upload(instance, filename):
    return 'uploads/{0}/avatar/{1}/'.format(instance.username, filename)


class MyUser(AbstractBaseUser):
    email = models.EmailField('Email', max_length=255, unique=True,)
    username = models.CharField(u'Имя пользователя ', max_length=100, unique=True)
    first_name = models.CharField(u'Имя ', max_length=100)
    last_name = models.CharField(u'Фамилия ', max_length=100)
    avatar = models.ImageField(u'Аватар ', blank=True, null=True, upload_to=user_avatar_upload)
    is_active = models.BooleanField(u'Активный ', default=False)
    is_admin = models.BooleanField(u'Суперпользователь ', default=False)
    is_teacher = models.BooleanField(u'Учитель ', default=False)
    is_student = models.BooleanField(u'Студент ', default=True)
    date_joined = models.DateTimeField(u'Дата регистрации ', auto_now_add=True)

    objects = MyUserManager()

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

    def __unicode__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def avatar_pic(self):
        if self.avatar:
            return u'<img src="%s"  width="100" height="100"/>' % (self.avatar.url)
    avatar_pic.short_description = u'Аватар'
    avatar_pic.allow_tags = True

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
