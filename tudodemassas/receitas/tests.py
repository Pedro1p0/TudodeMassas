from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.management import call_command
from django.urls import reverse

from noticias.models import Noticia
from .models import Receita


class ReceitaModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )

    def test_receita_criada_com_sucesso(self):
        receita = Receita.objects.create(
            name='Macarrão Teste',
            category='Massas',
            ingredientes='200g de macarrão\nSal a gosto',
            modo_de_preparo='Cozinhe em água salgada.',
            user=self.user,
        )
        self.assertEqual(receita.name, 'Macarrão Teste')
        self.assertEqual(receita.user, self.user)

    def test_str_retorna_nome(self):
        receita = Receita.objects.create(
            name='Pizza Teste',
            category='Pizzas',
            ingredientes='Massa\nQueijo',
            modo_de_preparo='Monte e asse.',
            user=self.user,
        )
        self.assertEqual(str(receita), 'Pizza Teste')

    def test_categoria_padrao_e_massas(self):
        receita = Receita.objects.create(
            name='Sem Categoria Explícita',
            ingredientes='x',
            modo_de_preparo='x',
            user=self.user,
        )
        self.assertEqual(receita.category, Receita.Categoria.MASSAS)


class ReceitaViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.receita = Receita.objects.create(
            name='Lasanha Teste',
            category='Massas',
            ingredientes='Massa\nMolho\nQueijo',
            modo_de_preparo='Monte camadas e asse.',
            user=self.user,
        )

    def test_lista_receitas_retorna_200(self):
        response = self.client.get(reverse('lista_receita'))
        self.assertEqual(response.status_code, 200)

    def test_detalhe_receita_retorna_200(self):
        response = self.client.get(reverse('detail_receita', args=[self.receita.id]))
        self.assertEqual(response.status_code, 200)

    def test_criar_receita_sem_login_redireciona_para_login(self):
        response = self.client.get(reverse('criar_receita'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_criar_receita_autenticado_persiste_no_banco(self):
        self.client.login(username='testuser', password='testpass123')
        self.client.post(reverse('criar_receita'), {
            'name': 'Bolo Criado no Teste',
            'category': 'Bolos',
            'ingredientes': '3 ovos\n2 xícaras de farinha',
            'modo_de_preparo': 'Misture e asse a 180°C.',
        })
        self.assertTrue(Receita.objects.filter(name='Bolo Criado no Teste').exists())

    def test_excluir_receita_de_outro_usuario_nao_permitido(self):
        User.objects.create_user(username='outro', password='outro123')
        self.client.login(username='outro', password='outro123')
        response = self.client.post(reverse('excluir_receita', args=[self.receita.id]))
        self.assertNotEqual(response.status_code, 200)
        self.assertTrue(Receita.objects.filter(id=self.receita.id).exists())


class PopulateDBCommandTest(TestCase):

    def test_populate_db_cria_usuarios_receitas_e_noticias(self):
        call_command('populate_db', verbosity=0)
        self.assertGreater(User.objects.count(), 0)
        self.assertGreater(Receita.objects.count(), 0)
        self.assertGreater(Noticia.objects.count(), 0)

    def test_populate_db_idempotente(self):
        """Rodar duas vezes não deve duplicar dados."""
        call_command('populate_db', verbosity=0)
        count_primeira = Receita.objects.count()
        call_command('populate_db', verbosity=0)
        count_segunda = Receita.objects.count()
        self.assertEqual(count_primeira, count_segunda)
