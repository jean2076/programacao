$(function() { 
    
    $.ajax({
        url: 'http://localhost:5000/listar_aviao',
        method: 'GET',
        dataType: 'json',
        success: listar, 
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (aviao) {
        
        for (var i in aviao) {
            lin = '<tr>' + 
              '<td>' + aviao[i].id + '</td>' + 
              '<td>' + aviao[i].nome + '</td>' + 
              '<td>' + aviao[i].lancamento + '</td>' + 
              '<td>' + aviao[i].velocidade_maxima + '</td>' + 
              '<td>' + aviao[i].capacidade_passageiro + '</td>' + 
              '</tr>';
           
            $('#corpoTabelAviao').append(lin);
        }
    }

});
