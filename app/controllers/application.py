from typing import Any

from bottle import template

from app.models.mercado import Mercado
from app.controllers.autenticacao import GerenciadorAutenticacao
from app.controllers.persistencia import GerenciadorPersistencia
from app.models.administrador import Administrador

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
    
    def get_login_page(self, erro=None):
        return template('app/views/html/login', erro=erro)

    def __seed_admin_padrao(self):
        if not self.mercado.lista_administradores:
            admin = Administrador('12345678901', 'Admin Padrao', 'admin@teste.com', 20, '123456', False)
            self.mercado.cadastrar_administrador(admin)
            self.gerenciador_persistencia.salvar_administradores(self.mercado)

    