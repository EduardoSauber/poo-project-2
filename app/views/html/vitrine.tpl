% link_css = '<link rel="stylesheet" type="text/css" href="static/css/vitrine.css">'
% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra=link_css)

<div class="vitrine">
    % for produto in lista_produtos:
    <div class="card">
        <h3>{{ produto['nome'] }}</h3>
        <p>R$ {{ "%.2f" % produto['preco'] }}</p>
        <p>Estoque: {{ produto['qtd_estoque'] }}</p>
        <form method="POST" action="/carrinho/adicionar">
            <input type="hidden" name="produto_id" value="{{ produto['id'] }}">
            <input type="number" name="quantidade" value="1" min="1" max="{{ produto['qtd_estoque'] }}">
            <button type="submit">Adicionar ao Carrinho</button>
        </form>
    </div>
    % end
</div>
