def buscar_pn(matriz, r, c, palavra, tentativas, n):
    # vr limites da matriz
    if r < 0 or r >= n or c < 0 or c >= n:
        return False

    celula_atual = matriz[r][c]
    # vr se é espinheiro ou se já passou por aqui
    if celula_atual == '0' or celula_atual == 'V':
        return False

    # Caso de Sucesso
    if celula_atual == '2':
        return True

    novas_tentativas = tentativas
    if celula_atual not in palavra:
        novas_tentativas -= 1

    if novas_tentativas < 0:
        return False

    # Backtracking
    valor_original = matriz[r][c]
    matriz[r][c] = 'V'

    # testar as 4 direções
    if (buscar_pn(matriz, r + 1, c, palavra, novas_tentativas, n) or
        buscar_pn(matriz, r - 1, c, palavra, novas_tentativas, n) or
        buscar_pn(matriz, r, c + 1, palavra, novas_tentativas, n) or
            buscar_pn(matriz, r, c - 1, palavra, novas_tentativas, n)):
        return True

    # testar outros caminhos
    matriz[r][c] = valor_original
    return False


def ler_matriz(n, contador):
    if contador == n:
        return []

    linha = input().split()
    return [linha] + ler_matriz(n, contador + 1)

# mensagens e inputs


def iniciar_programa():
    print("Eu te amo tanto agora quanto da primeira vez em que eu vi você...")

    linha_n = input()
    print("O mapa da floresta me parece esquisito, certo Pascal?")
    n = int(linha_n)

    palavra_chave = input()
    print("Minha querida Rapunzel, a palavra-chave é?")

    coords = input().split()
    print("Vamos por aqui, esse deve ser o local certo para se descer!")
    r_ini = int(coords[0])
    c_ini = int(coords[1])

    print("Segundo o mapa essas são as informações da floresta:")
    matriz = ler_matriz(n, 0)

    tentativas_max = int(input())
    print("Eu não tenho todo o tempo do mundo!")

    resultado = buscar_pn(matriz, r_ini, c_ini,
                          palavra_chave, tentativas_max, n)

    if resultado:
        print("A CAÇADA TERMINOU! O SOL BRILHA NO HORIZONTE E O PIQUE-NIQUE REAL ESTÁ SERVIDO! JOSÉ FINALMENTE PODE DESCANSAR ENQUANTO PASCAL VIGIA A TORTA DE MAÇÃ.")
    else:
        print("O SOL SE PÔS NO REINO DE CORONA E AS ÚLTIMAS LANTERNAS SE APAGARAM. JOSÉ BEZERRA VAGOU POR HORAS, MAS O DESTINO FOI CRUEL: ELE NÃO CHEGOU AO PIQUE-NIQUE. ENQUANTO O CAVALO MAXIMUS SE DELICIA COM A ÚLTIMA FATIA DE TORTA DE MAÇÃ, JOSÉ TERÁ QUE SE CONTENTAR EM DIVIDIR UMA FRUTA SILVESTRE AZEDA COM O PASCAL. A CAÇADA FOI UM FRACASSO E A FOME VENCEU DESTA VEZ.")
    return False


iniciar_programa()
