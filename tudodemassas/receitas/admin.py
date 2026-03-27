from django.contrib import admin
from .models import Receita


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'user', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'user__username')
