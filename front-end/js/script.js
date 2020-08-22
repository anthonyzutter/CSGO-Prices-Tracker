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
        $('#corpoTabelaItens').empty();
        console.log(itens);
        for (var i in itens) {
            lin = '<tr>' +
                //'<td>' + itens[i].id + '</td>' +
                '<td><a href="' + itens[i].url + '">' + itens[i].nome + '</a></td>' +
                '<td>R$ ' + itens[i].preco + '</td>' +
                '<td>R$ ' + itens[i].preco_atual + '</td>' +
                '<td>' + itens[i].data + '</td>' +
                '</tr>';
            $('#corpoTabelaItens').append(lin);
        }   
        }
    };
    listar_itens();

});