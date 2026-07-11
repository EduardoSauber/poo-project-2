from app.models.pessoa import Pessoa
from app.models.carrinho import Carrinho
from typing import Any


class Cliente(Pessoa):
    def __init__(self,cpf:str,nome:str,email:str,idade:int,senha:str,db_read:bool):
        super().__init__(cpf=cpf,nome=nome,email=email,idade=idade,senha=senha,db_read=db_read)
        self.__compras = 0
        self.carrinho = Carrinho()

    def get_compras(self):
        return self.__compras
    def set_compras(self,valor:float) -> bool:
        if not valor:
            return False
        self.__compras = valor
        return True

    def to_dict(self,publico:bool=True) -> dict[str,Any]:
        data = {
            'cpf'   : self.get_cpf(),
            'nome'  : self.get_nome(),
            'email' : self.email,
            'idade' : self.idade,
            'compras' : self.get_compras()
        }
        if not publico:
            data['carrinho'] = self.carrinho.to_dict()
            # Não acho uma boa prática criar um get_senha() só para salvar no to_dict()
            # noinspection PyUnresolvedReferences
            data['senha'] = self._Pessoa__senha
        return data