moedas_total = 0
moedas_dia = 0

print("Ô promessa sem jeito…")
print()
# primeira fase
for dia in range(1, 8):
    print(f"Dia {dia}: Quantas moedas João Grilo conseguiu arrecadar hoje?")
    moedas_dia = int(input())
    moedas_total = moedas_total + moedas_dia
    print(f"No dia {dia}, o baú já tem R$ {moedas_total}")
print()
print(f"Total arrecadado após o plano: R$ {moedas_total}")
print()

# nao tiver moedas
if moedas_total == 0:
    print("João Grilo não conseguiu arrecadar nada... direto para o plano B!!")

    print()
    print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
    qtddesculpas = int(input())
    print()

    for i in range(1, qtddesculpas + 1):
        print(f"Digite a {i}ª desculpa:")
        desculpas = input()

        print(
            f"João Grilo disse: '{desculpas}'... e o padeiro caiu na conversa!")
    print("Chicó: 'Não sei, só sei que foi assim!'")

# se tiver moedas
else:

    print("João Grilo começa a despedida da cachorra:")
    print("'Canis Mortus, Dinherus no Bolsus'")
    print("'Caro nostra quae in patina eius est, canis.'")
    print()

    print("João Grilo, o padeiro acreditou?")
    sinal = input()

    if sinal.lower() == 'sim':
        print("O padeiro acreditou! Chicó pode se casar com Rosinha!")
        print("Como o padeiro acreditou?")
        print("Chicó: 'Não sei, só sei que foi assim!'")

    # plano B
    else:
        print("O padeiro não acreditou... João Grilo parte para o Plano B!")

        print()
        print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
        qtddesculpas = int(input())
        print()

        for i in range(1, qtddesculpas + 1):
            print(f"Digite a {i}ª desculpa:")
            desculpas = input()

            print(
                f"João Grilo disse: '{desculpas}'... e o padeiro caiu na conversa!")
        print("Chicó: 'Não sei, só sei que foi assim!'")
