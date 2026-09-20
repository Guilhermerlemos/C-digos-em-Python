# maquina 1 ============================================================================================================
nome_maquina1 = input()
qtd_pecas1 = int(input())
reacao_candace1 = input()

reacao_candace1 = reacao_candace1.upper()
# conta de caracteres
qtd_caracteres1 = len(nome_maquina1)
# soma de pontos
pts_maq1 = (qtd_pecas1 + qtd_caracteres1)
# vr de nome inator
if (
    'i' in nome_maquina1
    and 'n' in nome_maquina1
    and 'a' in nome_maquina1
    and 't' in nome_maquina1
    and 'o' in nome_maquina1
    and 'r' in nome_maquina1
):
    pts_maq1 = (pts_maq1 - 50)
# vr de nome perry
if (
    'P' in nome_maquina1
    and 'e' in nome_maquina1
    and 'r' in nome_maquina1
    and 'y' in nome_maquina1
):
    pts_maq1 = (pts_maq1 + 20)

# reação de candace =====================================================================================================
    # ganha pts
if reacao_candace1 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pts_maq1 = (pts_maq1 + 30)
if reacao_candace1 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pts_maq1 = (pts_maq1 + 20)
if reacao_candace1 == 'OK... ISSO É BEM ESTRANHO.':
    pts_maq1 = (pts_maq1 + 10)
if reacao_candace1 == 'AH, NEM É TÃO IMPRESSIONANTE ASSIM.':
    pts_maq1 = (pts_maq1 + 0)
    # perde pts
if reacao_candace1 == 'SÉRIO? SÓ ISSO?':
    pts_maq1 = (pts_maq1 - 5)
if reacao_candace1 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pts_maq1 = (pts_maq1 - 10)
if reacao_candace1 == 'AH, ESQUECE…':
    pts_maq1 = (pts_maq1 - 15)

# preferencias ===========================================================================================
if nome_maquina1 == 'HidromassagemAutomáticaDoPerry':
    pts_maq1 = (pts_maq1 * 2)

if nome_maquina1 == 'MáquinaDeBanhoForçado':
    pts_maq1 = (pts_maq1 - 20)

# maquina 2 ============================================================================================================
nome_maquina2 = input()
qtd_pecas2 = int(input())
reacao_candace2 = input()

reacao_candace2 = reacao_candace2.upper()
# conta de caracteres
qtd_caracteres2 = len(nome_maquina2)
# soma de pontos
pts_maq2 = (qtd_pecas2 + qtd_caracteres2)
# vr de nome inator
if (
    'i' in nome_maquina2
    and 'n' in nome_maquina2
    and 'a' in nome_maquina2
    and 't' in nome_maquina2
    and 'o' in nome_maquina2
    and 'r' in nome_maquina2
):
    pts_maq2 = (pts_maq2 - 50)
# vr de nome perry
if (
    'P' in nome_maquina2
    and 'e' in nome_maquina2
    and 'r' in nome_maquina2
    and 'y' in nome_maquina2
):
    pts_maq2 = (pts_maq2 + 20)

# reação de candace ===============================================================================================
    # ganha pts
if reacao_candace2 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pts_maq2 = (pts_maq2 + 30)
if reacao_candace2 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pts_maq2 = (pts_maq2 + 20)
if reacao_candace2 == 'OK... ISSO É BEM ESTRANHO.':
    pts_maq2 = (pts_maq2 + 10)
if reacao_candace2 == 'AH, NEM É TÃO IMPRESSIONANTE ASSIM.':
    pts_maq2 = (pts_maq2 + 0)
    # perde pts
if reacao_candace2 == 'SÉRIO? SÓ ISSO?':
    pts_maq2 = (pts_maq2 - 5)
if reacao_candace2 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pts_maq2 = (pts_maq2 - 10)
if reacao_candace2 == 'AH, ESQUECE…':
    pts_maq2 = (pts_maq2 - 15)

# preferencias =======================================================================================
if nome_maquina2 == 'HidromassagemAutomáticaDoPerry':
    pts_maq2 = (pts_maq2 * 2)

if nome_maquina2 == 'áquinaDeBanhoForçado':
    pts_maq2 = (pts_maq2 - 20)

# maquina 3 ============================================================================================================
nome_maquina3 = input()
qtd_pecas3 = int(input())
reacao_candace3 = input()

