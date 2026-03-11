from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from receitas.models import Receita

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bem-vindo de volta, {user.username}!')
            return redirect('home')
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, "users/login.html", context)


    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Você saiu com sucesso.')
        return redirect('login')
    return render(request, "users/logout.html", {})


    
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Conta criada com sucesso! Faça login.')
        return redirect('login')
    context = {'form': form}
    return render(request, 'users/cadastro.html', context)

def home_view(request):
    from receitas.models import Receita
    from noticias.models import Noticia
    receitas_recentes = Receita.objects.all()[:6]
    noticias_recentes = Noticia.objects.all()[:3]
    categorias = Receita.Categoria.choices
    return render(request, 'home-view.html', {
        'receitas_recentes': receitas_recentes,
        'noticias_recentes': noticias_recentes,
        'categorias': categorias,
    })

def noticias_view(request):
    return redirect('noticias')

def sobre_view(request):
    from receitas.models import Receita
    categorias = [c.label for c in Receita.Categoria]
    return render(request, 'sobre.html', {'categorias': categorias})


@login_required
def perfil_view(request):
    receitas_usuario = Receita.objects.filter(user=request.user)
    context = {
        "queryset": receitas_usuario
    }
    return render(request, "perfil.html", context=context)