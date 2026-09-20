numero_rodadas = int(input())
print("Radar de Fofocas de Copacabana iniciado!")

for i in range(1, numero_rodadas + 1):
    pontuacao = 15
    pontuacao_atual = pontuacao
    todas_fofocas = ""

    numero_fofocas = int(input())

    print(f"Rodada {i}/{numero_rodadas}")
    print(f"Fofocas registradas: {numero_fofocas}")
    print("Pontuação inicial: 15")

    for f in range(numero_fofocas):
        fofoca = input()
        todas_fofocas += fofoca + " "

    palavra_proibida = str(input())

    tentativa = input()
    todas_tentativas = ""

    while tentativa != 'fim' and pontuacao > 0:
        ocorrencias = 0
        palavra = ""

        for letra in todas_fofocas + " ":
            if letra != " ":
                palavra += letra
            else:
                if palavra == tentativa:
                    ocorrencias += 1
                palavra = ""

        if " " + tentativa + " " in " " + todas_tentativas:
            print(f"Você já investigou '{tentativa}'. Tente outra.")
        else:
            todas_tentativas += tentativa + " "

            if tentativa == palavra_proibida:
                print(
                    f"Armadilha da Sueli! '{tentativa}' era proibida! -5 pontos")
                pontuacao = pontuacao - 5
                pontuacao_atual = pontuacao
                print(f"Pontuação atual: {pontuacao_atual}")

            elif ocorrencias > 0:
                print(
                    f"Investigação bem sucedida! '{tentativa}' apareceu {ocorrencias} vez(es).")
                pontuacao += ocorrencias * 2
                pontuacao_atual = pontuacao
                print(f"Pontuação atual: {pontuacao_atual}")

            else:
                print(f"Nada encontrado sobre '{tentativa}'. -1 ponto")
                pontuacao = pontuacao - 1
                pontuacao_atual = pontuacao
                print(f"Pontuação atual: {pontuacao_atual}")

        if pontuacao > 0:
            tentativa = input()
    if pontuacao <= 0:
        print("Você ficou sem pontos! Sueli venceu essa rodada")

    elif tentativa == "fim":
        print(f'Rodada encerrada! Pontuação final: {pontuacao_atual}')
