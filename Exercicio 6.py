def blackjack(a,b,c):
    soma = a + b + c
    if soma <= 21:
        return soma

    elif soma > 21 and a == 11 or b == 11 or c == 11:
        return soma - 10

    elif soma > 21:
        return "BUST"

