# Índice do Presságio
def somar_alg(num):
    if num < 10:
        return num
    return (num % 10) + somar_alg(num // 10)


def calcular_total_ajustado(num):
    soma = somar_alg(num)

    if soma < 2:
        return 2
    return soma

# vr se algum resultado já foi calculado


def verificar_historico(cache, n, k, idx):  # idx = indec3
    if idx < 0:
        return -1

    if cache[idx][0] == n and cache[idx][1] == k:
        return cache[idx][2]
    return verificar_historico(cache, n, k, idx - 1)


# Evita que fique vários valores
def ajustar_tamanho_cache(cache):
    if len(cache) > 300:
        cache.pop(0)

# Fatorial Caótico


def fatorial_floresta(n, cache_fatorial):
    dado_armazenado = verificar_historico(
        cache_fatorial, n, 0, len(cache_fatorial) - 1)

    if dado_armazenado != -1:
        return dado_armazenado
    if n <= 1:
        retorno_calculado = 1
    elif n % 2 == 0:
        retorno_calculado = (
            n * fatorial_floresta(n // 2, cache_fatorial)) % 500
    else:
        retorno_calculado = (
            n + fatorial_floresta(n - 1, cache_fatorial)) % 500
    cache_fatorial.append([n, 0, retorno_calculado])
    ajustar_tamanho_cache(cache_fatorial)
    return retorno_calculado

# Fibonacci Generalizado


def fibonacci_magico(n, k, cache_fibonacci):
    dado_armazenado = verificar_historico(
        cache_fibonacci, n, k, len(cache_fibonacci) - 1)
    if dado_armazenado != -1:
        return dado_armazenado
    if n == 0:
        retorno_calculado = 0
    elif n < k:
        retorno_calculado = 1
    else:

        def somar_termos(i):
            if i > k:
                return 0
            return (fibonacci_magico(n - i, k, cache_fibonacci) + somar_termos(i + 1)) % 500
        retorno_calculado = somar_termos(1)
    cache_fibonacci.append([n, k, retorno_calculado])
    ajustar_tamanho_cache(cache_fibonacci)
    return retorno_calculado

# Primalidade


def verificar_primalidade(n, divisor=2):
    if n <= 1:
        return 0

    if divisor * divisor > n:
        return 1

    if n % divisor == 0:
        return 0
    return verificar_primalidade(n, divisor + 1)

# Formatar


def ajustar_digitos_texto(texto):
    if len(texto) >= 3:
        return texto
    return ajustar_digitos_texto("0" + texto)


def exibir_tres_casas(numero):
    return ajustar_digitos_texto(str(numero))


def analisar_elemento(n, cache_fatorial, cache_fibonacci):
    sinal_antigo = fatorial_floresta(n, cache_fatorial) % 500
    posicao_pressagio = calcular_total_ajustado(sinal_antigo)
    historico_passado = calcular_total_ajustado(posicao_pressagio)
    eco_luzes = fibonacci_magico(
        posicao_pressagio, historico_passado, cache_fibonacci) % 500
    total_julgamento = sinal_antigo + eco_luzes

    if verificar_primalidade(total_julgamento):
        resultado_final = "SEGURO"
    else:
        resultado_final = "PERIGOSO"

    # todos os prints
    print(f"Numero {exibir_tres_casas(n)} | "
          f"Sinal = {exibir_tres_casas(sinal_antigo)} | "
          f"Indice = {exibir_tres_casas(posicao_pressagio)} | "
          f"Memorias = {exibir_tres_casas(historico_passado)} | "
          f"Eco das Luzes = {exibir_tres_casas(eco_luzes)} | "
          f"Julgamento: {resultado_final}")


def mapear_elementos(lista, cache_fatorial, cache_fibonacci, posicao=0):
    if posicao >= len(lista):
        return

    analisar_elemento(lista[posicao], cache_fatorial, cache_fibonacci)
    mapear_elementos(lista, cache_fatorial, cache_fibonacci, posicao + 1)

# Converter entrada


def c_entrada(dados_brutos):
    texto_puro = dados_brutos.replace("[", "").replace("]", "")

    def criar_lista_valores(inicio=0):
        pos_virgula = texto_puro.find(",", inicio)
        if pos_virgula == -1:
            return [int(texto_puro[inicio:].strip())]
        atual = int(texto_puro[inicio:pos_virgula].strip())
        return [atual] + criar_lista_valores(pos_virgula + 1)
    return criar_lista_valores()


# input
fluxo_entrada = input()
lista_final = c_entrada(fluxo_entrada)
cache_fatorial = []
cache_fibonacci = []
mapear_elementos(lista_final, cache_fatorial, cache_fibonacci)
