from lib.interface import *


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
            listaresumo[pos+1] = listaresumo[pos+1] + x['valor']
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


def exiberesumomeiossaldo(listameios, listameiossaldo, mestrabalho, anotrabalho):
    cabecalho('SALDO DE MEIOS DE PAGAMENTO')
    for x in listameiossaldo:
        if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
            nomemeio = list(filter(lambda meio: meio["cod"] == x["cod"], listameios))[0]["nome"]
            print(f'{espacos()}{x["cod"]} {nomemeio:<20} {x["saldo"]:>10,.2f} {x["saldofim"]:>10,.2f}')
