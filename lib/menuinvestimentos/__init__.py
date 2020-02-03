# Funções do Menu INVESTIMENTOS
from lib.interface import *


def newinvest(lista, mestrabalho, anotrabalho):
    tipoinvest = exibeinvest(lista, mestrabalho, anotrabalho)
    cabecalho(f'ANO TRABALHO: {anotrabalho} - MES TRABALHO: {mestrabalho}')
    cabecalho('NOVO INVESTIMENTO')
    while True:
        if tipoinvest == '':
            tipoinvest = input(f'{espacos()}Digite o tipo do investimento: ')
        else:
            print(f'{espacos()}Tipo do investimento: {tipoinvest}')
        nomeinvest = input(f'{espacos()}Digite o nome do investimento: ')
        diainiinvest = leiaint('Digite o dia do início do investimento: ')
        mesiniinvest = leiaint('Digite o mês do início do investimento: ')
        anoiniinvest = leiaint('Digite o ano do início do investimento: ')
        qtdeini = leiaint('Digite quantidade inicial: ')
        vlruniini = leiafloat('Digite valor unitário inicial: ')
        vlrtotini = vlruniini * qtdeini
        cabecalho(f'CONFIRMA REGISTRO ? ')
        opcao = input(f'{espacos()}Sim (S) ou Não (N) ? ')
        if opcao in 'Ss':
            registro = {'ano': anotrabalho,
                        'mes': mestrabalho,
                        'diainiinvest': diainiinvest,
                        'mesiniinvest': mesiniinvest,
                        'anoiniinvest': anoiniinvest,
                        'tipoinvest': tipoinvest,
                        'nomeinvest': nomeinvest,
                        'vlruniini': vlruniini,
                        'qtdeini': qtdeini,
                        'vlrtotini': vlrtotini,
                        'qtdefim': 0,
                        'vlrunifim': 0,
                        'vlrtotfim': 0,
                        }
            lista.append(registro.copy())
            print(f'{espacos()}REGISTRO INSERIDO')
        opcao = input(f'{espacos()}Lançar outra transação? Sim (S) ou Não (N) ? ')
        if opcao in 'Nn':
            break


def exibeinvest(lista, mes, ano, tipoinvest=''):
    system("cls")
    margem = 3
    cabecalho('INVESTIMENTOS DO MES E ANO DE TRABALHO', 150, margem)
    if tipoinvest == '':
        opcao = leiaint('Digite 1 para ver todos ou 2 para um tipo específico: ', margem)
        if opcao == 1:
            tipoinvest = '*'
        elif opcao == 2:
            tipoinvest = input(f'{espacos(margem)}Digite o tipo do investimento: ')
        else:
            tipoinvest = ''
    vlrtotini = 0
    vlrtotfim = 0
    for c, x in enumerate(lista):
        if x["mes"] == mes and x["ano"] == ano and (x["tipoinvest"] == tipoinvest or tipoinvest == '*'):
            if x["tipoinvest"] != 'Fundo Provisão':
                vlrtotini += x["vlrtotini"]
                vlrtotfim += x["vlrtotfim"]
            print(f'{espacos(margem)}ID: {c:3} - {x["diainiinvest"]:2}/{x["mesiniinvest"]:2}/{x["anoiniinvest"]} '
                  f'{x["tipoinvest"]:<30} {x["nomeinvest"]:<50} '
                  f'{x["vlruniini"]:>10,.2f} {x["qtdeini"]:>6,} {x["vlrtotini"]:>10,.2f} '
                  f'{x["vlrunifim"]:>10,.2f} {x["qtdefim"]:>6,} {x["vlrtotfim"]:>10,.2f} ')
    print(linha(150, 0))
    print(f'VALOR TOTAL INICIAL.: {vlrtotini:>10,.2f}')
    print(f'VALOR TOTAL FINAL...: {vlrtotfim:>10,.2f}')
    print(linha(150, 0))
    aguardaenter(margem)
    return tipoinvest


def deletainvest(lista, mes, ano):
    exibeinvest(lista, mes, ano)
    cabecalho('Deletar Investimento')
    while True:
        idtransacao = leiaint('Digite ID do Investimento que deseja deletar ou -1 para desistir: ')
        if -1 <= idtransacao <= len(lista) - 1:
            break
        else:
            print(f'{espacos()}ID Inválido !')
    if idtransacao >= 0:
        print(f'{espacos()}ID DELETADO !')
        del lista[idtransacao]
    else:
        print(f'{espacos()}Deleção CANCELADA !')
    aguardaenter()


def updateinvest(lista, mes, ano):
    tipoinvest = ''
    while True:
        tipoinvest = exibeinvest(lista, mes, ano, tipoinvest)
        cabecalho('Atualizar Investimento')
        while True:
            idtrans = leiaint('Digite ID do Investimento que deseja atualizar ou -1 para finalizar: ')
            if -1 <= idtrans <= len(lista) - 1:
                break
            else:
                print(f'{espacos()}ID Inválido !')
        if idtrans >= 0:
            lista[idtrans]["vlrunifim"] = leiafloat('Digite novo valor unitário final: ')
            lista[idtrans]["qtdefim"] = leiaint('Digite nova qtde final: (-1 para manter qtde inicial)')
            if lista[idtrans]["qtdefim"] == -1:
                lista[idtrans]["qtdefim"] = lista[idtrans]["qtdeini"]
            lista[idtrans]["vlrtotfim"] = lista[idtrans]["vlrunifim"] * lista[idtrans]["qtdefim"]
            print(f'{espacos()}ID ALTERADO !')
            aguardaenter()
        else:
            print(f'{espacos()}Alteração FINALIZADA !')
            aguardaenter()
            break
