% link_css = '<link rel="stylesheet" type="text/css" href="static/css/vitrine.css">'
% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra=link_css)
<script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>

<div class="grid-cards w-100" style="padding: 40px 0; max-width: 1400px; margin: 0 auto;">
    % if get('sucesso'):
        <div id="toast-sucesso" class="toast sucesso">{{ sucesso }}</div>
        <script>
            setTimeout(function() {
                var toast = document.getElementById('toast-sucesso');
                if(toast) {
                    toast.style.opacity = '0';
                    setTimeout(function() { toast.style.display = 'none'; }, 500);
                }
            }, 3000);
        </script>
    % end
    % if get('erro'):
        <div id="toast-erro" class="toast erro">{{ erro }}</div>
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
    <div class="glass-card" style="display: flex; flex-direction: column; padding: 24px;">
        <h3 style="font-size: 1.4rem; font-weight: 600; color: var(--text-main); margin-bottom: 8px;">{{ produto['nome'] }}</h3>
        <p style="font-size: 1.8rem; font-weight: 700; color: var(--primary); margin: 0;">R$ {{ "%.2f" % produto['preco'] }}</p>
        <p style="font-size: 0.9rem; color: var(--text-sub); margin: 0; font-weight: 400; display: flex; align-items: center; gap: 6px;">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
            Estoque: {{ produto['qtd_estoque'] }} un.
        </p>
        <form method="POST" action="/carrinho/adicionar" style="display: flex; flex-direction: column; gap: 16px; margin-top: auto; padding-top: 20px; border-top: 1px solid var(--border);">
            <input type="hidden" name="produto_nome" value="{{ produto['nome'] }}">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <label style="font-size: 0.95rem; color: var(--text-sub); font-weight: 600;">Quantidade</label>
                <input type="number" name="quantidade" value="1" min="1" max="{{ produto['qtd_estoque'] }}" style="width: 80px; text-align: center; border: 2px solid var(--border); border-radius: 8px; padding: 10px 12px; font-family: 'Outfit';">
            </div>
            <button type="submit" class="btn-primary">Adicionar ao Carrinho</button>
        </form>
    </div>
    % end
</div>

<script>
    const socket = io();
    socket.on('atualizar_vitrine',function(dados) {
        // console.log("Sinal recebido do servidor:", dados.mensagem);
        location.reload();
    });
</script>