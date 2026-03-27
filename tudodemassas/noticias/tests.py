from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Noticia


class NoticiaModelTest(TestCase):

    def setUp(self):
        self.staff = User.objects.create_user(
            username='staff', password='pass123', is_staff=True
        )

    def test_noticia_criada_com_sucesso(self):
        noticia = Noticia.objects.create(
            titulo='Notícia Teste',
            conteudo='Conteúdo da notícia de teste.',
            autor=self.staff,
        )
        self.assertEqual(noticia.titulo, 'Notícia Teste')
        self.assertEqual(noticia.autor, self.staff)

    def test_str_retorna_titulo(self):
        noticia = Noticia.objects.create(
            titulo='Título Esperado',
            conteudo='Conteúdo.',
            autor=self.staff,
        )
        self.assertEqual(str(noticia), 'Título Esperado')


class NoticiaViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.staff = User.objects.create_user(
            username='staff', password='pass123', is_staff=True
        )
        self.user = User.objects.create_user(
            username='comum', password='pass123'
        )
        self.noticia = Noticia.objects.create(
            titulo='Notícia Pública',
            conteudo='Conteúdo visível para todos.',
            autor=self.staff,
        )

    def test_lista_noticias_retorna_200(self):
        response = self.client.get(reverse('noticias'))
        self.assertEqual(response.status_code, 200)

    def test_detalhe_noticia_retorna_200(self):
        response = self.client.get(reverse('noticia_detail', args=[self.noticia.id]))
        self.assertEqual(response.status_code, 200)

    def test_criar_noticia_sem_login_redireciona(self):
        response = self.client.get(reverse('criar_noticia'))
        self.assertEqual(response.status_code, 302)

    def test_criar_noticia_usuario_comum_nao_permitido(self):
        """Usuário sem is_staff não pode criar notícias."""
        self.client.login(username='comum', password='pass123')
        response = self.client.get(reverse('criar_noticia'))
        self.assertNotEqual(response.status_code, 200)
