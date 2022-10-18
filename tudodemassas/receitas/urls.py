from django.urls import re_path,path
from . import views 

urlpatterns = [ 
    path('receita/<int:id>/',views.receita_detail_view, name = 'detail_receita'),
    path('receitas/',views.receita_list_view, name = 'lista_receita'),
]