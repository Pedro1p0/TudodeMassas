from django import forms
from .models import Receita

INPUT_CLASS = (
    "w-full border border-stone-300 rounded-lg px-3 py-2 text-stone-800 "
    "focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-transparent"
)
TEXTAREA_CLASS = (
    "w-full border border-stone-300 rounded-lg px-3 py-2 text-stone-800 "
    "focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-transparent resize-y"
)
SELECT_CLASS = (
    "w-full border border-stone-300 rounded-lg px-3 py-2 text-stone-800 bg-white "
    "focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-transparent"
)


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['name', 'category', 'ingredientes', 'modo_de_preparo', 'imagem']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Ex: Macarrão à Carbonara',
            }),
            'category': forms.Select(attrs={'class': SELECT_CLASS}),
            'ingredientes': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 6,
                'placeholder': 'Liste os ingredientes, um por linha...',
            }),
            'modo_de_preparo': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 8,
                'placeholder': 'Descreva o passo a passo do preparo...',
            }),
            'imagem': forms.ClearableFileInput(attrs={'class': INPUT_CLASS}),
        }
        labels = {
            'name': 'Nome da Receita',
            'category': 'Categoria',
            'ingredientes': 'Ingredientes',
            'modo_de_preparo': 'Modo de Preparo',
            'imagem': 'Imagem (opcional)',
        }
