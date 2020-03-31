#Este é o codigo completo criado para rodar o jogo de Craps
#As 9 primeiras linhas mostram algumas definições de bibliotecas e classes que usamos para aperfeiçoar tanto a performance quanto a estetica do código
class cor:
    vermelho="\033[91m"
    azul="\033[94m"
    verde="\033[92m"
    negrito="\033[1m"
    fim="\033[0m"
import random
import time
#Aqui o jogo se inicia com o titulo. Vai ser possivel observar diversos time.sleep no codigo inteiro, função que utilizamos para deixar o jogo mais natural e menos crû
print(cor.vermelho + "JOGO DE CRAPS" + cor.fim)
time.sleep (2)
print(cor.vermelho + "ATENÇÃO" + cor.fim )
time.sleep (1)
print(cor.azul + "É recomendado que se leia o arquivo README.md pois nele contém as regras para este jogo. \nDivirta-se :)" + cor.fim)
time.sleep (4)
#Leia o README para ver as nossas regras Andrew


craps=True
fichas=100
#Todo o código do jogo está dentro desse while
while craps:
    print ("Você possui", cor.verde +  "{} fichas.".format (fichas) + cor.fim)
    print ("Para jogar, digite", cor.azul + "J" + cor.fim,"\nPara sair do jogo, digite", cor.vermelho + "S" + cor.fim)
    jogo=str(input("-"))
