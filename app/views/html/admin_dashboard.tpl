% link_css = '<link rel="stylesheet" href="/static/css/admin.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Gerenciamento do Sistema', css_extra=link_css)

<div class="w-100" style="max-width: 1200px; margin: 0 auto;">
    <h1 class="text-center mb-20">Gerenciamento de Sistema</h1>
    <div class="dashboard">

        <button class="dash-btn" onclick="location.href='/admin/produtos'">
            <span class="dash-btn-titulo">Produtos</span>
            <img src="/static/img/box-icon.svg" style="width: 80px; height: 80px; object-fit: contain; margin-bottom: 10px;" alt="" aria-hidden="true">
            <p style="color: var(--text-sub);">Total cadastrado: <strong>{{total_produtos}}</strong></p>
        </button>

        <button class="dash-btn" onclick="location.href='/admin/clientes'">
            <span class="dash-btn-titulo">Clientes</span>
            <img src="/static/img/login-icon.svg" style="width: 80px; height: 80px; object-fit: contain; margin-bottom: 10px;" alt="" aria-hidden="true">
            <p style="color: var(--text-sub);">Total cadastrado: <strong>{{total_clientes}}</strong></p>
        </button>

        <button class="dash-btn" onclick="location.href='/admin/vendas'">
            <span class="dash-btn-titulo">Vendas</span>
            <img src="/static/img/cart-icon.svg" style="width: 80px; height: 80px; object-fit: contain; margin-bottom: 10px;" alt="" aria-hidden="true">
            <p style="color: var(--text-sub);">Total realizadas: <strong>{{total_vendas}}</strong></p>
        </button>
    </div>
</div>