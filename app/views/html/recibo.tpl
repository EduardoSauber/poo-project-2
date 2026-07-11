% rebase('app/views/html/base.tpl', titulo_pagina=titulo_pagina, logado=logado, usuario_admin=usuario_admin, usuario_nome=usuario_nome, css_extra='')

<div class="glass-card mt-20" style="max-width: 600px; text-align: center;">
    <h1 style="color: var(--success); margin-bottom: 20px;">Compra Realizada com Sucesso!</h1>
    
    <h2>Recibo Oficial</h2>
    <p><strong>ID do Pedido:</strong> {{ recibo['id'] }}</p>
    <p><strong>Data:</strong> {{ recibo['data'] }}</p>
    <p class="mb-20"><strong>Cliente:</strong> {{ recibo['cliente']['nome'] }} (CPF: {{ recibo['cliente']['cpf'] }})</p>

    <div class="table-container mb-20" style="box-shadow: none; border: none;">
        <table class="table-styled">
            <tr><th>Item</th><th>Qtd</th></tr>
            % for item in recibo['itens']:
            <tr>
                <td>{{ item['produto']['nome'] }}</td>
                <td>{{ item['quantidade'] }} un.</td>
            </tr>
            % end
        </table>
    </div>

    <h3 class="mb-20">Valor Pago: R$ {{ "%.2f" % recibo['total'] }}</h3>

    <a href="/vitrine" class="btn-primary">Voltar para a Vitrine</a>
</div>