reacao_candace3 = reacao_candace3.upper()
# conta de caracteres
qtd_caracteres3 = len(nome_maquina3)
# soma de pontos
pts_maq3 = (qtd_pecas3 + qtd_caracteres3)
# vr de nome inator
if (
    'i' in nome_maquina3
    and 'n' in nome_maquina3
    and 'a' in nome_maquina3
    and 't' in nome_maquina3
    and 'o' in nome_maquina3
    and 'r' in nome_maquina3
):
    pts_maq3 = (pts_maq3 - 50)
# vr de nome perry
if (
    'P' in nome_maquina3
    and 'e' in nome_maquina3
    and 'r' in nome_maquina3
    and 'y' in nome_maquina3
):
    pts_maq3 = (pts_maq3 + 20)

# reação de candace ===========================================================================================
    # ganha pts
if reacao_candace3 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pts_maq3 = (pts_maq3 + 30)
if reacao_candace3 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pts_maq3 = (pts_maq3 + 20)
if reacao_candace3 == 'OK... ISSO É BEM ESTRANHO.':
    pts_maq3 = (pts_maq3 + 10)
if reacao_candace3 == 'AH, NEM É TÃO IMPRESSIONANTE ASSIM.':
    pts_maq3 = (pts_maq3 + 0)
    # perde pts
if reacao_candace3 == 'SÉRIO? SÓ ISSO?':
    pts_maq3 = (pts_maq3 - 5)
if reacao_candace3 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pts_maq3 = (pts_maq3 - 10)
if reacao_candace3 == 'AH, ESQUECE…':
    pts_maq3 = (pts_maq3 - 15)

# preferencias ====================================================================
if nome_maquina3 == 'HidromassagemAutomáticaDoPerry':
    pts_maq3 = (pts_maq3 * 2)

if nome_maquina3 == 'MáquinaDeBanhoForçado':
    pts_maq3 = (pts_maq3 - 20)

# Maquina 4 ============================================================================================================
nome_maquina4 = input()
qtd_pecas4 = int(input())
reacao_candace4 = input()

reacao_candace4 = reacao_candace4.upper()
# conta de caracteres
qtd_caracteres4 = len(nome_maquina4)
# soma de pontos
pts_maq4 = (qtd_pecas4 + qtd_caracteres4)
# vr de nome inator
if (
    'i' in nome_maquina4
    and 'n' in nome_maquina4
    and 'a' in nome_maquina4
    and 't' in nome_maquina4
    and 'r' in nome_maquina4
):
    pts_maq4 = (pts_maq4 - 50)
# vr de nome perry
if (
    'P' in nome_maquina4
    and 'e' in nome_maquina4
    and 'r' in nome_maquina4
    and 'y' in nome_maquina4
):
    pts_maq4 = (pts_maq4 + 20)

# reação de candace =================================================================================================
    # ganha pts
if reacao_candace4 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pts_maq4 = (pts_maq4 + 30)
if reacao_candace4 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pts_maq4 = (pts_maq4 + 20)
if reacao_candace4 == 'OK... ISSO É BEM ESTRANHO.':
    pts_maq4 = (pts_maq4 + 10)
if reacao_candace4 == 'AH, NEM É TÃO IMPRESSIONANTE ASSIM.':
    pts_maq4 = (pts_maq4 + 0)
    # perde pts
if reacao_candace4 == 'SÉRIO? SÓ ISSO?':
    pts_maq4 = (pts_maq4 - 5)
if reacao_candace4 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pts_maq4 = (pts_maq4 - 10)
if reacao_candace4 == 'AH, ESQUECE…':
    pts_maq4 = (pts_maq4 - 15)

# preferencias =================================================================================
if nome_maquina4 == 'HidromassagemAutomáticaDoPerry':
    pts_maq4 = (pts_maq4 * 2)

if nome_maquina4 == 'MáquinaDeBanhoForçado':
    pts_maq4 = (pts_maq4 - 20)

# desempate ===========================================================================================================
parametro1 = 0
parametro2 = 0
parametro3 = 0
parametro4 = 0

