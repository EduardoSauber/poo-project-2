from typing import Any
from app.models.mercado import Mercado
from app.models.produto import Produto

class GerenciadorProduto:
    def criar_produto(self,data:dict[str,Any],mercado:Mercado) -> dict:
        if not data or not mercado:
            return {'ok': False, 'erro': 'Data e/ou instância de mercado não podem ser vazio.'}

        nome = data.get('nome')
        preco = data.get('preco')
        qtd_estoque = data.get('qtd_estoque')

        if not nome or not preco or not qtd_estoque:
            return {'ok': False, 'erro': 'Preencha todos os campos.'}
        if preco < 0:
            return {'ok': False, 'erro': 'O preço deve ser maior que zero.'}
        if qtd_estoque < 0:
            return {'ok': False, 'erro': 'O estoque não pode ser negativo.'}

        produto = Produto(nome=nome, preco=float(preco), qtd_estoque=int(qtd_estoque))
        if not mercado.cadastrar_produto(produto):
            return {'ok': False, 'erro': 'Produto já cadastrado.'}
        return {'ok' : True}

    def excluir_produto(self,nome:str,mercado:Mercado):
        if not nome:
            return {'ok': False, 'erro': 'Nome não pode ser vazio.'}

        for item in mercado.lista_produtos:
            if item.nome == nome:
                mercado.lista_produtos.remove(item)
                return {'ok': True}
        return {'ok': False, 'erro': 'Nenhum dado enviado.'}
