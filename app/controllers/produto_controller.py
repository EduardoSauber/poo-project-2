from typing import Any
from app.models.mercado import Mercado
from app.models.produto import Produto

class GerenciadorProduto:
    def criar_produto(self,data:dict[str,Any],mercado:Mercado) -> dict:
        if not data or not mercado:
            return {'ok': False, 'erro': 'Data e/ou instância de mercado não podem ser vazio.'}

        nome = str(data.get('nome'))
        preco = float(data.get('preco'))
        qtd_estoque = int(data.get('qtd_estoque'))

        if not nome or not preco or not qtd_estoque:
            return {'ok': False, 'erro': 'Preencha todos os campos.'}
        if preco < 0:
            return {'ok': False, 'erro': 'O preço deve ser maior que zero.'}
        if qtd_estoque < 0:
            return {'ok': False, 'erro': 'O estoque não pode ser negativo.'}

        produto = Produto(nome=nome, preco=preco, qtd_estoque=qtd_estoque)
        if not mercado.cadastrar_produto(produto):
            return {'ok': False, 'erro': 'Produto já cadastrado.'}
        return {'ok' : True}

    def editar_produto(self,data:dict[str,Any],mercado:Mercado) -> dict:
        if not data or not mercado:
            return {'ok': False, 'erro': 'Data e/ou instância de mercado não podem ser vazio.'}

        nome_original = data.get('nome_original')
        if not nome_original:
            return {'ok': False, 'erro': 'Nome do produto não pode ser vazio.'}

        nome = str(data.get('nome'))
        preco = float(data.get('preco'))
        qtd_estoque = int(data.get('qtd_estoque'))

        if not nome or not preco or not qtd_estoque:
            return {'ok': False, 'erro': 'Preencha todos os campos.'}
        if preco < 0:
            return {'ok': False, 'erro': 'O preço deve ser maior que zero.'}
        if qtd_estoque < 0:
            return {'ok': False, 'erro': 'O estoque não pode ser negativo.'}

        for item in mercado.lista_produtos:
            if item.nome == nome_original:
                item.nome = nome
                item.set_preco(preco)
                item.set_estoque(qtd_estoque)
                return {'ok': True}
        return {'ok': False, 'erro': 'Produto não encontrado.'}

    def excluir_produto(self,nome:str,mercado:Mercado):
        if not nome:
            return {'ok': False, 'erro': 'Nome não pode ser vazio.'}

        for item in mercado.lista_produtos:
            if item.nome == str(nome):
                mercado.lista_produtos.remove(item)
                return {'ok': True}
        return {'ok': False, 'erro': 'Produto não encontrado.'}
