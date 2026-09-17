matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0,]]


def fun_matriz(matriz):
    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] = int(input())
    return matriz


def fun_aux(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


def soma_colunas(matriz):
    for c in range(0, 3):
        coluna = []

        for l in range(0, 3):
            coluna.append(matriz[l][c])

        print(fun_aux(coluna))


matriz = fun_matriz(matriz)
soma_colunas(matriz)
