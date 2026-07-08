% link_css = '<link rel="stylesheet" href="static/css/admin.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Gerenciamento do Sistema', css_extra=link_css)

<div class="conteudo">
    <h1>Gerenciamento de Sistema</h1>
    <div class="dashboard">

        <button class="dash-btn">
            <span class="dash-btn-titulo">Gerenciamento de Produtos</span>
            <img src="static/img/box-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
        </button>

        <button class="dash-btn">
            <span class="dash-btn-titulo">Gerenciamento de Clientes</span>
            <img src="static/img/login-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
        </button>

        <button class="dash-btn">
            <span class="dash-btn-titulo">Gerenciamento de Vendas</span>
            <img src="static/img/cart-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
        </button>
    </div>
</div>