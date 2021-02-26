def display(lin1 = [1,2,3], lin2 = [4,5,6], lin3 = [7,8,9]):

    if lin1[]
    print()
    print(lin1)
    print(lin2)
    print(lin3)

    return lin1, lin2, lin3

def jogadaX(lin1, lin2, lin3):
    # recebe o display
    display(lin1, lin2, lin3)

    # jogador fala onde ele vai jogar e código verifica se o numero é jogável(preciso fazer)
    jogadaPlayer = int(input("Aonde você quer jogar? (X) "))

    # substitui o número da jogadaPlayer pelo x
    if jogadaPlayer in lin1:
        lin1[jogadaPlayer - 1] = "x"
    if jogadaPlayer in lin2:
        lin2[jogadaPlayer - 4] = "x"
    if jogadaPlayer in lin3:
        lin3[jogadaPlayer - 7] = "x"

    # chama a jogada do proximo jogador
    jogadaO(lin1, lin2, lin3)



def jogadaO(lin1, lin2, lin3):
    # recebe o display
    display(lin1, lin2, lin3)

    # jogador fala onde ele vai jogar e código verifica se o numero é jogável(preciso fazer)
    jogadaPlayer = int(input("Aonde você quer jogar? (O) "))

    # substitui o número da jogadaPlayer pelo o
    if jogadaPlayer in lin1:
        lin1[jogadaPlayer - 1] = "o"
    if jogadaPlayer in lin2:
        lin2[jogadaPlayer - 4] = "o"
    if jogadaPlayer in lin3:
        lin3[jogadaPlayer - 7] = "o"

    # chama a jogada do proximo jogador
    jogadaX(lin1, lin2, lin3)


print("Bem Vindo ao Jogo da Velha!!")
jogadaX(lin1 = [1,2,3], lin2 = [4,5,6], lin3 = [7,8,9])