import uuid

from app.models.cliente import Cliente
from app.models.administrador import Administrador
from app.models.mercado import Mercado

class GerenciadorAutenticacao:
    def __init__(self):
        self.__usuarios_autenticados = {}

    def autenticar(self,mercado:Mercado, cpf: str, senha: str) -> str|None:
        usuario = self.get_usuario_por_cpf(mercado=mercado,cpf=cpf)
        if not usuario:
            return None
        if not usuario.check_senha(senha=senha):
            return None
        id_sessao = uuid.uuid4().hex
        self.__usuarios_autenticados[id_sessao] = usuario
        return id_sessao

    def logout(self,id_sessao:str):
        if id_sessao in self.__usuarios_autenticados:
            del self.__usuarios_autenticados[id_sessao]

    def get_usuario_por_cpf(self,mercado:Mercado, cpf:str) -> Cliente|Administrador|None:
        tentativa = mercado.get_cliente_por_cpf(cpf=cpf)
        if tentativa:
            return tentativa
        tentativa = mercado.get_administrador_por_cpf(cpf=cpf)
        if tentativa:
            return tentativa
        return None

    def get_usuario_por_id_sessao(self, id_sessao:str) -> Cliente|Administrador|None:
        if not id_sessao:
            return None
        return self.__usuarios_autenticados[id_sessao]