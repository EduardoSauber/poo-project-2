% link_css = '<link rel="stylesheet" href="/static/css/admin.css">'
% rebase('app/views/html/base.tpl', titulo_pagina='Gerenciamento de Clientes', css_extra=link_css)

<div class="conteudo">
    <h1>Gerenciamento de Clientes</h1>
    <h2>Lista de Produtos</h2>
    <div class="lista-clientes">
        % for cliente in get('lista_clientes',[]):
        <div class="cliente-card">
            <p><strong>{{cliente['nome']}}</strong></p>
            <img src="/static/img/user-icon.svg" style="width: 100px; height: 100px; object-fit: contain; align-self: center;" alt="" aria-hidden="true">
            <div class="cliente-card-info">CPF: {{cliente['cpf']}}</div>
            <div class="cliente-card-info">E-Mail: {{cliente['email']}}</div>
            <div class="cliente-card-info">Total de Compras: </div>
            <div class="cliente-card-btns">
                <button type="button" class="btn-editar"
                        data-nome="{{cliente['nome']}}"
                        data-cpf="{{cliente['cpf']}}"
                        data-idade="{{cliente['idade']}}"
                        data-email="{{cliente['email']}}"
                        onclick="abrirModalEditarCliente(this)">
                    Editar Cliente
                </button>
                <form action="/admin/clientes/excluir/{{cliente['cpf']}}" method="POST">
                    <button type="submit" class="btn-excluir" onclick="return confirm('Clique novamente para excluir.')">Excluir Cliente</button>
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

            <label for="edit-senha">Nova Senha do Cliente:</label>
            <small>Deixe em branco para manter a atual.</small>
            <input type="password" id="edit-senha" name="senha">
        </div>
        <div class="modal-botoes">
            <button class="btn-modal-salvar" type="submit" onclick="return confirm('Deseja realmente alterar os dados do Cliente?')">Salvar Alterações</button>
            <button class="btn-modal-cancelar" type="button" onclick="document.getElementById('editar-cliente').close()">Cancelar</button>
        </div>
    </form>
</dialog>

<script src="/static/js/admin.js"></script>

% if get('erro'):
<script>alert("Erro:\n{{erro}}")</script>
% end