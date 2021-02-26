def old_macdonald(name):
    quantidadeExecutadas = 1
    palavra = ""
    for letra in name:
        if quantidadeExecutadas == 1 or quantidadeExecutadas == 4:
            palavra = palavra + letra.upper()
        else:
            palavra = palavra + letra
        quantidadeExecutadas = quantidadeExecutadas  + 1
    return palavra


old_macdonald('macdonald')
