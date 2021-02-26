def up_low(s):
    print(f'Original String : {s}')

    quantidade_minúscula = 0
    quantidadeMaiúscula = 0
    for letra in s:
        if letra.isupper():
            quantidadeMaiúscula = quantidadeMaiúscula + 1
        if letra.islower():
            quantidade_minúscula = quantidade_minúscula + 1

    print(f'No. of Upper case characters : {quantidadeMaiúscula}')
    print(f'No. of Lower case Characters : {quantidade_minúscula}')