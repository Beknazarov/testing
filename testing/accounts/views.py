# -*- coding: utf-8 -*-

import hashlib
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.utils import timezone
from models import UserActivationKey
from forms import *

from django.contrib.auth import logout


def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            message = "User is valid, active and authenticated"
            return redirect('/admin/')  # Пока админ, потом в профиль
        else:
            message = "The password is valid, but the account has bees disabled"
    else:
        message = "The username and password were incorrect"
    return render(request, '', {'error_message': message})


def signup(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        datas = {}
        datas['username'] = form.cleaned_data['username']
        datas['first_name'] = form.cleaned_data['first_name']
        datas['last_name'] = form.cleaned_data['last_name']
        datas['email'] = form.cleaned_data['email']
        datas['password1'] = form.cleaned_data['password1']

        # We will generate a random activation key
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        usernamesalt = datas['username']
        if isinstance(usernamesalt, unicode):
            usernamesalt = usernamesalt.encode('utf8')
        datas['activation_key'] = hashlib.sha1(salt+usernamesalt).hexdigest()
        form.emailActivation(datas)
        form.save(datas)
        # Send email with activation key

        return redirect('')  # /profiles/profile/
    return render(request, "accounts/signup.html", {'form': form})


def register_confirm(request, activation_key):
    activation_expired = False
    already_active = False
    profil = get_object_or_404(UserActivationKey, activation_key=activation_key)
    if profil.user.is_active == False:  # !!! Надо проверить !!!
        if timezone.now() > profil.key_expires:
            activation_expired = True
            # Display : offer to user to have another activation
            # link (a link in template sending to the view new_activation_link)
            id_user = profil.user.id
        else:  # Activation successful
            profil.user.is_active = True
            profil.user.save()

    # If user is already active, simply display error message
    else:
        already_active = True  # Display : error message
    return render(request, 'accounts/profile.html', locals())


def signout(request):
    logout(request)
    return redirect('/')
