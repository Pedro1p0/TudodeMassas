from socket import fromshare
from django import forms
from .models import receita

class ReceitaModelForm(forms.ModelForm):
    class Meta:
        model = receita
        fields = ['name','category','ingredientes','modo_de_preparo','user']