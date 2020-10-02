$(function() { 
    
    function exibir_itens() {
        $.ajax({
            url: 'http://localhost:5000/listar_itens',
            method: 'GET',
            dataType: 'json',
            success: listar,
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar (itens) {
            $('#corpoTabelaItens').empty();
            mostrar_conteudo("tabelaItens");      
            for (var i in itens) { 
                lin = '<tr>' + 
                '<td><a href="' + itens[i].url + '">' + itens[i].nome + '</a></td>' +
                '<td>R$ ' + itens[i].preco + '</td>' +
                '<td>R$ ' + itens[i].preco_atual + '</td>' +
                '<td>' + itens[i].data + '</td>' +
                '</tr>';
                $('#corpoTabelaItens').append(lin);
            }
        }
    }

    function mostrar_conteudo(identificador) {
        $("#tabelaItens").addClass('invisible');
        $("#conteudoInicial").addClass('invisible');
        $("#"+identificador).removeClass('invisible');      
    }

    $(document).on("click", "#linkListarItens", function() {
        exibir_itens();
    });
    
    $(document).on("click", "#linkInicio", function() {
        mostrar_conteudo("conteudoInicial");
    });

    $(document).on("click", "#btIncluirItem", function() {
        nome = $("#campoNome").val();
        preco = $("#campoPreço").val();
        var dados = JSON.stringify({ nome: nome, preco: preco });
        $.ajax({
            url: 'http://localhost:5000/incluir_item',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json', 
            data: dados, 
            success: itemIncluido, 
            error: erroAoIncluir
        });
        function itemIncluido (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Item incluido com sucesso!");
                $("#campoNome").val("");
                $("#campoPreço").val("");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

    $('#modalIncluirItem').on('hide.bs.modal', function (e) {
        if (! $("#tabelaItens").hasClass('invisible')) {
            exibir_itens();
        }
    });

    mostrar_conteudo("conteudoInicial");
});