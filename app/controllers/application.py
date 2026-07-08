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

    def render(self,page):
       content = self.pages.get(page, self.helper())
       return content

    def helper(self):
        return template('app/views/html/helper')

    def login(self, cpf, senha):
        return self.gerenciador_autenticacao.autenticar(self.mercado, cpf, senha)

    def logout(self, id_sessao):
        return self.gerenciador_autenticacao.logout(id_sessao)
    
    def get_login_page(self, erro=None):
        return template('app/views/html/login', erro=erro)

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
                        usuario_nome = usuario.get_nome() if logado else ''
                        )

    def render_admin_produtos(self,usuario:Cliente|Administrador=None):
        logado = usuario is not None
        return template('app/views/html/admin_produtos',
                        titulo_pagina = 'Gerenciamento de Produtos',
                        logado = logado,
                        usuario_admin = isinstance(usuario, Administrador) if logado else False,
                        usuario_nome = usuario.get_nome() if logado else '',
                        lista_produtos=[p.to_dict() for p in self.mercado.lista_produtos]
                        )

    def cadastrar_produto(self,data:dict[str,Any]) -> dict:
        if not data:
            return {'ok' : False, 'erro' : 'Nenhum dado enviado.'}
        evento = self.gerenciador_produto.criar_produto(data=data,mercado=self.mercado)
        if evento.get('ok'):
            self.gerenciador_persistencia.salvar_produtos(self.mercado)
        return evento

    def excluir_produto(self,nome:str):
        if not nome:
            return {'ok': False, 'erro': 'Nenhum dado enviado.'}
        evento = self.gerenciador_produto.excluir_produto(nome=nome,mercado=self.mercado)
        if evento.get('ok'):
            self.gerenciador_persistencia.salvar_produtos(self.mercado)
        return evento

    def __seed_admin_padrao(self):
        if not self.mercado.lista_administradores:
            admin = Administrador('12345678901', 'Admin Padrao', 'admin@teste.com', 20, '123456', False)
            self.mercado.cadastrar_administrador(admin)
            self.gerenciador_persistencia.salvar_administradores(self.mercado)

    def get_usuario_logado(self, id_sessao):
        return self.gerenciador_autenticacao.get_usuario_por_id_sessao(id_sessao)