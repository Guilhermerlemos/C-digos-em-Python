# Função de compra
def comprar_plantas(qtd_sois):
    print("O quintal está sendo invadido! Prepare a melhor linha de defesa possível!")
    plantas = []  # lista de plantas existentes na área
    fim = False

    while fim == False:
        nome = input()
        if nome == "FIM":
            fim = True
        else:
            if nome == "Disparervilha":  # 50 sóis
                custo = 50
            elif nome == "Noz-Obstáculo":  # 75 sóis / unica planta a ter 2 de vida
                custo = 75
            elif nome == "Gelervilha":  # 100 sóis
                custo = 100
            else:
                custo = 0  # só para não realizar a compra

            if qtd_sois >= custo:
                if nome == "Noz-Obstáculo":
                    plantas.append([nome, 2])  # nome e vida
                else:
                    plantas.append([nome, 1])
                qtd_sois = qtd_sois - custo
            else:
                print("Você não tem sóis suficientes para isso!")
    return plantas
# ============================================================================================

# Função de batalha
def batalha(plantas, nome_zumbi):
    print("Lá vem o zumbi... espero que suas plantas estejam preparadas!")

    # Caracteristicas iniciais dos zumbis
    vida = 10
    velocidade = 2
    posicao = 17
    perdeu_jornal = False  # um dos tipos de zumbi

    # cada zumbi de cone, ganha mais vida
    if nome_zumbi == "Zumbi Cabeça-de-Cone":
        vida = vida + 4
    acabou = False

    # Sistema de ataque de plantas
    while acabou == False:
        i = 0
        while i < len(plantas):
            nome = plantas[i][0]

            if nome != "morta":
                # cada tiro, retira apenas 1 da vida do zumbi
                if nome == "Disparervilha":
                    vida = vida - 1
                elif nome == "Gelervilha":
                    vida = vida - 1
                    velocidade = velocidade - 1  # velocidade diminui

                    if velocidade < 1:  # se o zumbi perder o jonal, vl aumenta e vida baixa
                        if nome_zumbi == "Zumbi do Jornal" and perdeu_jornal == True:
                            velocidade = 2
                        else:
                            velocidade = 1
            i = i + 1

        # zumbi jornal ficando mais rápido
        if nome_zumbi == "Zumbi do Jornal":
            if perdeu_jornal == False:
                if vida <= 5:
                    velocidade = 3
                    perdeu_jornal = True

        # vr se zumbi morreu
        if vida <= 0:
            print("Bom trabalho! Dave Doidão nunca esteve tão feliz...")
            acabou = True

        # se nao morreu, precisa continuar andando
        if acabou == False:
            passos = 0

            #vr se zumbi chegou no limite ou seja chegou na casa
            while passos < velocidade and acabou == False:
                alvo = posicao - 1

                if alvo < 0:
                    print("O zumbi chegou à porta! Você perdeu!")
                    acabou = True
                
                #Vr se existe uma planta viva no alvo
                elif alvo < len(plantas) and plantas[alvo][0] != "morta":
                    nome_planta = plantas[alvo][0]

                    #Zumbi Saltador vs Noz
                    if nome_zumbi == "Zumbi Saltador" and nome_planta == "Noz-Obstáculo":
                        posicao = posicao - 1 #Pula a planta e a posição dela
                        passos = passos + 1
                    else:
                        #Zumbi está bloqueado pela planta, então ele ataca
                        plantas[alvo][1] = plantas[alvo][1] - 1
                        
                        if plantas[alvo][1] <= 0:
                            plantas[alvo][0] = "morta"
                            print("NOMNOMNOM!")
                        
                        passos = velocidade 
                else:
                    #Caminho livre ou planta morta, o zumbi avança
                    posicao = posicao - 1
                    passos = passos + 1


# inputs principais e chamando as funções
qtd_sois = int(input())
plantas = comprar_plantas(qtd_sois)

nome_zumbi = input()
batalha(plantas, nome_zumbi)
