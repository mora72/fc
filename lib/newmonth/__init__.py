from lib.interface import *


def gonewmonth(listameios, listameiossaldo, listacontaprovisaosaldo, listainvest, listaemprest,
               mestrabalho, anotrabalho):
    if mestrabalho == 12:
        mesnovo = 1
        anonovo = anotrabalho + 1
    else:
        anonovo = anotrabalho
        mesnovo = mestrabalho + 1
    cabecalho('PROCESSA CRIAÇÃO DE BASES PARA NOVO MES')
    print(f'{espacos()}ANO TRABALHO: {anotrabalho} - ANO NOVO: {anonovo}')
    print(f'{espacos()}MES TRABALHO: {mestrabalho} - MES NOVO: {mesnovo}')
    print(linha())
    opcao = input(f'{espacos()} Posso processar MEIOS SALDO? Sim (S) ou Não (N) ? ')
    if opcao in 'Ss':
        for x in listameiossaldo:
            tipomeio = list(filter(lambda meio: meio["cod"] == x["cod"], listameios))[0]["tipo"]
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                if tipomeio == 'CA':
                    registro = {'cod': x['cod'], 'saldo': 0, 'mes': mesnovo, 'ano': anonovo, 'saldofim': 0}
                else:
                    registro = {'cod': x['cod'], 'saldo': x["saldofim"], 'mes': mesnovo, 'ano': anonovo,
                                'saldofim': x["saldofim"]}
                print(f'{espacos()}REGISTRO {x["cod"]} INSERIDO')
                listameiossaldo.append(registro.copy())
    opcao = input(f'{espacos()} Posso processar PROVISOES? Sim (S) ou Não (N) ? ')
    if opcao in 'Ss':
        for x in listacontaprovisaosaldo:
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                registro = {'nome': x['nome'], 'saldoini': x['saldofim'], 'mes': mesnovo, 'ano': anonovo,
                            'realizado': 0, 'saldofim': x['saldofim']}
                print(f'{espacos()}REGISTRO {x["nome"]} INSERIDO')
                listacontaprovisaosaldo.append(registro.copy())
    opcao = input(f'{espacos()} Posso processar INVESTIMENTOS? Sim (S) ou Não (N) ? ')
    if opcao in 'Ss':
        for x in listainvest:
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                registro = {'ano': anonovo,
                            'mes': mesnovo,
                            'diainiinvest': x['diainiinvest'],
                            'mesiniinvest': x['mesiniinvest'],
                            'anoiniinvest': x['anoiniinvest'],
                            'tipoinvest': x['tipoinvest'],
                            'nomeinvest': x['nomeinvest'],
                            'vlruniini': x['vlrunifim'],
                            'qtdeini': x['qtdefim'],
                            'vlrtotini': x['vlrtotfim'],
                            'qtdefim': x['qtdefim'],
                            'vlrunifim': x['vlrunifim'],
                            'vlrtotfim': x['vlrtotfim']
                            }
                print(f'{espacos()}REGISTRO {x["nomeinvest"]} INSERIDO')
                listainvest.append(registro.copy())
    opcao = input(f'{espacos()} Posso processar EMPRÉSTIMOS? Sim (S) ou Não (N) ? ')
    if opcao in 'Ss':
        for x in listaemprest:
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                registro = {'nome': x['nome'], 'saldoini': x['saldofim'], 'mes': mesnovo, 'ano': anonovo,
                            'realizado': 0, 'saldofim': x['saldofim']}
                print(f'{espacos()}REGISTRO {x["nome"]} INSERIDO')
                listaemprest.append(registro.copy())
    print(f'{espacos()}PROCESSADO COM SUCESSO !')
    aguardaenter()
    return mesnovo, anonovo
