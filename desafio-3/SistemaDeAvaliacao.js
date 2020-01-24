function avaliacao(x){
    //separa x no valor inteiro e no decimal dele
    var inteiro = parseInt(x);
    var decimal = x - inteiro;
    var resp = [];
    for(i=0; i < 5; i++){
        //preenche inteiro vezes com Star
        if(i<inteiro){
            resp.push("star");
            continue;
        }
        //após preencher com todos stars, ele testa o caso do Star_half
        if(i==inteiro&&decimal>=0.5){
            resp.push("star_half");
            continue;
        }
        //como os outros casos tem continue, ele só fará essa partes depois de preencher com todos stars e star_halfs.
        resp.push("star_border");
    }
    return resp;
}

//console.log(avaliacao(3.2))

/*
avaliacao(0) = ["star_border", "star_border", "star_border", "star_border", "star_border"]
avaliacao(5) = ["star", "star", "star", "star", "star"]
avaliacao(3.7) = ["star", "star", "star", "star_half", "star_border"]
avaliacao(3.2) = ["star", "star", "star", "star_border", "star_border"]
*/