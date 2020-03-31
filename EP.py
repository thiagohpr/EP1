import random
craps=True
fichas=100

while craps:
    jogo=str(input("Para jogar, digite J \nPara sair do jogo, digite S  "))
    if jogo=="S":
        craps=False
        print ("Obrigado por jogar. Você iniciou o jogo com 100 fichas e saiu dele com {}.".format (fichas))

        if fichas>100:
            print ("Parabéns! Você lucrou {} fichas.".format(fichas-100))
        elif fichas<100:
            print ("Que pena! Infelizmente, voce perdeu {} fichas. :(".format(100-fichas))
        elif fichas==100:
            print ("Parece até que não jogou.")

    elif jogo=="J":
        print ("Fase de Come Out")
        dado11=random.randint (1,6)
        dado12=random.randint (1,6)
        soma1=dado11+dado12

        print ("Você tem {} fichas.".format (fichas))

        
        fiec=True
        anyc=True
        twec=True
        plbc=True
        
        while fiec:
            fie=int(input("Aposta para Field\nSe não quiser apostar, digite 0.   "))
            if fie>fichas or fie<0:
                print ("Aposta inválida.\nVocê possui {} fichas".format (fichas))
            elif fie>0:
                fichas=fichas-fie
                fiec=False
                print ("Você agora tem {} fichas.".format (fichas))
            else:
                fiec=False

        while anyc:
            any=int(input("Aposta para Any Craps\nSe não quiser apostar, digite 0.   "))
            if any>fichas or any<0:
                print ("Aposta inválida.\nVocê possui {} fichas".format (fichas))
            elif any>0:
                fichas=fichas-any
                anyc=False
                print ("Você agora tem {} fichas.".format (fichas))
            else:
                anyc=False

        while twec:
            twe=int(input("Aposta para Twelve\nSe não quiser apostar, digite 0.   "))
            if twe>fichas or twe<0:
                print ("Aposta inválida.\nVocê possui {} fichas".format (fichas))
            elif twe>0:
                fichas=fichas-twe
                twec=False
                print ("Você agora tem {} fichas.".format (fichas))
            else:
                twec=False

        while plbc:
            plb=int(input("Aposta para Pass line Bet\nSe não quiser apostar, digite 0.   "))
            if plb>fichas or plb<0:
                print ("Aposta inválida.\nVocê possui {} fichas".format (fichas))
            elif plb>0:
                fichas=fichas-plb
                plbc=False
                print("Você agora tem {} fichas.".format (fichas))
            else:
                plbc=False


        print ("Primeiro dado: {}".format (dado11))
        print ("Segundo dado: {}".format (dado12))
        print ("Soma de {}.".format (soma1))

        if fie>0:
            if soma1==3 or soma1==4 or soma1==9 or soma1==10 or soma1==11:
                fichas=fichas+2*fie
                print ("Você recuperou sua aposta e ganhou {} no field.".format (fie))
            elif soma1==2:
                fichas=fichas+3*fie
                print ("Você recuperou sua aposta e ganhou {} no field.".format (2*fie))
            elif soma1==12:
                fichas=fichas+4*fie
                print ("Você recuperou sua aposta e ganhou {} no field.".format (3*fie))
            else:
                print ("Você perdeu no field.")

        if any>0:
            if soma1==2 or soma1==3 or soma1==12:
                fichas=fichas+8*any 
                print ("Craps! Você recuperou sua aposta e ganhou {} no any craps.".format (7*any))
            else:
                print ("Você perdeu no any craps")
            
        if twe>0:
            if soma1==12:
                fichas=fichas+31*twe
                print ("JACKPOT! Você recuperou sua aposta e ganhou {} no twelve!".format (30*twe))
            else:
                print ("Você perdeu no twelve.")
        
        if plb>0:
            if soma1==7 or soma1==11:
                fichas=fichas+2*plb
                print ("Você recuperou sua aposta e ganhou {} no pass line betJ.".format (plb))
            elif soma1==2 or soma1==3 or soma1==12:
                print ("Craps! Você perdeu no pass line bet.")
            else:
                point=soma1
                print ("Você entrou na fase de Point")
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
                        fie=int(input("Aposta para Field\nSe não quiser apostar, digite 0.   "))
                        if fie>fichas or fie<0:
                            print ("Aposta inválida.\nVocê possui {} fichas".format (fichas))
                        elif fie>0:
                            fichas=fichas-fie
                            fiec=False
                            print ("Você agora tem {} fichas.".format (fichas))
                        else:
                            fiec=False

                    while anyc:
                        any=int(input("Aposta para Any Craps\nSe não quiser apostar, digite 0.   "))
                        if any>fichas or any<0:
                            print ("Aposta inválida.\nVocê possui {} fichas".format (fichas))
                        elif any>0:
                            fichas=fichas-any
                            anyc=False
                            print ("Você agora tem {} fichas.".format (fichas))
                        else:
                            anyc=False

                    while twec:
                        twe=int(input("Aposta para Twelve\nSe não quiser apostar, digite 0.   "))
                        if twe>fichas or twe<0:
                            print ("Aposta inválida.\nVocê possui {} fichas".format (fichas))
                        elif twe>0:
                            fichas=fichas-twe
                            twec=False
                            print ("Você agora tem {} fichas.".format (fichas))
                        else:
                            twec=False

                    print ("Primeiro dado: {}".format (dado21))
                    print ("Segundo dado: {}".format (dado22))
                    print ("Soma de {}.".format (soma2))

                    if fie>0:
                        if soma1==3 or soma1==4 or soma1==9 or soma1==10 or soma1==11:
                            fichas=fichas+2*fie
                            print ("Você recuperou sua aposta e ganhou {} no field.".format (fie))
                        elif soma1==2:
                            fichas=fichas+3*fie
                            print ("Você recuperou sua aposta e ganhou {} no field.".format (2*fie))
                        elif soma1==12:
                            fichas=fichas+4*fie
                            print ("Você recuperou sua aposta e ganhou {} no field.".format (3*fie))
                        else:
                            print ("Você perdeu no field.")

                    if any>0:
                        if soma1==2 or soma1==3 or soma1==12:
                            fichas=fichas+8*any 
                            print ("Craps! Você recuperou sua aposta e ganhou {} no any craps.".format (7*any))
                        else:
                            print ("Você perdeu no any craps")
            
                    if twe>0:
                        if soma1==12:
                            fichas=fichas+31*twe
                            print ("JACKPOT! Você recuperou sua aposta e ganhou {} no twelve!".format (30*twe))
                        else:
                            print ("Você perdeu no twelve.")
                    

                    if soma2==7:
                        print ("Você perdeu as {} fichas apostadas no pass line bet e saiu do Point.".format (plb))
                        fasePoint=False

                    elif soma2==point:
                        fichas=fichas+2*plb
                        print ("Você recuperou sua aposta no pass line bet, ganhou {} fichas e saiu do Point.".format(plb))
                        fasePoint = False
                    
                    else:
                        print ("Você não saiu do Point.")

        if fichas==0:
            print ("Você zerou suas fichas. :(")
            craps=False

        
        

        
            
            
        
        
        

    
