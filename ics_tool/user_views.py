# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.template import Context
import datetime
from django.http import HttpResponse
import re

from .forms import *
from .models import *


def health(request):
    return HttpResponse("3")

def user_login(request):
    template_name = 'ics_tool/login.html'

    if request.method == "GET":
        return render(request, template_name)

    form = LoginForm(request.POST)
    if form.is_valid():
      username       = request.POST.get('username', '')
      password       = request.POST.get('password', '')

      user = authenticate(username=username, password=password)

      if user:
            if user.is_active:
                login(request, user)
                return render(request,'ics_tool/home.html',{})
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
      else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details"
            return HttpResponse("Invalid login details supplied.")


    print(form.errors)

    return render(request,'ics_tool/login.html',{})

def user_logout(request):
    logout(request)
    return render(request,'ics_tool/logout.html',{})
