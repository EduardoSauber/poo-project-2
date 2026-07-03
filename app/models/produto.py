from typing import Any


class Produto:
    def __init__(self,id_produto,nome,preco,qtd_estoque):
        self.id = id_produto
        self.nome = nome
        self.__preco = preco
        self.__qtd_estoque = qtd_estoque

    def get_preco(self) -> float:
        return self.__preco
    def set_preco(self,preco:float) -> bool:
        if not preco:
            return False
        self.__preco = float(preco)
        return True

    def get_estoque(self) -> int:
        return self.__qtd_estoque
    def set_estoque(self,qtd_estoque:int) -> bool:
        if not qtd_estoque:
            return False
        self.__qtd_estoque = qtd_estoque
        return True

    def descontar_estoque(self,quantidade:int) -> bool:
        if not quantidade:
            return False
        self.__qtd_estoque -= quantidade
        return True

    def to_dict(self) -> dict[str,Any]:
        return {
            "id"            : self.id,
            "nome"          : self.nome,
            "preco"         : self.get_preco(),
            "qtd_estoque"   : self.get_estoque()
        }