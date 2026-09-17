# Caminho impossível
inf = 1000000000.0


def encontrar_menor(a, b, c):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor


def ler_pistas(n):
    # condição de stopppp
    if n == 0:
        return []

    entrada = input().split()
    # estrutura da pista: tipo, distancia, p1, p2
    pista = [entrada[0], float(entrada[1]), float(
        entrada[2]), float(entrada[3])]
    return [pista] + ler_pistas(n - 1)


def simular_corrida(idx_pista, v_atual, g_atual, pistas, n):
    # condição de stoppp
    if idx_pista == n:
        return 0.0

    # Acelerar (+10) / Manter (0) /Frear (-10)
    tempo_acelerar = calcular_trecho(
        idx_pista, v_atual, g_atual, 10, pistas, n)
    tempo_manter = calcular_trecho(idx_pista, v_atual, g_atual, 0, pistas, n)
    tempo_frear = calcular_trecho(idx_pista, v_atual, g_atual, -10, pistas, n)

    return encontrar_menor(tempo_acelerar, tempo_manter, tempo_frear)


def calcular_trecho(idx, v_atual, g_atual, acao, pistas, n):
    v_entrada = v_atual + acao
    pista = pistas[idx]

    # recebendo os idx
    tipo = pista[0]
    distancia = pista[1]
    p1 = pista[2]
    p2 = pista[3]

    acidente = False
    v_saida = 0.0
    tempo_gasto = 0.0

    # vr de movimento mínimo
    if v_entrada <= 0:
        acidente = True
    else:
        tempo_gasto = distancia / v_entrada

        # fsica da pista
        if tipo == "Reta":
            v_saida = v_entrada
        elif tipo == "Curva":
            if v_entrada > p1:
                acidente = True
            else:
                v_saida = v_entrada
        elif tipo == "Subida":
            v_saida = v_entrada - p1
            if v_saida <= 0:
                acidente = True
        elif tipo == "Descida":
            v_saida = v_entrada + p1
            if v_saida > p2:
                acidente = True
            else:
                v_saida = v_entrada + p1

    # tratamento de acidentes
    if acidente:
        if g_atual > 0:
            return 0.0 + simular_corrida(idx + 1, 10.0, g_atual - 1, pistas, n)
        else:
            return inf
    else:
        return tempo_gasto + simular_corrida(idx + 1, v_saida, g_atual, pistas, n)


def iniciar_programa():  # inicio de programa
    primeira_linha = input().split()
    # separando a lista por variaveis
    n = int(primeira_linha[0])
    v0 = float(primeira_linha[1])
    g = int(primeira_linha[2])
    pistas = ler_pistas(n)

    print("Calibrando a gravidade e o atrito da pista...")
    print()

    resultado = simular_corrida(0, v0, g, pistas, n)

    if resultado >= inf:
        print("Bug fatal! Vanellope capotou e o kart virou pixels.")
    else:
        print(
            f"A corrida foi um sucesso! Tempo minimo cravado: {resultado:.2f}s.")


iniciar_programa()
