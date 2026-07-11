% # Bottle
% rebase('app/views/html/base.tpl', titulo_pagina='Loja', css_extra='')

<div class="w-100" style="max-width: 1400px; margin: 0 auto;">
    <h1 class="text-center mb-20">Mercadinho</h1>

    <div class="grid-cards">
        % for produto in get('lista_produtos',[]):
        <div class="glass-card text-center" style="padding: 24px;">
            <h3 style="font-size: 1.4rem; font-weight: 600; color: var(--text-main); margin-bottom: 8px;">{{produto['nome']}}</h3>
            <img src="/static/img/box-icon.svg" style="width: 80px; height: 80px; object-fit: contain; margin-bottom: 15px;" alt="" aria-hidden="true"></img>
            <p style="font-size: 1.8rem; font-weight: 700; color: var(--primary); margin: 0;">R$ {{produto['preco']}} </p>
            <button class="btn-primary mt-20" onclick="location.href='/vitrine'">Ir para Vitrine</button>
        </div>
        % end
    </div>
</div>
