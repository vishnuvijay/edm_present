# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Database Tables should be defined as class object
class Customer(models.Model):
    CustomerId          = models.IntegerField(unique=True)
    CustomerName        = models.CharField(max_length=200)

class Feedback(models.Model):
    Feedback = models.CharField(max_length=255)

class Donors(models.Model):
    OrganizationName    = models.CharField(max_length=100)
    Salutation          = models.CharField(max_length=100)
    FirstName           = models.CharField(max_length=100)
    LastName            = models.CharField(max_length=100)
    Email               = models.EmailField(max_length=100)
    PhoneNumber         = models.CharField(max_length=15)
    Comments            = models.CharField(max_length=100)
    StreetAddress       = models.CharField(max_length=100)
    City                = models.CharField(max_length=100)
    State               = models.CharField(max_length=100)
    Zip                 = models.CharField(max_length=100)
    ICS                 = models.CharField(max_length=2)

class SearchDonor(models.Model):

    SearchQuery        = models.CharField(max_length=255)

class Donations(models.Model):
    donationID    = models.IntegerField(primary_key=True)
    donor_id      = models.ForeignKey(Donors)
    donation_date = models.DateField()
    comments      = models.CharField(max_length=100)

class InKind(models.Model):
    donationID   = models.ForeignKey(Donations)
    description  = models.CharField(max_length=1000)
    isack_sent   = models.BooleanField(default=False)
    approxValue  = models.IntegerField()

class CatDonations(models.Model):
    donationID   = models.ForeignKey(Donations)
    Grocery      = models.IntegerField()
    Meat         = models.IntegerField()
    Bread        = models.IntegerField()
    Produce      = models.IntegerField()
    Toiletries   = models.IntegerField()
    Diaper       = models.IntegerField()
    Other        = models.IntegerField()
    TotalPounds  = models.IntegerField()
    desc         = models.CharField(max_length=1000)

class GOLF(models.Model):
    donationID   = models.ForeignKey(Donations)
    Donation     = models.CharField(max_length=1000)
    Value        = models.IntegerField()
    Contact      = models.CharField(max_length=100)
    ReceivedBy   = models.CharField(max_length=100)

class GenericDonation(models.Model):
    EventName    = models.CharField(max_length=100)
    OrgName      = models.CharField(max_length=100)
    Contact      = models.CharField(max_length=100)
    FoodDesc     = models.CharField(max_length=100)
    Gallons      = models.CharField(max_length=100)
    Servings     = models.IntegerField
    avgCost      = models.IntegerField()
    totalCost    = models.IntegerField()
    GenDonation  = models.CharField(max_length=1000)
    Value        = models.IntegerField()
    ReceivedDate = models.DateField()
    Comments     = models.CharField(max_length=1000)
