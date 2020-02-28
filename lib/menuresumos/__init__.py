from lib.interface import *
import locale


def resumomes(listatrans, mestrabalho, anotrabalho, listacontas, listacontasprevisto):
    system("cls")
    listaresumo = []
    listacontasord = sorted(listacontas, key=lambda i: i['nome'])
    for x in listacontasord:
        listaresumo.append(x['nome'])
        listaresumo.append(float(0))
        vlrprevtemp = list(filter(lambda conta: (conta['nome'] == x['nome'] and conta['mes'] == mestrabalho and
                                                 conta['ano'] == anotrabalho), listacontasprevisto))
        if len(vlrprevtemp) > 0:
            vlrprev = vlrprevtemp[0]['valorprevisto']
        else:
            vlrprev = 0
        listaresumo.append(vlrprev)
    for x in listatrans:
        if mestrabalho == x['mes'] and anotrabalho == x['ano']:
            pos = listaresumo.index(x['conta'])
            listaresumo[pos+1] += x['valor']
    cabecalho('RESUMO DO MES POR CONTA', 63)
    totrecreal = 0
    totrecprev = 0
    totrecdelta = 0
    tipoconta = ''
    gastoreal = 0
    cabecalho('RECEITAS', 63)
    print(f'{espacos()}{"CONTA":<30} {"REALIZADO":>10} {"PREVISTO":>10} {"DELTA":>10}')
    for c, x in enumerate(listaresumo):
        if c % 3 == 0 or c == 0:
            tipoconta = list(filter(lambda conta: conta["nome"] == x, listacontas))[0]["tipo"]
            if tipoconta == 'R':
                print(f'{espacos()}{x:<30} ', end="")
        elif (c-1) % 3 == 0 or (c-1) == 0:
            if tipoconta == 'R':
                gastoreal = x
                print(f'{x:>10,.2f} ', end="")
                totrecreal += x
        else:
            if tipoconta == 'R':
                gastoprev = x
                totrecprev += x
                vlrdelta = gastoreal - gastoprev
                totrecdelta += vlrdelta
                print(f'{gastoprev:>10,.2f} {vlrdelta:>10,.2f}')
    print(linha(63))
    print(f'{espacos()}{"TOTAL RECEITAS:":<30} {totrecreal:>10,.2f} {totrecprev:>10,.2f} {totrecdelta:>10,.2f}')
    aguardaenter()

    totdesreal = 0
    totdesprev = 0
    totdesdelta = 0
    totalemprestimos = 0
    cabecalho('DESPESAS', 63)
    print(f'{espacos()}{"CONTA":<30} {"REALIZADO":>10} {"PREVISTO":>10} {"DELTA":>10}')
    for c, x in enumerate(listaresumo):
        if c % 3 == 0 or c == 0:
            tipoconta = list(filter(lambda conta: conta["nome"] == x, listacontas))[0]["tipo"]
            if tipoconta in ('D', 'E'):
                print(f'{espacos()}{x:<30} ', end="")
        elif (c-1) % 3 == 0 or (c-1) == 0:
            if tipoconta in ('D', 'E'):
                gastoreal = x
                print(f'{x:>10,.2f} ', end="")
                if tipoconta == 'D':
                    totdesreal += x
                elif tipoconta == 'E':
                    totalemprestimos += x
        else:
            if tipoconta in ('D', 'E'):
                gastoprev = x
                totdesprev += x
                vlrdelta = gastoreal - gastoprev
                totdesdelta += vlrdelta
                print(f'{gastoprev:>10,.2f} {vlrdelta:>10,.2f}')
    print(linha(63))
    print(f'{espacos()}{"TOTAL RECEITAS:":<30} {totrecreal:>10,.2f} {totrecprev:>10,.2f} {totrecdelta:>10,.2f}')
    print(f'{espacos()}{"TOTAL DESPESAS:":<30} {totdesreal:>10,.2f} {totdesprev:>10,.2f} {totdesdelta:>10,.2f}')
    print(linha(63))
    print(f'{espacos()}{"DELTA TOTAL:":<30} {(totrecreal+totdesreal):>10,.2f} {(totrecprev+totdesprev):>10,.2f}'
          f' {(totrecdelta+totdesdelta):>10,.2f}')
    print(linha(63))
    print(f'{espacos()}TOTAL EMPRÉSTIMOS: {totalemprestimos:>8,.2f}')
    print(linha(63))
    aguardaenter()


