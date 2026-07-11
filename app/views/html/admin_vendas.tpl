% link_css = '<link rel="stylesheet" href="/static/css/admin.css">'
% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra=link_css)

<div class="conteudo">
    <h1>Gerenciamento de Vendas</h1>
    Receita Total: R$ {{f"{receita_total:.2f}"}}
    Quantidade de Vendas Realizadas: {{total_vendas}}
    <h2>Lista de Vendas</h2>
    <div class="lista-vendas">
        % for recibo in get('lista_vendas',[]):
        <div class="recibo-card">
            <img src="/static/img/box-icon.svg" style="width: 100px; height: 100px; object-fit: contain; align-self: center;" alt="" aria-hidden="true">
            <div class="recibo-card-info">Cliente: {{recibo['cliente']['nome']}} (CPF:{{recibo['cliente']['cpf']}})</div>
            <div class="recibo-card-info">Data: {{recibo['data']}}</div>
            <div class="recibo-card-info">Total: R$ {{recibo['total']}}</div>
            <div class="recibo-card-btns">
                <form action="/admin/vendas/{{recibo['id']}}" method="GET">
                    <button type="submit" class="btn-abrir">Abrir Recibo</button>
                </form>
            </div>
        </div>
        % end
    </div>
</div>
