function abrirModalEditar(botao) {
        let nomeProduto = botao.getAttribute('data-nome');
        let precoProduto = botao.getAttribute('data-preco');
        let qtdProduto = botao.getAttribute('data-quantidade');

        document.getElementById('edit-nome-original').value = nomeProduto;
        document.getElementById('edit-nome').value = nomeProduto;
        document.getElementById('edit-preco').value = parseFloat(precoProduto).toFixed(2);
        document.getElementById('edit-quantidade').value = qtdProduto;

        document.getElementById('editar-produto').showModal();
}

function abrirModalEditarCliente(botao) {
        let nomeCliente = botao.getAttribute('data-nome');
        let cpfCliente = botao.getAttribute('data-cpf');
        let idadeCliente = botao.getAttribute('data-idade');
        let emailCliente = botao.getAttribute('data-email');

        document.getElementById('edit-cpf-original').value = cpfCliente;
        document.getElementById('edit-nome').value = nomeCliente;
        document.getElementById('edit-cpf').value = cpfCliente;
        document.getElementById('edit-idade').value = idadeCliente;
        document.getElementById('edit-email').value = emailCliente;

        document.getElementById('editar-cliente').showModal();
}