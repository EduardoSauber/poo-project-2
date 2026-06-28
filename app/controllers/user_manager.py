########################################################################################################################
# Import
import os
import json
import uuid

from app.models.user import User, SuperUser


########################################################################################################################
# Class
class UserManager:
    """"Banco de Dados JSON e Controle de Usuários"""

    def __init__(self):
        self.__all_users = {'user_accounts' : [], 'superuser_accounts' : []}
        self.__authenticated_users = {}
        self.__DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),"db")

        self.__read('user_accounts')
        self.__read('superuser_accounts')
        self.check_admins()

    # -- Leitura e Escrita Banco de Dados -- #
    def __read(self,database):
        account_class = SuperUser if (database == 'superuser_accounts') else User
        try:
            with open(f"{self.__DATA_PATH}/{database}.json", "r") as FILE:
                user_data = json.load(FILE)
                self.__all_users[database] = [account_class(**data,is_hashed=True) for data in user_data]
        except FileNotFoundError:
            print(f"(READ) userController: Não foi encontrado um banco de dados de '{database}'.")
            self.__all_users[database].append(account_class(username="Guest",
                                                            password="000000",
                                                            cpf="00000000000",
                                                            contact="",
                                                            email=""))

    def __write(self, database):
        try:
            with open(f"{self.__DATA_PATH}/{database}.json", "w") as FILE:
                user_data = [usr_account.to_dict() for usr_account in self.__all_users[database]]
                json.dump(user_data, FILE)
                print(f"(WRITE) userController: Arquivo '{database}.json' gravado no banco de dados.")
        except FileNotFoundError:
            raise TypeError(f"(WRITE) userController: O sistema não conseguiu gerar o arquivo '{database}.json'.")

    # -- Adicionar Admin genérico -- #
    def check_admins(self):
        if not self.get_superuser_accounts():
            self.create_user(username="admin", password="admin123", cpf="admin", email=None, contact=None,
                             perms=['admin'])
            self.__write('superuser_accounts')  # será que o admin genérico deveria ser salvo?
                                                # ou melhor, só manter ele criado enquanto não existir um admin
                                                # fixo no sistema (criar um admin pelo admin genérico)

    # -- Manuseamento de usuários -- #
    def create_user(self, username:str, password:str, cpf:str, email:str='', contact:str='', perms=None) \
            -> User | SuperUser |  None:
        if cpf is None:
            print("Valor 'cpf' não pode ser vazio.")
            return None
        if self.get_user_account_by_id(cpf) is not None:
            print(f"userController: Já existe um usuário com ID '{cpf}'.")
            return None

        if perms:
            user_type = 'superuser_accounts'
            new_user = SuperUser(username=username, password=password, cpf=cpf, email=email, contact=contact,
                                 permissions=perms)
        else:
            user_type = 'user_accounts'
            new_user = User(username=username, password=password, cpf=cpf, email=email, contact=contact)

        self.__all_users[user_type].append(new_user)

        print(f"userController: Usuário '{new_user.cpf}' cadastrado no banco de dados.")
        self.__write(user_type)
        return new_user

    def modify_user(self,user_id:str,n_username=None,n_pswrd=None,n_cpf=None,n_mail=None,n_contact=None) -> bool:
        user:User|SuperUser|None = self.get_user_account_by_id(user_id)
        if not user:
            print(f"userController: Usuário '{user_id}' não encontrado no banco de dados.")
            return False

        user_type = ('superuser_accounts' if user.is_admin() else 'user_accounts')

        if n_username:
            user.username = n_username
        if n_pswrd:
            user.password = n_pswrd
        if n_cpf:
            if not self.get_user_account_by_id(n_cpf):
                user.cpf = n_cpf
        if n_mail:
            user.email = n_mail
        if n_contact:
            user.contact = n_contact

        print(f"userController: {'Super ' if user_type == 'superuser_accounts' else ''}Usuário '{user.cpf}'"
              f" atualizado no banco de dados.")
        self.__write(user_type)
        return True

    def remove_user(self,user_id:str) -> bool:
        if not user_id:
            return False

        user = self.get_user_account_by_id(user_id)

        if not user:
            print(f"userController: Usuário {user_id} não foi encontrado no banco de dados.")
            return False

        user_type = 'superuser_accounts' if user.is_admin() else 'user_accounts'
        self.__all_users[user_type].remove(user)

        print(f"userController: O usuário {'(Super) ' if user.is_admin() else ''}{user.username}"
              f" foi removido do banco de dados.")
        self.__write(user_type)
        return True

    def get_authenticated_users(self) -> dict[str,User|SuperUser]:
        return self.__authenticated_users

    def get_user_accounts(self) -> list | None:
        return self.__all_users.get("user_accounts")

    def get_superuser_accounts(self) -> list | None:
        return self.__all_users.get("superuser_accounts")

    def get_user_account_by_id(self, user_id:str) -> User | SuperUser | None:
        if not user_id:
            return None
        for user_type in ['user_accounts','superuser_accounts']:
            for user in self.__all_users[user_type]:
                if user.cpf == user_id:
                    return user
        return None

    def get_user_account_by_session_id(self, session_id) -> User | SuperUser | None:
        return self.__authenticated_users.get(session_id)

    def get_username(self,session_id:str) -> str | None:
        user = self.get_user_account_by_session_id(session_id)
        return user.username if user else None

    def get_session_permissions(self, session_id) -> list:
        if session_id:
            user = self.__authenticated_users.get(session_id)
            if user and hasattr(user,'permissions'):
                return user.permissions
        return []

    def authenticate_user(self, cpf:str, password:str) -> str | None:
        user = self.get_user_account_by_id(cpf)

        if user and user.check_password(password):
            session_id = uuid.uuid4().hex
            self.__authenticated_users[session_id] = user
            return session_id

        return None

    def logout(self, session_id):
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id]

# Testbench
def testbench():
    Controller = UserManager()

    Controller.create_user("Teste","12345","12345678912","mail@mail.m","1212345678")
    for item in Controller.get_user_accounts():
        print(item)
    Controller.modify_user("12345678912",n_username="NomeTeste")
    for item in Controller.get_user_accounts():
        print(item)
    Controller.remove_user("12345678912")
    for item in Controller.get_user_accounts():
        print(item)

if __name__ == '__main__':
    testbench()