from tokenize import Name
from django.db import models

# Create your models here.


class User(models.Model):
    SELECT_TYPE = [(1,"homem"),(2,"mulher")]
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = SELECT_TYPE
    

