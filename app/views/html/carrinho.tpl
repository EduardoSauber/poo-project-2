% link_css = '<link rel="stylesheet" type="text/css" href="/static/css/carrinho.css">'
% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra=link_css)

<div class="carrinho-container">
    <h1>Meu Carrinho</h1>

    % if not itens:
        <p>Seu carrinho está vazio. <a href="/vitrine">Continuar comprando</a></p>
    % else:
        <table class="carrinho-table">
            <tr><th>Produto</th><th>Preço Un.</th><th>Qtd</th><th>Subtotal</th><th>Ações</th></tr>
            % for item in itens:
            <tr>
                <td>{{ item['produto']['nome'] }}</td>
                <td>R$ {{ "%.2f" % item['produto']['preco'] }}</td>
                <td>{{ item['quantidade'] }}</td>
                <td>R$ {{ "%.2f" % item['subtotal'] }}</td>
                <td>
                    <form method="POST" action="/carrinho/remover" class="acoes-form">
                        <input type="hidden" name="produto_nome" value="{{ item['produto']['nome'] }}">
                        <input type="number" name="quantidade" value="1" min="1" max="{{ item['quantidade'] }}" style="width: 50px;">
                        <button type="submit" class="btn-remove qtd">Remover Qtd</button>
                    </form>
                    <form method="POST" action="/carrinho/remover" class="acoes-form">
                        <input type="hidden" name="produto_nome" value="{{ item['produto']['nome'] }}">
                        <button type="submit" class="btn-remove">Remover Tudo</button>
                    </form>
                </td>
            </tr>
            % end
        </table>
        <h3>Total: R$ {{ "%.2f" % total }}</h3>
        <a href="/checkout" class="btn-checkout">Prosseguir para o Checkout</a>
    % end
</div>

