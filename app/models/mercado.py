from app.models.produto import Produto
from app.models.cliente import Cliente
from app.models.administrador import Administrador
from app.models.recibo import Recibo


class Mercado:
    def __init__(self, lista_produtos, lista_clientes, lista_administradores):

        self.lista_produtos = lista_produtos if lista_produtos else []
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

    def emitir_recibo(self, cliente:Cliente):
        """
        pegar Cliente
        criar Recibo
        Recibo.set_id()
        Recibo.set_data()
        Recibo.set_cliente(cliente_nome=Cliente.get_nome(),cliente_cpf=Cliente.get_cpf()
        Recibo.adicionar_itens(Cliente.carrinho.lista_items)
        Recibo.set_total(Cliente.carrinho.total)
        """
        pass

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



