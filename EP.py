class cor:
    vermelho="\033[91m"
    azul="\033[94m"
    verde="\033[92m"
    negrito="\033[1m"
    fim="\033[0m"

print(cor.vermelho + "JOGO DE CRAPS" + cor.fim)

import random
import time

craps=True
fichas=100

while craps:
    print ("Você possui", cor.verde +  "{} fichas.".format (fichas) + cor.fim)
    print ("Para jogar, digite", cor.azul + "J" + cor.fim,"\nPara sair do jogo, digite", cor.vermelho + "S" + cor.fim)
    jogo=str(input("-"))
    if jogo=="S":
        craps=False
        print ("Obrigado por jogar. Você iniciou o jogo com 100 fichas e saiu dele com {}.".format (fichas))

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

        print ("Você tem {} fichas.".format (fichas))

        
        fiec=True
        anyc=True
        twec=True
        plbc=True
        
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


        print (cor.negrito + "Primeiro dado: " + cor.fim)
        time.sleep (3)
        print (cor.verde + "{}".format(dado11) + cor.fim)
        time.sleep (1)
        print (cor.negrito + "Segundo dado: " + cor.fim)
        time.sleep (3)
        print (cor.verde + "{}".format(dado12) + cor.fim)
        time.sleep (1)
        print (cor.verde + "A soma é de {}" .format(soma1) + cor.fim)

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
                print (cor.negrito + "Você entrou na fase de Point" + cor.fim)
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
                    print ("Você possui {} fichas.".format (fichas))
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

                    print (cor.negrito + "Primeiro dado: " + cor.fim)
                    time.sleep (3)
                    print (cor.verde + "{}".format(dado21) + cor.fim)
                    time.sleep (1)
                    print (cor.negrito + "Segundo dado: " + cor.fim)
                    time.sleep (3)
                    print (cor.verde + "{}".format(dado22) + cor.fim)
                    time.sleep (1)
                    print (cor.verde + "A soma é de {}.".format (soma2) + cor.fim)

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
            print (cor.negrito + cor.vermelho + "Você zerou suas fichas. :(" + cor.fim)
            craps=False

        
        

        
            
            
        
        
        

    
