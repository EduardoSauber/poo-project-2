% link_css = '<link rel="stylesheet" href="/static/css/admin.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Gerenciamento de Clientes', css_extra=link_css)

<div class="w-100" style="max-width: 1200px; margin: 0 auto;">
    <h1 class="text-center mb-20">Gerenciamento de Clientes</h1>

    <div class="grid-cards">
        % for cliente in get('lista_clientes',[]):
        <div class="glass-card text-center" style="padding: 20px;">
            <p style="font-size: 1.2rem; margin-bottom: 10px;"><strong>{{cliente['nome']}}</strong></p>
            <img src="/static/img/user-icon.svg" style="width: 80px; height: 80px; object-fit: contain; margin-bottom: 15px;" alt="" aria-hidden="true">
            <p style="color: var(--text-sub); font-size: 0.9rem; margin-bottom: 5px;">CPF: {{cliente['cpf']}}</p>
            <p style="color: var(--text-sub); font-size: 0.9rem; margin-bottom: 5px;">{{cliente['email']}}</p>
            <p style="color: var(--text-sub); font-size: 0.9rem; margin-bottom: 15px;">Compras: {{cliente['compras']}}</p>
            
            <div style="display: flex; gap: 10px; justify-content: center;">
                <button type="button" class="btn-warning"
                        data-nome="{{cliente['nome']}}"
                        data-cpf="{{cliente['cpf']}}"
                        data-idade="{{cliente['idade']}}"
                        data-email="{{cliente['email']}}"
                        onclick="abrirModalEditarCliente(this)">
                    Editar
                </button>
                <form action="/admin/clientes/excluir/{{cliente['cpf']}}" method="POST">
                    <button type="submit" class="btn-danger" onclick="return confirm('Tem certeza que deseja excluir?')">Excluir</button>
                </form>
            </div>
        </div>
        % end
    </div>
</div>

<dialog id="editar-cliente" class="modal">
    <h2>Editar Cliente</h2>
    <form action="/admin/clientes/editar" method="POST">
        <div class="modal-entradas">
            <input type="hidden" id="edit-cpf-original" name="cpf_original">

            <label for="edit-nome">Nome do Cliente:</label>
            <input type="text" id="edit-nome" name="nome" required>

            <label for="edit-cpf">CPF do Cliente:</label>
            <input type="text" id="edit-cpf" name="cpf" maxlength="11" placeholder="Somente números" required>

            <label for="edit-idade">Idade do Cliente:</label>
            <input type="number" min="1" step="1" id="edit-idade" name="idade" required>

            <label for="edit-email">E-Mail do Cliente:</label>
            <input type="text" id="edit-email" name="email" required>

            <label for="edit-senha">Nova Senha:</label>
            <input type="password" id="edit-senha" name="senha" placeholder="Deixe em branco para manter a atual">
        </div>
        <div class="modal-botoes">
            <button class="btn-modal-salvar" type="submit" onclick="return confirm('Deseja realmente alterar os dados do Cliente?')">Salvar</button>
            <button class="btn-modal-cancelar" type="button" onclick="document.getElementById('editar-cliente').close()">Cancelar</button>
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