def exiberesumomeiossaldo(listameios, listameiossaldo, listacontasprevisto, listacontas, listatrans,
                          listacontaprovisaosaldo, listainvest, mestrabalho, anotrabalho):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    tam = 57
    borda = 55
    bordasup(2)
    cabecalho('SALDO DE MEIOS DE PAGAMENTO', tam, borda)
    print(f'{espacos(borda)}{" ":<25} {"SALDO INICIAL":>15} {"SALDO FINAL":>15}')
    for x in listameiossaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            nomemeio = list(filter(lambda meio: meio["cod"] == x["cod"], listameios))[0]["nome"]
            print(f'{espacos(borda)}{nomemeio:<25} {locale.format_string("%15.2f", x["saldo"], grouping=True)} '
                  f'{locale.format_string("%15.2f", x["saldofim"], grouping=True)}')
    bordasup(1)
    print(linha(tam, borda))
    bordasup(2)

    cabecalho(f'RESULTADO DO MÊS', tam, borda)
    vlr_rec_prev = vlr_des_prev = 0
    for x in listacontasprevisto:
        if mestrabalho == x['mes'] and anotrabalho == x['ano']:
            tipoconta = list(filter(lambda conta: conta["nome"] == x['nome'], listacontas))[0]["tipo"]
            if tipoconta == 'R':
                vlr_rec_prev += x['valorprevisto']
            elif tipoconta in ('D', 'E'):
                vlr_des_prev += x['valorprevisto']

    vlr_rec_real = vlr_des_real = 0
    for x in listatrans:
        if mestrabalho == x['mes'] and anotrabalho == x['ano']:
            tipoconta = list(filter(lambda conta: conta["nome"] == x['conta'], listacontas))[0]["tipo"]
            if tipoconta == 'R':
                vlr_rec_real += x['valor']
            elif tipoconta in ('D', 'E'):
                vlr_des_real += x['valor']
    vlr_rec_delta = vlr_rec_real - vlr_rec_prev
    vlr_des_delta = vlr_des_real - vlr_des_prev
    vlr_real_delta = vlr_rec_real + vlr_des_real
    vlr_prev_delta = vlr_rec_prev + vlr_des_prev
    vlr_delta_delta = vlr_rec_delta + vlr_des_delta

    print(f'{espacos(borda)}{"                 "} {"REALIZADO":>12} {"PREVISTO":>12} {"DELTA":>12}')
    print(f'{espacos(borda)}{"RECEITAS:         "} {vlr_rec_real:>12,.2f} {vlr_rec_prev:>12,.2f} '
          f'{vlr_rec_delta:>12,.2f}')
    print(f'{espacos(borda)}{"DESPESAS:         "} {vlr_des_real:>12,.2f} {vlr_des_prev:>12,.2f} '
          f'{vlr_des_delta:>12,.2f}')
    print(linha(tam, borda))
    print(f'{espacos(borda)}{"RESULTADO LÍQUIDO:"} {vlr_real_delta:>12,.2f} {vlr_prev_delta:>12,.2f}'
          f' {vlr_delta_delta:>12,.2f}')
    bordasup(1)
    print(linha(tam, borda))
    bordasup(2)

    cabecalho(f'RESUMO PATRIMONIAL', tam, borda)
    bordasup(1)
    tot_saldo_ini = tot_saldo_fim = 0
    tot_aposent_ini = tot_aposent_fim = 0
    for x in listameiossaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            tipomeio = list(filter(lambda meio: meio['cod'] == x['cod'], listameios))[0]['tipo']
            if tipomeio in ('CC', 'DI', 'CO'):
                tot_saldo_ini += x['saldo']
                tot_saldo_fim += x['saldofim']
                if tipomeio == 'CO':
                    tot_aposent_ini += x['saldo']
                    tot_aposent_fim += x['saldofim']

    for x in listainvest:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            tot_saldo_ini += x['vlrtotini']
            tot_saldo_fim += x['vlrtotfim']
            if x['tipoinvest'] != 'Fundo Provisão':
                tot_aposent_ini += x['vlrtotini']
                tot_aposent_fim += x['vlrtotfim']

    saldoprovini = saldoprovfim = 0
    for x in listacontaprovisaosaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            saldoprovini += x["saldoini"]
            saldoprovfim += x["saldofim"]
    saldo_capgiro_ini = tot_saldo_ini - saldoprovini - tot_aposent_ini
    saldo_capgiro_fim = tot_saldo_fim - saldoprovfim - tot_aposent_fim
    print(f'{espacos(borda)}{" ":<27} {"SALDO INICIAL":>14} {"SALDO FINAL":>14}')
    print(f'{espacos(borda)}{"Provisão":<27} {saldoprovini:>14,.2f} {saldoprovfim:>14,.2f}')
    print(f'{espacos(borda)}{"Capital de Giro":<27} {saldo_capgiro_ini:>14,.2f} {saldo_capgiro_fim:>14,.2f}')
    print(f'{espacos(borda)}{"Aposentadoria":<27} {tot_aposent_ini:>14,.2f} {tot_aposent_fim:>14,.2f}')
    print(linha(tam, borda))
    print(f'{espacos(borda)}{"TOTAIS":<27} {tot_saldo_ini:>14,.2f} {tot_saldo_fim:>14,.2f}')
    print(linha(tam, borda))


