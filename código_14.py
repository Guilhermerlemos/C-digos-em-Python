qtd_pendrive = int(input())

print("Avenida Brasil: A Vingança de Nina!")
pendrive_abertos = 0

# vr qtd de pendrives e pedido de senha secreta
for i in range(1, qtd_pendrive + 1):
    letras = 0
    estado = ""
    print(f"Descriptografando pendrive {i} de {qtd_pendrive}...")
    senha_secreta = str(input())

    # contando as letras
    for letra in senha_secreta:
        if letra != " ":
            letras += 1

    tentativas = (letras * 2)

    # vr de espaços
    for letra in senha_secreta:
        if letra == " ":
            estado += " "
        else:
            estado += "_"

    # todas as letras que foram chutadas pelo usuáriooo
    letras_de_chute = ''

    # vr se existe ou nnão as letras na senha / vr se a letra já foi chutada
    while tentativas > 0 and "_" in estado:
        chutes = input()
        if chutes in letras_de_chute:
            print("Max: Ele já tentou isso, Carminha...")
        else:
            letras_de_chute += chutes

            if chutes in senha_secreta:
                print("Nina: Boa, Tufão! Menos uma mentira da Carminha.")

                # como estar a situação das senha após os chutes
                novo_estado = ""

                # fazendo a letra apararecer nas suas posições
                for letra_senha, letra_estado in zip(senha_secreta, estado):
                    if letra_senha == chutes:
                        novo_estado += chutes
                    else:
                        novo_estado += letra_estado
                estado = novo_estado
            else:
                print("Carminha: Você é um idiota, Tufão! Isso não faz sentido.")

        tentativas = tentativas - 1

        print(f"Senha: {estado}")

# caso a senha estiver completa sem traços
    if "_" not in estado:
        print(
            f"Tufão: Agora eu sei de toda a verdade! O pendrive {i} está aberto.")
        pendrive_abertos = pendrive_abertos + 1

    else:
        print(
            f"Carminha: Consegui! As fotos do pendrive {i} estão a salvo comigo.")

print(f"Conseguimos abrir {pendrive_abertos} de {qtd_pendrive} pendrives!")

# calculo da taxa de acertos

t = (pendrive_abertos / qtd_pendrive)*100

if t == 0:
    print("Tufão continuará sendo enganado para sempre...")

elif t > 0 and t <= 50:
    print("Tufão descobriu algumas coisas, mas Carminha ainda tem poder.")

elif t > 50 and t < 100:
    print("A casa caiu para a Carminha! Quase todas as provas foram recuperadas.")

elif t == 100:
    print("Justiça por Rita! Todas as provas estão nas mãos de Tufão.")
