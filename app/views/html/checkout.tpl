% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra='')
<script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>

<div class="glass-card mt-20" style="max-width: 800px;">
    <h2>Revisão do Pedido</h2>

    <div class="table-container mb-20" style="box-shadow: none; border: none;">
        <table class="table-styled">
            <tr><th>Produto</th><th>Qtd</th><th>Subtotal</th></tr>
            % for item in itens:
            <tr>
                <td>{{ item['produto']['nome'] }}</td>
                <td>{{ item['quantidade'] }}</td>
                <td>R$ {{ "%.2f" % item['subtotal'] }}</td>
            </tr>
            % end
        </table>
    </div>

    <h3 class="mb-20">Total a pagar: R$ {{ "%.2f" % total }}</h3>

    <form method="POST" action="/checkout/confirmar">
        <button type="submit" class="btn-primary">Confirmar Compra</button>
    </form>
</div>

<script>
    const socket = io();
    socket.on('atualizar_vitrine',function(dados) {
        alert(dados.mensagem);
        location.reload();
    });
</script>