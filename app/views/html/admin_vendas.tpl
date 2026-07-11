% link_css = '<link rel="stylesheet" href="/static/css/admin.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Gerenciamento de Vendas', css_extra=link_css)

<div class="w-100" style="max-width: 1200px; margin: 0 auto;">
    <h1 class="text-center mb-20">Gerenciamento de Vendas</h1>
    
    <div class="glass-card text-center mb-20" style="max-width: 600px;">
        <h3>Resumo</h3>
        <p>Receita Total: <strong>R$ {{f"{receita_total:.2f}"}}</strong></p>
        <p>Vendas Realizadas: <strong>{{total_vendas}}</strong></p>
    </div>

    <h2 class="text-center mb-20">Lista de Vendas</h2>
    
    <div class="grid-cards">
        % for recibo in get('lista_vendas',[]):
        <div class="glass-card text-center" style="padding: 20px;">
            <img src="/static/img/cart-icon.svg" style="width: 60px; height: 60px; object-fit: contain; margin-bottom: 15px;" alt="" aria-hidden="true">
            <p style="font-weight: 600; margin-bottom: 5px;">{{recibo['cliente']['nome']}}</p>
            <p style="color: var(--text-sub); font-size: 0.9rem; margin-bottom: 5px;">CPF: {{recibo['cliente']['cpf']}}</p>
            <p style="color: var(--text-sub); font-size: 0.9rem; margin-bottom: 5px;">Data: {{recibo['data']}}</p>
            <p style="color: var(--primary); font-weight: 700; margin-bottom: 15px;">Total: R$ {{recibo['total']}}</p>
            
            <form action="/admin/vendas/{{recibo['id']}}" method="GET">
                <button type="submit" class="btn-primary" style="padding: 8px 16px;">Ver Detalhes</button>
            </form>
        </div>
        % end
    </div>
</div>
