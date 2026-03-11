from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Noticia
from .forms import NoticiaForm


def noticia_list_view(request):
    q = request.GET.get('q', '').strip()
    noticias = Noticia.objects.all()
    if q:
        noticias = noticias.filter(Q(titulo__icontains=q) | Q(conteudo__icontains=q))
    paginator = Paginator(noticias, 6)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'noticias/noticias_list.html', {'page_obj': page_obj, 'query': q})


def noticia_detail_view(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticias/noticia_detail.html', {'noticia': noticia})


@login_required
def noticia_create_view(request):
    if not request.user.is_staff:
        raise PermissionDenied
    form = NoticiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        noticia = form.save(commit=False)
        noticia.autor = request.user
        noticia.save()
        messages.success(request, 'Notícia publicada com sucesso!')
        return redirect('noticia_detail', id=noticia.id)
    return render(request, 'noticias/noticia_form.html', {'form': form, 'action': 'Publicar'})


@login_required
def noticia_update_view(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if not request.user.is_staff:
        raise PermissionDenied
    form = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)
    if form.is_valid():
        form.save()
        messages.success(request, 'Notícia atualizada com sucesso!')
        return redirect('noticia_detail', id=noticia.id)
    return render(request, 'noticias/noticia_form.html', {'form': form, 'action': 'Editar'})


@login_required
def noticia_delete_view(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if not request.user.is_staff:
        raise PermissionDenied
    if request.method == 'POST':
        noticia.delete()
        messages.success(request, 'Notícia excluída.')
        return redirect('noticias')
    return render(request, 'noticias/noticia_confirm_delete.html', {'noticia': noticia})
