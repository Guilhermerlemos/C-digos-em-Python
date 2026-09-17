# Guarda apenas as tuplas: nome -> (gols, assist, dribles, lesao)
dados_jogadores = {}
vagas = int(input())

# print inical
print("Conexão CBF e CIn-UFPE estabelecida! Processando os dados da convocação rumo ao Hexa...")
print()

# controle principal
if vagas == 0:
    print("Vixe, zero vagas? Parece que a panela já ta formada e o mister já tem os 26 nomes na cabeça.")
else:
    processando = True
    alguem_analisado = False

# Coletiva
    while processando:
        linha = input()
        if linha == "A coletiva vai começar":
            if not alguem_analisado:
                print(
                    "Ue, a coletiva começou mas ninguém foi analisado? O professor vai convocar os gandulas?")
            else:
                processando = False
        else:
            # qtd de varivel - casos que aconteceram durante o jogo
            partes = linha.split(' - ')
            info_nome = partes[0].split('Partida: ')
            nome = info_nome[1]
            gols = int(partes[1])
            assist = int(partes[2])
            dribles = int(partes[3])
            lesao = int(partes[4])

            # vr existencia
            ja_analisado = False
            for n in dados_jogadores:
                if n == nome:
                    ja_analisado = True

             # atualizações das ações durante o jogo
            if ja_analisado:
                stats = dados_jogadores[nome]
                nova_tupla = (stats[0] + gols, stats[1] +
                              assist, stats[2] + dribles, stats[3] + lesao)
                dados_jogadores[nome] = nova_tupla
            else:
                dados_jogadores[nome] = (gols, assist, dribles, lesao)
                alguem_analisado = True

            if nome == "Neymar":
                if lesao == 0:
                    print("O homem jogou! A esperanca do hexa respira.")
                else:
                    print(
                        "Neymar machucou... Mas deixa ele recuperar, na Copa ele decide!")
            else:
                if lesao == 1:
                    print(
                        f"Ih, {nome} foi pro estaleiro. Ancelotti ta preocupado.")
                else:
                    if ja_analisado:
                        print(f"Mais um jogo pra conta de {nome}.")
                    else:
                        print(f"Vamos ver o que Ancelotti achará de {nome}.")

    print()
    print("--- CONVOCADOS PARA O HEXA ---")

    total_jogadores = 0
    for n in dados_jogadores:
        total_jogadores += 1

    jogadores_ja_convocados = ""
    vagas_preenchidas = 0
    neymar_convocado = False

    while vagas_preenchidas < vagas and vagas_preenchidas < total_jogadores:

        # ranqueamento
        melhor_nome = ""
        melhor_score = -99999
        melhor_gols = -99999

        for nome in dados_jogadores:
            busca = " " + nome + " "
            if busca not in jogadores_ja_convocados:
                stats = dados_jogadores[nome]
                g = stats[0]
                a = stats[1]
                d = stats[2]
                l = stats[3]

                if nome == "Neymar":
                    score = (g * 5) + (a * 3) + (d * 1) + 20
                else:
                    score = (g * 5) + (a * 3) + (d * 1) - (l * 10)

                # Criterios
                trocar = False
                if melhor_nome == "":
                    trocar = True
                elif score > melhor_score:  # pontos
                    trocar = True
                elif score == melhor_score:
                    if g > melhor_gols:  # gols
                        trocar = True
                    elif g == melhor_gols:
                        if nome < melhor_nome:  # Ordem alfabética
                            trocar = True

                if trocar:
                    melhor_nome = nome
                    melhor_score = score
                    melhor_gols = g

        # o melhor da rodada
        stats_melhor = dados_jogadores[melhor_nome]
        print(
            f"{vagas_preenchidas + 1}. {melhor_nome} - {melhor_score} pts (G: {stats_melhor[0]}, A: {stats_melhor[1]})")

        if melhor_nome == "Neymar":
            neymar_convocado = True

        # Adiciona o jogador em um dicionario
        jogadores_ja_convocados = jogadores_ja_convocados + " " + melhor_nome + " "
        vagas_preenchidas += 1

    # caso neymar
    if alguem_analisado:
        if neymar_convocado:
            print("Prepara o pagode e a caixa de som, o Ney ta on!")
            if vagas_preenchidas < vagas:
                print(
                    "A lista não encheu, mas com o camisa 10 lá dentro, Ancelotti já tá com a cabeça no Hexa.")
        else:
            print("Eita... Ancelotti bancou a tática e deixou o menino Ney de fora!")
            if vagas_preenchidas < vagas:
                print("Se liga, professor... ainda tem espaço pra o Ney!")
    else:

        print("Eita... Ancelotti bancou a tática e deixou o menino Ney de fora!")
