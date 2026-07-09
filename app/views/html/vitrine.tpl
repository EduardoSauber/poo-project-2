% link_css = '<link rel="stylesheet" type="text/css" href="static/css/vitrine.css">'
% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra=link_css)

<div class="vitrine">
    % if get('sucesso'):
        <div id="toast-sucesso" style="position: fixed; bottom: 20px; right: 20px; background-color: #28a745; color: white; padding: 15px 20px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); z-index: 1000; opacity: 1; transition: opacity 0.5s ease;">
            {{ sucesso }}
        </div>
        <script>
            setTimeout(function() {
                var toast = document.getElementById('toast-sucesso');
                if(toast) {
                    toast.style.opacity = '0';
                    setTimeout(function() { toast.style.display = 'none'; }, 500);
                }
            }, 2000);
        </script>
    % end
    % if get('erro'):
        <div id="toast-erro" style="position: fixed; bottom: 20px; right: 20px; background-color: #dc3545; color: white; padding: 15px 20px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); z-index: 1000; opacity: 1; transition: opacity 0.5s ease;">
            {{ erro }}
        </div>
        <script>
            setTimeout(function() {
                var toast = document.getElementById('toast-erro');
                if(toast) {
                    toast.style.opacity = '0';
                    setTimeout(function() { toast.style.display = 'none'; }, 500);
                }
            }, 3000);
        </script>
    % end
    % for produto in lista_produtos:
    <div class="card">
        <h3>{{ produto['nome'] }}</h3>
        <p class="preco">R$ {{ "%.2f" % produto['preco'] }}</p>
        <p class="estoque">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
            Estoque: {{ produto['qtd_estoque'] }} un.
        </p>
        <form method="POST" action="/carrinho/adicionar">
            <input type="hidden" name="produto_nome" value="{{ produto['nome'] }}">
            <div class="quantidade-wrapper">
                <label>Quantidade</label>
                <input type="number" name="quantidade" value="1" min="1" max="{{ produto['qtd_estoque'] }}">
            </div>
            <button type="submit">Adicionar ao Carrinho</button>
        </form>
    </div>
    % end
</div>
