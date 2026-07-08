% link_css = '<link rel="stylesheet" href="/static/css/admin.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Gerenciamento de Produtos', css_extra=link_css)

<div class="conteudo">
    <h1>Gerenciamento de Produtos</h1>
    <div class="dashboard">
        <button class="dash-btn" onclick="location.href='/admin/produtos/criar'">
            <span class="dash-btn-titulo">Adicionar Produto</span>
            <img src="/static/img/box-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
        </button>

        <button class="dash-btn" onclick="location.href='/admin/produtos/editar'">
            <span class="dash-btn-titulo">Editar Produto</span>
            <img src="/static/img/login-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
        </button>

        <button class="dash-btn" onclick="location.href='/admin/produtos/excluir'">
            <span class="dash-btn-titulo">Remover Produto</span>
            <img src="/static/img/cart-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
        </button>
    </div>
    <h2>Lista de Produtos</h2>
    <div class="lista-produtos">
        % for produto in get('lista_produtos',[]):
        <div class="produto-card">
            <p><strong>{{produto['nome']}}</strong></p>
            <img src="/static/img/box-icon.svg" style="width: 100px; height: 100px; object-fit: contain; align-self: center;" alt="" aria-hidden="true">
            <div class="produto-card-info">{{produto['id']}}</div>
            <div class="produto-card-info">R$ {{produto['preco']}} </div>
        </div>
        % end
    </div>
</div>