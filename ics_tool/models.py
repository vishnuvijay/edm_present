# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Database Tables should be defined as class object
class Customer(models.Model):
    CustomerId          = models.IntegerField(unique=True)
    CustomerName        = models.CharField(max_length=200)

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

class DonationsLog(models.Model):

    logID           = models.IntegerField(primary_key=True)
    lastModifidDate = models.DateField()
    lastChangedBy   = models.CharField(max_length=100)


class Donations(models.Model):
    donationID =models.IntegerField(primary_key=True)
    donation_date=models.DateField()
    additional_comments=models.CharField(max_length=100)
    dontype=models.CharField(max_length=20)

class EBDGFOOD(models.Model):
    EDBGEvent_foodID= models.IntegerField(primary_key=True)
    ServingsPerGallon=models.IntegerField()
    EBDGtype=models.CharField(max_length=20)
    RestaurantName=models.CharField(max_length=100)

class EMPTYBOWLFOOD(models.Model):
    EmptyBowlEvent_foodID=models.IntegerField(primary_key=True)
    food_description=models.CharField(max_length=100)
    quantity=models.IntegerField()
    totalServings=models.IntegerField()

class FOOD(models.Model):
    foodEntryID=models.IntegerField(primary_key=True)
    foodtype=models.CharField(max_length=100)
    avgCost=models.IntegerField()
    totalPounds=models.IntegerField()
    totalValue=models.IntegerField()
    NoPounds=models.IntegerField()
    ServingsperPound=models.IntegerField()

class FOODCATEGORY(models.Model):
    donationID=models.ForeignKey(Donations, on_delete=models.CASCADE)
    categoryID=models.IntegerField()

class FOODENTRY(models.Model):
    CategoryID=models.ForeignKey(FOODCATEGORY, on_delete=models.CASCADE)
    foodEntryID=models.IntegerField(primary_key=True)

class FOODCATEGORYDESC(models.Model):
    categoryID=models.ForeignKey(FOODCATEGORY, on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
    categoryName=models.CharField(max_length=100)

class FUNDRAISINGEVENTS(models.Model):
    eventID=models.IntegerField(primary_key=True)
    estimatedValue=models.IntegerField()
    receivedDate=models.DateField()
    location=models.CharField(max_length=100)

class GOLF(models.Model):
    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE)
    dtype=models.CharField(max_length=100)

class ITEMS(models.Model):
    donationID=models.ForeignKey(Donations, on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
    isack_sent=models.BooleanField(default=False)
    approxValue=models.IntegerField()

class MONETARY (models.Model):
    donationID=models.ForeignKey(Donations, on_delete=models.CASCADE)
    amount=models.IntegerField()
    modeOfPayment=models.CharField(max_length=100)

class Reports(models.Model):
    reportID=models.IntegerField(primary_key=True)
    filename=models.CharField(max_length=100)
    reportgen_date=models.DateField()

class ServiceEvents(models.Model):
    service_detailID=models.IntegerField(primary_key=True)
    date_of_service=models.DateField()
    serviceID=models.IntegerField()

class EBDGRAFFLE(models.Model):
    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE)
    donation=models.CharField(max_length=100)

class EMPTYBOWLRAFFLEAUCTION(models.Model):
    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    receivedDate=models.DateField()
