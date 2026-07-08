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