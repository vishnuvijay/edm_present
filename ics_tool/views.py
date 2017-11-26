# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.contrib.auth import authenticate, login, logout
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


def health(request):
    return HttpResponse("3")

def index(request):
    template_name = 'ics_tool/home.html'

    if request.method == "GET":
        cnt = Donors.objects.count()
        return render(request, template_name, {'cnt':cnt})

    form = SearchDataForm(request.POST)
    if form.is_valid():

      results = 'Welcome'

      return render(request,'ics_tool/home.html',{'Results' : results})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})


@login_required
def add_donor(request):
    template_name = 'ics_tool/add_donor.html'

    if request.method == "GET":
        return render(request, template_name)

    form = AddDonorForm(request.POST)
    if form.is_valid():
      OrganizationName = request.POST.get('OrganizationName', '')
      Salutation       = request.POST.get('Salutation', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      Email            = request.POST.get('Email', '')
      PhoneNumber      = request.POST.get('PhoneNumber', '')
      Comments         = request.POST.get('Comments', '')
      StreetAddress    = request.POST.get('StreetAddress', '')
      City             = request.POST.get('City', '')
      State            = request.POST.get('State', '')
      Zip              = request.POST.get('Zip', '')
      ICS              = request.POST.get('ICS', '')

      LoadDonorObj = Donors(OrganizationName=OrganizationName,Salutation=Salutation,FirstName=FirstName,LastName=LastName,
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,Zip=Zip,ICS=ICS)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/add_donor.html',{})

def edit_donor(request):
    template_name = 'ics_tool/add_donor.html'

    if request.method == "GET":
        pid = request.GET.get('id','')
        donors = Donors.objects.get(id=pid)
        return render(request, 'ics_tool/edit_donor.html',{'donors':donors})

    form = AddDonorForm(request.POST)
    if form.is_valid():
      pid              = request.POST.get('id','')
      OrganizationName = request.POST.get('OrganizationName', '')
      Salutation       = request.POST.get('Salutation', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      Email            = request.POST.get('Email', '')
      PhoneNumber      = request.POST.get('PhoneNumber', '')
      Comments         = request.POST.get('Comments', '')
      StreetAddress    = request.POST.get('StreetAddress', '')
      City             = request.POST.get('City', '')
      State            = request.POST.get('State', '')
      Zip              = request.POST.get('Zip', '')
      ICS              = request.POST.get('ICS', '')

      d = Donors.objects.get(id=pid)

      d.OrganizationName=OrganizationName
      d.Salutation=Salutation
      d.FirstName=FirstName
      d.LastName=LastName
      d.Email=Email
      d.PhoneNumber=PhoneNumber
      d.Comments=Comments
      d.StreetAddress=StreetAddress
      d.City=City
      d.State=State
      d.Zip=Zip
      d.ICS=ICS
      d.save()

      return render(request,'ics_tool/search_donor.html',{})

    print(form.errors)

    return render(request,'ics_tool/search_donor.html',{})

@login_required
def search_donor(request):

    template_name = 'ics_tool/search_donor.html'

    if request.method == "GET":
        return render(request, template_name)

    form = SearchDonorForm(request.POST)
    if form.is_valid():
      SearchQuery = request.POST.get('SearchQuery', '')

      results = Donors.objects.filter(Q(FirstName__icontains=SearchQuery)).values()

      return render(request,'ics_tool/donor_results.html',{'Results' : results})

    print(form.errors)

    return render(request,'ics_tool/search_donor.html',{})
