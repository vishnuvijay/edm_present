# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.contrib.auth.decorators import login_required
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


@login_required
def add_donations(request):
    template_name = 'ics_tool/add_donations.html'

    if request.method == "GET":
        results = Donors.objects.all()
        return render(request, template_name,{'results':results})
    else:
        return render(request,template_name)
