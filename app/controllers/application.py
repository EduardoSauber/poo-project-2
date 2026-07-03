from typing import Any

from bottle import template


class Application():

    def __init__(self):
        self.pages = {
            'home'  : self.home()
        }


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
