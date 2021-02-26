def summer_69(arr):
    if 6 in arr and 9 in arr:
        block = False
        soma = 0
        for num in arr:
            if num == 6:
                block = True
            if block and num == 9:
                block = False
            if block == False and num != 6 and num != 9:
                soma = soma + num
        return soma

    else:
        return sum(arr)