# noinspection PyTypeChecker
def resumo_patrimonio(listameios, listameiossaldo, listainvest, listacontaprovisaosaldo, mestrabalho, anotrabalho):
    system("cls")
    cabecalho('RESUMO PATRIMÔNIO - VISÃO "LOCAL"')
    locais_saldo = {'Conta Corrente + Dinheiro': {'saldoini': 0, 'saldofim': 0},
                    'Conta Corretora': {'saldoini': 0, 'saldofim': 0}}
    tot_saldo_ini = tot_saldo_fim = 0
    tot_aposent_ini = tot_aposent_fim = 0
    for x in listameiossaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            tipomeio = list(filter(lambda meio: meio['cod'] == x['cod'], listameios))[0]['tipo']
            if tipomeio in ('CC', 'DI'):
                locais_saldo['Conta Corrente + Dinheiro']['saldoini'] += x['saldo']
                locais_saldo['Conta Corrente + Dinheiro']['saldofim'] += x['saldofim']
            elif tipomeio == 'CO':
                locais_saldo['Conta Corretora']['saldoini'] += x['saldo']
                locais_saldo['Conta Corretora']['saldofim'] += x['saldofim']
                tot_aposent_ini += x['saldo']
                tot_aposent_fim += x['saldofim']

    for x in listainvest:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            if x['tipoinvest'] not in locais_saldo.keys():
                locais_saldo[x['tipoinvest']] = {'saldoini': x['vlrtotini'], 'saldofim': x['vlrtotfim']}
            else:
                locais_saldo[x['tipoinvest']]['saldoini'] += x['vlrtotini']
                locais_saldo[x['tipoinvest']]['saldofim'] += x['vlrtotfim']
            if x['tipoinvest'] != 'Fundo Provisão':
                tot_aposent_ini += x['vlrtotini']
                tot_aposent_fim += x['vlrtotfim']

    print(f'{espacos()}{"PATRIMONIO":<30} {"SALDO INICIAL":>14} {"SALDO FINAL":>14}')
    for local, saldo in locais_saldo.items():
        print(f'{espacos()}{local:<30} {saldo["saldoini"]:>14,.2f} {saldo["saldofim"]:>14,.2f}')
        tot_saldo_ini += saldo['saldoini']
        tot_saldo_fim += saldo['saldofim']
    print(linha())
    print(f'{espacos()}{"TOTAIS":<30} {tot_saldo_ini:>14,.2f} {tot_saldo_fim:>14,.2f}')
    print(linha())
    print()

    cabecalho(f'RESUMO PATRIMÔNIO - VISÃO "TIPO"')
    saldoprovini = saldoprovfim = 0
    for x in listacontaprovisaosaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            saldoprovini += x["saldoini"]
            saldoprovfim += x["saldofim"]
    saldo_capgiro_ini = tot_saldo_ini - saldoprovini - tot_aposent_ini
    saldo_capgiro_fim = tot_saldo_fim - saldoprovfim - tot_aposent_fim
    print(f'{espacos()}{"PATRIMONIO":<30} {"SALDO INICIAL":>14} {"SALDO FINAL":>14}')
    print(f'{espacos()}{"Provisão":<30} {saldoprovini:>14,.2f} {saldoprovfim:>14,.2f}')
    print(f'{espacos()}{"Capital de Giro":<30} {saldo_capgiro_ini:>14,.2f} {saldo_capgiro_fim:>14,.2f}')
    print(f'{espacos()}{"Aposentadoria":<30} {tot_aposent_ini:>14,.2f} {tot_aposent_fim:>14,.2f}')
    print(linha())
    print(f'{espacos()}{"TOTAIS":<30} {tot_saldo_ini:>14,.2f} {tot_saldo_fim:>14,.2f}')
    print(linha())
    aguardaenter()
