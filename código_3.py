dados = {
    "brasil_convocacao": {
        'Alisson': [], 'Ederson': [], 'Bento': [], 'Alex Sandro': [], 'Danilo': [],
        'Douglas Santos': [], 'Wesley': [], 'Marquinhos': [], 'Gabriel Magalhães': [],
        'Bremer': [], 'Léo Pereira': [], 'Andrey Santos': [], 'Bruno Guimarães': [],
        'Casemiro': [], 'Danilo Santos': [], 'Fabinho': [], 'Joelinton': [],
        'Endrick': [], 'Igor Thiago': [], 'Gabriel Martinelli': [], 'João Pedro': [],
        'Neymar': [], 'Luiz Henrique': [], 'Matheus Cunha': [], 'Raphinha': [],
        'Vinícius Júnior': []
    },
    "marrocos_convocacao": {
        'Bounou': [], 'Munir Mohamedi': [], 'El Mehdi Benabid': [], 'Hakimi': [],
        'Mazraoui': [], 'Aguerd': [], 'Chadi Riad': [], 'Yahya Attiat-Allah': [],
        'Abdelkabir Abqar': [], 'Achraf Dari': [], 'Ayoub El Amloud': [], 'Amrabat': [],
        'Ounahi': [], 'Brahim Díaz': [], 'Bilal El Khannouss': [], 'Ismael Saibari': [],
        'Amir Richardson': [], 'Oussama El Azzouzi': [], 'Amine Harit': [], 'Ziyech': [],
        'Amine Adli': [], 'En-Nesyri': [], 'Ezzalzouli': [], 'Soufiane Rahimi': [],
        'Ilias Akhomach': [], 'Ayoub El Kaabi': []
    },
    "jogo": {
        "status": "ativo",
        "tempo_anterior": 0,
        "gols_brasil": 0,
        "gols_marrocos": 0,
        "subs_brasil": 0,
        "subs_marrocos": 0,
        "log": [],
        "jogadores": {}  # nome --> [time, pontos, status, cartoes e saidas]
    }
}

# Fase 1
esquema = input()
partes = esquema.split('-')

# validação do esquema
esquema_valido = False
if len(partes) == 3:
    if partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
        a, b, c = int(partes[0]), int(partes[1]), int(partes[2])
        if a >= 1 and b >= 1 and c >= 1 and (a + b + c) == 10:
            esquema_valido = True

if not esquema_valido:
    print("Esquema inválido!")
    dados["jogo"]["status"] = "encerrado"
else:
    # identificação de jogadores
    jogadores_input = []
    for i in range(11):
        jogadores_input.append(input())

    # consolidação do time
    elenco_ok = True
    for player in jogadores_input:
        if player not in dados["brasil_convocacao"]:
            elenco_ok = False

    if not elenco_ok:
        print("Elenco inválido. Simulação Cancelada!")
        dados["jogo"]["status"] = "encerrado"
    else:
        # formação dos titulares do Brasil
        goleiro = jogadores_input[0]
        defensores = jogadores_input[1:1+a]
        meias = jogadores_input[1+a:1+a+b]
        atacantes = jogadores_input[1+a+b:]

        # inserir no estado do jogo
        todos_brasil = [goleiro] + defensores + meias + atacantes
        for p in todos_brasil:
            dados["jogo"]["jogadores"][p] = {
                'time': 'Brasil', 'pontos': 0, 'status': 'campo', 'cartoes': 0, 'entrou': True}

        # inserir no banco do Brasil
        for p in dados["brasil_convocacao"]:
            if p not in dados["jogo"]["jogadores"]:
                dados["jogo"]["jogadores"][p] = {
                    'time': 'Brasil', 'pontos': 0, 'status': 'banco', 'cartoes': 0, 'entrou': False}

        # formação do Marrocos
        marrocos_titulares = ["Bounou", "Hakimi", "Mazraoui", "Aguerd", "Chadi Riad",
                              "Amrabat", "Ounahi", "Brahim Díaz", "Ziyech", "Amine Adli", "En-Nesyri"]
        for p in marrocos_titulares:
            dados["jogo"]["jogadores"][p] = {
                'time': 'Marrocos', 'pontos': 0, 'status': 'campo', 'cartoes': 0, 'entrou': True}
        for p in dados["marrocos_convocacao"]:
            if p not in dados["jogo"]["jogadores"]:
                dados["jogo"]["jogadores"][p] = {
                    'time': 'Marrocos', 'pontos': 0, 'status': 'banco', 'cartoes': 0, 'entrou': False}

        # prints de formação
        print(f"O Brasil vem a campo com o goleiro {goleiro}.")
        print(f"A defesa é composta por {', '.join(defensores)}.")
        print(f"O meio de campo vem com {', '.join(meias)}.")
        print(f"E no ataque temos {', '.join(atacantes)}.")

