<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{{ get('titulo_pagina', 'Mercadinho') }}</title>
    <link rel="stylesheet" href="static/css/base.css">
    {{!get('css_extra','') }}
</head>
<body>
    <header>
        <nav class="navbar">
            <button class="btn-navbar" onclick="location.href='/'">
                <div class="btn-navbar-content">
                    <img src="static/img/home-icon.svg" style="width: 24px; height: 24px; object-fit: contain;" alt="" aria-hidden="true"></img>
                    Página Inicial
                </div>
            </button>
                % if get('logado',False):
                    % if get('usuario_admin',False):
                        <button class="btn-navbar" onclick="location.href='/dashboard'">
                            <div class="btn-navbar-content">
                                <img src="static/img/settings-icon.svg" style="width: 24px; height: 24px; object-fit: contain;" alt="" aria-hidden="true"></img>
                                Painel de Gerenciamento
                            </div>
                        </button>
                    % else:
                        <button class="btn-navbar" onclick="location.href='/cart'">
                            <div class="btn-navbar-content">
                                <img src="static/img/cart-icon.svg" style="width: 24px; height: 24px; object-fit: contain;" alt="" aria-hidden="true"></img>
                                Meu Carrinho
                            </div>
                        </button>
                    % end
                % end
        </nav>
        <nav class="user">
            % if get('logado',False):
                <p>Bem-vindo, {{ usuario_nome }}!</p>
                <button class="btn-navbar" onclick="location.href='/logout'">
                    <div class="btn-navbar-content">
                        <img src="static/img/logout-icon.svg" style="width: 24px; height: 24px; object-fit: contain;" alt="" aria-hidden="true"></img>
                        Sair
                    </div>
                </button>
            % else:
                <button class="btn-navbar" onclick="location.href='/login'">
                    <div class="btn-navbar-content">
                        <img src="static/img/login-icon.svg" style="width: 24px; height: 24px; object-fit: contain;" alt="" aria-hidden="true"></img>
                        Logar
                    </div>
                </button>
            % end
        </nav>
    </header>

    <main>
        {{!base}}
    </main>

</body>
</html>