from unicodedata import category
from django.db import models
from django.conf import settings
from django import forms
# Create your models here.

class receita(models.Model):
    name = models.CharField(max_length=30, blank=False, null=True)
    Pizzas = 'Pizzas'
    Massas = 'Massas'
    Salgados = 'Salgados'
    Bolos = 'Bolos'
    Tortas = 'Tortas'
    Pao = 'Pão Caseiro'
    category_list = (
        (Pizzas, 'Pizzas'),
        (Massas, 'Massas'),
        (Salgados, 'Salgados'),
        (Bolos, 'Bolos'),
        (Tortas, 'Tortas'),
        (Pao, 'Pão Caseiro'),
        )
    category = models.CharField(max_length=20, choices=category_list, default='category')
    ingredientes = models.TextField(blank=False, null=True)
    modo_de_preparo = models.TextField(blank=False, null=True)
    #created_at = models.DateField(default=datetime.today, blank=True)
    #updated_at = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name
class ReceitaForm(forms.ModelForm):
    class Meta:
        model=receita
        fields= '__all__'
            