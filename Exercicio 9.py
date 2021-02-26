def count_primes(num):
    listPrimo = []
    x = 2
    while num >= x:
        #Checar se o número é primo
        checarPrimo = 0
        for i in range(2, x):
            if num % i == 0:
                checarPrimo = checarPrimo + 1
                print(checarPrimo)
        if checarPrimo == 0:
            listPrimo.append(x)
        x = x + 1

    print(listPrimo)

count_primes(100)