from django.db import models
from myapp.models import *
from Admin.models import *

# Create your models here.

class Ins(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    pic = models.FileField(upload_to = 'Profile', default='default.jpg')

    def __str__(self):
        return self.fname + " " + self.lname

class Sub(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    pic = models.FileField(upload_to = 'Profile', default='default.jpg')

    def __str__(self):
        return self.fname + " " + self.lname