from django.db import models
from django.conf import settings


class Receita(models.Model):

    class Categoria(models.TextChoices):
        PIZZAS = 'Pizzas', 'Pizzas'
        MASSAS = 'Massas', 'Massas'
        SALGADOS = 'Salgados', 'Salgados'
        BOLOS = 'Bolos', 'Bolos'
        TORTAS = 'Tortas', 'Tortas'
        PAO = 'Pão Caseiro', 'Pão Caseiro'

    name = models.CharField(max_length=100, blank=False)
    category = models.CharField(
        max_length=20,
        choices=Categoria.choices,
        default=Categoria.MASSAS,
    )
    ingredientes = models.TextField(blank=False)
    modo_de_preparo = models.TextField(blank=False)
    imagem = models.ImageField(upload_to='receitas/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ['-created_at']