#Foi possivel observar a utilização do comando \n, com o intuito de deixar o jogo mais organizado na hora de rodar 
    if jogo=="S":
        craps=False
        print ("Obrigado por jogar. Você iniciou o jogo com 100 fichas e saiu dele com {}.".format (fichas))
        time.sleep (2)
        if fichas>100:
            print (cor.verde + "Parabéns! Você lucrou {} fichas.".format(fichas-100) + cor.fim)
        elif fichas<100:
            print (cor.vermelho + "Que pena! Infelizmente, voce perdeu {} fichas. :(".format(100-fichas) + cor.fim)
        elif fichas==100:
            print ("Parece até que não jogou.")

    elif jogo=="J":
        print (cor.negrito + "Fase de Come Out" + cor.fim)
        dado11=random.randint (1,6)
        dado12=random.randint (1,6)
        soma1=dado11+dado12
        time.sleep (1)
        print ("Você tem {} fichas.".format (fichas))
        time.sleep (1)
        
        fiec=True
        anyc=True
        twec=True
        plbc=True
    #Aqui foi utilizado condições para obrigar o jogador a apostar um valor possível (ou não apostar) e impedir-lo de apostar numeros maiores que sua
    #quantidade de fichas ou até mesmo numeros negativos, o que seria impossível.
        while fiec:
            print (cor.azul + "Aposta para Field\nSe não quiser apostar, digite 0.   " + cor.fim)
            fie=int(input("-"))
            if fie>fichas or fie<0:
                print (cor.vermelho + "Aposta inválida.\nVocê possui {} fichas".format (fichas) + cor.fim)
            elif fie>0:
                fichas=fichas-fie
                fiec=False
                print ("Você agora tem {} fichas.".format (fichas))
            else:
                fiec=False
        time.sleep (2)
        while anyc:
            print (cor.azul + "Aposta para Any Craps\nSe não quiser apostar, digite 0.   " + cor.fim)
            any=int(input("-"))
            if any>fichas or any<0:
                print (cor.vermelho + "Aposta inválida.\nVocê possui {} fichas".format (fichas) + cor.fim)
            elif any>0:
                fichas=fichas-any
                anyc=False
                print ("Você agora tem {} fichas.".format (fichas))
            else:
                anyc=False
        time.sleep (2)
        while twec:
            print (cor.azul + "Aposta para Twelve\nSe não quiser apostar, digite 0.   " + cor.fim)
            twe=int(input("-"))
            if twe>fichas or twe<0:
                print (cor.vermelho + "Aposta inválida.\nVocê possui {} fichas".format (fichas) + cor.fim)
            elif twe>0:
                fichas=fichas-twe
                twec=False
                print ("Você agora tem {} fichas.".format (fichas))
            else:
                twec=False
        time.sleep (2)
        while plbc:
            print (cor.azul + "Aposta para Pass line Bet\nSe não quiser apostar, digite 0.   " + cor.fim)
            plb=int(input("-"))
            if plb>fichas or plb<0:
                print (cor.vermelho + "Aposta inválida.\nVocê possui {} fichas".format (fichas) + cor.fim)
            elif plb>0:
                fichas=fichas-plb
                plbc=False
                print("Você agora tem {} fichas.".format (fichas))
            else:
                plbc=False
    #Na hora de sortear os dados, utilizamos o time.sleep para assim criar aquele drama semelhante ao jogo real,
    #quando se espera os resultados dos dados.
        time.sleep (1)
        print (cor.negrito + "Primeiro dado: " + cor.fim)
        time.sleep (3)
        print (cor.verde + "{}".format(dado11) + cor.fim)
        time.sleep (1)
        print (cor.negrito + "Segundo dado: " + cor.fim)
        time.sleep (3)
        print (cor.verde + "{}".format(dado12) + cor.fim)
        time.sleep (1)
        print (cor.verde + "A soma é de {}" .format(soma1) + cor.fim)
        time.sleep (2)
        if fie>0:
            if soma1==3 or soma1==4 or soma1==9 or soma1==10 or soma1==11:
                fichas=fichas+2*fie
                print (cor.verde + "Você recuperou sua aposta e ganhou {} no field.".format (fie) + cor.fim)
            elif soma1==2:
                fichas=fichas+3*fie
                print (cor.verde + "Você recuperou sua aposta e ganhou {} no field.".format (2*fie) + cor.fim)
            elif soma1==12:
                fichas=fichas+4*fie
                print (cor.verde + "Você recuperou sua aposta e ganhou {} no field.".format (3*fie) + cor.fim)
            else:
                print (cor.vermelho + "Você perdeu no field." + cor.fim)
        time.sleep (2)
        if any>0:
            if soma1==2 or soma1==3 or soma1==12:
                fichas=fichas+8*any 
                print (cor.verde + "Craps! Você recuperou sua aposta e ganhou {} no any craps.".format (7*any) + cor.fim)
            else:
                print (cor.vermelho + "Você perdeu no any craps" + cor.fim)
        time.sleep (2)    
        if twe>0:
            if soma1==12:
                fichas=fichas+31*twe
                print (cor.negrito + cor.verde +"JACKPOT! Você recuperou sua aposta e ganhou {} no twelve!".format (30*twe) + cor.fim)
            else:
                print (cor.vermelho + "Você perdeu no twelve." + cor.fim)
        time.sleep (2)
        if plb>0:
            if soma1==7 or soma1==11:
                fichas=fichas+2*plb
                print (cor.verde + "Você recuperou sua aposta e ganhou {} no pass line bet.".format (plb) + cor.fim)
            elif soma1==2 or soma1==3 or soma1==12:
                print (cor.vermelho + "Craps! Você perdeu no pass line bet." + cor.fim)
            else:
                point=soma1
                time.sleep (2)
                print (cor.negrito + "Você entrou na fase de Point" + cor.fim)
                time.sleep (2)
                fasePoint=True
                while fasePoint:
                    print ("Para sair da fase Point, você precisa conseguir a soma de {}.\nSe a soma for 7, você sai do Point perdendo os {} apostados.".format(point, plb))
                    dado21=random.randint(1,6)
                    dado22=random.randint(1,6)
                    soma2=dado21+dado22
                    fiec=True
                    anyc=True
                    twec=True
                    plbc=True
                    #para criar a segunda fase do jogo, nós basicamente reutilizamos a primeira fase e adcionamos o revéz de ficar preso dentro da Point,
                    #tanto que se observar o código de ambos é bem parecido
                    time.sleep (2)
                    print ("Você possui {} fichas.".format (fichas))
                    time.sleep (2)
                    while fiec:
                        print (cor.azul + "Aposta para Field\nSe não quiser apostar, digite 0.   " + cor.fim)
                        fie=int(input("-"))
                        if fie>fichas or fie<0:
                            print (cor.vermelho + "Aposta inválida.\nVocê possui {} fichas".format (fichas) + cor.fim)
                        elif fie>0:
                            fichas=fichas-fie
                            fiec=False
                            print ("Você agora tem {} fichas.".format (fichas))
                        else:
                            fiec=False
                    time.sleep (2)
                    while anyc:
                        print (cor.azul + "Aposta para Any Craps\nSe não quiser apostar, digite 0.   " + cor.fim)
                        any=int(input("-"))
                        if any>fichas or any<0:
                            print (cor.vermelho + "Aposta inválida.\nVocê possui {} fichas".format (fichas) + cor.fim)
                        elif any>0:
                            fichas=fichas-any
                            anyc=False
                            print ("Você agora tem {} fichas.".format (fichas))
                        else:
                            anyc=False
                    time.sleep (2)
                    while twec:
                        print (cor.azul + "Aposta para Twelve\nSe não quiser apostar, digite 0.   " + cor.fim)
                        twe=int(input("-"))
                        if twe>fichas or twe<0:
                            print (cor.vermelho + "Aposta inválida.\nVocê possui {} fichas".format (fichas) + cor.fim)
                        elif twe>0:
                            fichas=fichas-twe
                            twec=False
                            print ("Você agora tem {} fichas.".format (fichas))
                        else:
                            twec=False
                    time.sleep (2)
                    print (cor.negrito + "Primeiro dado: " + cor.fim)
                    time.sleep (3)
                    print (cor.verde + "{}".format(dado21) + cor.fim)
                    time.sleep (1)
                    print (cor.negrito + "Segundo dado: " + cor.fim)
                    time.sleep (3)
                    print (cor.verde + "{}".format(dado22) + cor.fim)
                    time.sleep (1)
                    print (cor.verde + "A soma é de {}.".format (soma2) + cor.fim)
                    time.sleep (1)
                    #Nossa regra de manter o jogador preso na Point mesmo zerado foi proposital
                    if fie>0:
                        if soma2==3 or soma2==4 or soma2==9 or soma2==10 or soma2==11:
                            fichas=fichas+2*fie
                            print (cor.verde + "Você recuperou sua aposta e ganhou {} no field.".format (fie) + cor.fim)
                        elif soma2==2:
                            fichas=fichas+3*fie
                            print (cor.verde + "Você recuperou sua aposta e ganhou {} no field.".format (2*fie) + cor.fim)
                        elif soma2==12:
                            fichas=fichas+4*fie
                            print (cor.verde + "Você recuperou sua aposta e ganhou {} no field.".format (3*fie) + cor.fim)
                        else:
                            print (cor.vermelho + "Você perdeu no field." + cor.fim)
                    time.sleep (2)
                    if any>0:
                        if soma2==2 or soma2==3 or soma2==12:
                            fichas=fichas+8*any 
                            print (cor.verde + "Craps! Você recuperou sua aposta e ganhou {} no any craps.".format (7*any) + cor.fim)
                        else:
                            print (cor.vermelho + "Você perdeu no any craps" + cor.fim)
                    time.sleep (2)
                    if twe>0:
                        if soma2==12:
                            fichas=fichas+31*twe
                            print (cor.negrito + cor.verde +"JACKPOT! Você recuperou sua aposta e ganhou {} no twelve!".format (30*twe) + cor.fim)
                        else:
                            print (cor.vermelho + "Você perdeu no twelve." + cor.fim)
                    time.sleep (2)

                    if soma2==7:
                        print ("Você perdeu as {} fichas apostadas no pass line bet e saiu do Point.".format (plb))
                        fasePoint=False

                    elif soma2==point:
                        fichas=fichas+2*plb
                        print ("Você recuperou sua aposta no pass line bet, ganhou {} fichas e saiu do Point.".format(plb))
                        fasePoint = False
                    
                    else:
                        print (cor.negrito + "Você não saiu do Point." + cor.fim)

        if fichas==0:
            time.sleep (1)
            print (cor.negrito + cor.vermelho + "Você zerou suas fichas. :(" + cor.fim)
            craps=False

        
        

        
            
            
        
        
        

    
