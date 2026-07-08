from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response

from functools import wraps
from app.models.administrador import Administrador

app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')

@app.error(404)
def error404(error):
    return template('app/views/html/404',erro=error.status,req_url=request.url)

#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/', method=['GET'])
def home(info=None):
    id_sessao = request.get_cookie('sessao', secret='chave-secreta')
    usuario = ctl.get_usuario_logado(id_sessao)
    if not usuario:
        return redirect('/login')
    return ctl.render_home(usuario)


@app.route('/login', method=['GET', 'POST'])
def login_handler(info=None):
    if request.method == 'POST':
        cpf   = request.forms.get('cpf')
        senha = request.forms.get('senha')
        id_sessao = ctl.login(cpf, senha)
        if id_sessao:
            response.set_cookie('sessao', id_sessao, secret='chave-secreta')
            return redirect('/')
        return ctl.get_login_page(erro='CPF ou senha incorretos.')
    return ctl.get_login_page()



@app.route('/logout', method=['GET'])
def logout(info=None):
    id_sessao = request.get_cookie('sessao', secret='chave-secreta')

    ctl.logout(id_sessao)
    response.delete_cookie('sessao')
    return redirect('/login')
    
def requer_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        id_sessao = request.get_cookie('sessao', secret='chave-secreta')
        if not ctl.get_usuario_logado(id_sessao):
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
def requer_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        id_sessao = request.get_cookie('sessao', secret='chave-secreta')
        usuario = ctl.get_usuario_logado(id_sessao)
        if not usuario or not isinstance(usuario, Administrador):
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper


@app.route('/admin', method=['GET'])
@requer_admin
def admin_dashboard():
    id_sessao = request.get_cookie('sessao', secret='chave-secreta')
    usuario = ctl.get_usuario_logado(id_sessao)
    return ctl.render_admin_dashboard(usuario)


@app.route('/admin/produtos', method=['GET'])
@requer_admin
def admin_dashboard_produtos():
    id_sessao = request.get_cookie('sessao', secret='chave-secreta')
    usuario = ctl.get_usuario_logado(id_sessao)
    return ctl.render_admin_produtos(usuario)
#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)
