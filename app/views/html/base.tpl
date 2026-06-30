<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{{ get('titulo_pagina', 'Mercadinho') }}</title>
    <style>
        /* Organização Cabeçalho */
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #f4f4f4;
        }
        nav {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .btn {
            padding: 5px 10px;
            cursor: pointer;
        }
    </style>
    <!-- Para injetar CSS mais bonito pelas páginas que vão herdar essa base -->
    {{!get('css_extra','') }}
</head>
<body>
    <header>
        <nav class="navbar">
            <button class="btn" onclick="location.href='/home'">Página Inicial</button>
                % if get('logado',False):
                    % if get('usuario_admin',False):
                        <button class="btn" onclick="location.href='/dashboard'">Painel de Gerenciamento</button>
                    % else:
                        <button class="btn" onclick="location.href='/cart'">Meu Carrinho</button>
                    % end
                % end
        </nav>
        <nav class="user">
            % if get('logado',False):
                <p>Bem-vindo, {{ usuario_nome }}!</p>
                <button class="btn" onclick="location.href='/logout'">Sair</button>
            % else:
                <button class="btn" onclick="location.href='/login'">Logar</button>
            % end
        </nav>
    </header>

    <main>
        {{!base}}
    </main>

</body>
</html>