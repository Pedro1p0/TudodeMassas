from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import receita
# Create your views here.


def receita_list_view(request):
    receita_queryset = receita.objects.all()
    context = { 
        "queryset":receita_queryset,
    }
    return render(request,"receitas/receitas_list.html",context=context)

def receita_detail_view(request, id = None):
    receita_obj = None 
    if id is not None:
        receita_obj = receita.objects.get(id = id)
    context = {
        "object" : receita_obj,
        }

    return render(request,"receitas/receitas_detail.html",context=context)

def receita_list_pizza_view(request):
    receita_pizza_queryset = receita.objects.all().filter(category = 'Pizzas')
    context = { 
        "queryset":receita_pizza_queryset
    }
    return render(request,"receitas/receitas_pizza.html",context = context)


def receita_list_massas_view(request):
    receita_massas_queryset = receita.objects.all().filter(category = 'Massas')
    context = { 
        "queryset":receita_massas_queryset
    }
    return render(request,"receitas/receitas_massas.html",context = context)

