import json
import os
from app.models.mercado import Mercado
from app.models.produto import Produto
from app.models.recibo import Recibo
from app.models.cliente import Cliente
from app.models.administrador import Administrador
from app.controllers.autenticacao import GerenciadorAutenticacao

'''
No arquivo de 'dependências' para o Docker, existe o filelock. Ele pode ser muito útil para evitar que dados sejam
corrompidos na hora de ler/gravar. - Eduardo
'''

class GerenciadorPersistencia:
    def __init__(self,caminho_db:str=os.path.join(os.path.dirname(os.path.abspath(__file__)),"db")):
        self.caminho = caminho_db

    def salvar_produtos(self,mercado:Mercado):
        produtos_dict = []
        for produtos in mercado.lista_produtos:
            produtos_dict.append(produtos.to_dict())
        self.salvar_dados(produtos_dict,"produtos")

    def salvar_vendas(self,mercado:Mercado):
        vendas_dict = []
        for recibo in mercado.lista_vendas:
            vendas_dict.append(recibo.to_dict())
        self.salvar_dados(vendas_dict,"vendas")

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
                print(f"\n(PERSISTENCIA - SALVAR) Banco de dados '{banco_dados}' salvo.")
        except Exception as e:
            print(f"\n(PERSISTENCIA - SALVAR) Erro ao salvar banco de dados '{banco_dados}': {e}")

    def carregar_dados(self,mercado:Mercado):
        try:
            with open(f"{self.caminho}/produtos.json","r",encoding="utf-8") as ARQUIVO:
                dados = json.load(ARQUIVO)
                for p_dict in dados:
                    novo_produto = Produto(
                        nome        = p_dict['nome'],
                        preco       = p_dict['preco'],
                        qtd_estoque = p_dict['qtd_estoque']
                    )
                    mercado.cadastrar_produto(novo_produto)
        except FileNotFoundError:
            print(f"\n(PERSISTENCIA - CARREGAR) Banco de dados não encontrado.")
        except json.JSONDecodeError:
            print(f"\n(PERSISTENCIA - CARREGAR) Arquivo de dados corrompido.")
        except Exception as e:
            print(f"\n(PERSISTENCIA - CARREGAR) Erro ao carregar dados: {e}")

        try:
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
                    mercado.cadastrar_cliente(cliente=novo_cliente)
                    novo_cliente.set_compras(c_dict.get('compras',0))
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
        except FileNotFoundError:
            print(f"\n(PERSISTENCIA - CARREGAR) Banco de dados não encontrado.")
        except json.JSONDecodeError:
            print(f"\n(PERSISTENCIA - CARREGAR) Arquivo de dados corrompido.")
        except Exception as e:
            print(f"\n(PERSISTENCIA - CARREGAR) Erro ao carregar dados: {e}")

        try:
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
                    mercado.cadastrar_administrador(administrador=novo_admin)
        except FileNotFoundError:
            print(f"\n(PERSISTENCIA - CARREGAR) Banco de dados não encontrado.")
        except json.JSONDecodeError:
            print(f"\n(PERSISTENCIA - CARREGAR) Arquivo de dados corrompido.")
        except Exception as e:
            print(f"\n(PERSISTENCIA - CARREGAR) Erro ao carregar dados: {e}")

        try:
            with open(f"{self.caminho}/vendas.json","r",encoding="utf-8") as ARQUIVO_4:
                dados = json.load(ARQUIVO_4)
                for v_dict in dados:
                    novo_recibo = Recibo()
                    novo_recibo.set_id(v_dict['id'])
                    novo_recibo.set_data(v_dict['data'])
                    novo_recibo.set_cliente(v_dict['cliente']['nome'],v_dict['cliente']['cpf'])
                    v_produtos = v_dict['itens']
                    for vp_dict in v_produtos:
                        v_produto = Produto(
                        nome        = vp_dict['produto'].get('nome',''),
                        preco       = vp_dict['produto'].get('preco',0.0),
                        qtd_estoque = vp_dict['produto'].get('qtd_estoque',0)
                        )
                        novo_recibo.adicionar_itens({'produto':v_produto,'quantidade':vp_dict['quantidade']})
                    novo_recibo.set_total(v_dict.get('total',0.0))
                    mercado.lista_vendas.append(novo_recibo)
        except FileNotFoundError:
            print(f"\n(PERSISTENCIA - CARREGAR) Banco de dados não encontrado.")
        except json.JSONDecodeError:
            print(f"\n(PERSISTENCIA - CARREGAR) Arquivo de dados corrompido.")
        except Exception as e:
            print(f"\n(PERSISTENCIA - CARREGAR) Erro ao carregar dados: {e}")

        return True
