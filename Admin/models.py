from django.db import models
from myapp.models import *

# Create your models here.

class Admin(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    pic = models.FileField(upload_to = 'Profile', default='default.jpg')

    def __str__(self):
        return self.fname + " " + self.lname
        
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category