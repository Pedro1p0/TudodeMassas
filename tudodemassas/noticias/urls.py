from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticia_list_view, name='noticias'),
    path('<int:id>/', views.noticia_detail_view, name='noticia_detail'),
    path('criar/', views.noticia_create_view, name='criar_noticia'),
    path('<int:id>/editar/', views.noticia_update_view, name='editar_noticia'),
    path('<int:id>/excluir/', views.noticia_delete_view, name='excluir_noticia'),
]
