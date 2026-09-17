def encontrar_jasmine(matriz, r, c, linhas, colunas):
    # condição de stopp
    if r >= linhas:
        return -1, -1

    if c >= colunas:
        return encontrar_jasmine(matriz, r + 1, 0, linhas, colunas)

    # encontrou Jasmine ---- retorna posicao
    if matriz[r][c] == 'J':
        return r, c
    return encontrar_jasmine(matriz, r, c + 1, linhas, colunas)


def contar_caminhos(matriz, r, c, linhas, colunas, espinhos):
    # vr de limites da matriz
    if r < 0 or r >= linhas or c < 0 or c >= colunas:
        return 0

    celula = matriz[r][c]

    # vr de obstáculos
    if celula == '|' or celula == 'V':
        return 0

    # espinhos
    novos_espinhos = espinhos
    if celula == ',':
        novos_espinhos += 1

    # morte de Jasmine
    if novos_espinhos >= 3:
        return 0

    # venceu
    if celula == 'S':
        return 1

    # Backtracking
    valor_original = matriz[r][c]
    matriz[r][c] = 'V'

    total = (contar_caminhos(matriz, r + 1, c, linhas, colunas, novos_espinhos) +
             contar_caminhos(matriz, r - 1, c, linhas, colunas, novos_espinhos) +
             contar_caminhos(matriz, r, c + 1, linhas, colunas, novos_espinhos) +
             contar_caminhos(matriz, r, c - 1, linhas, colunas, novos_espinhos))

    matriz[r][c] = valor_original
    return total


def ler_matriz(m, contador):
    # condição de stop
    if contador == m:
        return []

    linha = list(input())
    return [linha] + ler_matriz(m, contador + 1)


def iniciar_fuga():  # inicio do programa
    m_input = input()
    m = int(m_input)
    n_input = input()
    n = int(n_input)
    labirinto = ler_matriz(m, 0)

    # encontra posição inicial
    r_ini, c_ini = encontrar_jasmine(labirinto, 0, 0, m, n)

    # qtds de caminhos
    total = contar_caminhos(labirinto, r_ini, c_ini, m, n, 0)

    # prints
    print(f"Existem {total} maneira(s) de sair do labirinto!")

    if total == 0:
        print("Pelo visto Jafar conseguiu tudo que ele sempre quis, Jasmine ficara calada para sempre, ouvi dizer que ele vai espandir o reino até Ababwa")
    elif total == 1:
        print("Ufa! Jasmine consegue escapar, mas agora precisam tirar Jafar do poder, é melhor pedirem ajuda ao gênio!")
    else:
        print("Ninguém me cala! Jasmine derruba Jafar sozinha sem a ajuda de ninguém.")
    return False


iniciar_fuga()
