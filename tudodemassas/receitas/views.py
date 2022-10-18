from site import USER_BASE
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import ReceitaForm, receita
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


def form_modelform(request):
    user = request.user.id
    if request.method=='GET':
        form =ReceitaForm()
        context = {
            'form':form
        }
        return render(request,"criar_receita.html",context=context)
    else:
        form=ReceitaForm( request.POST)
        if form.is_valid():
            receita =form.save()
            form = ReceitaForm()

        context = {
            'form':form,
        }
        return render(request,"criar_receita.html",context=context)