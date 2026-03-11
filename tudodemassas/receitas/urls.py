from django.urls import path
from . import views

urlpatterns = [
    path('receita/<int:id>/', views.receita_detail_view, name='detail_receita'),
    path('receitas/', views.receita_list_view, name='lista_receita'),
    path('receitas/pizzas/', views.receita_list_pizza_view, name='lista_pizza_receita'),
    path('receitas/massas/', views.receita_list_massas_view, name='lista_massas_receita'),
    path('receitas/criar/', views.receita_create_view, name='criar_receita'),
    path('receita/<int:id>/editar/', views.receita_update_view, name='editar_receita'),
    path('receita/<int:id>/excluir/', views.receita_delete_view, name='excluir_receita'),
]