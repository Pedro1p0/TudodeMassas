from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)
