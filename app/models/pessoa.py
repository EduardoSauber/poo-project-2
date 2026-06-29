from abc import ABC, abstractmethod
import hashlib
from typing import Any


class Pessoa(ABC):
    def __init__(self,cpf:str,nome:str,email:str,idade:int,senha:str,db_read=False):
        self.__cpf = cpf
        self._nome = nome
        self.email = email
        self.idade = idade
        self.__senha = senha if db_read else self.set_senha(senha)

    @abstractmethod
    def to_dict(self,publico:bool=True) -> dict[str,Any]:
        pass

    def get_cpf(self) -> str:
        return self.__cpf
    def set_cpf(self,cpf:str) -> bool:
        if not cpf:
            return False
        self.__cpf = cpf
        return True

    def get_nome(self) -> str:
        return self._nome
    def set_nome(self,nome:str) -> bool:
        if not nome:
            return False
        self._nome = nome
        return True

    def set_senha(self,senha:str) -> bool:
        if not senha:
            return False
        self.__senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        return True
    def check_senha(self,senha:str) -> bool:
        if not senha:
            return False
        return self.__senha == hashlib.sha256(senha.encode('utf-8')).hexdigest()