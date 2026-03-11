# 🍝 Tudo de Massas

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
| Banco de dados | SQLite (desenvolvimento) |
| Frontend | [Tailwind CSS](https://tailwindcss.com/) via CDN |
| Tipografia | Google Fonts — Playfair Display + Inter |
| Imagens | Pillow |
| Dados de teste | Faker |

---

## 🚀 Como rodar localmente

### Pré-requisitos

- Python 3.10 ou superior
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/TudodeMassas.git
cd TudodeMassas
```

### 2. Crie e ative o ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
cd tudodemassas
python manage.py migrate
```

### 5. (Opcional) Popule o banco com dados de teste

```bash
python manage.py populate_db
```

Isso cria **11 usuários**, **22 receitas** e **10 notícias** prontos para uso.

> Credenciais dos usuários de teste:
> - **Staff (publica notícias):** `admin_testes` / `senha123`
> - **Usuários comuns:** `usuario01` até `usuario10` / `senha123`

Para limpar tudo e recriar do zero:

```bash
python manage.py populate_db --limpar
```

### 6. Crie um superusuário (acesso ao Django Admin)

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse em: **http://127.0.0.1:8000**  
Django Admin: **http://127.0.0.1:8000/admin**

---

## 📁 Estrutura do Projeto

```
TudodeMassas/
├── requirements.txt
├── tudodemassas/               # Raiz do projeto Django
│   ├── manage.py
│   ├── tudodemassas/           # Configurações (settings, urls)
│   ├── receitas/               # App de receitas (CRUD)
│   ├── noticias/               # App de notícias (staff only)
│   ├── users/                  # App de autenticação e perfil
│   └── templates/              # Templates HTML globais e por app
```

---

## 👤 Autor

Pedro — UFRN
