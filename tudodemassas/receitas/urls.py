from django.urls import re_path,path
from . import views 

urlpatterns = [ 
   
    path('receitas/',views.receita_list_view, name = 'lista_receita'),
    path('receita/<int:id>/',views.receita_detail_view, name = 'detail_receita'),
    path('receitas/buscar/',views.receita_search_view, name = 'busca_receita'),
    path('receitas/Pizza/',views.receita_list_pizza_view, name = 'lista_Pizza_receita'),
    path('receitas/Massas/',views.receita_list_massas_view, name = 'lista_Massas_receita'),
    path('receitas/Bolos/',views.receita_list_bolos_view, name = 'lista_Bolos_receita'),
    path('receitas/Salgado/',views.receita_list_salgado_view, name = 'lista_Salgado_receita'),
    path('receitas/paocaseiro/',views.receita_list_pao_view, name = 'lista_pao_receita'),
    path('receitas/torta/',views.receita_list_torta_view, name = 'lista_torta_receita'),
    path('receitas/criar/',views.receita_create_view,name='cria')
    
]