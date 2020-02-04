# Funções do Menu TRANSACOES
# from os import system
from lib.interface import *


def lanctrans(lista, anotrabalho, mestrabalho, listameios, listacontas):
    system("cls")
    cabecalho(f'ANO TRABALHO: {anotrabalho} - MES TRABALHO: {mestrabalho}')
    cabecalho('Lançamento de Transações')
    meiotrans = leiameio('Digite o meio desta transação: ', listameios)
    while True:
        nomeemprest = ''
        cabecalho(f'NOVO REGISTRO DO MEIO: {meiotrans}')
        diatrans = leiadia('Digite o dia da transação: ', mestrabalho, anotrabalho)
        valortrans = leiafloat('Digite o valor da transação: ')
        contatrans = leiaconta('Digite a conta da transação: ', listacontas)
        descrtrans = input(f'{espacos(50)}Digite uma descrição para esta transação: ')
        if descrtrans == '':
            descrtrans = contatrans
        if contatrans == 'Empréstimo':
            nomeemprest = input(f'{espacos(50)}Digite o nome do Empréstimo: ')
        cabecalho('CONFIRMA REGISTRO ? ')
        print(f'{espacos(50)}data...: {diatrans:2}/{mestrabalho:2}/{anotrabalho}')
        print(f'{espacos(50)}meio..: {meiotrans}')
        print(f'{espacos(50)}conta.: {contatrans}')
        print(f'{espacos(50)}valor.: {valortrans}')
        print(f'{espacos(50)}descrição...: {descrtrans}')
        print(f'{espacos(50)}empréstimo...: {nomeemprest}')
        opcao = input(f'{espacos(50)}Sim (S) ou Não (N) ? ')
        if opcao in 'Ss':
            registrotrans = {'ano': anotrabalho,
                             'mes': mestrabalho,
                             'dia': diatrans,
                             'valor': valortrans,
                             'conta': contatrans,
                             'descr': descrtrans,
                             'meio': meiotrans,
                             'nomeemprest': nomeemprest}
            lista.append(registrotrans.copy())
            print(f'{espacos(50)}REGISTRO INSERIDO')
        opcao = input(f'{espacos(50)}Lançar outra transação? Sim (S) ou Não (N) ? ')
        if opcao in 'Nn':
            break


def exibetrans(lista, mes, ano, listacontas):
    system("cls")
    cabecalho('LANCAMENTOS DO MES E ANO DE TRABALHO', 42, 0)
    opcao = leiaint('Digite 1 para ver todos ou 2 para uma conta específica: ', 0)
    if opcao == 1:
        nomeconta = '*'
    elif opcao == 2:
        nomeconta = leiaconta('Digite nome da conta: ', listacontas, 0)
    else:
        nomeconta = ''
    for c, x in enumerate(lista):
        if x["mes"] == mes and x["ano"] == ano and (x["conta"] == nomeconta or nomeconta == '*'):
            if nomeconta == 'Empréstimo' or nomeconta == '*':
                print(f'ID: {c:2} - {x["dia"]:2}/{x["mes"]:2}/{x["ano"]} - ', end='')
                print(f'{x["valor"]:>10,.2f} - {x["conta"]:<30} - {x["descr"]:<50} - {x["meio"]} - {x["nomeemprest"]}')
            else:
                print(f'ID: {c:2} - {x["dia"]:2}/{x["mes"]:2}/{x["ano"]} - ', end='')
                print(f'{x["valor"]:>10,.2f} - {x["conta"]:<30} - {x["descr"]:<50} - {x["meio"]}')
    aguardaenter(0)


def exibetransmeiosaldo(listatrans, listameios, listameiossaldo, mestrabalho, anotrabalho):
    system("cls")
    cabecalho('LANCAMENTOS E SALDO DE UM MEIO', 42, 0)
    codmeio = leiameio('Digite código do meio: ', listameios, 0)
    saldofim = 0
    pos = 0
    achou = 'N'
    for b, y in enumerate(listameiossaldo):
        if y["cod"] == codmeio and y["ano"] == anotrabalho and y["mes"] == mestrabalho:
            saldofim = y["saldo"]
            pos = b
            achou = 'S'
            break
    for c, x in enumerate(listatrans):
        if x["meio"] == codmeio and x['mes'] == mestrabalho and x['ano'] == anotrabalho:
            saldofim = saldofim + x["valor"]
            print(f'ID: {c:2} - {x["dia"]:2}/{x["mes"]:2}/{x["ano"]} - ', end='')
            print(f'{x["valor"]:>8.2f} - {x["conta"]:<30} - {x["descr"]:<30} - {x["meio"]} - saldo: {saldofim:>9.2f}')
    if achou == 'S':
        listameiossaldo[pos]['saldofim'] = saldofim
    aguardaenter(0)


def deletatrans(lista, mes, ano, listacontas):
    exibetrans(lista, mes, ano, listacontas)
    cabecalho('Deletar Meio de Transação Financeira')
    while True:
        idtransacao = leiaint('Digite ID da Transação que deseja deletar ou -1 para desistir: ', 0)
        if -1 <= idtransacao <= len(lista) - 1:
            break
        else:
            print(f'ID Inválido !')
    if idtransacao >= 0:
        print(f'ID DELETADO !')
        del lista[idtransacao]
    else:
        print(f'Deleção CANCELADA !')
    aguardaenter()
