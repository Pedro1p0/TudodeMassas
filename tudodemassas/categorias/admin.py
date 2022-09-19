from django.contrib import admin
from .models import Categoria

# Register your models here.
class ListandoCategorias(admin.ModelAdmin):
    list_display=('id','nome_categoria')
    list_display_links=('id', 'nome_categoria')
    search_fields=('nome_categoria',)#buscando

admin.site.register(Categoria,ListandoCategorias)