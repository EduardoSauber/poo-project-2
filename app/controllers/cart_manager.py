########################################################################################################################
# Import
import os
import json

from typing import Any
from app.models.cart import UserCart

########################################################################################################################
# Class
class CartManager:
    def __init__(self):
        self.__all_carts = []
        self.__DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),"db")

        self.__read()

    # Leitura e Escrita de Banco de Dados
    def __read(self):
        try:
            with open(f"{self.__DATA_PATH}/carts.json", "r") as FILE:
                cart_data = json.load(FILE)
                self.__all_carts = [UserCart(**data) for data in cart_data]
        except FileNotFoundError:
            print("(READ) cartController: Não foi encontrado um banco de dados de carrinhos.")

    def __write(self):
        try:
            with open(f"{self.__DATA_PATH}/carts.json", "w") as FILE:
                cart_data = [cart.to_dict() for cart in self.__all_carts]
                json.dump(cart_data, FILE)
                print(f"(WRITE) cartController: Arquivo 'carts.json' gravado no banco de dados.")
        except FileNotFoundError:
            raise TypeError(f"(WRITE) cartController: O sistema não conseguiu gerar o arquivo 'carts.json'.")

    # Manuseamento de carrinho
    def get_cart(self, user_id) -> UserCart | None:
        if not user_id:
            return None

        cart = self.find_cart(user_id)
        if cart:
            return cart

        new_cart = UserCart(user_id)
        self.__all_carts.append(new_cart)
        self.__write()
        return new_cart

    def remove_cart(self,owner_id) -> bool:
        if not owner_id:
            return False

        cart = self.find_cart(owner_id)
        if not cart:
            return False

        self.__all_carts.remove(cart)
        self.__write()
        return True

    def add_to_user_cart(self, owner_id:str, product_id:str, quantity:int) -> bool:
        if not owner_id:
            return False

        cart = self.get_cart(owner_id)
        cart.add_product(product_id, quantity)
        self.__write()
        return True

    def remove_from_cart(self, owner_id, product_id) -> bool:
        if not owner_id:
            return False

        cart = self.find_cart(owner_id)
        event = cart.remove_product(product_id) if cart else False
        if not event:
            return False

        self.__write()
        return event

    def find_cart(self, owner_id) -> UserCart | None:
        if not owner_id:
            return None
        for cart in self.__all_carts:
            if cart.owner == owner_id:
                return cart
        return None

    def get_user_cart_products(self, owner_id) -> dict[str,Any] | None:
        if not owner_id:
            return None

        cart = self.find_cart(owner_id)
        return cart.products if cart else None

########################################################################################################################
# Testbench

def testbench():
    Controller = CartManager()

    print(Controller.get_cart("12345678912"))
    Controller.add_to_user_cart("12345678912","codigoteste123", 25)
    print(Controller.get_user_cart_products("12345678912"))
    Controller.remove_from_cart("12345678912","codigoteste123")
    print(Controller.get_user_cart_products("12345678912"))

    Controller.remove_cart("12345678912")

if __name__ == '__main__':
    testbench()