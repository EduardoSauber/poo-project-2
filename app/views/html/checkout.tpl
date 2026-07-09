% link_css = '<link rel="stylesheet" type="text/css" href="/static/css/carrinho.css">'
% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra=link_css)

<div class="carrinho-container">
    <h1>Revisão do Pedido</h1>

    <table class="carrinho-table">
        <tr><th>Produto</th><th>Qtd</th><th>Subtotal</th></tr>
        % for item in itens:
        <tr>
            <td>{{ item['produto']['nome'] }}</td>
            <td>{{ item['quantidade'] }}</td>
            <td>R$ {{ "%.2f" % item['subtotal'] }}</td>
        </tr>
        % end
    </table>

    <h3>Total a pagar: R$ {{ "%.2f" % total }}</h3>

    <form method="POST" action="/checkout/confirmar">
        <button type="submit" class="btn-checkout">Confirmar Compra</button>
    </form>
</div>
