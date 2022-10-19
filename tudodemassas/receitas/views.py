from site import USER_BASE
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import ReceitaForm, receita
from django.contrib.auth.decorators import login_required
import datetime
from django.core.paginator import Paginator
from .forms import ReceitaModelForm
from django.db.models import F
# Create your views here.


def receita_list_view(request):
    receita_queryset = receita.objects.all()
    p = Paginator(receita.objects.all(), 5)
    page = request.GET.get('page')
    receitas = p.get_page(page)
    context = { 
        "queryset":receita_queryset,
        "receitas": receitas,
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
    receita_queryset = receita.objects.all().filter(category='Pizzas')
    p = Paginator(receita.objects.all().filter(category='Pizzas'), 5)
    page = request.GET.get('page')
    receitas = p.get_page(page)
    context = { 
        "queryset":receita_queryset,
        "receitas": receitas,
    }
    return render(request,"receitas/receitas_list.html",context=context)


def receita_list_massas_view(request):
    receita_queryset = receita.objects.all().filter(category='Massas')
    p = Paginator(receita.objects.all().filter(category='Massas'), 5)
    page = request.GET.get('page')
    receitas = p.get_page(page)
    context = { 
        "queryset":receita_queryset,
        "receitas": receitas,
    }
    return render(request,"receitas/receitas_list.html",context=context)

def receita_list_bolos_view(request):
    receita_queryset = receita.objects.all().filter(category='Bolos')
    p = Paginator(receita.objects.all().filter(category='Bolos'), 5)
    page = request.GET.get('page')
    receitas = p.get_page(page)
    context = { 
        "queryset":receita_queryset,
        "receitas": receitas,
    }
    return render(request,"receitas/receitas_list.html",context=context)

def receita_list_salgado_view(request):
    receita_queryset = receita.objects.all().filter(category='Salgados')
    p = Paginator(receita.objects.all().filter(category='Salgados'), 5)
    page = request.GET.get('page')
    receitas = p.get_page(page)
    context = { 
        "queryset":receita_queryset,
        "receitas": receitas,
    }
    return render(request,"receitas/receitas_list.html",context=context)

def receita_list_pao_view(request):
    receita_queryset = receita.objects.all().filter(category='Pão Caseiro')
    p = Paginator(receita.objects.all().filter(category='Pão Caseiro'), 5)
    page = request.GET.get('page')
    receitas = p.get_page(page)
    context = { 
        "queryset":receita_queryset,
        "receitas": receitas,
    }
    return render(request,"receitas/receitas_list.html",context=context)

def receita_list_torta_view(request):
    receita_queryset = receita.objects.all().filter(category='Tortas')
    p = Paginator(receita.objects.all().filter(category='Tortas'), 5)
    page = request.GET.get('page')
    receitas = p.get_page(page)
    context = { 
        "queryset":receita_queryset,
        "receitas": receitas,
    }
    return render(request,"receitas/receitas_list.html",context=context)



# def receita_create_view(CreateView):
#     template_name = 'receitas/criar_receita.html'
#     form_class = ReceitaModelForm
#     queryset = receita.objects.all()








@login_required(login_url = '../login')
def receita_create_view(request,*keys,**kwargs):
    if request.method=='GET':
        form =ReceitaForm()
        context = {
            'form':form
        }
        return render(request,"receitas/criar_receita.html",context=context)
    else:
        form=ReceitaForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user 
            print(form.instance.user) 
            #form.instance.creat = datetime.now 
            receita = form.save()
            form = ReceitaForm()

        context = {
            'form':form,
        }
        return render(request,"receitas/criar_receita.html",context=context)


def receita_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    receita_obj = None
    if query is not None:
        receita_query = receita.objects.get(id = query)
    context={
        "receita":receita_obj
    }
    return render(request,"receitas/busca.html",context=context)