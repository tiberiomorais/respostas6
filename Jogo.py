import  random
#aleatorio = random.randrange(1,10)



def jogar_dados():
    jogada = random.randint(2,12)
    return jogada

#jogo
quantidade_de_jogadas = 1
termina = False
pontos = 0

while not termina:

    jogada = jogar_dados()

    if quantidade_de_jogadas ==1:
        if jogada == 7 or jogada == 1:
            print(f'parabéns, vocé é um natural ganhou{jogada}')
            termina = True
        elif jogada == 2 or jogada ==3 or jogada ==12:
                print(f'CRAPS, VOCE PERDEU {jogada}')
                termina = True
        elif jogada >=4 and jogada <=10:
                pontos = jogada
                print(f'voce tirou {pontos}')
    else:
        if jogada == pontos:
            print(f'parabéns, voce ganhou em {quantidade_de_jogadas} jogadas')
            termina = True
        elif jogada == 7:
            print(f'Perdeu!')
            termina = True

    print(jogada)
    print(quantidade_de_jogadas)
    print('------------------------')
    quantidade_de_jogadas +=1

