########################################################################################################################
# Import
from typing import Any


########################################################################################################################
# Class

class Product:
    def __init__(self,name:str,product_id:str,price:float,stock:int):
        self._name = name
        self._product_id = product_id
        self._price = price
        self._stock = stock

    # Representação por String
    def __str__(self):
        return f"Produto: {self.name} | ID: {self.product_id} | Preço: R${self.price:.2f} | Estoque: {self.stock}"

    # Propriedades
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self,value:str):
        if isinstance(value,str):
            self._name = value
        else:
            raise TypeError("O valor inserido deve ser uma string!")

    @property
    def product_id(self) -> str:
        return self._product_id
    @product_id.setter
    def product_id(self,value:str):
        if value.isalnum():
            self._product_id = value
        else:
            raise TypeError("O valor inserido deve ser uma string de números!")

    @property
    def price(self) -> float:
        return self._price
    @price.setter
    def price(self,value):
        if float(value):
            self._price = float(value)
        else:
            raise TypeError("O valor inserido deve ser um número!")

    @property
    def stock(self) -> int:
        return self._stock
    @stock.setter
    def stock(self,value:int):
        if isinstance(value,int):
            self._stock = value
        else:
            raise TypeError("O valor inserido deve ser um integer!")

    # Métodos
    def to_dict(self) -> dict[str,Any]:
        return {
            "name":self.name,
            "product_id":self.product_id,
            "price":self.price,
            "stock":self.stock
        }