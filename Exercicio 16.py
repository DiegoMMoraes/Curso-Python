def ispangram(str1):
    list1 = []
    for letra in str1.lower():
        list1.append(letra)
    list1 = list(set(list1))
    list1.sort()
    list1.remove(' ')
    quantidadeLetras = 0
    for item in list1:
        quantidadeLetras = quantidadeLetras + 1
    return quantidadeLetras == 26







ispangram("The quick brown fox jumps over the lazy og")