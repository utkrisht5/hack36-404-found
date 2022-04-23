from datetime import datetime
from django.db.models.deletion import CASCADE, DO_NOTHING, RESTRICT
from django.db import models

# Create your models here.


class Victim(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    phone = models.IntegerField()
    address = models.TextField(null=True)
    pincode = models.IntegerField()


class Authority(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    address = models.TextField(null=True)
    pincode = models.IntegerField()
    field = models.TextField(default="All", null=True)


class Complain(models.Model):
    subject = models.CharField(max_length=10000)
    description = models.TextField()
    date = models.DateField()
    address = models.TextField(null=True)
    pincode = models.IntegerField()
    type = models.CharField(null=True, max_length=1000)
    person = models.CharField(max_length=1000, null=True)
    scope = models.CharField(null=True, max_length=1000)


class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
