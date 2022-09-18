from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Categoria

# Create your views here.

def categoria(request,slug=None,*argws,**kwargs):
    categoria_obj=None
    if slug is not None :
        categoria_obj=Categoria.objects.get(nome_categoria=slug)
    context = {
        "categoria": categoria_obj,
    }
    return render(request,'categoria.html',context=context)
 