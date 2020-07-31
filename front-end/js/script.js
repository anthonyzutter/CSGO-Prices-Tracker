$(function () {

    $.ajax({
        url: 'http://localhost:5000/listar_itens',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(itens) {
        for (var i in comidas) {
            lin = '<tr>' +
                '<td>' + itens[i].id + '</td>' +
                '<td>' + itens[i].nome + '</td>' +
                '<td>' + itens[i].preço + '</td>' +
                '<td>' + itens[i].exterior + '</td>' +
                '<td>' + itens[i].quantidade + '</td>' +
                '</tr>';
            $('#corpoTabelaItem').append(lin);
        }
    }

});