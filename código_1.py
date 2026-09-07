numero_secao = int(input())

# verificação de seção  --- lembrando que numero tem que ser maio que 9
if numero_secao < 9:
    print("Essa seção foi excluída por motivos que não podem ser revelados. Entre no labirinto e corra novamente.")
else:
    primos = []  # lista de todos os primos

    # vr de numeros primos
    for k in range(2, numero_secao + 1):
        for num in range(k + 1, 2*k):
            primo = True

            if num < 2:
                primo = False
            else:
                for i in range(2, num):
                    if num % i == 0:
                        primo = False

            if primo:
                primos.append(num)

        # bubble sort na ordem decrescente
    for i in range(len(primos)):
        for j in range(len(primos)-1):
            if primos[j] < primos[j + 1]:
                t = primos[j]
                primos[j] = primos[j + 1]
                primos[j + 1] = t

    # mostrar lista dos numeros primos

    lista_primos_unico = []  # lista de primos que apararecem somente uma vez

    for p in primos:
        if p not in lista_primos_unico:
            lista_primos_unico.append(p)

    lista_primos_unico.sort(reverse=True)

    for i in range(len(lista_primos_unico)):
      if i == len(lista_primos_unico) - 1:
        print(lista_primos_unico[i], end="")
      else:
        print(lista_primos_unico[i], end=" ")  # printar todos os numeros em uma única linha
    print()
    
    lista_primos_unico.sort()
    for num in lista_primos_unico:
        qtd_vezes = primos.count(num)
        print(f"O número {num} apareceu {qtd_vezes} vezes.")

    # cálculo do resultado final
    maior_numero = primos[0]
    resultado_final = (maior_numero + 1) // 2
    print()

    # prints finais
    if resultado_final == numero_secao:
        print(
            "Thomas: O cálculo apontou para a seção que você estava! Isso é uma armadilha.")
        print("Minho: O Thomas tem razão.")

    elif numero_secao - resultado_final == 1:
        print("Thomas: A decodificação diz que a saída está na seção imediatamente anterior a que você estava.")
        print("Minho: Se isso realmente for válido, então restam 2 opções de saída.")

    elif numero_secao - resultado_final > 1:
        print("De todos os cálculos feitos, a única seção que apresentou diferença maior do que 1 foi essa.")