# maq 1 vs maq 2 ==========================================================================
if pts_maq1 == pts_maq2:
    if qtd_pecas1 > 25:
        parametro1 = (parametro1 + 1)
    if qtd_caracteres1 > 15:
        parametro1 = (parametro1 + 1)
    if qtd_pecas2 > 25:
        parametro2 = (parametro2 + 1)
    if qtd_caracteres2 > 15:
        parametro2 = (parametro2 + 1)

    if parametro1 < parametro2:
        pts_maq1, pts_maq2 = pts_maq2, pts_maq1
        nome_maquina1, nome_maquina2 = nome_maquina2, nome_maquina1
        parametro1, parametro2 = parametro2, parametro1
        qtd_caracteres1, qtd_caracteres2 = qtd_caracteres2, qtd_caracteres1
        qtd_pecas1, qtd_pecas2 = qtd_pecas2, qtd_pecas1

    elif parametro1 == parametro2:
        if qtd_pecas1 < qtd_pecas2:
            pts_maq1, pts_maq2 = pts_maq2, pts_maq1
            nome_maquina1, nome_maquina2 = nome_maquina2, nome_maquina1
            parametro1, parametro2 = parametro2, parametro1
            qtd_caracteres1, qtd_caracteres2 = qtd_caracteres2, qtd_caracteres1
            qtd_pecas1, qtd_pecas2 = qtd_pecas2, qtd_pecas1

        elif qtd_pecas1 == qtd_pecas2:
            if qtd_caracteres1 < qtd_caracteres2:
                pts_maq1, pts_maq2 = pts_maq2, pts_maq1
                nome_maquina1, nome_maquina2 = nome_maquina2, nome_maquina1
                parametro1, parametro2 = parametro2, parametro1
                qtd_caracteres1, qtd_caracteres2 = qtd_caracteres2, qtd_caracteres1
                qtd_pecas1, qtd_pecas2 = qtd_pecas2, qtd_pecas1

# maq 1 vs maq 4 =================================================================================
if pts_maq1 == pts_maq4:
    if qtd_pecas1 > 25:
        parametro1 = (parametro1 + 1)
    if qtd_caracteres1 > 15:
        parametro1 = (parametro1 + 1)
    if qtd_pecas4 > 25:
        parametro4 = (parametro4 + 1)
    if qtd_caracteres4 > 15:
        parametro4 = (parametro4 + 1)

    if parametro1 < parametro4:
        pts_maq1, pts_maq4 = pts_maq4, pts_maq1
        nome_maquina1, nome_maquina4 = nome_maquina4, nome_maquina1
        parametro1, parametro4 = parametro4, parametro1
        qtd_caracteres1, qtd_caracteres4 = qtd_caracteres4, qtd_caracteres1
        qtd_pecas1, qtd_pecas4 = qtd_pecas4, qtd_pecas1

    elif parametro1 == parametro4:
        if qtd_pecas1 < qtd_pecas4:
            pts_maq1, pts_maq4 = pts_maq4, pts_maq1
            nome_maquina1, nome_maquina4 = nome_maquina4, nome_maquina1
            parametro1, parametro4 = parametro4, parametro1
            qtd_caracteres1, qtd_caracteres4 = qtd_caracteres4, qtd_caracteres1
            qtd_pecas1, qtd_pecas4 = qtd_pecas4, qtd_pecas1

        elif qtd_pecas1 == qtd_pecas4:
            if qtd_caracteres1 < qtd_caracteres4:
                pts_maq1, pts_maq4 = pts_maq4, pts_maq1
                nome_maquina1, nome_maquina4 = nome_maquina4, nome_maquina1
                parametro1, parametro4 = parametro4, parametro1
                qtd_caracteres1, qtd_caracteres4 = qtd_caracteres4, qtd_caracteres1
                qtd_pecas1, qtd_pecas4 = qtd_pecas4, qtd_pecas1

