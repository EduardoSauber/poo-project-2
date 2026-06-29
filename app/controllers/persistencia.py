import json
import os
from app.models.mercado import Mercado
from app.models.produto import Produto
from app.models.cliente import Cliente
from app.models.administrador import Administrador
from app.controllers.autenticacao import GerenciadorAutenticacao

class GerenciadorPersistencia:
    def __init__(self,caminho_db:str=os.path.join(os.path.dirname(os.path.abspath(__file__)),"db")):
        self.caminho = caminho_db

    def salvar_produtos(self,mercado:Mercado):
        produtos_dict = []
        for produtos in mercado.lista_produtos:
            produtos_dict.append(produtos.to_dict())
        self.salvar_dados(produtos_dict,"produtos")

    def salvar_clientes(self,mercado:Mercado):
        clientes_dict = []
        for clientes in mercado.lista_clientes:
            clientes_dict.append(clientes.to_dict(publico=False))
        self.salvar_dados(clientes_dict,"clientes")

    def salvar_administradores(self,mercado:Mercado):
        admin_dict = []
        for admin in mercado.lista_administradores:
            admin_dict.append(admin.to_dict(publico=False))
        self.salvar_dados(admin_dict,"administradores")

    def salvar_dados(self,dados:list,banco_dados:str):
        try:
            with open(f"{self.caminho}/{banco_dados}.json","w",encoding="utf-8") as ARQUIVO:
                json.dump(dados,ARQUIVO)
                print(f"n\(PERSISTENCIA - SALVAR) Banco de dados '{banco_dados}' salvo.")
        except Exception as e:
            print(f"\n(PERSISTENCIA - SALVAR) Erro ao salvar banco de dados '{banco_dados}': {e}")

    def carregar_dados(self,mercado:Mercado,autenticador:GerenciadorAutenticacao):
        try:
            with open(f"{self.caminho}/produtos.json","r",encoding="utf-8") as ARQUIVO:
                dados = json.load(ARQUIVO)
                for p_dict in dados:
                    novo_produto = Produto(
                        id_produto  = p_dict['id'],
                        nome        = p_dict['nome'],
                        preco       = p_dict['preco'],
                        qtd_estoque = p_dict['qtd_estoque']
                    )
                    mercado.cadastrar_produto(novo_produto)

            with open(f"{self.caminho}/clientes.json","r",encoding="utf-8") as ARQUIVO_2:
                dados_2 = json.load(ARQUIVO_2)
                for c_dict in dados_2:
                    novo_cliente = Cliente(
                        cpf     = c_dict['cpf'],
                        nome    = c_dict['nome'],
                        email   = c_dict['email'],
                        idade   = c_dict['idade'],
                        senha   = c_dict['senha'],
                        db_read = True
                    )
                    autenticador.cadastrar_cliente(mercado=mercado,cliente=novo_cliente)
                    novo_cliente.set_saldo(c_dict['saldo'])
                    for item in c_dict['carrinho']['itens']:
                        prod_dict = item['produto']
                        qtd = item['quantidade']
                        produto_recuperado = None
                        for p in mercado.lista_produtos:
                            if p.id == prod_dict['id']:
                                produto_recuperado = p
                                break
                        if produto_recuperado:
                            novo_cliente.carrinho.adicionar_ao_carrinho(produto_recuperado,qtd)
                        else:
                            print(f"Produto '{prod_dict['id']}' não existe mais no mercado.")

            with open(f"{self.caminho}/administradores.json","r",encoding="utf-8") as ARQUIVO_3:
                dados_3 = json.load(ARQUIVO_3)
                for a_dict in dados_3:
                    novo_admin = Administrador(
                        cpf     = a_dict['cpf'],
                        nome    = a_dict['nome'],
                        email   = a_dict['email'],
                        idade   = a_dict['idade'],
                        senha   = a_dict['senha'],
                        db_read = True
                    )
                    autenticador.cadastrar_administrador(mercado=mercado,administrador=novo_admin)

        except FileNotFoundError:
            print(f"n\(PERSISTENCIA - CARREGAR) Banco de dados não encontrado.")
        except json.JSONDecodeError:
            print(f"n\(PERSISTENCIA - CARREGAR) Arquivo de dados corrompido.")
        except Exception as e:
            print(f"n\(PERSISTENCIA - CARREGAR) Erro ao carregar dados: {e}")

        return True