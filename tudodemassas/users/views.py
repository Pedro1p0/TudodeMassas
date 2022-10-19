from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from receitas.models import receita
from django.core.paginator import Paginator
# Create your views here.

def login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, "users/login.html",context)


    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    return render(request, "users/logout.html",{})


    
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, 'users/cadastro.html' , context)

def home_view(request):
    return render(request, 'home-view.html')

def noticias_view(request):
    return render(request, 'noticias.html')

def sobre_view(request):
    return render(request,'sobre.html')


def perfil_view(request):
    receita_queryset = receita.objects.all()
    p = Paginator(receita.objects.all().filter(user = request.user), 5)
    page = request.GET.get('page')
    receitas = p.get_page(page)
    context = { 
        "queryset":receita_queryset,
        "receitas": receitas,
    }


    return render(request,"perfil.html", context = context)