# maq 1 vs maq 3 ==================================================================================
if pts_maq1 == pts_maq3:
    if qtd_pecas1 > 25:
        parametro1 = (parametro1 + 1)
    if qtd_caracteres1 > 15:
        parametro1 = (parametro1 + 1)
    if qtd_pecas3 > 25:
        parametro3 = (parametro3 + 1)
    if qtd_caracteres3 > 15:
        parametro3 = (parametro3 + 1)

    if parametro1 < parametro3:
        pts_maq1, pts_maq3 = pts_maq3, pts_maq1
        nome_maquina1, nome_maquina3 = nome_maquina3, nome_maquina1
        parametro1, parametro3 = parametro3, parametro1
        qtd_caracteres1, qtd_caracteres3 = qtd_caracteres3, qtd_caracteres1
        qtd_pecas1, qtd_pecas3 = qtd_pecas3, qtd_pecas1

    elif parametro1 == parametro3:
        if qtd_pecas1 < qtd_pecas3:
            pts_maq1, pts_maq3 = pts_maq3, pts_maq1
            nome_maquina1, nome_maquina3 = nome_maquina3, nome_maquina1
            parametro1, parametro3 = parametro3, parametro1
            qtd_caracteres1, qtd_caracteres3 = qtd_caracteres3, qtd_caracteres1
            qtd_pecas1, qtd_pecas3 = qtd_pecas3, qtd_pecas1

        elif qtd_pecas1 == qtd_pecas3:
            if qtd_caracteres1 < qtd_caracteres3:
                pts_maq1, pts_maq3 = pts_maq3, pts_maq1
                nome_maquina1, nome_maquina3 = nome_maquina3, nome_maquina1
                parametro1, parametro3 = parametro3, parametro1
                qtd_caracteres1, qtd_caracteres3 = qtd_caracteres3, qtd_caracteres1
                qtd_pecas1, qtd_pecas3 = qtd_pecas3, qtd_pecas1

# maq 3 vs maq 4 ==================================================================================
if pts_maq3 == pts_maq4:
    if qtd_pecas3 > 25:
        parametro3 = (parametro3 + 1)
    if qtd_caracteres3 > 15:
        parametro3 = (parametro3 + 1)
    if qtd_pecas4 > 25:
        parametro4 = (parametro4 + 1)
    if qtd_caracteres4 > 15:
        parametro4 = (parametro4 + 1)

    if parametro3 < parametro4:
        pts_maq3, pts_maq4 = pts_maq4, pts_maq3
        nome_maquina3, nome_maquina4 = nome_maquina4, nome_maquina3
        parametro3, parametro4 = parametro4, parametro3
        qtd_caracteres3, qtd_caracteres4 = qtd_caracteres4, qtd_caracteres3
        qtd_pecas3, qtd_pecas4 = qtd_pecas4, qtd_pecas3

    elif parametro3 == parametro4:
        if qtd_pecas3 < qtd_pecas4:
            pts_maq3, pts_maq4 = pts_maq4, pts_maq3
            nome_maquina3, nome_maquina4 = nome_maquina4, nome_maquina3
            parametro3, parametro4 = parametro4, parametro3
            qtd_caracteres3, qtd_caracteres4 = qtd_caracteres4, qtd_caracteres3
            qtd_pecas3, qtd_pecas4 = qtd_pecas4, qtd_pecas3

        elif qtd_pecas3 == qtd_pecas4:
            if qtd_caracteres3 < qtd_caracteres4:
                pts_maq3, pts_maq4 = pts_maq4, pts_maq3
                nome_maquina3, nome_maquina4 = nome_maquina4, nome_maquina3
                parametro3, parametro4 = parametro4, parametro3
                qtd_caracteres3, qtd_caracteres4 = qtd_caracteres4, qtd_caracteres3
                qtd_pecas3, qtd_pecas4 = qtd_pecas4, qtd_pecas3

# maq 2 vs maq 4 ==================================================================================
if pts_maq2 == pts_maq4:
    if qtd_pecas2 > 25:
        parametro2 = (parametro2 + 1)
    if qtd_caracteres2 > 15:
        parametro2 = (parametro2 + 1)
    if qtd_pecas4 > 25:
        parametro4 = (parametro4 + 1)
    if qtd_caracteres4 > 15:
        parametro4 = (parametro4 + 1)

    if parametro2 < parametro4:
        pts_maq2, pts_maq4 = pts_maq4, pts_maq2
        nome_maquina2, nome_maquina4 = nome_maquina4, nome_maquina2
        parametro2, parametro4 = parametro4, parametro2
        qtd_caracteres2, qtd_caracteres4 = qtd_caracteres4, qtd_caracteres2
        qtd_pecas2, qtd_pecas4 = qtd_pecas4, qtd_pecas2

    elif parametro2 == parametro4:
        if qtd_pecas2 < qtd_pecas4:
            pts_maq2, pts_maq4 = pts_maq4, pts_maq2
            nome_maquina2, nome_maquina4 = nome_maquina4, nome_maquina2
            parametro2, parametro4 = parametro4, parametro2
            qtd_caracteres2, qtd_caracteres4 = qtd_caracteres4, qtd_caracteres2
            qtd_pecas2, qtd_pecas4 = qtd_pecas4, qtd_pecas2

        elif qtd_pecas2 == qtd_pecas4:
            if qtd_caracteres2 < qtd_caracteres4:
                pts_maq2, pts_maq4 = pts_maq4, pts_maq2
                nome_maquina2, nome_maquina4 = nome_maquina4, nome_maquina2
                parametro1, parametro2 = parametro2, parametro1
                qtd_caracteres2, qtd_caracteres4 = qtd_caracteres4, qtd_caracteres2
                qtd_pecas2, qtd_pecas4 = qtd_pecas4, qtd_pecas2


