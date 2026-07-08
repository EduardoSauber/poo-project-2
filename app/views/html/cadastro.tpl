% link_css = '<link rel="stylesheet" type="text/css" href="static/css/login.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Cadastro', logado=False, usuario_admin=False, usuario_nome='', css_extra=link_css)

<div class='login'>
    <form method="POST" action="/cadastro">
        % if get('erro', None):
            <p class="erro">{{ get('erro', '') }}</p>
        %end

        <h2>Criar Conta</h2>

        <label for="nome">Nome</label>
        <input type="text" id="nome" name="nome">

        <label for="cpf">CPF</label>
        <input type="text" id="cpf" name="cpf" maxlength="11" placeholder="Somente números">

        <label for="email">E-mail</label>
        <input type="email" id="email" name="email">

        <label for="idade">Idade</label>
        <input type="number" id="idade" name="idade" min="1">

        <label for="senha">Senha</label>
        <input type="password" id="senha" name="senha">

        <button type="submit">Cadastrar</button>
        <a href="/login">Já tem conta? Faça login</a>
    </form>
</div>
