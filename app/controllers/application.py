from typing import Any

from bottle import template

from app.models.mercado import Mercado
from app.controllers.autenticacao import GerenciadorAutenticacao
from app.controllers.persistencia import GerenciadorPersistencia
from app.models.administrador import Administrador
from app.models.cliente import Cliente
from app.controllers.loja_controllers import LojaController

class Application():

    def __init__(self):
        self.pages = {
            'home'  : self.home()
        }
        self.gerenciador_autenticacao = GerenciadorAutenticacao()
        self.gerenciador_persistencia = GerenciadorPersistencia()
        self.mercado = Mercado()
        self.gerenciador_persistencia.carregar_dados(self.mercado)
        self.__seed_admin_padrao()

        self.loja_controller = LojaController()

    def render(self,page):
       content = self.pages.get(page, self.helper())
       return content

    def helper(self):
        return template('app/views/html/helper')

    def home(self):
        lista_produtos = [
            {'nome': 'PLACEHOLDER','preco':'12,34'},
            {'nome': 'PLACEHOLDER','preco':'12,34'},
            {'nome': 'PLACEHOLDER','preco':'12,34'},
            {'nome': 'PLACEHOLDER','preco':'12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'},
            {'nome': 'PLACEHOLDER', 'preco': '12,34'}
        ]
        return template('app/views/html/home',
                        titulo_pagina='Pagina Inicial',
                        logado = False,
                        usuario_admin = False,
                        usuario_nome='PLACEHOLDER',
                        lista_produtos=lista_produtos
                        )
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

    def get_vitrine_page(self, usuario):
        produtos = self.loja_controller.get_vitrine(self.mercado)
        logado = usuario is not None
        return template('app/views/html/vitrine',
                        titulo_pagina='Vitrine',
                        logado=logado,
                        usuario_admin=isinstance(usuario, Administrador) if logado else False,
                        usuario_nome=usuario.get_nome() if logado else '',
                        lista_produtos=produtos
                        )