# Fase 2
while dados["jogo"]["status"] == "ativo":
    linha_tempo = input().upper()

    if linha_tempo == "FIM":
        dados["jogo"]["status"] = "fim"
    elif not linha_tempo.isdigit():
        if dados["jogo"]["tempo_anterior"] == 0:
            print("Entrada inválida. O jogo não foi iniciado!")
            dados["jogo"]["status"] = "erro"
        else:
            dados["jogo"]["status"] = "fim"
    else:
        tempo = int(linha_tempo)
        if tempo < 1 or tempo > 90 or tempo <= dados["jogo"]["tempo_anterior"]:
            if dados["jogo"]["tempo_anterior"] == 0:
                print("Entrada inválida. O jogo não foi iniciado!")
                dados["jogo"]["status"] = "erro"
            else:
                dados["jogo"]["status"] = "fim"
        else:
            dados["jogo"]["tempo_anterior"] = tempo
            acao = input().lower()

            # vr de ações
            if acao not in ["gol", "cartão amarelo", "cartão vermelho", "substituição"]:
                print("Ação inválida! Simulação Cancelada")
                dados["jogo"]["status"] = "erro"
            else:
                jogador_nome = input()
                if jogador_nome not in dados["jogo"]["jogadores"]:
                    print("Jogador inválido. Simulação Cancelada")
                    dados["jogo"]["status"] = "erro"
                elif dados["jogo"]["jogadores"][jogador_nome]["status"] != "campo":
                    print(f"{jogador_nome} não está em campo! Simulação Cancelada")
                    dados["jogo"]["status"] = "erro"
                else:
                    if acao == "gol":
                        h_assist = input().lower()
                        gol_valido = True

                        if h_assist == "sim":
                            assist = input()
                            if (assist in dados["jogo"]["jogadores"] and
                                    dados["jogo"]["jogadores"][assist]["status"] == "campo" and
                                    dados["jogo"]["jogadores"][assist]["time"] == dados["jogo"]["jogadores"][jogador_nome]["time"]):

                                dados["jogo"]["jogadores"][jogador_nome]["pontos"] += 8
                                dados["jogo"]["jogadores"][assist]["pontos"] += 5
                                dados["jogo"]["log"].append(
                                    f"{tempo}'⚽ {jogador_nome}; 🅰️ {assist}")
                            else:
                                print("Jogador inválido. Simulação Cancelada")
                                dados["jogo"]["status"] = "erro"
                                gol_valido = False

                        elif h_assist == "não":
                            dados["jogo"]["jogadores"][jogador_nome]["pontos"] += 8
                            dados["jogo"]["log"].append(
                                f"{tempo}'⚽ {jogador_nome}")
                        else:
                            print("Entrada inválida!")
                            dados["jogo"]["status"] = "erro"
                            gol_valido = False

                        if gol_valido:
                            if dados["jogo"]["jogadores"][jogador_nome]["time"] == "Brasil":
                                dados["jogo"]["gols_brasil"] += 1
                            else:
                                dados["jogo"]["gols_marrocos"] += 1

                    elif acao == "cartão amarelo":
                        dados["jogo"]["jogadores"][jogador_nome]["cartoes"] += 1
                        dados["jogo"]["jogadores"][jogador_nome]["pontos"] -= 2
                        dados["jogo"]["log"].append(
                            f"{tempo}'🟨 {jogador_nome}")
                        if dados["jogo"]["jogadores"][jogador_nome]["cartoes"] >= 2:
                            dados["jogo"]["jogadores"][jogador_nome]["status"] = "expulso"
                            dados["jogo"]["jogadores"][jogador_nome]["pontos"] -= 1
                            dados["jogo"]["log"].append(
                                f"{tempo}'🟥 {jogador_nome}")

                    elif acao == "cartão vermelho":
                        dados["jogo"]["jogadores"][jogador_nome]["status"] = "expulso"
                        dados["jogo"]["jogadores"][jogador_nome]["pontos"] -= 5
                        dados["jogo"]["log"].append(
                            f"{tempo}'🟥 {jogador_nome}")

                    elif acao == "substituição":
                        novo_jogador = input()
                        time = dados["jogo"]["jogadores"][jogador_nome]["time"]
                        subs_count = dados["jogo"]["subs_brasil"] if time == "Brasil" else dados["jogo"]["subs_marrocos"]

                        if (novo_jogador not in dados["jogo"]["jogadores"] or
                                dados["jogo"]["jogadores"][novo_jogador]["status"] != "banco" or
                                dados["jogo"]["jogadores"][novo_jogador]["time"] != time or
                                subs_count >= 5):
                            print(
                                "A substituição não pôde ser concluída! Simulação Cancelada")
                            dados["jogo"]["status"] = "erro"
                        else:
                            dados["jogo"]["jogadores"][jogador_nome]["status"] = "substituido"
                            dados["jogo"]["jogadores"][novo_jogador]["status"] = "campo"
                            dados["jogo"]["jogadores"][novo_jogador]["entrou"] = True
                            dados["jogo"]["log"].append(
                                f"{tempo}'⬆️ {novo_jogador} ⬇️ {jogador_nome}")
                            if time == "Brasil":
                                dados["jogo"]["subs_brasil"] += 1
                            else:
                                dados["jogo"]["subs_marrocos"] += 1

