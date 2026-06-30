from app.models.produto import Produto
from typing import Any


class Carrinho:
    def __init__(self):
        self.total = 0.0
        self.lista_items = []

    def adicionar_ao_carrinho(self,produto:Produto,quantidade:int) -> bool:
        if not produto:
            return False
        c_produto = self.get_produto_quantidade(produto)
        if c_produto:
            c_produto['quantidade'] += quantidade
        else:
            self.lista_items.append({
                'produto': produto,
                'quantidade': quantidade
            })
        self.total += round(produto.get_preco() * quantidade,2)
        return True

    def remover_do_carrinho(self,produto:Produto,quantidade:int) -> bool:
        if not produto:
            return False
        c_produto = self.get_produto_quantidade(produto)
        if not c_produto:
            return False
        if quantidade >= c_produto['quantidade']:
            self.lista_items.remove(c_produto)
            self.total -= round(c_produto['produto'].get_preco() * c_produto['quantidade'], 2)
        else:
            c_produto['quantidade'] -= quantidade
            self.total -= round(c_produto['produto'].get_preco() * quantidade,2)
        return True

    def calcular_total(self) -> float:
        total = 0.0
        for c_produto in self.lista_items:
            total += round(c_produto['produto'].get_preco() * c_produto['quantidade'],2)
        return total

    def get_produto_quantidade(self,produto:Produto) -> dict[str,Any] | None:
        if not produto:
            return None
        for c_produto in self.lista_items:
            if produto == c_produto['produto']:
                return c_produto
        return None

    def limpar_carrinho(self):
        self.lista_items = []
        self.total = 0.0

    def to_dict(self):
        itens_formatados = []
        for c_produto in self.lista_items:
            itens_formatados.append({
                'produto'       : c_produto['produto'].to_dict(),
                'quantidade'    : c_produto['quantidade']
            })
        return {
            'itens' : itens_formatados,
            'total' : self.total
        }