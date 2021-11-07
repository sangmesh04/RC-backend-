from abc import _FuncT
from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import Random

# Create your models here.

class signup(models.Model):
    id = Random(1000,99999)
    id = models.indexes() 
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    username = models.UniqueConstraint()
    college = models.CharField(max_length=122)
    year = models.SmallIntegerField(max_length=5)
    password = models.CharField(max_length=50)