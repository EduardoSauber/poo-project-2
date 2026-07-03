from app.models.pessoa import Pessoa
from typing import Any


class Administrador(Pessoa):
    def __init__(self,cpf:str,nome:str,email:str,idade:int,senha:str,db_read:bool):
        super().__init__(cpf=cpf,nome=nome,email=email,idade=idade,senha=senha,db_read=db_read)

    def to_dict(self,publico:bool=True) -> dict[str,Any]:
        data = {
            'cpf'   : self.get_cpf(),
            'nome'  : self.get_nome(),
            'email' : self.email,
            'idade' : self.idade
        }
        if not publico:
            # Não acho uma boa prática criar um get_senha() só para salvar no to_dict()
            # noinspection PyUnresolvedReferences
            data['senha'] = self._Pessoa__senha
        return data