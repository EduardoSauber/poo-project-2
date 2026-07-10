from typing import Any

from bottle import template

from app.models import produto
from app.models.cliente import Cliente
from app.models.mercado import Mercado
from app.controllers.autenticacao import GerenciadorAutenticacao
from app.controllers.persistencia import GerenciadorPersistencia
from app.controllers.produto_controller import GerenciadorProduto
from app.models.administrador import Administrador
from app.models.produto import Produto

from app.models.cliente import Cliente
from app.controllers.loja_controllers import LojaController

class Application():

    def __init__(self):
        self.pages = {
        }
        self.gerenciador_autenticacao = GerenciadorAutenticacao()
        self.gerenciador_persistencia = GerenciadorPersistencia()
        self.gerenciador_produto = GerenciadorProduto()
        self.mercado = Mercado()
        self.gerenciador_persistencia.carregar_dados(self.mercado)
        self.__seed_admin_padrao()

        self.loja_controller = LojaController()

    def render(self,page):
       content = self.pages.get(page, self.helper())
       return content

    def helper(self):
        return template('app/views/html/helper')

    def login(self, cpf, senha):
        return self.gerenciador_autenticacao.autenticar(self.mercado, cpf, senha)

    def logout(self, id_sessao):
        return self.gerenciador_autenticacao.logout(id_sessao)
    
    def get_login_page(self, erro=None, sucesso=None):
        return template('app/views/html/login', erro=erro, sucesso=sucesso)

    def render_home(self, usuario=None):
        from app.models.administrador import Administrador
        logado = usuario is not None
        return template('app/views/html/home',
                        titulo_pagina='Pagina Inicial',
                        logado=logado,
                        usuario_admin=isinstance(usuario, Administrador) if logado else False,
                        usuario_nome=usuario.get_nome() if logado else '',
                        lista_produtos=[p.to_dict() for p in self.mercado.lista_produtos]
                        )

    def render_admin_dashboard(self,usuario:Cliente|Administrador=None):
        logado = usuario is not None
        return template('app/views/html/admin_dashboard',
                        titulo_pagina = 'Painel Administrador',
                        logado = logado,
                        usuario_admin = isinstance(usuario, Administrador) if logado else False,
                        usuario_nome = usuario.get_nome() if logado else '',
                        total_clientes = len(self.mercado.lista_clientes),
                        total_produtos = len(self.mercado.lista_produtos)
                        )

    def render_admin_produtos(self,usuario:Cliente|Administrador=None,erro=None):
        logado = usuario is not None
        return template('app/views/html/admin_produtos',
                        titulo_pagina = 'Gerenciamento de Produtos',
                        logado = logado,
                        usuario_admin = isinstance(usuario, Administrador) if logado else False,
                        usuario_nome = usuario.get_nome() if logado else '',
                        lista_produtos=[p.to_dict() for p in self.mercado.lista_produtos],
                        erro=erro
                        )

    def cadastrar_produto(self,data:dict[str,Any]) -> dict:
        if not data:
            return {'ok' : False, 'erro' : 'Nenhum dado enviado.'}
        evento = self.gerenciador_produto.criar_produto(data=data,mercado=self.mercado)
        if evento.get('ok'):
            self.gerenciador_persistencia.salvar_produtos(self.mercado)
        return evento

    def excluir_produto(self,nome:str) -> dict:
        if not nome:
            return {'ok': False, 'erro': 'Nenhum dado enviado.'}
        evento = self.gerenciador_produto.excluir_produto(nome=nome,mercado=self.mercado)
        if evento.get('ok'):
            self.gerenciador_persistencia.salvar_produtos(self.mercado)
        return evento

    def editar_produto(self,data:dict[str,Any]) -> dict:
        if not data:
            return {'ok': False, 'erro': 'Nenhum dado enviado.'}
        evento = self.gerenciador_produto.editar_produto(data=data, mercado=self.mercado)
        if evento.get('ok'):
            self.gerenciador_persistencia.salvar_produtos(self.mercado)
        return evento

    def get_admin_clientes_page(self,usuario:Cliente|Administrador=None,erro=None):
        logado = usuario is not None
        return template('app/views/html/admin_clientes',
                        titulo_pagina = 'Gerenciamento de Clientes',
                        logado = logado,
                        usuario_admin = isinstance(usuario, Administrador) if logado else False,
                        usuario_nome = usuario.get_nome() if logado else '',
                        lista_clientes=[c.to_dict(publico=True) for c in self.mercado.lista_clientes],
                        erro=erro
                        )

    def excluir_cliente(self,cpf:str) -> dict:
        if not str(cpf):
            return {'ok': False, 'erro': 'Nenhum dado enviado.'}
        for cliente in self.mercado.lista_clientes:
            if cliente.get_cpf() == str(cpf):
                self.mercado.lista_clientes.remove(cliente)
                self.gerenciador_persistencia.salvar_clientes(self.mercado)
                return {'ok': True}
        return {'ok': False, 'erro': 'Cliente não encontrado.'}

    def editar_cliente(self,data:dict[str,Any]) -> dict:
        if not data:
            return {'ok': False, 'erro': 'Nenhum dado enviado.'}

        cpf_original = str(data.get('cpf_original'))
        if not cpf_original:
            return {'ok': False, 'erro': 'CPF do cliente não pode ser vazio.'}

        nome = data.get('nome',"").strip()
        cpf = data.get('cpf',"").strip()
        email = data.get('email',"").strip()
        idade = data.get('idade',"")
        senha = data.get('senha',"")

        if not nome or not cpf or not email or not idade:
            return {'ok': False, 'erro': 'Preencha todos os campos.'}
        if senha and len(senha) < 6:
            return {'ok': False, 'erro': 'A senha deve ter no mínimo 6 caracteres.'}
        if cpf != cpf_original:
            if self.gerenciador_autenticacao.get_usuario_por_cpf(cpf=str(cpf),mercado=self.mercado):
                return {'ok': False, 'erro': 'CPF já cadastrado.'}

        try:
            idade = int(idade)
        except (ValueError, TypeError):
            return {'ok': False, 'erro': 'Idade inválida.'}

        if idade < 0 or idade > 100:
            return {'ok': False, 'erro': 'Idade inválida.'}

        alteracoes = 0
        cliente_encontrado = False
        for cliente in self.mercado.lista_clientes:
            if cliente.get_cpf() == cpf_original:
                cliente_encontrado = True
                if nome != cliente.get_nome():
                    cliente.set_nome(nome)
                    alteracoes += 1
                if cpf != cliente.get_cpf() :
                    cliente.set_cpf(cpf)
                    alteracoes += 1
                if email != cliente.email:
                    cliente.email = email
                    alteracoes += 1
                if idade != cliente.idade:
                    cliente.idade = idade
                    alteracoes += 1
                if senha != '' and not cliente.check_senha(senha):
                    cliente.set_senha(senha)
                    alteracoes += 1
                break
        if not cliente_encontrado:
            return {'ok': False, 'erro': 'Cliente não encontrado no sistema.'}

        if alteracoes > 0:
            self.gerenciador_persistencia.salvar_clientes(self.mercado)
            return {'ok': True}

        return {'ok': False, 'erro': 'Nenhuma alteração feita.'}


    def __seed_admin_padrao(self):
        if not self.mercado.lista_administradores:
            admin = Administrador('12345678901', 'Admin Padrao', 'admin@teste.com', 20, '123456', False)
            self.mercado.cadastrar_administrador(admin)
            self.gerenciador_persistencia.salvar_administradores(self.mercado)

    def get_usuario_logado(self, id_sessao):
        return self.gerenciador_autenticacao.get_usuario_por_id_sessao(id_sessao)

    def get_cadastro_page(self, erro=None):
        return template('app/views/html/cadastro', erro=erro)
        
    def cadastrar_cliente(self, dados: dict) -> dict:
        nome = dados.get('nome')
        cpf = dados.get('cpf')
        email = dados.get('email')
        idade = dados.get('idade')
        senha = dados.get('senha')

        if not nome or not cpf or not email or not idade or not senha:
            return {'ok': False, 'erro': 'Preencha todos os campos.'}

        if len(senha) < 6:
            return {'ok': False, 'erro': 'A senha deve ter no mínimo 6 caracteres.'}

        try:
            idade = int(idade)
        
        except (ValueError, TypeError):
            return {'ok': False, 'erro': 'Idade inválida.'}

        if idade < 0 or idade > 100:
            return {'ok': False, 'erro': 'Idade inválida.'}

        cliente = Cliente(cpf, nome, email, idade, senha, db_read=False)

        if not self.mercado.cadastrar_cliente(cliente):
            return {'ok': False, 'erro': 'CPF já cadastrado.'}

        self.gerenciador_persistencia.salvar_clientes(self.mercado)
        return {'ok': True}

    def get_vitrine_page(self, usuario, sucesso=None, erro=None):
        produtos = self.loja_controller.get_vitrine(self.mercado)
        logado = usuario is not None
        return template('app/views/html/vitrine',
                        titulo_pagina='Vitrine',
                        logado=logado,
                        usuario_admin=isinstance(usuario, Administrador) if logado else False,
                        usuario_nome=usuario.get_nome() if logado else '',
                        lista_produtos=produtos,
                        sucesso=sucesso,
                        erro=erro
                        )

    def adicionar_ao_carrinho(self, usuario, produto_nome: str, quantidade: int) -> dict:
        produto = next((p for p in self.mercado.lista_produtos if p.nome == produto_nome), None)

        if not produto:
            return {'ok': False, 'erro': 'Produto nao encontrado'}

        item_no_carrinho = usuario.carrinho.get_produto_quantidade(produto)
        quantidade_no_carrinho = item_no_carrinho['quantidade'] if item_no_carrinho else 0
        quantidade_total_desejada = quantidade_no_carrinho + quantidade

        if quantidade_total_desejada > produto.get_estoque():
            return {'ok': False, 'erro': f'Atenção! Você já tem {quantidade_no_carrinho} deste produto no carrinho. O estoque limite é de {produto.get_estoque()}.'}

        usuario.carrinho.adicionar_ao_carrinho(produto, quantidade)
        return {'ok': True}

    def get_carrinho_page(self, usuario):
        logado = usuario is not None

        itens = []

        for item in usuario.carrinho.lista_items:
            itens.append({
                'produto' : item['produto'].to_dict(),
                'quantidade' : item['quantidade'],
                'subtotal': round(item['produto'].get_preco() * item['quantidade'], 2)
            })

        return template('app/views/html/carrinho',
                    titulo_pagina='Meu Carrinho',
                    logado=logado,
                    usuario_admin=isinstance(usuario, Administrador) if logado else False,
                    usuario_nome=usuario.get_nome() if logado else '',
                    itens=itens,
                    total=usuario.carrinho.total
                    )

    def remover_do_carrinho(self, usuario, produto_nome: str, quantidade: int = None) -> dict:
        produto = next((p for p in self.mercado.lista_produtos if p.nome == produto_nome), None)

        if not produto:
            return {'ok': False, 'erro': 'Produto nao encontrado'}

        item_no_carrinho = usuario.carrinho.get_produto_quantidade(produto)
        if item_no_carrinho:
            qtd_remover = quantidade if quantidade is not None else item_no_carrinho['quantidade']
            usuario.carrinho.remover_do_carrinho(produto, qtd_remover)
            return {'ok': True}
        
        return {'ok': False, 'erro': 'Produto não está no carrinho.'}

    def get_recibo_page(self, usuario, recibo_dict):
        logado = usuario is not None
        return template('app/views/html/recibo',
                        titulo_pagina='Recibo da Compra',
                        logado=logado,
                        usuario_admin=False,
                        usuario_nome=usuario.get_nome() if logado else '',
                        recibo=recibo_dict
                        )

        

    def get_checkout_page(self, usuario):
        if not usuario.carrinho.lista_items: 
            return None

        logado = usuario is not None
        
        itens = []
        for item in usuario.carrinho.lista_items:
            itens.append({
                'produto': item['produto'].to_dict(),
                'quantidade': item['quantidade'],
                'subtotal': round(item['produto'].get_preco() * item['quantidade'], 2)
            })
        
        return template('app/views/html/checkout',
                    titulo_pagina='Checkout',
                    logado=logado,
                    usuario_admin=False,
                    usuario_nome=usuario.get_nome() if logado else '',
                    itens=itens,
                    total=usuario.carrinho.total
                    )

    def confirmar_compra(self, usuario) -> dict:
        if not usuario.carrinho.lista_items:
            return {'ok': False, 'erro': 'Carrinho vazio'}
        
        for item in usuario.carrinho.lista_items:
            item['produto'].descontar_estoque(item['quantidade'])
            
        recibo = self.mercado.emitir_recibo(usuario)

        usuario.carrinho.limpar_carrinho()

        self.gerenciador_persistencia.salvar_produtos(self.mercado)
        self.gerenciador_persistencia.salvar_clientes(self.mercado)

        return {'ok': True, 'recibo': recibo.to_dict()}