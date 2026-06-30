import datetime
import uuid

from typing import Optional, Any
from app.models.cliente import Cliente


class Recibo:
    def __init__(self):
        self.__id = None
        self.__data = None
        self.__cliente = {
            'nome'  : "",
            'cpf'   : ""
        }
        self.__itens = []
        self.__total = 0.0

    def set_id(self,recibo_id:Optional[str]=None):
        if not recibo_id:
            self.__id = uuid.uuid4().hex
        else:
            self.__id = recibo_id

    def set_data(self,recibo_data:Optional[str]=None):
        if not recibo_data:
            self.__data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        else:
            self.__data = recibo_data

    def set_cliente(self,cliente_nome:str,cliente_cpf:str) -> bool:
        if not cliente_nome or not cliente_cpf:
            return False
        self.__cliente['nome'] = cliente_nome
        self.__cliente['cpf'] = cliente_cpf
        return True

    def adicionar_itens(self,item:dict[str,Any]):
        if item:
            self.__itens.append(item)

    def set_total(self,total:float):
        if not total:
            for item in self.__itens:
                self.__total += round(item['produto'].get_preco() * item['quantidade'],2)
        else:
            self.__total = round(total,2)

    def to_dict(self) -> dict[str,Any]:
        itens_formatados = []
        for c_produto in self.__itens:
            itens_formatados.append({
                'produto': c_produto['produto'].to_dict(),
                'quantidade': c_produto['quantidade']
            })
        return {
            "id"                : self.__id,
            "data"              : self.__data,
            "cliente"           : self.__cliente,
            "itens"             : itens_formatados,
            "total"             : self.__total
        }