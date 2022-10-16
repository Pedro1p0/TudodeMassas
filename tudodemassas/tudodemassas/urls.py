"""tudodemassas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import *

#  mantenha as URLS em ordem alfabética, menos aquelas que a ordem importa !!! Pedro Vitor 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/',logout_view),
    path('cadastro/',register_view),
    path('home/',home_view),
    path('noticias/',noticias_view),
    path('sobre/',sobre_view),

]
