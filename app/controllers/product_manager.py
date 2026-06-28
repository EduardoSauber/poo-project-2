########################################################################################################################
# Import
import os
import json

from app.models.product import Product

########################################################################################################################
# Class
class ProductManager:
    def __init__(self):
        self.__all_products= []
        self.__DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),"db")

        self.__read()

    def __read(self):
        try:
            with open(f"{self.__DATA_PATH}/products.json", "r") as FILE:
                product_data = json.load(FILE)
                self.__all_products = [Product(**data) for data in product_data]
        except FileNotFoundError:
            pass
            print("(READ) productController: Não foi encontrado um banco de dados de produtos.")

    def __write(self):
        try:
            with open(f"{self.__DATA_PATH}/products.json", "w") as FILE:
                product_data = [product.to_dict() for product in self.__all_products]
                json.dump(product_data, FILE)
                print(f"(WRITE) productController: Arquivo 'products.json' gravado no banco de dados.")
        except FileNotFoundError:
            raise TypeError(f"(WRITE) productController: O sistema não conseguiu gerar o arquivo 'products.json'.")

    def add_to_stock(self,product_name:str,product_id:str,price:float,quantity_to_stock:int) -> Product | None:
        if not product_id:
            return None

        product = self.get_product_by_id(product_id)
        if product:
            return None

        novo_produto = Product(product_name, product_id, price, quantity_to_stock)
        self.__all_products.append(novo_produto)
        self.__write()
        return novo_produto

    def edit_on_stock(self,product_id=None,new_product_id=None,new_product_name=None,new_price=None,new_quantity=None)\
            -> bool:
        if not product_id:
            return False

        product = self.get_product_by_id(product_id)
        if not product:
            print(f"Produto '{product_id}' não existe no banco de dados.")
            return False

        if new_product_id:
            if not self.get_product_by_id(new_product_id):
                product.product_id = new_product_id
        if new_product_name:
            product.name = new_product_name
        if new_price is not None:
            product.price = new_price
        if new_quantity is not None:
            product.stock = new_quantity

        print(f"Produto '{product_id}' atualizado no banco de dados.")
        self.__write()
        return True

    def remove_from_stock(self,product_id) -> bool:
        if not product_id:
            return False

        product = self.get_product_by_id(product_id)

        if not product:
            return False

        self.__all_products.remove(product)

        print(f"productController: O produto {product.product_id} foi removido do banco de dados")
        self.__write()
        return True

    def get_product_by_id(self,product_id) -> Product | None:
        if not product_id:
            return None

        for product in self.__all_products:
            if product.product_id == product_id:
                return product
        return None

    def get_products(self) -> list:
        return self.__all_products

########################################################################################################################
# Testbench

def testbench():
    Controller = ProductManager()

    Controller.add_to_stock("Teste","codigoteste123",12.95,50)
    for item in Controller.get_products():
        print(item)
    Controller.edit_on_stock("codigoteste123",new_product_name="ProdutoTeste")
    for item in Controller.get_products():
        print(item)
    Controller.remove_from_stock("codigoteste123")
    for item in Controller.get_products():
        print(item)

if __name__ == "__main__":
    testbench()