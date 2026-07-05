from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response


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

@app.route('/', methods=['GET'])
def home(info=None):
    return ctl.render('home')


#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True)
