% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra='')
<script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>

<div class="w-100" style="max-width: 1000px; margin: 0 auto;">
    <h2 class="mb-20">Meu Carrinho</h2>

    % if not itens:
        <div class="glass-card text-center">
            <p class="mb-20">Seu carrinho está vazio.</p>
            <a href="/vitrine" class="btn-primary">Continuar comprando</a>
        </div>
    % else:
        <div class="table-container mb-20">
            <table class="table-styled">
                <tr><th>Produto</th><th>Preço Un.</th><th>Qtd</th><th>Subtotal</th><th>Ações</th></tr>
                % for item in itens:
                <tr>
                    <td>{{ item['produto']['nome'] }}</td>
                    <td>R$ {{ "%.2f" % item['produto']['preco'] }}</td>
                    <td>{{ item['quantidade'] }}</td>
                    <td>R$ {{ "%.2f" % item['subtotal'] }}</td>
                    <td>
                        <div class="table-actions">
                            <form method="POST" action="/carrinho/remover" style="display: flex; gap: 8px;">
                                <input type="hidden" name="produto_nome" value="{{ item['produto']['nome'] }}">
                                <input type="number" name="quantidade" value="1" min="1" max="{{ item['quantidade'] }}" style="width: 70px; padding: 4px;">
                                <button type="submit" class="btn-warning">Remover Qtd</button>
                            </form>
                            <form method="POST" action="/carrinho/remover">
                                <input type="hidden" name="produto_nome" value="{{ item['produto']['nome'] }}">
                                <button type="submit" class="btn-danger">Tudo</button>
                            </form>
                        </div>
                    </td>
                </tr>
                % end
            </table>
        </div>
        <div class="glass-card text-center" style="max-width: 400px; margin-left: auto; margin-right: 0;">
            <h3 class="mb-20">Total: R$ {{ "%.2f" % total }}</h3>
            <a href="/checkout" class="btn-primary">Prosseguir para o Checkout</a>
        </div>
    % end
</div>

<script>
    const socket = io();
    socket.on('atualizar_vitrine',function(dados) {
        alert(dados.mensagem);
        location.reload();
    });
</script>