# Fase 3
if dados["jogo"]["status"] == "fim":
    print()
    print(
        f"Fim de jogo! Brasil {dados['jogo']['gols_brasil']}x{dados['jogo']['gols_marrocos']} Marrocos.")
    for l in dados["jogo"]["log"]:
        print(l)

    # melhor da partida
    mvp = ""
    max_pts = -999

    # desemparte alfabetico
    nomes = sorted(list(dados["jogo"]["jogadores"].keys()))
    for p in nomes:
        if dados["jogo"]["jogadores"][p]["entrou"]:
            pts = dados["jogo"]["jogadores"][p]["pontos"]
            if pts > max_pts:
                max_pts = pts
                mvp = p

    if mvp:
        time_mvp = dados["jogo"]["jogadores"][mvp]["time"]
        print(f"🏆 O melhor em campo foi {mvp}, do {time_mvp}.")
    else:
        print("Não houve jogadores elegíveis para o prêmio de melhor em campo.")
    print()

    # prints finais
    dif = dados["jogo"]["gols_brasil"] - dados["jogo"]["gols_marrocos"]
    if dif >= 3:
        print("QUE GOLEADA! O INÍCIO DO SONHO DO HEXA!!!")
    elif dif > 0:
        print("Boa vitória! Essa Copa é nossa, Brasil!")
    elif dif <= -3:
        print("Era melhor nem ter vindo pra essa Copa…")
    elif dif < 0:
        print("Foco, Brasil! Vamos nos recuperar dessa!")
    else:
        if dados["jogo"]["gols_brasil"] == 0:
            print("Zzzzzzzzzzzzz…")
        else:
            print("Jogo difícil, mas podia ser melhor!")
