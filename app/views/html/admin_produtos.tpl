% link_css = '<link rel="stylesheet" href="/static/css/admin.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Gerenciamento de Produtos', css_extra=link_css)

<div class="conteudo">
    <h1>Gerenciamento de Produtos</h1>
    <div class="dashboard">
        <button class="dash-btn" onclick="document.getElementById('criar-produto').showModal()">
            <span class="dash-btn-titulo">Adicionar Produto</span>
            <img src="/static/img/box-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
        </button>

        <button class="dash-btn" onclick="location.href='/admin/produtos/editar'">
            <span class="dash-btn-titulo">Editar Produto</span>
            <img src="/static/img/login-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
        </button>

        <button class="dash-btn" onclick="location.href='/admin/produtos/excluir'">
            <span class="dash-btn-titulo">Remover Produto</span>
            <img src="/static/img/cart-icon.svg" style="width: 100px; height: 100px; object-fit: contain;" alt="" aria-hidden="true"></img>
        </button>
    </div>
    <h2>Lista de Produtos</h2>
    <div class="lista-produtos">
        % for produto in get('lista_produtos',[]):
        <div class="produto-card">
            <p><strong>{{produto['nome']}}</strong></p>
            <img src="/static/img/box-icon.svg" style="width: 100px; height: 100px; object-fit: contain; align-self: center;" alt="" aria-hidden="true">
            <div class="produto-card-info">R$ {{produto['preco']}} </div>
            <button class="btn-editar">Editar Produto</button>
            <form action="/admin/produtos/excluir/{{produto['nome']}}" method="POST">
                <button type="submit" class="btn-excluir" onclick="return confirm('Clique novamente para excluir.')">Excluir Produto</button>
            </form>
        </div>
        % end
    </div>
</div>

<dialog id="criar-produto" class="modal">
    <h2>Cadastrar Produto</h2>
    <form action="/admin/produtos/criar" method="POST">
        <div class="modal-entradas">
            <label for="nome">Nome do Produto:</label>
            <input type="text" id="nome" name="nome" required>

            <label for="preco">Preço do Produto:</label>
            <input type="text" inputmode="decimal" id="preco" name="preco" step="0.01" min="0" required
                   oninput="this.value = this.value.replace(/,/g, '.').replace(/[^0-9.]/g, '');"
                   onblur="if(this.value && !isNaN(this.value)) this.value = parseFloat(this.value).toFixed(2); else this.value = '';">

            <label for="quantidade">Quantidade do Produto:</label>
            <input type="text" inputmode="numeric" id="quantidade" name="quantidade" step="1" min="0" required
                   oninput="this.value = this.value.replace(/[^0-9]/g, '');"
                   onblur="if(this.value && !isNaN(this.value)) this.value = parseInt(this.value, 10); else this.value = '';">
        </div>
        <div class="modal-botoes">
            <button class="btn-modal-salvar" type="submit">Salvar</button>
            <button class="btn-modal-cancelar" type="button" onclick="document.getElementById('criar-produto').close()">Cancelar</button>
        </div>
    </form>
</dialog>