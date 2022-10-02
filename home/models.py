from django.db import models

# Create your models here.
class Form(models.Model):
    fname = models.CharField(max_length=15)
    lname =  models.CharField(max_length=15)
    email =  models.CharField(max_length=15)
    description = models.TextField()