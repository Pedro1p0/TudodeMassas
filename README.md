# 🍝 Tudo de Massas

[![CI](https://github.com/Pedro1p0/TudodeMassas/actions/workflows/ci.yml/badge.svg)](https://github.com/Pedro1p0/TudodeMassas/actions/workflows/ci.yml)

Plataforma de receitas culinárias desenvolvida com Django. Usuários podem publicar, editar e excluir suas próprias receitas, explorar receitas de outros usuários, buscar por ingredientes ou categorias, e acompanhar as últimas notícias do mundo das massas.

Projeto acadêmico desenvolvido para a disciplina **Projeto e Engenharia de Software** — Universidade Federal do Rio Grande do Norte (UFRN).

---

## ✨ Funcionalidades

- **Receitas** — CRUD completo: criar, visualizar, editar e excluir receitas com imagem, ingredientes e modo de preparo
- **Categorias** — Massas, Pizzas, Salgados, Bolos, Tortas, Pão Caseiro
- **Busca** — Busca por nome, ingrediente ou categoria em receitas e notícias
- **Paginação** — Listas paginadas (9 receitas / 6 notícias por página)
- **Notícias** — Publicação de notícias restrita a usuários staff (administradores)
- **Perfil** — Página pessoal com todas as receitas do usuário logado
- **Autenticação** — Cadastro, login e logout com proteção por `@login_required`
- **Permissões** — Somente o autor pode editar/excluir sua própria receita; somente staff gerencia notícias
- **Página inicial** — Hero com busca central, chips de categoria, receitas recentes e últimas notícias
- **Página 404** — Página de erro personalizada

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | [Django](https://www.djangoproject.com/) 4.1+ |
| Banco de dados | PostgreSQL 15 |
| Frontend | [Tailwind CSS](https://tailwindcss.com/) via CDN |
| Tipografia | Google Fonts — Playfair Display + Inter |
| Imagens | Pillow |
| Dados de teste | Faker |
| Containers | Docker + Docker Compose |
| CI | GitHub Actions |

---

## 🚀 Como rodar localmente

### Pré-requisitos

- [Docker](https://www.docker.com/) e Docker Compose

### 1. Clone o repositório

```bash
git clone https://github.com/Pedro1p0/TudodeMassas.git
cd TudodeMassas
```

### 2. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o `.env` se quiser alterar senha do banco ou outras configurações. Para desenvolvimento, os valores padrão já funcionam.

### 3. Suba os containers

```bash
docker compose up --build
```

As migrations rodam automaticamente. Acesse em: **http://localhost:8000**

### 4. (Opcional) Popule o banco com dados de teste

```bash
docker compose exec web python manage.py populate_db
```

Isso cria **11 usuários**, **22 receitas** e **10 notícias** prontos para uso.

> Credenciais dos usuários de teste:
> - **Staff (publica notícias):** `admin_testes` / `senha123`
> - **Usuários comuns:** `usuario01` até `usuario10` / `senha123`

Para limpar tudo e recriar do zero:

```bash
docker compose exec web python manage.py populate_db --limpar
```

### 5. (Opcional) Crie um superusuário

```bash
docker compose exec web python manage.py createsuperuser
```

Django Admin disponível em: **http://localhost:8000/admin**

---

## 🧪 Testes

```bash
docker compose exec web python manage.py test --verbosity=2
```

---

## 🔍 Lint

```bash
docker compose exec web flake8 tudodemassas/
```

---

## 📁 Estrutura do Projeto

```
TudodeMassas/
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
├── .env.example
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline: lint → testes → docker build
└── tudodemassas/           # Raiz do projeto Django
    ├── manage.py
    ├── tudodemassas/       # Configurações (settings, urls)
    ├── receitas/           # App de receitas (CRUD)
    ├── noticias/           # App de notícias (staff only)
    ├── users/              # App de autenticação e perfil
    └── templates/          # Templates HTML globais e por app
```

---

## ⚙️ CI — GitHub Actions

A cada push ou pull request na `main`, a pipeline executa automaticamente:

1. **Lint** — verifica estilo de código com `flake8`
2. **Testes** — roda os testes Django contra um PostgreSQL real
3. **Docker Build** — garante que a imagem builda sem erros

---

## 👤 Autor

Pedro — UFRN
