from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from receitas.models import Receita
from noticias.models import Noticia
from faker import Faker
import random

fake = Faker('pt_BR')

RECEITAS_DADOS = [
    {
        'name': 'Macarrão à Carbonara',
        'category': 'Massas',
        'ingredientes': '400g de espaguete\n200g de pancetta ou bacon\n4 ovos\n100g de queijo parmesão ralado\nPimenta-do-reino a gosto\nSal a gosto',
        'modo_de_preparo': '1. Cozinhe o espaguete em água salgada até ficar al dente.\n2. Frite a pancetta em fio de azeite até dourar.\n3. Misture os ovos com o parmesão e pimenta.\n4. Escorra a massa, reserve um pouco da água do cozimento.\n5. Misture a massa quente com a pancetta, retire do fogo e adicione a mistura de ovos.\n6. Mexa rapidamente adicionando água do cozimento aos poucos para criar um molho cremoso.\n7. Sirva imediatamente com mais parmesão.',
    },
    {
        'name': 'Pizza Margherita Clássica',
        'category': 'Pizzas',
        'ingredientes': '500g de farinha de trigo\n7g de fermento biológico seco\n300ml de água morna\n1 colher de sopa de azeite\n1 colher de chá de sal\n300g de molho de tomate\n200g de mussarela\nFolhas de manjericão fresco',
        'modo_de_preparo': '1. Dissolva o fermento na água morna com uma pitada de açúcar.\n2. Misture a farinha, sal, azeite e o fermento. Sove por 10 minutos.\n3. Deixe descansar por 1 hora coberto com pano úmido.\n4. Abra a massa em superfície enfarinhada.\n5. Espalhe o molho de tomate, adicione a mussarela fatiada.\n6. Asse em forno pré-aquecido a 220°C por 15-20 minutos.\n7. Finalize com folhas de manjericão fresco.',
    },
    {
        'name': 'Lasanha Bolognesa',
        'category': 'Massas',
        'ingredientes': '400g de massa para lasanha\n500g de carne moída\n1 cebola\n3 dentes de alho\n400g de tomate pelado\n500ml de molho bechamel\n200g de mussarela\n100g de parmesão\nSal e pimenta a gosto',
        'modo_de_preparo': '1. Refogue a cebola e alho no azeite.\n2. Adicione a carne moída e refogue até dourar.\n3. Acrescente o tomate pelado, sal e pimenta. Cozinhe por 30 minutos.\n4. Monte em refratário: molho, massa, bolonhesa, bechamel, queijos. Repita as camadas.\n5. Finalize com bechamel e parmesão.\n6. Asse a 180°C por 40 minutos coberto com papel alumínio.\n7. Retire o papel e asse mais 10 minutos para dourar.',
    },
    {
        'name': 'Bolo de Cenoura com Cobertura de Chocolate',
        'category': 'Bolos',
        'ingredientes': '3 cenouras médias\n3 ovos\n1 xícara de óleo\n2 xícaras de farinha de trigo\n2 xícaras de açúcar\n1 colher de sopa de fermento\nCobertura: 4 colheres de cacau, 4 colheres de açúcar, 2 colheres de manteiga, 5 colheres de leite',
        'modo_de_preparo': '1. Bata no liquidificador as cenouras, ovos e óleo.\n2. Misture em tigela com farinha, açúcar e fermento.\n3. Asse em forma untada a 180°C por 40 minutos.\n4. Para a cobertura, misture todos os ingredientes e leve ao fogo mexendo até engrossar.\n5. Despeje a cobertura quente sobre o bolo ainda na forma.',
    },
    {
        'name': 'Pizza Quatro Queijos',
        'category': 'Pizzas',
        'ingredientes': '1 massa de pizza\n100g de mussarela\n80g de gorgonzola\n80g de provolone\n80g de parmesão\nMolho de tomate a gosto\nOrégano',
        'modo_de_preparo': '1. Prepare ou abra a massa de pizza.\n2. Espalhe uma camada fina de molho de tomate.\n3. Distribua os queijos em fatias ou ralados sobre a massa.\n4. Polvilhe orégano a gosto.\n5. Asse em forno bem quente (220-250°C) por 15 minutos ou até o queijo dourar.',
    },
    {
        'name': 'Torta de Frango com Cream Cheese',
        'category': 'Tortas',
        'ingredientes': 'Massa: 3 xícaras de farinha, 1 colher de fermento, 3 ovos, 1 xícara de leite, 1/2 xícara de óleo\nRecheio: 2 peitos de frango cozido e desfiado, 200g de cream cheese, 1 cebola, sal e temperos',
        'modo_de_preparo': '1. Bata todos os ingredientes da massa no liquidificador.\n2. Refogue a cebola, adicione o frango desfiado e o cream cheese. Tempere.\n3. Em forma untada, despeje metade da massa.\n4. Adicione o recheio de frango.\n5. Cubra com o restante da massa.\n6. Asse a 180°C por 40-45 minutos até dourar.',
    },
    {
        'name': 'Pão Caseiro de Fermentação Rápida',
        'category': 'Pão Caseiro',
        'ingredientes': '500g de farinha de trigo\n10g de fermento biológico seco\n300ml de água morna\n1 colher de chá de sal\n1 colher de sopa de açúcar\n2 colheres de sopa de azeite',
        'modo_de_preparo': '1. Misture o fermento com água morna e açúcar. Aguarde espumar por 10 minutos.\n2. Adicione a farinha, sal e azeite. Sove por 10-15 minutos até ficar elástico.\n3. Deixe descansar coberto por 1 hora.\n4. Modele o pão e coloque em forma untada.\n5. Deixe crescer mais 30 minutos.\n6. Asse a 200°C por 30-35 minutos até dourar e soar oco ao bater.',
    },
    {
        'name': 'Salgado de Frango Assado',
        'category': 'Salgados',
        'ingredientes': 'Massa: 500g de farinha, 1 ovo, 150ml de leite, 1 colher de fermento, sal\nRecheio: frango desfiado, requeijão, temperos',
        'modo_de_preparo': '1. Misture os ingredientes da massa e sove bem.\n2. Abra a massa e corte círculos médios.\n3. Coloque uma colher de recheio no centro.\n4. Feche e aperte as bordas.\n5. Pincele com gema de ovo.\n6. Asse a 180°C por 25-30 minutos até dourar.',
    },
    {
        'name': 'Bolo Red Velvet',
        'category': 'Bolos',
        'ingredientes': '2 xícaras de farinha\n1 xícara de açúcar\n2 ovos\n1 xícara de buttermilk\n2 colheres de cacau\n1 colher de corante vermelho\nCobertura: cream cheese, açúcar de confeiteiro, manteiga',
        'modo_de_preparo': '1. Misture os ingredientes secos separados dos úmidos.\n2. Combine as misturas com o corante vermelho.\n3. Asse em duas formas redondas a 175°C por 30 minutos.\n4. Bata a cobertura de cream cheese até ficar firme.\n5. Recheie e cubra o bolo com a cobertura.',
    },
    {
        'name': 'Tagliatelle ao Pesto de Manjericão',
        'category': 'Massas',
        'ingredientes': '400g de tagliatelle\n2 xícaras de manjericão fresco\n3 dentes de alho\n50g de pinoli ou castanha de caju\n80ml de azeite extra virgem\n50g de parmesão\nSal e pimenta',
        'modo_de_preparo': '1. Bata no processador o manjericão, alho, pinoli e azeite.\n2. Adicione o parmesão e ajuste o sal.\n3. Cozinhe o tagliatelle al dente.\n4. Reserve um pouco da água do cozimento.\n5. Misture a massa quente com o pesto, adicionando água do cozimento se necessário.\n6. Sirva com folhas de manjericão e parmesão extra.',
    },
    {
        'name': 'Fettuccine Alfredo',
        'category': 'Massas',
        'ingredientes': '400g de fettuccine\n200g de manteiga sem sal\n200g de queijo parmesão ralado fino\nSal e pimenta-do-reino a gosto\nNoz-moscada a gosto',
        'modo_de_preparo': '1. Cozinhe o fettuccine em água bem salgada até al dente.\n2. Enquanto a massa cozinha, derreta a manteiga em fogo baixo.\n3. Escorra a massa reservando 1 xícara da água do cozimento.\n4. Fora do fogo, misture a massa com a manteiga e o parmesão.\n5. Adicione água do cozimento aos poucos até atingir consistência cremosa.\n6. Tempere com sal, pimenta e noz-moscada. Sirva imediatamente.',
    },
    {
        'name': 'Pizza Portuguesa',
        'category': 'Pizzas',
        'ingredientes': '1 massa de pizza\n200g de mussarela\n100g de presunto\n3 ovos cozidos fatiados\n1 cebola em rodelas\n50g de azeitonas pretas\nMolho de tomate\nOrégano',
        'modo_de_preparo': '1. Espalhe o molho de tomate sobre a massa aberta.\n2. Distribua a mussarela por toda a superfície.\n3. Coloque o presunto, os ovos fatiados e as rodelas de cebola.\n4. Finalize com as azeitonas e orégano.\n5. Asse em forno a 220°C por 15-18 minutos até a borda dourar.',
    },
    {
        'name': 'Pão de Queijo Mineiro',
        'category': 'Pão Caseiro',
        'ingredientes': '500g de polvilho azedo\n200ml de leite\n100ml de óleo\n2 ovos\n200g de queijo minas curado ralado\n1 colher de chá de sal',
        'modo_de_preparo': '1. Aqueça o leite e o óleo até ferver e despeje sobre o polvilho.\n2. Misture bem e deixe esfriar um pouco.\n3. Adicione os ovos um a um, o queijo ralado e o sal.\n4. Sove até formar uma massa homogênea.\n5. Faça bolinhas e coloque em assadeira untada.\n6. Asse a 200°C por 20-25 minutos até dourar.',
    },
    {
        'name': 'Torta Salgada de Legumes',
        'category': 'Tortas',
        'ingredientes': 'Massa: 300g de farinha, 150g de manteiga gelada, 1 ovo, sal\nRecheio: 2 abobrinhas, 1 cenoura, 1 cebola, 2 ovos, 200ml de creme de leite, queijo ralado, sal e ervas',
        'modo_de_preparo': '1. Prepare a massa misturando farinha, manteiga gelada em cubos, ovo e sal até formar uma farofa que se une.\n2. Forre uma forma de torta e leve ao forno por 15 min a 180°C (cega).\n3. Refogue os legumes em azeite com alho e tempere.\n4. Misture os ovos com creme de leite, sal e ervas.\n5. Coloque os legumes na massa pré-assada, despeje a mistura de ovos e cubra com queijo.\n6. Asse a 180°C por 35 minutos.',
    },
    {
        'name': 'Coxinha de Frango',
        'category': 'Salgados',
        'ingredientes': 'Massa: 500ml de caldo de frango, 500g de farinha de trigo, 1 colher de manteiga\nRecheio: 2 peitos de frango cozido desfiado, requeijão cremoso, cebola, alho, temperos\nPara empanar: farinha de rosca, ovos',
        'modo_de_preparo': '1. Ferva o caldo de frango com a manteiga. Adicione a farinha de uma vez e mexa até soltar da panela.\n2. Deixe a massa esfriar. Para o recheio, refogue alho e cebola, adicione o frango desfiado e o requeijão.\n3. Modele as coxinhas com a massa, colocando o recheio no centro.\n4. Passe no ovo batido e na farinha de rosca.\n5. Frite em óleo quente a 170°C até dourar.',
    },
    {
        'name': 'Bolo de Limão com Calda',
        'category': 'Bolos',
        'ingredientes': '2 xícaras de farinha\n1 e 1/2 xícara de açúcar\n3 ovos\n1/2 xícara de óleo\n1/2 xícara de leite\n1 colher de fermento\nRaspas e suco de 2 limões\nCalda: 1/2 xícara de suco de limão, 1/2 xícara de açúcar',
        'modo_de_preparo': '1. Bata os ovos com o açúcar até dobrar de volume.\n2. Adicione o óleo, leite, raspas e suco de limão.\n3. Incorpore a farinha e o fermento delicadamente.\n4. Asse em forma untada a 180°C por 35-40 minutos.\n5. Para a calda, ferva o suco de limão com o açúcar por 5 minutos.\n6. Fure o bolo quente e despeje a calda.',
    },
    {
        'name': 'Rigatoni ao Molho de Linguiça',
        'category': 'Massas',
        'ingredientes': '400g de rigatoni\n300g de linguiça italiana\n1 lata de tomate pelado\n1 cebola\n3 dentes de alho\n1/2 xícara de vinho branco\nFolhas de manjericão\nParmesão para servir',
        'modo_de_preparo': '1. Retire a linguiça da tripa e esfarelea.\n2. Doure a linguiça na panela. Reserve.\n3. No mesmo azeite, refogue cebola e alho.\n4. Deglace com o vinho branco.\n5. Adicione o tomate pelado amassado e cozinhe por 20 minutos.\n6. Volte a linguiça ao molho e ajuste o sal.\n7. Cozinhe o rigatoni al dente e misture ao molho. Finalize com manjericão.',
    },
    {
        'name': 'Pizza Calabresa',
        'category': 'Pizzas',
        'ingredientes': '1 massa de pizza\n200g de mussarela\n150g de calabresa fatiada\n1 cebola em rodelas\nMolho de tomate\nOrégano\nAzeite',
        'modo_de_preparo': '1. Abra a massa e espalhe o molho de tomate.\n2. Cubra com a mussarela fatiada.\n3. Distribua a calabresa por cima.\n4. Coloque as rodelas de cebola.\n5. Regue com fio de azeite e polvilhe orégano.\n6. Asse a 220°C por 15-18 minutos.',
    },
    {
        'name': 'Torta de Maçã',
        'category': 'Tortas',
        'ingredientes': 'Massa: 300g de farinha, 150g de manteiga, 2 colheres de açúcar, 1 ovo\nRecheio: 4 maçãs, 3 colheres de açúcar, canela, suco de 1 limão\nCobertura: gema para pincelar',
        'modo_de_preparo': '1. Misture farinha, manteiga fria, açúcar e ovo até virar uma massa. Leve à geladeira por 30 min.\n2. Descasque e fatie as maçãs. Misture com açúcar, canela e limão.\n3. Divida a massa em 2 partes. Forre o fundo da forma com uma parte.\n4. Adicione o recheio de maçã.\n5. Cubra com a outra metade da massa. Pincele com gema.\n6. Asse a 180°C por 45 minutos.',
    },
    {
        'name': 'Pão Sírio Caseiro',
        'category': 'Pão Caseiro',
        'ingredientes': '500g de farinha de trigo\n7g de fermento biológico seco\n300ml de água morna\n1 colher de chá de sal\n1 colher de chá de açúcar\n2 colheres de sopa de azeite',
        'modo_de_preparo': '1. Dissolva o fermento na água morna com o açúcar.\n2. Misture com a farinha, sal e azeite. Sove por 8 minutos.\n3. Deixe descansar por 1 hora em local quente.\n4. Divida em bolinhas e abra fino com o rolo (3mm).\n5. Deixe descansar mais 20 minutos.\n6. Asse em forno bem quente (250°C) por 3-4 minutos. Os pães devem inflar como bola.',
    },
    {
        'name': 'Esfirra Aberta de Carne',
        'category': 'Salgados',
        'ingredientes': 'Massa: 500g de farinha, 7g de fermento, 250ml de leite morno, 50ml de óleo, sal, açúcar\nRecheio: 300g de carne moída, 1 tomate, 1 cebola, suco de limão, sal, pimenta',
        'modo_de_preparo': '1. Prepare a massa com fermento ativado no leite morno. Sove e deixe crescer 1 hora.\n2. Para o recheio, misture a carne moída crua com os legumes picadinhos, limão e temperos.\n3. Divida a massa em bolinhas de 50g. Abra em formato oval.\n4. Coloque 1 colher de recheio no centro e pressione levemente.\n5. Asse a 200°C por 15-20 minutos.',
    },
    {
        'name': 'Bolo de Chocolate Úmido',
        'category': 'Bolos',
        'ingredientes': '2 xícaras de farinha\n2 xícaras de açúcar\n3/4 xícara de cacau em pó\n2 colheres de fermento\n1 colher de bicarbonato\n2 ovos\n1 xícara de leite\n1 xícara de óleo\n1 xícara de água quente',
        'modo_de_preparo': '1. Misture todos os ingredientes secos.\n2. Adicione os ovos, leite e óleo. Bata bem.\n3. Por último, adicione a água quente (a massa ficará líquida, isso é normal).\n4. Asse em forma untada e enfarinhada a 180°C por 40 minutos.\n5. Sirva com ganache ou brigadeiro por cima.',
    },
    {
        'name': 'Gnocchi de Batata ao Molho Sugo',
        'category': 'Massas',
        'ingredientes': '1kg de batatas\n300g de farinha de trigo\n1 ovo\n1 colher de sal\nMolho: 1 lata de tomate pelado, alho, azeite, manjericão, sal',
        'modo_de_preparo': '1. Cozinhe as batatas com casca. Descasque quente e passe pelo espremedor.\n2. Misture com a farinha, ovo e sal até formar uma massa que não grude.\n3. Enrole em cordões de 2cm e corte em pedaços de 2cm.\n4. Cozinhe em água salgada fervente. Retire quando subirem à superfície.\n5. Para o molho, refogue o alho no azeite, adicione o tomate e cozinhe 15 min.\n6. Sirva o gnocchi com o molho e manjericão.',
    },
]

