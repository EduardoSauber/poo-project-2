from app.models.pessoa import Pessoa
from app.models.carrinho import Carrinho
from typing import Any


class Cliente(Pessoa):
    def __init__(self,cpf:str,nome:str,email:str,idade:int,senha:str,db_read:bool):
        super().__init__(cpf=cpf,nome=nome,email=email,idade=idade,senha=senha,db_read=db_read)
        self.__saldo = 0.0
        self.carrinho = Carrinho()

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,valor:float) -> bool:
        if not valor:
            return False
        self.__saldo = valor
        return True

    def to_dict(self,publico:bool=True) -> dict[str,Any]:
        data = {
            'cpf'   : self.get_cpf(),
            'nome'  : self.get_nome(),
            'email' : self.email,
            'idade' : self.idade,
            'saldo' : self.get_saldo()
        }
        if not publico:
            data['carrinho'] = self.carrinho.to_dict()
            # Não acho uma boa prática criar um get_senha() só para salvar no to_dict()
            # noinspection PyUnresolvedReferences
            data['senha'] = self._Pessoa__senha
        return data