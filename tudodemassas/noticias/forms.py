from django import forms
from .models import Noticia

INPUT_CLASS = (
    "w-full border border-stone-300 rounded-lg px-3 py-2 text-stone-800 "
    "focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-transparent"
)
TEXTAREA_CLASS = (
    "w-full border border-stone-300 rounded-lg px-3 py-2 text-stone-800 "
    "focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-transparent resize-y"
)


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo', 'imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Título da notícia...',
            }),
            'conteudo': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 10,
                'placeholder': 'Escreva o conteúdo da notícia...',
            }),
            'imagem': forms.ClearableFileInput(attrs={'class': INPUT_CLASS}),
        }
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'imagem': 'Imagem (opcional)',
        }
