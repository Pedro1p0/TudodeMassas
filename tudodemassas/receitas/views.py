from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Receita
from .forms import ReceitaForm

RECEITAS_POR_PAGINA = 9


def _paginar(queryset, request, por_pagina=RECEITAS_POR_PAGINA):
    paginator = Paginator(queryset, por_pagina)
    return paginator.get_page(request.GET.get('page'))


def receita_list_view(request):
    q = request.GET.get('q', '').strip()
    queryset = Receita.objects.all()
    if q:
        queryset = queryset.filter(
            Q(name__icontains=q) | Q(ingredientes__icontains=q) | Q(category__icontains=q)
        )
    context = {
        "page_obj": _paginar(queryset, request),
        "titulo": "Todas as Receitas",
        "query": q,
    }
    return render(request, "receitas/receitas_list.html", context=context)


def receita_detail_view(request, id=None):
    receita_obj = get_object_or_404(Receita, id=id)
    context = {
        "object": receita_obj,
    }
    return render(request, "receitas/receitas_detail.html", context=context)


def receita_list_pizza_view(request):
    q = request.GET.get('q', '').strip()
    queryset = Receita.objects.filter(category=Receita.Categoria.PIZZAS)
    if q:
        queryset = queryset.filter(Q(name__icontains=q) | Q(ingredientes__icontains=q))
    context = {
        "page_obj": _paginar(queryset, request),
        "titulo": "Pizzas",
        "query": q,
    }
    return render(request, "receitas/receitas_list.html", context=context)


def receita_list_massas_view(request):
    q = request.GET.get('q', '').strip()
    queryset = Receita.objects.filter(category=Receita.Categoria.MASSAS)
    if q:
        queryset = queryset.filter(Q(name__icontains=q) | Q(ingredientes__icontains=q))
    context = {
        "page_obj": _paginar(queryset, request),
        "titulo": "Massas",
        "query": q,
    }
    return render(request, "receitas/receitas_list.html", context=context)


@login_required
def receita_create_view(request):
    form = ReceitaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        receita = form.save(commit=False)
        receita.user = request.user
        receita.save()
        messages.success(request, 'Receita criada com sucesso!')
        return redirect('detail_receita', id=receita.id)
    return render(request, 'receitas/receita_form.html', {'form': form, 'action': 'Criar'})


@login_required
def receita_update_view(request, id):
    receita = get_object_or_404(Receita, id=id)
    if receita.user != request.user:
        raise PermissionDenied
    form = ReceitaForm(request.POST or None, request.FILES or None, instance=receita)
    if form.is_valid():
        form.save()
        messages.success(request, 'Receita atualizada com sucesso!')
        return redirect('detail_receita', id=receita.id)
    return render(request, 'receitas/receita_form.html', {'form': form, 'action': 'Editar'})


@login_required
def receita_delete_view(request, id):
    receita = get_object_or_404(Receita, id=id)
    if receita.user != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        receita.delete()
        messages.success(request, 'Receita excluída com sucesso.')
        return redirect('perfil')
    return render(request, 'receitas/receita_confirm_delete.html', {'object': receita})
