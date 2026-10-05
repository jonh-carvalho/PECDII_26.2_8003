from django.test import TestCase
from django.urls import reverse

from .models import Produto


class ProdutoCatalogoTests(TestCase):
    def setUp(self):
        self.produto_1 = Produto.objects.create(
            nome='Notebook Gamer',
            descricao='Notebook com processador de alto desempenho para jogos.',
            preco='4999.90',
            estoque=8,
            categoria='Eletrônicos',
            disponivel=True,
        )
        self.produto_2 = Produto.objects.create(
            nome='Camiseta Premium',
            descricao='Camiseta de algodão com ótimo caimento.',
            preco='89.90',
            estoque=25,
            categoria='Vestuário',
            disponivel=True,
        )

    def test_lista_de_produtos_exibe_produtos_do_catalogo(self):
        response = self.client.get(reverse('produto_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.produto_1.nome)
        self.assertContains(response, self.produto_2.nome)

    def test_busca_filtra_produtos_pelo_termo_digitado(self):
        response = self.client.get(reverse('produto_list'), {'q': 'notebook'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.produto_1.nome)
        self.assertNotContains(response, self.produto_2.nome)

    def test_criacao_de_produto_pelo_formulario(self):
        dados = {
            'nome': 'Smartphone X',
            'descricao': 'Celular com câmera de alta resolução.',
            'preco': '2499.00',
            'estoque': 15,
            'categoria': 'Eletrônicos',
            'disponivel': True,
        }

        response = self.client.post(reverse('produto_create'), dados)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Produto.objects.filter(nome='Smartphone X').exists())