# maq 2 vs maq 3 ==================================================================================
if pts_maq2 == pts_maq3:
    if qtd_pecas2 > 25:
        parametro2 = (parametro2 + 1)
    if qtd_caracteres2 > 15:
        parametro2 = (parametro2 + 1)
    if qtd_pecas3 > 25:
        parametro3 = (parametro3 + 1)
    if qtd_caracteres3 > 15:
        parametro3 = (parametro3 + 1)

    if parametro2 < parametro3:
        pts_maq2, pts_maq3 = pts_maq3, pts_maq2
        nome_maquina2, nome_maquina3 = nome_maquina3, nome_maquina2
        parametro2, parametro3 = parametro3, parametro2
        qtd_caracteres2, qtd_caracteres3 = qtd_caracteres3, qtd_caracteres2
        qtd_pecas2, qtd_pecas3 = qtd_pecas3, qtd_pecas2

    elif parametro2 == parametro3:
        if qtd_pecas2 < qtd_pecas3:
            pts_maq2, pts_maq3 = pts_maq3, pts_maq2
            nome_maquina2, nome_maquina3 = nome_maquina3, nome_maquina2
            parametro2, parametro3 = parametro3, parametro2
            qtd_caracteres2, qtd_caracteres3 = qtd_caracteres3, qtd_caracteres2
            qtd_pecas2, qtd_pecas3 = qtd_pecas3, qtd_pecas2

        elif qtd_pecas2 == qtd_pecas3:
            if qtd_caracteres2 < qtd_caracteres3:
                pts_maq2, pts_maq3 = pts_maq3, pts_maq2
                nome_maquina2, nome_maquina3 = nome_maquina3, nome_maquina2
                parametro2, parametro3 = parametro3, parametro2
                qtd_caracteres2, qtd_caracteres3 = qtd_caracteres3, qtd_caracteres2
                qtd_pecas2, qtd_pecas3 = qtd_pecas3, qtd_pecas2

# tabele de ranking ====================================================================================================
if pts_maq1 < pts_maq2:
    pts_maq1, pts_maq2 = pts_maq2, pts_maq1
    nome_maquina1, nome_maquina2 = nome_maquina2, nome_maquina1

if pts_maq3 < pts_maq4:
    pts_maq3, pts_maq4 = pts_maq4, pts_maq3
    nome_maquina3, nome_maquina4 = nome_maquina4, nome_maquina3

if pts_maq1 < pts_maq3:
    pts_maq1, pts_maq3 = pts_maq3, pts_maq1
    nome_maquina1, nome_maquina3 = nome_maquina3, nome_maquina1

if pts_maq2 < pts_maq4:
    pts_maq2, pts_maq4 = pts_maq4, pts_maq2
    nome_maquina2, nome_maquina4 = nome_maquina4, nome_maquina2

if pts_maq2 < pts_maq3:
    pts_maq2, pts_maq3 = pts_maq3, pts_maq2
    nome_maquina2, nome_maquina3 = nome_maquina3, nome_maquina2

# prints da tabela ===============================================================================================================================

print(f"1º lugar - {nome_maquina1} : {pts_maq1} pontos")
print(f"2º lugar - {nome_maquina2} : {pts_maq2} pontos")
print(f"3º lugar - {nome_maquina3} : {pts_maq3} pontos")
print(f"4º lugar - {nome_maquina4} : {pts_maq4} pontos")
