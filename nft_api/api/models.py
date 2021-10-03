from django.db import models
from django.db.models.base import Model
import jsonfield 
from django.db import models


# Create your models here.

class collection(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    abi=jsonfield.JSONField()
