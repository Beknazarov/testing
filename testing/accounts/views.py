# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            message = "User is valid, active and authenticated"
            return redirect('/admin/')
        else:
            message = "The password is valid, but the account has bees disabled"
    else:
        message = "The username and password were incorrect"
    return render(request, 'accounts/signin.html', {'error_message': message})


def signout(request):
    logout(request)
    return redirect('/')
