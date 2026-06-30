from bottle import template


class Application():

    def __init__(self):
        self.pages = {
        }


    def render(self,page):
       content = self.pages.get(page, self.helper)
       return content()


    def helper(self):
        return template('app/views/html/helper')

    def home(self,info):
        return template('home',
                        logado = False,
                        usuario_admin = False,
                        titulo_pagina='Pagina Inicial',
                        usuario_nome='PLACEHOLDER',
                        )
