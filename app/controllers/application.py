from typing import Any

from bottle import template

from app.models.mercado import Mercado
from app.controllers.autenticacao import GerenciadorAutenticacao
from app.controllers.persistencia import GerenciadorPersistencia

class Application():

    def __init__(self):
        self.pages = {
            'home'  : self.home()
        }
        self.gerenciador_autenticacao = GerenciadorAutenticacao()
        self.gerenciador_persistencia = GerenciadorPersistencia()
        self.mercado = Mercado()
        self.gerenciador_persistencia.carregar_dados(self.mercado)
        
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
