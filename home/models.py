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

class Complain(models.Model):
    subject = models.CharField(max_length=10000)
    description = models.TextField()
    date = models.DateField()
    address = models.TextField(null=True)
    pincode = models.IntegerField()
    person = models.ForeignKey(Victim, on_delete=CASCADE, null=True)