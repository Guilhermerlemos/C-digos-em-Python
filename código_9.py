def yesod():
    print("Hoje é dia do Yesod!")
    print("Yesod: Você é a cabeça dessa corporação, você deve agir como um exemplo para os outros e fazer certeza que esse dia passe coordialmente seguindo as regras.")
    print("Yesod: Hoje estamos com um problema a resolver. Você é um progamador, não é? Hoje recebemos vários caracteres, e você terá de as comprimir para facilitar as informações.\n")

    sequencia = input()

    resultado = ""
    contador = 1
    corrupcao = False

    i = 0

    while i < len(sequencia):
        atual = sequencia[i]

        if atual == '&':
            corrupcao = True  # só para parar o loop
            i = len(sequencia)
        else:
            # vr do proximo caractere
            if i + 1 < len(sequencia) and sequencia[i] == sequencia[i + 1]:
                contador += 1
            else:
                if contador > 1:
                    resultado = resultado + str(contador) + sequencia[i]
                else:
                    resultado = resultado + sequencia[i]
                contador = 1
            i += 1
    if corrupcao:
        print("Yesod: Os caracteres de hoje estavam corrompidas... devemos encerrar o dia mais cedo e investigar.")
        print(
            f"Yesod: Pelo menos, essas informações ainda estão conosco: '{resultado}'\n")
        return False
    else:
        print(
            f"Yesod: Aqui está a lista de caracteres comprimidos: '{resultado}'\n")
        return True


def binah(energia_necessaria):
    print("Hoje é o dia da Binah.")
    print("Binah: ...Você chegou.")
    print("Binah: Você já deve saber o que fazer. Espero um bom resultado vindo de você.\n")

    # listas de entrada
    B = []
    A = []

    # leitura da matriz A
    for m in range(3):
        linha = input().split()
        A.append([int(linha[0]), int(linha[1]), int(linha[2])])

    # leitura da matriz B
    for m in range(3):
        linha = input().split()
        B.append([int(linha[0]), int(linha[1]), int(linha[2])])

    C = []
    energia = 0

    # multiplicação da matriz
    for i in range(3):
        linha_resultado = []
        for j in range(3):
            soma = 0
            for k in range(3):
                soma = soma + A[i][k] * B[k][j]
            linha_resultado.append(soma)

            if i == j:
                energia = energia + soma

        C.append(linha_resultado)

    for linha in C:
        print(linha)

    print()
    print(f"Energia Coletada: {energia} / {energia_necessaria}")

    if energia >= energia_necessaria:
        print("Binah: O expediente foi concluído. Não cometa os mesmos erros amanhã.\n")
        return True
    else:
        print("Binah: É realmente uma sensação única te ver falhando...\n")
        return False


def malkuth(energia_necessaria):
    print("Hoje é o dia da Malkuth!")
    print("Malkuth: Ah, onde estão meus modos! Malkuth se apresentando!")
    print("Malkuth: Estamos responsáveis hoje por organizar por tamanho nossa lista de funcionários do time de controle, vamos entregar com resultados perfeitos!\n")

    nomes_entrada = input()
    # vr de espaço vazio
    if nomes_entrada.strip() == "":
        print("Malkuth: Pessoal?! Onde está todo mundo?! Isso é inaceitável!\n")
        return False

    # criando lista com espaços
    nomes = nomes_entrada.split()

    # bubble sort
    for t in range(len(nomes)):
        for k in range(len(nomes)-1):
            if len(nomes[k]) > len(nomes[k+1]):
                variavel_vazia = nomes[k]
                nomes[k] = nomes[k+1]
                nomes[k+1] = variavel_vazia
    print(" ".join(nomes))

    # calculando energia
    energia = (len(nomes[0]) + len(nomes[-1])) * 20
    print(f"Energia Coletada: {energia} / {energia_necessaria}")

    # vr status da energia coletada
    if energia >= energia_necessaria:
        print("Malkuth: O treino vespertino de hoje foi um sucesso! Estarei esperando vocês no período noturno, pessoal!\n")
        return True
    else:
        print("Malkuth: Ah não.. não conseguimos energia suficiente... amanhã eu dobrarei a carga horária para que a gente possa concluir o expediente com excelência!\n")
        return False


def gerenciamento_dias():
    qtd_dias = int(input())

    print("Hoje é o dia da Lobotomy CinCorporation!\n")

    resultados = []
    dia_atual = 1

    # Mudança de dia e vr de quantidade de energia
    while dia_atual <= qtd_dias:
        energia_necessaria = 100 + (dia_atual - 1) * 40

        print(
            f"Angela: Hoje é o dia {dia_atual} de {qtd_dias}. Espero mais um expediente concluído com excelência.")

        # vr dos nomes das sáfiras
        sefirot = input()
        # Malkuth
        if sefirot == 'Malkuth':
            resultado = malkuth(energia_necessaria)
            resultados.append(resultado)

        # Yesod
        elif sefirot == 'Yesod':
            resultado = yesod()
            resultados.append(resultado)

        # Binah
        elif sefirot == 'Binah':
            resultado = binah(energia_necessaria)
            resultados.append(resultado)

        else:
            print("Angela: Essa sefirot não está disponível hoje.\n")
            resultados.append(False)
        dia_atual += 1

    print("Angela: O relatório dessa semana está pronto.")

    i = 0
    while i < len(resultados):
        if resultados[i]:
            print(f"Dia {i+1} | Status: Energia necessária adquirida.")
        else:
            print(f"Dia {i+1} | Status: Energia necessária não adquirida.")
        i += 1


gerenciamento_dias()
