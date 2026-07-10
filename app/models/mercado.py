from app.models.produto import Produto
from app.models.cliente import Cliente
from app.models.administrador import Administrador
from app.models.recibo import Recibo


class Mercado:
    def __init__(self, lista_produtos = None, lista_clientes = None, lista_administradores = None, lista_vendas = None):

        self.lista_produtos = lista_produtos if lista_produtos else []
        self.lista_vendas = lista_vendas if lista_vendas else []
        self.lista_clientes = lista_clientes if lista_clientes else []
        self.lista_administradores = lista_administradores if lista_administradores else []

    # === PRODUTOS ===
    def cadastrar_produto(self, produto:Produto):
        for prod in self.lista_produtos:
            if prod.nome == produto.nome:
                print(f"Produto já existe na lista!")
                return False

        self.lista_produtos.append(produto)
        return True

    def emitir_recibo(self, cliente: Cliente):
        recibo = Recibo()
        recibo.set_id()
        recibo.set_data()
        recibo.set_cliente(cliente_nome=cliente.get_nome(), cliente_cpf=cliente.get_cpf())
        for item in cliente.carrinho.lista_items:
            recibo.adicionar_itens(item)
        recibo.set_total(cliente.carrinho.total)
        self.lista_vendas.append(recibo)
        return recibo


    # === USUARIOS ===
    def cadastrar_cliente(self, cliente: Cliente) -> bool:
        if self.get_cliente_por_cpf(cliente.get_cpf()):
            print(f"Cliente já existe na lista!")
            return False
        self.lista_clientes.append(cliente)
        return True

    def cadastrar_administrador(self,administrador: Administrador) -> bool:
        if self.get_administrador_por_cpf(administrador.get_cpf()):
            print(f"Administrador já existe na lista!")
            return False
        self.lista_administradores.append(administrador)
        return True

    def get_cliente_por_cpf(self, cpf:str) -> Cliente | None:
        for cliente in self.lista_clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None

    def get_administrador_por_cpf(self, cpf:str) -> Administrador | None:
        for admin in self.lista_administradores:
            if admin.get_cpf() == cpf:
                return admin
        return None



