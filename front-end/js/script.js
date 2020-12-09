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
                lin = '<tr id="linha_'+itens[i].id+'">' +
                '<td><a href="' + itens[i].url + '">' + itens[i].nome + '</a></td>' +
                '<td>R$ ' + itens[i].preco + '</td>' +
                '<td>R$ ' + itens[i].preco_atual + '</td>' +
                '<td>' + itens[i].data + '</td>' +
                '<td><a href=# id="excluir_' + itens[i].id + '" ' + 
                  'class="excluir_item"><img src="img/excluir.png" '+
                  'alt="Excluir item" title="Excluir item" width=40px></a>' + 
                '</td>' +
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

    $(document).on("click", ".excluir_item", function() {
        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_";
        var id_item = componente_clicado.substring(nome_icone.length);
        $.ajax({
            url: 'http://localhost:5000/excluir_item/'+id_item,
            type: 'DELETE',
            dataType: 'json',
            success: itemExcluido,
            error: erroAoExcluir
        });
        function itemExcluido (retorno) {
            if (retorno.resultado == "ok") {
                $("#linha_" + id_item).fadeOut(1000, function(){
                    alert("Item removido com sucesso!");
                });
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoExcluir (retorno) {
            alert("erro ao excluir dados, verifique o backend: ");
        }
    });

    function listar (ranking) {
        $('#corpoTabelaRanking').empty();
        mostrar_conteudo("cadastroRanking");      
        for (var i in ranking) { 
            lin = '<tr id="linha_ranking_'+ranking[i].id+'">' + 
            '<td>' + ranking[i].nota + '</td>' + 
            '<td>' + ranking[i].autor + '</td>' + 
            '<td>' + ranking[i].item.nome + '</td>' + 
            '<td>' + ranking[i].item.preco + '</td>' + 
            '<td>' + ranking[i].item.preco_atual + '</td>' + 
            '<td>' + ranking[i].comida.data + '</td>' + 
            '<td><a href=# id="excluir_ranking_' + ranking[i].id + '" ' + 
                'class="excluir_ranking"><img src="img/excluir.png" '+
                'alt="Excluir ranking" title="Excluir ranking"  width=40px></a>' + 
            '</td>' + 
            '</tr>';
            $('#corpoTabelaRanking').append(lin);
        }
    }

    $(document).on("click", "#linkListarRanking", function() {
        exibir_ranking();
    });

    function exibir_jogo() {
        $.ajax({
            url: 'http://localhost:5000/listar_jogo',
            method: 'GET',
            dataType: 'json', 
            success: listar, 
            error: function(problema) {
                alert("erro ao ler dados, verifique o backend: ");
            }
        });

        function listar (jogo) {
            $('#corpoTabelaJogo').empty();
            mostrar_conteudo("cadastroJogo");      
            for (var i in jogo) { 
                lin = '<tr id="linha_jogo_'+jogo[i].id+'">' + 
                '<td>' + jogo[i].nome + '</td>' + 
                '<td>' + jogo[i].item.nome + '</td>' + 
                '<td>' + jogo[i].item.preco + '</td>' + 
                '<td>' + jogo[i].item.preco_atual + '</td>' + 
                '<td>' + jogo[i].item.data + '</td>' + 
                '<td><a href=# id="excluir_jogo_' + jogo[i].id + '" ' + 
                    'class="excluir_jogo"><img src="img/excluir.png" '+
                    'alt="Excluir jogo" title="Excluir jogo"  width=40px></a>' + 
                '</td>' + 
                '</tr>';
                $('#corpoTabelaJogo').append(lin);
            }
        }
    }

    $(document).on("click", "#linkListarJogo", function() {
        exibir_jogo();    
    });
});