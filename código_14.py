print("Bem, amigos da rede! Sistema de Estatísticas VAR Edition no ar. Aguardando comandos...")
banco_de_dados = {}
sistema_ativo = True

# Controle do laço principal de operações
while sistema_ativo:
    comando_bruto = input().strip()
    palavras_comando = ()
    palavra_temporaria = ""
    indice_letra = 0

    while indice_letra < len(comando_bruto):
        letra = comando_bruto[indice_letra]
        if letra == ' ':
            if palavra_temporaria != "":
                palavras_comando += (palavra_temporaria,)
                palavra_temporaria = ""
        else:
            palavra_temporaria += letra
        indice_letra += 1

    if palavra_temporaria != "":
        palavras_comando += (palavra_temporaria,)

    # identificador da ação
    acao = palavras_comando[0]
    # adicionar um jogador
    if acao == "*ADD":
        nome_jogador = palavras_comando[1]
        nome_selecao = palavras_comando[2]
        qtd_gols = int(palavras_comando[3])
        qtd_assistencias = int(palavras_comando[4])
        qtd_passes = int(palavras_comando[5])
        qtd_amarelos = int(palavras_comando[6])
        qtd_vermelhos = int(palavras_comando[7])
        chave = (nome_jogador, nome_selecao)

        # vr se já esta cadastrado na tupla, caso não, adiciona lá
        if chave in banco_de_dados:
            dados_atuais = banco_de_dados[chave]
            banco_de_dados[chave] = (
                nome_selecao,
                dados_atuais[1] + qtd_gols,
                dados_atuais[2] + qtd_assistencias,
                dados_atuais[3] + qtd_passes,
                dados_atuais[4] + qtd_amarelos,
                dados_atuais[5] + qtd_vermelhos
            )
        else:
            banco_de_dados[chave] = (
                nome_selecao, qtd_gols, qtd_assistencias, qtd_passes, qtd_amarelos, qtd_vermelhos)
    # remove jogador
    elif acao == "*DEL":
        nome_jogador = palavras_comando[1]
        nome_selecao = palavras_comando[2]
        jogador_removido = False

        while not jogador_removido:
            chave = (nome_jogador, nome_selecao)

            if chave in banco_de_dados:
                novo_banco_de_dados = {}
                for jogador_salvo in banco_de_dados:
                    if jogador_salvo != chave:
                        novo_banco_de_dados[jogador_salvo] = banco_de_dados[jogador_salvo]

                banco_de_dados = novo_banco_de_dados
                jogador_removido = True
                print(
                    f"O jogador: {nome_jogador} da seleção: {nome_selecao} foi retirado do sistema")
            else:
                print(
                    f"O jogador: {nome_jogador} da seleção: {nome_selecao} não foi encontrado insira uma outra combinação de jogador e seleção:")
                nova_tentativa = input().strip()

                # fatia o novo palpite
                novas_palavras = ()
                nova_temp = ""
                indice_nova = 0
                while indice_nova < len(nova_tentativa):
                    letra = nova_tentativa[indice_nova]
                    if letra == ' ':
                        if nova_temp != "":
                            novas_palavras += (nova_temp,)
                            nova_temp = ""
                    else:
                        nova_temp += letra
                    indice_nova += 1
                if nova_temp != "":
                    novas_palavras += (nova_temp,)

                nome_jogador = novas_palavras[0]
                nome_selecao = novas_palavras[1]

    # consulta o status do jogador
    elif acao == "*BUSCAR":
        nome_jogador = palavras_comando[1]
        nome_selecao = palavras_comando[2]
        chave = (nome_jogador, nome_selecao)

        if chave in banco_de_dados:
            dados = banco_de_dados[chave]
            print(
                f"{nome_jogador} ({nome_selecao}): {dados[1]}G, {dados[2]}A, {dados[3]}P, {dados[4]}CA, {dados[5]}CV")
        else:
            # caso Neymar
            if nome_jogador == "Neymar":
                print(
                    "E o pessoal tá lá: 'será que Carlo Ancelotti vai convocar o Neymar?'")
            else:
                print(f"Jogador não encontrado na seleção {nome_selecao}")

    # destaques
    elif acao == "*DESTAQUE_SELECAO":
        selecao_alvo = palavras_comando[1]

        # apenas jogadors da seleção especifica
        jogadores_da_selecao = ()
        for chave_jogador in banco_de_dados:
            if chave_jogador[1] == selecao_alvo:
                jogadores_da_selecao += (chave_jogador,)

        if len(jogadores_da_selecao) == 0:
            print(f"Nenhum dado encontrado para a seleção {selecao_alvo}")
        else:
            # buble sort
            total_jog = len(jogadores_da_selecao)
            indice_ord = 0
            while indice_ord < total_jog:
                indice_comp = 0
                while indice_comp < total_jog - indice_ord - 1:
                    chave_1 = jogadores_da_selecao[indice_comp]
                    chave_2 = jogadores_da_selecao[indice_comp+1]
                    dados_1 = banco_de_dados[chave_1]
                    dados_2 = banco_de_dados[chave_2]
                    precisa_trocar = False

                    if dados_1[1] < dados_2[1]:
                        precisa_trocar = True
                    elif dados_1[1] == dados_2[1]:
                        if dados_1[2] < dados_2[2]:
                            precisa_trocar = True
                        elif dados_1[2] == dados_2[2]:
                            if dados_1[5] > dados_2[5]:
                                precisa_trocar = True
                            elif dados_1[5] == dados_2[5]:
                                if dados_1[4] > dados_2[4]:
                                    precisa_trocar = True
                                elif dados_1[4] == dados_2[4]:
                                    if dados_1[3] < dados_2[3]:
                                        precisa_trocar = True
                                    elif dados_1[3] == dados_2[3]:
                                        if dados_1[0] > dados_2[0]:
                                            precisa_trocar = True
                                        elif dados_1[0] == dados_2[0]:
                                            if chave_1[0] > chave_2[0]:
                                                precisa_trocar = True

                    if precisa_trocar:
                        jogadores_da_selecao = jogadores_da_selecao[:indice_comp] + (
                            chave_2, chave_1) + jogadores_da_selecao[indice_comp+2:]
                    indice_comp += 1
                indice_ord += 1

            melhor_chave = jogadores_da_selecao[0]
            melhor_dados = banco_de_dados[melhor_chave]
            print(
                f"Destaque da {selecao_alvo}: {melhor_chave[0]} {melhor_dados[1]} gols, {melhor_dados[2]} assistências")

    # bola de ouro
    elif acao == "*BOLA_DE_OURO":
        todos_jogadores = ()
        for chave_jogador in banco_de_dados:
            todos_jogadores += (chave_jogador,)

        if len(todos_jogadores) == 0:
            print("Nenhum jogador registrado no torneio")
        else:
            total_jog = len(todos_jogadores)
            indice_ord = 0
            while indice_ord < total_jog:
                indice_comp = 0
                while indice_comp < total_jog - indice_ord - 1:
                    chave_1 = todos_jogadores[indice_comp]
                    chave_2 = todos_jogadores[indice_comp+1]
                    dados_1 = banco_de_dados[chave_1]
                    dados_2 = banco_de_dados[chave_2]
                    precisa_trocar = False

                    if dados_1[1] < dados_2[1]:
                        precisa_trocar = True
                    elif dados_1[1] == dados_2[1]:
                        if dados_1[2] < dados_2[2]:
                            precisa_trocar = True
                        elif dados_1[2] == dados_2[2]:
                            if dados_1[5] > dados_2[5]:
                                precisa_trocar = True
                            elif dados_1[5] == dados_2[5]:
                                if dados_1[4] > dados_2[4]:
                                    precisa_trocar = True
                                elif dados_1[4] == dados_2[4]:
                                    if dados_1[3] < dados_2[3]:
                                        precisa_trocar = True
                                    elif dados_1[3] == dados_2[3]:
                                        if dados_1[0] > dados_2[0]:
                                            precisa_trocar = True
                                        elif dados_1[0] == dados_2[0]:
                                            if chave_1[0] > chave_2[0]:
                                                precisa_trocar = True

                    if precisa_trocar:
                        todos_jogadores = todos_jogadores[:indice_comp] + (
                            chave_2, chave_1) + todos_jogadores[indice_comp+2:]
                    indice_comp += 1
                indice_ord += 1

            melhor_chave = todos_jogadores[0]
            melhor_dados = banco_de_dados[melhor_chave]
            print(
                f"Bola de Ouro atual: {melhor_chave[0]} {melhor_chave[1]} com {melhor_dados[1]} gols")

    # gera o ranking final
    elif acao == "*FIM":
        sistema_ativo = False

        todos_jogadores = ()
        for chave_jogador in banco_de_dados:
            todos_jogadores += (chave_jogador,)

        if len(todos_jogadores) == 0:
            print("Nenhum jogador registrado para o ranking final.")
        else:
            total_jog = len(todos_jogadores)
            indice_ord = 0
            while indice_ord < total_jog:
                indice_comp = 0
                while indice_comp < total_jog - indice_ord - 1:
                    chave_1 = todos_jogadores[indice_comp]
                    chave_2 = todos_jogadores[indice_comp+1]
                    dados_1 = banco_de_dados[chave_1]
                    dados_2 = banco_de_dados[chave_2]
                    precisa_trocar = False

                    if dados_1[1] < dados_2[1]:
                        precisa_trocar = True
                    elif dados_1[1] == dados_2[1]:
                        if dados_1[2] < dados_2[2]:
                            precisa_trocar = True
                        elif dados_1[2] == dados_2[2]:
                            if dados_1[5] > dados_2[5]:
                                precisa_trocar = True
                            elif dados_1[5] == dados_2[5]:
                                if dados_1[4] > dados_2[4]:
                                    precisa_trocar = True
                                elif dados_1[4] == dados_2[4]:
                                    if dados_1[3] < dados_2[3]:
                                        precisa_trocar = True
                                    elif dados_1[3] == dados_2[3]:
                                        if dados_1[0] > dados_2[0]:
                                            precisa_trocar = True
                                        elif dados_1[0] == dados_2[0]:
                                            if chave_1[0] > chave_2[0]:
                                                precisa_trocar = True

                    if precisa_trocar:
                        todos_jogadores = todos_jogadores[:indice_comp] + (
                            chave_2, chave_1) + todos_jogadores[indice_comp+2:]
                    indice_comp += 1
                indice_ord += 1

            print("Ranking Final:")
            indice_impressao = 0
            while indice_impressao < len(todos_jogadores):
                chave = todos_jogadores[indice_impressao]
                dados = banco_de_dados[chave]

                print(
                    f"{indice_impressao+1}. {chave[0]} ({chave[1]}) - G: {dados[1]}, A: {dados[2]}, P: {dados[3]}, CA: {dados[4]}, CV: {dados[5]}")
                indice_impressao += 1
