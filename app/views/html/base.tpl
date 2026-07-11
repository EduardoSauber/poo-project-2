<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ get('titulo_pagina', 'Mercadinho') }}</title>
    <!-- Favicon temporário removido -->
    <link rel="stylesheet" href="/static/css/base.css?v=2">
    {{!get('css_extra','') }}
</head>
<body>
    <header>
        <a href="/" class="brand-logo">
            <svg width="28" height="28" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
            Mercadinho
        </a>
        <nav class="navbar">
            <a href="/" class="btn-navbar">
                <div class="btn-navbar-content">
                    Página Inicial
                </div>
            </a>
            % if get('logado',False):
                % if get('usuario_admin',False):
                    <a href="/admin" class="btn-navbar">
                        <div class="btn-navbar-content">
                            Painel de Gerenciamento
                        </div>
                    </a>
                % else:
                    <a href="/carrinho" class="btn-navbar">
                        <div class="btn-navbar-content">
                            Meu Carrinho
                        </div>
                    </a>
                % end
            % end
        </nav>
        <nav class="user">
            % if get('logado',False):
                <p>Olá, {{ usuario_nome }}</p>
                <a href="/logout" class="btn-navbar">
                    <div class="btn-navbar-content">
                        Sair
                    </div>
                </a>
            % else:
                <a href="/login" class="btn-navbar">
                    <div class="btn-navbar-content">
                        Entrar
                    </div>
                </a>
            % end
        </nav>
    </header>

    <main>
        {{!base}}
    </main>

    <footer>
        &copy; 2026 Mercadinho. Todos os direitos reservados.
    </footer>
</body>
</html>