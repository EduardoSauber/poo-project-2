% rebase('app/views/html/base.tpl', titulo_pagina='Login', logado=False, usuario_admin=False, usuario_nome='', css_extra='')

<div class="glass-card mt-20">
    <h2>Entrar</h2>
    <form method="POST" action="/login">
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
        % if get('sucesso', None):
            <div id="toast-sucesso" class="toast sucesso">Cadastro realizado! Faça login.</div>
            <script>
                setTimeout(function() {
                    var toast = document.getElementById('toast-sucesso');
                    if(toast) {
                        toast.style.opacity = '0';
                        setTimeout(function() { toast.style.display = 'none'; }, 500);
                    }
                }, 3000);
            </script>
        %end

        <div class="form-group">
            <label for="cpf">CPF</label>
            <input type="text" id="cpf" name="cpf" required>
        </div>
        
        <div class="form-group">
            <label for="senha">Senha</label>
            <input type="password" id="senha" name="senha" required>
        </div>
        
        <button type="submit" class="btn-primary mb-20">Login</button>
        <div class="text-center">
            <a href="/cadastro" style="color: var(--primary); text-decoration: none; font-weight: 600;">Não tem conta? Cadastre-se</a>
        </div>
    </form>
</div>
