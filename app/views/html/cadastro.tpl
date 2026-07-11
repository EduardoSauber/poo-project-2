% rebase('app/views/html/base.tpl', titulo_pagina='Cadastro', logado=False, usuario_admin=False, usuario_nome='', css_extra='')

<div class="glass-card mt-20">
    <h2>Criar Conta</h2>
    <form method="POST" action="/cadastro">
        % if get('erro', None):
            <div id="toast-erro" class="toast erro">{{ get('erro', '') }}</div>
            <script>
                setTimeout(function() {
                    var toast = document.getElementById('toast-erro');
                    if(toast) {
                        toast.style.opacity = '0';
                        setTimeout(function() { toast.style.display = 'none'; }, 500);
                    }
                }, 3000);
            </script>
        %end

        <div class="form-group">
            <label for="nome">Nome</label>
            <input type="text" id="nome" name="nome" required>
        </div>

        <div class="form-group">
            <label for="cpf">CPF</label>
            <input type="text" id="cpf" name="cpf" maxlength="11" placeholder="Somente números" required>
        </div>

        <div class="form-group">
            <label for="email">E-mail</label>
            <input type="email" id="email" name="email" required>
        </div>

        <div class="form-group">
            <label for="idade">Idade</label>
            <input type="number" id="idade" name="idade" min="1" required>
        </div>

        <div class="form-group">
            <label for="senha">Senha</label>
            <input type="password" id="senha" name="senha" required>
        </div>

        <button type="submit" class="btn-primary mb-20">Cadastrar</button>
        <div class="text-center">
            <a href="/login" style="color: var(--primary); text-decoration: none; font-weight: 600;">Já tem conta? Faça login</a>
        </div>
    </form>
</div>
