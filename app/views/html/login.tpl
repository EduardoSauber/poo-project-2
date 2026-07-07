% link_css = '<link rel="stylesheet" type="text/css" href="static/css/login.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Login', logado=False, usuario_admin=False, usuario_nome='', css_extra=link_css)

<div class='login'>
    <form method="POST" action="/login">
        % if get('erro', None):
            <p class="erro">{{ get('erro', '') }}</p>
        %end

        <label for="cpf">CPF</label>
        <input type="text" id="cpf" name="cpf">
        <label for="senha">Senha</label>
        <input type="password" id="senha" name="senha">
        <button type="submit">Login</button>
    </form>
</div>