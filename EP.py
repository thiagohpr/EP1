import random
craps=True
fichas=100

while craps:
    jogo=str(input("Para jogar, digite J \nPara sair do jogo, digite S  "))
    if jogo=="S":
        craps=False
    elif jogo=="J":
        print ("Fase de Come Out")
    
