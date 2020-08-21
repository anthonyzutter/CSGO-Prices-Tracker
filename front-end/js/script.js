$(function () {

function listar_itens() {
    $.ajax({
        url: 'http://localhost:5000/listar_itens',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function () {
            alert("Erro ao ler dados, verifique o backend");
        }
    });

    function listar(itens) {
        $('#corpoTabelaEsportes').empty();
        console.log(itens);
        for (var i in itens) {
            lin = '<tr>' +
                //'<td>' + itens[i].id + '</td>' +
                '<td>' + itens[i].nome + '</td>' +
                '<td>' + itens[i].preco + '</td>' +
                '<td>' + itens[i].exterior + '</td>' +
                '<td>' + itens[i].quantidade + '</td>' +
                '</tr>';
            $('#corpoTabelaItens').append(lin);
        }   
        }
    };
    listar_itens();

});