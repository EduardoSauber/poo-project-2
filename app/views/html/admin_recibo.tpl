% link_css = '<link rel="stylesheet" type="text/css" href="/static/css/carrinho.css">'
% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra=link_css)

<div class="carrinho-container">
    <div class="recibo-card">
        <h2>Recibo Oficial</h2>
        <p><strong>ID do Pedido:</strong> {{ recibo['id'] }}</p>
        <p><strong>Data:</strong> {{ recibo['data'] }}</p>
        <p><strong>Cliente:</strong> {{ recibo['cliente']['nome'] }} (CPF: {{ recibo['cliente']['cpf'] }})</p>

        <table class="carrinho-table">
            <tr><th>Item</th><th>Qtd</th></tr>
            % for item in recibo['itens']:
            <tr>
                <td>{{ item['produto']['nome'] }}</td>
                <td>{{ item['quantidade'] }} un.</td>
            </tr>
            % end
        </table>

        <h3>Valor Pago: R$ {{ "%.2f" % recibo['total'] }}</h3>
    </div>

    <a href="/admin/vendas" class="btn-checkout">Voltar para Vendas</a>
</div>
