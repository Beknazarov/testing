# -*- coding: utf-8 -*-

import datetime
from models import UserActivationKey
from django import forms
from django.core.mail import send_mail
from profiles.models import MyUser
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    # Override of clean method for password check
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return self.cleaned_data

    # Override of save method for saving both User and UserActivationKey objects
    def save(self, datas):
        saveuser = MyUser.objects.create_user(
                    username=datas['username'],
                    first_name=datas['first_name'],
                    last_name=datas['last_name'],
                    email=datas['email'],
                    password=datas['password1'])
        saveuser.is_active = False
        saveuser.save()
        profil = UserActivationKey()
        profil.user = saveuser
        profil.activation_key = datas['activation_key']
        profil.key_expires = datetime.datetime.strftime(
            datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
        profil.save()
        return saveuser

    # Activation email sending
    def emailActivation(self, datas):
        email_subject = 'Подтверждение регистрации'
        email_body = "Hey %s, thanks for signing up. \
                    To activate your account, click this link within 48hours \
                    http://127.0.0.1:8000/accounts/confirm/%s" % (datas['username'],
                                                                  datas['activation_key'])

        send_mail(
            email_subject,
            email_body,
            'myemail@example.com',
            [datas['email']],
            fail_silently=False)