NOTICIAS_DADOS = [
    {
        'titulo': 'As tendências de massas para 2026',
        'conteudo': 'O mundo das massas está em constante evolução. Em 2026, os chefs apostam em massas artesanais com farinhas alternativas como a de grão-de-bico, espelta e centeio. A fermentação longa voltou com força, trazendo massas com mais sabor e digestibilidade.\n\nOutra tendência forte é a personalização: matérias-primas locais, receitas regionais resgatadas e combinações inusitadas de recheios entram na lista dos favoritos. O toque final? Ervas frescas colhidas no quintal.',
    },
    {
        'titulo': 'Por que a pizza napolitana conquistou o mundo?',
        'conteudo': 'A pizza napolitana, patrimônio cultural imaterial da UNESCO desde 2017, tem uma história que remonta ao século XVIII nas ruas de Nápoles, Itália. Sua simplicidade é o segredo: massa de fermentação longa, tomate San Marzano, mussarela de búfala e manjericão fresco.\n\nO forno a lenha a 485°C por apenas 60-90 segundos cria aquela borda característica, levemente carbonizada e cheia de bolhas. Hoje, pizzarias napolitanas certificadas espalhadas pelo Brasil mantêm viva essa tradição.',
    },
    {
        'titulo': 'Dicas para a massa de pão perfeita em casa',
        'conteudo': 'Fazer pão em casa pode parecer intimidador, mas com algumas dicas simples você consegue resultados incríveis. O segredo está na qualidade dos ingredientes, na temperatura da água (entre 35-38°C para não matar o fermento) e na paciência com o tempo de fermentação.\n\nSovar bem a massa desenvolve o glúten, fundamental para a estrutura final. E lembre-se: o forno bem quente (200°C ou mais) garante aquela casca crocante que todo mundo ama.\n\nPor fim, não abra o forno nos primeiros 20 minutos! O vapor interno é responsável por boa parte do crescimento do pão.',
    },
    {
        'titulo': 'Festival de Massas 2026 acontece em São Paulo',
        'conteudo': 'O maior festival de massas do Brasil acontece nos dias 15 e 16 de abril de 2026 no Parque Ibirapuera, em São Paulo. Com entrada gratuita, o evento reúne mais de 80 expositores entre restaurantes, produtores artesanais e importadores de ingredientes italianos.\n\nA programação inclui workshops de massas caseiras, aulas de pizza napolitana e demonstrações ao vivo com chefs renomados. Será um final de semana dedicado inteiramente ao universo das massas!',
    },
    {
        'titulo': 'Conheça os tipos de farinha para massas',
        'conteudo': 'A escolha da farinha é um dos fatores mais determinantes na textura final de qualquer massa. A farinha de trigo tipo 1 é a mais comum para pães e massas caseiras. A tipo 00, fina e refinada, é a preferida dos pizzaiolos e para massas frescas.\n\nPara quem busca alternativas sem glúten, as farinhas de arroz, amêndoas ou tapioca abrem um universo de possibilidades. Cada uma traz características únicas de sabor, textura e absorção de líquidos.\n\nExperimente misturar diferentes farinhas para encontrar sua combinação favorita!',
    },
    {
        'titulo': 'O segredo do molho bolonhesa autêntico',
        'conteudo': 'O verdadeiro ragù alla bolognese, originário de Bologna na Itália, pouco tem a ver com as versões que conhecemos. A receita registrada na Câmara de Comércio de Bologna em 1982 leva carne bovina, pancetta, cebola, cenoura, aipo, vinho branco, leite e apenas uma colherada de molho de tomate.\n\nO segredo está no tempo de cozimento lento — ao menos 3 horas em fogo baixíssimo. O leite é adicionado no final para suavizar a acidez e dar cremosidade. Sirva obrigatoriamente com tagliatelle fresco, nunca com espaguete!',
    },
    {
        'titulo': 'Como conservar sua massa fresca por mais tempo',
        'conteudo': 'Fazer massa fresca em casa é uma arte, mas muitas vezes preparamos mais do que o necessário. A boa notícia é que conservar bem a massa é simples.\n\nNa geladeira, a massa fresca dura até 2 dias coberta com plástico filme. Para congelar, enfarinhe bem, forme ninhos ou polvilhe com semolina e congele em camadas separadas por papel manteiga. Dura até 3 meses e vai direto do freezer para a água fervente — adicione apenas 1-2 minutos ao tempo de cozimento.',
    },
    {
        'titulo': 'Receitas com sobras de pão: zero desperdício',
        'conteudo': 'Pão amanhecido não é lixo — é ingrediente! A culinária italiana e portuguesa construiu pratos icônicos exatamente para aproveitar sobras de pão.\n\nA bruschetta clássica, a panzanella (salada toscana de pão com tomates), o ribollita (sopa densa com pão e legumes) e o clássico pudim de pão brasileiro são apenas alguns exemplos.\n\nEm casa, pão amanhecido vira farinha de rosca caseira, croutons para salada ou base para um delicioso recheio de torta. Aproveite cada fatia!',
    },
    {
        'titulo': 'Pizza nos EUA vs. pizza no Brasil: as diferenças',
        'conteudo': 'A pizza viajou da Itália para o mundo e em cada país ganhou uma identidade própria. Nos Estados Unidos, a New York-style tem fatias enormes e dobráveis com muito queijo. A deep dish de Chicago é quase uma torta salgada de tão alta.\n\nNo Brasil, a pizza ganhou uma identidade própria. São Paulo se tornou a maior cidade com pizzas do mundo fora da Itália, com dezenas de sabores únicos como frango com catupiry, banana com canela e os clássicos doces. A massa mais fina e crocante é a preferida dos paulistanos.',
    },
    {
        'titulo': 'Os 5 erros mais comuns ao fazer bolo',
        'conteudo': 'Mesmo chefs experientes já cometeram esses erros. Confira os cinco mais comuns e como evitá-los.\n\n1. Abrir o forno antes do tempo: o bolo murcha porque o vapor interno ainda não firmou a estrutura.\n2. Não peneirar a farinha: resulta em caroços e bolo pesado.\n3. Ovos gelados: dificulta a emulsificação. Use sempre em temperatura ambiente.\n4. Forma errada: forme muito grande = bolo fino demais. Muito pequena = não assa por dentro.\n5. Forno frio: sempre pré-aqueça por pelo menos 15 minutos antes de colocar o bolo.',
    },
]


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados falsos para testes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limpar',
            action='store_true',
            help='Apaga todos os dados existentes antes de popular',
        )

    def handle(self, *args, **options):
        if options['limpar']:
            self.stdout.write(self.style.WARNING('Limpando dados existentes...'))
            Noticia.objects.all().delete()
            Receita.objects.all().delete()
            User.objects.filter(is_superuser=False).delete()
            self.stdout.write(self.style.SUCCESS('Dados limpos.'))

        self.stdout.write('Criando usuários...')
        usuarios = self._criar_usuarios()

        self.stdout.write('Criando receitas...')
        self._criar_receitas(usuarios)

        self.stdout.write('Criando notícias...')
        self._criar_noticias(usuarios)

        self.stdout.write(self.style.SUCCESS(
            f'\n✓ Banco populado com sucesso!\n'
            f'  → {len(usuarios)} usuários criados\n'
            f'  → {len(RECEITAS_DADOS)} receitas criadas\n'
            f'  → {len(NOTICIAS_DADOS)} notícias criadas\n'
            f'\nUsuários disponíveis para login:\n'
            f'  Admin staff → usuario: admin_testes | senha: senha123\n'
            f'  Usuários comuns → usuario: usuario01 até usuario10 | senha: senha123\n'
        ))

    def _criar_usuarios(self):
        usuarios = []

        # Admin staff para publicar notícias
        admin, criado = User.objects.get_or_create(username='admin_testes')
        if criado:
            admin.set_password('senha123')
            admin.is_staff = True
            admin.email = 'admin@tudodemassas.com'
            admin.first_name = 'Admin'
            admin.last_name = 'Testes'
            admin.save()
        usuarios.append(admin)

        # Usuários comuns
        for i in range(1, 11):
            username = f'usuario{i:02d}'
            user, criado = User.objects.get_or_create(username=username)
            if criado:
                user.set_password('senha123')
                user.first_name = fake.first_name()
                user.last_name = fake.last_name()
                user.email = fake.email()
                user.save()
            usuarios.append(user)

        return usuarios

    def _criar_receitas(self, usuarios):
        usuarios_comuns = [u for u in usuarios if not u.is_staff]
        for dados in RECEITAS_DADOS:
            Receita.objects.get_or_create(
                name=dados['name'],
                defaults={
                    'category': dados['category'],
                    'ingredientes': dados['ingredientes'],
                    'modo_de_preparo': dados['modo_de_preparo'],
                    'user': random.choice(usuarios_comuns),
                }
            )

    def _criar_noticias(self, usuarios):
        admin = next(u for u in usuarios if u.is_staff)
        for dados in NOTICIAS_DADOS:
            Noticia.objects.get_or_create(
                titulo=dados['titulo'],
                defaults={
                    'conteudo': dados['conteudo'],
                    'autor': admin,
                }
            )
