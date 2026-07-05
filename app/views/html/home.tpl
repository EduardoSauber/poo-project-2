% # Bottle
% link_css = '<link rel="stylesheet" type="text/css" href="static/css/home.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Loja', css_extra=link_css)

<div class="conteudo">
    <h1>Mercadinho</h1>

    <div class="lista-produtos">

        % for produto in get('lista_produtos',[]):
        <div class="produto-card" style="flex-direction: column;"
            <p><strong>{{produto['nome']}}</strong></p>
            <img src="static/img/box-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
            <p>R$ {{produto['preco']}} </p>
            <button class="btn-comprar">Adicionar ao Carrinho</button>
        </div>
        % end

    </div>
</div>
