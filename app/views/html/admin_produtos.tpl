% link_css = '<link rel="stylesheet" href="/static/css/admin.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Gerenciamento de Produtos', css_extra=link_css)

<div class="w-100" style="max-width: 1200px; margin: 0 auto;">
    <h1 class="text-center mb-20">Gerenciamento de Produtos</h1>
    
    <div class="flex-center mb-20">
        <button class="btn-primary" onclick="document.getElementById('criar-produto').showModal()" style="max-width: 300px;">
            + Adicionar Produto
        </button>
    </div>

    <div class="grid-cards">
        % for produto in get('lista_produtos',[]):
        <div class="glass-card text-center" style="padding: 20px;">
            <p style="font-size: 1.2rem; margin-bottom: 15px;"><strong>{{produto['nome']}}</strong></p>
            <img src="/static/img/box-icon.svg" style="width: 80px; height: 80px; object-fit: contain; margin-bottom: 15px;" alt="" aria-hidden="true">
            <p class="mb-20" style="color: var(--text-sub);">Estoque: {{produto['qtd_estoque']}} un. <br> R$ {{ "%.2f" % produto['preco'] }}</p>
            
            <div style="display: flex; gap: 10px; justify-content: center;">
                <button type="button" class="btn-warning"
                        data-nome="{{produto['nome']}}"
                        data-preco="{{produto['preco']}}"
                        data-quantidade="{{produto['qtd_estoque']}}"
                        onclick="abrirModalEditar(this)">
                    Editar
                </button>
                <form action="/admin/produtos/excluir/{{produto['nome']}}" method="POST">
                    <button type="submit" class="btn-danger" onclick="return confirm('Tem certeza que deseja excluir?')">Excluir</button>
                </form>
            </div>
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

            <label for="preco">Preço (R$):</label>
            <input type="text" inputmode="decimal" id="preco" name="preco" step="0.01" min="0" required
                   oninput="this.value = this.value.replace(/,/g, '.').replace(/[^0-9.]/g, '');"
                   onblur="if(this.value && !isNaN(this.value)) this.value = parseFloat(this.value).toFixed(2); else this.value = '';">

            <label for="quantidade">Quantidade:</label>
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

<dialog id="editar-produto" class="modal">
    <h2>Editar Produto</h2>
    <form action="/admin/produtos/editar" method="POST">
        <div class="modal-entradas">
            <input type="hidden" id="edit-nome-original" name="nome_original">

            <label for="edit-nome">Nome do Produto:</label>
            <input type="text" id="edit-nome" name="nome" required>

            <label for="edit-preco">Preço (R$):</label>
            <input type="text" inputmode="decimal" id="edit-preco" name="preco" step="0.01" min="0" required
                   oninput="this.value = this.value.replace(/,/g, '.').replace(/[^0-9.]/g, '');"
                   onblur="if(this.value && !isNaN(this.value)) this.value = parseFloat(this.value).toFixed(2); else this.value = '';">

            <label for="edit-quantidade">Quantidade:</label>
            <input type="text" inputmode="numeric" id="edit-quantidade" name="quantidade" step="1" min="0" required
                   oninput="this.value = this.value.replace(/[^0-9]/g, '');"
                   onblur="if(this.value && !isNaN(this.value)) this.value = parseInt(this.value, 10); else this.value = '';">
        </div>
        <div class="modal-botoes">
            <button class="btn-modal-salvar" type="submit">Salvar</button>
            <button class="btn-modal-cancelar" type="button" onclick="document.getElementById('editar-produto').close()">Cancelar</button>
        </div>
    </form>
</dialog>

<script src="/static/js/admin.js"></script>

% if get('erro'):
<div id="toast-erro" class="toast erro">{{erro}}</div>
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