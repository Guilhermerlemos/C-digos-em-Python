# quantidade de cidades
qtd_cidades = int(input())

print("Pega a sua trouxa, moleque. O ônibus pro sertão já vai sair.")
print(
    f"Se ajeita nesse banco, menino, que o chacoalho vai ser grande. A gente tem {qtd_cidades} cidade(s) de poeira pela frente até achar o tal do teu pai. Presta atenção no que o povo fala...")
familia_encontrada = False

# loop das cidades
for cidade in range(1, qtd_cidades + 1):
    if familia_encontrada == False:

        print(
            f"Atenção, {cidade}ª cidade! Carta de graça! A gente só quer informação da minha família em troca!")

        # variavel de cidades
        estrutura = ""
        identidade_aberta = ""
        endereco_aberto = ""

        tem_identidade = False
        tem_endereco = False
        tem_lembranca = False

        aberto_identidade = False
        aberto_endereco = False
        aberto_lembranca = False

        # vr, se cidade tem informação
        informacao = input()

        if informacao == "FIM":
            print("Ô cidadezinha morta, Josué. Ninguém abriu a boca pra dar um pio do teu pai. Dobra essa mesa que aqui a gente só gastou saliva à toa.")

        else:

            while informacao != "FIM":
                texto = informacao.lower()

                # tipo de endereco
                if "sertao" in texto or "bom jesus" in texto:

                    tem_endereco = True
                    palavra = ""

                    if "sertao" in texto:
                        palavra = "sertao"
                    elif "bom jesus" in texto:
                        palavra = "bom jesus"

                    if aberto_endereco == False:
                        estrutura = estrutura + "{"
                        aberto_endereco = True
                        endereco_aberto = palavra

                    elif endereco_aberto == palavra:
                        estrutura = estrutura + "}"
                        aberto_endereco = False

                    else:
                        estrutura = estrutura + "{"
                        endereco_aberto = palavra
                        aberto_endereco = True

                # tipo de identidade
                elif "jesus" in texto or "isaias" in texto or "moises" in texto:

                    tem_identidade = True
                    palavra = ""

                    if "jesus" in texto:
                        palavra = "jesus"
                    elif "isaias" in texto:
                        palavra = "isaias"
                    elif "moises" in texto:
                        palavra = "moises"

                    if aberto_identidade == False:
                        estrutura = estrutura + "("
                        aberto_identidade = True
                        identidade_aberta = palavra

                    elif identidade_aberta == palavra:
                        estrutura = estrutura + ")"
                        aberto_identidade = False

                    else:
                        estrutura = estrutura + "("
                        identidade_aberta = palavra
                        aberto_identidade = True

                else:
                    tem_lembranca = True

                    if aberto_lembranca == False:
                        estrutura = estrutura + "["
                        aberto_lembranca = True

                    else:
                        estrutura = estrutura + "]"
                        aberto_lembranca = False

                informacao = input()

# fim de loopp
# ===========================================================================================================================
# delimitadores
            pilha = ""
            valido = True

            for caractere in estrutura:

                if caractere == "(" or caractere == "{" or caractere == "[":
                    pilha = pilha + caractere
                else:
                    if pilha == "":
                        valido = False

                    else:
                        topo = pilha[-1:]
                        if caractere == ")" and topo == "(":
                            pilha = pilha[:-1]
                        elif caractere == "}" and topo == "{":
                            pilha = pilha[:-1]
                        elif caractere == "]" and topo == "[":
                            pilha = pilha[:-1]
                        else:
                            valido = False

            if pilha != "":
                valido = False

            if valido and tem_identidade and tem_endereco and tem_lembranca:
                familia_encontrada = True

                print(
                    "A história bateu, Josué. O povo falou a mesma coisa. Pega tuas coisas que a gente achou o caminho do teu pai.")
                print("------------------------------------------------------------")
                print(
                    "✅ Pistas confirmadas. Josué encontrou os irmãos e uma carta de seu pai.")
                print(
                    "A missão de Dora terminou. Pela janela do ônibus, ela escreve para o menino que deixou para trás:")
                print("✉️ Dora: 'Você tem razão. Seu pai ainda vai aparecer e, com certeza, ele é tudo aquilo que você diz que ele é.'")
                print("✉️ Dora: 'Quando você estiver cruzando as estradas no seu caminhão enorme, espero que você lembre que fui eu a primeira pessoa a te fazer botar a mão no volante.'")
                print("✉️ Dora: 'No dia que você quiser lembrar de mim, dá uma olhada no retratinho que a gente tirou junto... Tenho medo que um dia você também me esqueça. Tenho saudade de tudo.'")
            else:
                if cidade != qtd_cidades and familia_encontrada == False:
                    print(
                        "Essa conversa tá toda torta, um fala uma coisa, outro fala outra. Vamos embora, menino, a busca continua.")

# caso não encontre sua família
if familia_encontrada == False:
    print("Não achamos eles nessas cidades, Dona Dora... Mas amanhã a gente bota a mesinha de novo, né? O Brasil é grande, uma hora a gente encontra.")
