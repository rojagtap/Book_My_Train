from django.db import models


class Log(models.Model):
    Email_id = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Email_id


class User(models.Model):
    Names = models.CharField(max_length=100)
    Email_id = models.CharField(max_length=100)
    Phone_no = models.CharField(max_length=100)
    DOB = models.CharField(max_length=20)


class Book(models.Model):
    Source = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    Train_Name = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    CC_fare = models.CharField(max_length=100)
    Ac3_fare = models.CharField(max_length=100)
    Ac2_fare = models.CharField(max_length=100)
    Ac1_fare = models.CharField(max_length=100)
    Departure_time = models.CharField(max_length=100)
    Arrival_time = models.CharField(max_length=10)


class Bank(models.Model):
    Card_Number = models.CharField(max_length=16)
    Card_Holder = models.CharField(max_length=100)
    Expiry = models.CharField(max_length=20)
    CVV = models.CharField(max_length=3)
