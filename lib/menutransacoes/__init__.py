# Funções do Menu TRANSACOES
# from os import system
from lib.interface import *
# import random


def lanctrans(lista, anotrabalho, mestrabalho, listameios, listacontas, listaemprest, listameiossaldo):
    system("cls")
    cabecalho(f'ANO TRABALHO: {anotrabalho} - MES TRABALHO: {mestrabalho}')
    cabecalho('Lançamento de Transações')
    meiotrans = leiameio('Digite o meio desta transação: ', listameios)
    saldofim = ler_saldo_fim_meio(listameiossaldo, meiotrans, mestrabalho, anotrabalho)
    print(f'{espacos(50)}Saldo Atual do Meio: {saldofim:>10,.2f}')
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
            nomeemprest = leiaemprestimo('Digite o nome do Empréstimo: ', listaemprest, mestrabalho, anotrabalho)
        cabecalho('CONFIRMA REGISTRO ? ')
        print(f'{espacos(50)}data...: {diatrans:2}/{mestrabalho:2}/{anotrabalho}')
        print(f'{espacos(50)}meio..: {meiotrans}')
        print(f'{espacos(50)}conta.: {contatrans}')
        print(f'{espacos(50)}valor.: {valortrans}')
        print(f'{espacos(50)}descrição...: {descrtrans}')
        if contatrans == 'Empréstimo':
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
            saldofim += valortrans
            grava_saldo_fim_meio(listameiossaldo, meiotrans, mestrabalho, anotrabalho, saldofim)
            print(f'{espacos(50)}Saldo Final do Meio {meiotrans}: {saldofim}')
            print(f'{espacos(50)}REGISTRO INSERIDO')
            if contatrans == 'Empréstimo':
                registrotrans = {'ano': anotrabalho,
                                 'mes': mestrabalho,
                                 'dia': diatrans,
                                 'valor': valortrans * -1,
                                 'conta': contatrans,
                                 'descr': descrtrans,
                                 'meio': 'PR',
                                 'nomeemprest': 'Provisão'
                                 }
                lista.append(registrotrans.copy())
                saldofim += valortrans * -1
                grava_saldo_fim_meio(listameiossaldo, meiotrans, mestrabalho, anotrabalho, saldofim)
                print(f'{espacos(50)}Saldo Final do Meio {meiotrans}: {saldofim}')
                print(f'{espacos(50)}REGISTRO PROVISÃO - EMPRESTIMO INSERIDO')
        opcao = input(f'{espacos(50)}Lançar outra transação? Sim (S) ou Não (N) ? ')
        if opcao in 'Nn':
            break


def ler_saldo_fim_meio(listameiossaldo, meio, mes, ano):
    saldofim = 0
    for x in listameiossaldo:
        if x["mes"] == mes and x["ano"] == ano and x['cod'] == meio:
            saldofim = x["saldofim"]
    return saldofim


def grava_saldo_fim_meio(listameiossaldo, meio, mes, ano, saldofim):
    for x in listameiossaldo:
        if x["mes"] == mes and x["ano"] == ano and x['cod'] == meio:
            x["saldofim"] = saldofim
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


def deletatrans(listatrans, mes, ano, listacontas, listameiossaldo):
    exibetrans(listatrans, mes, ano, listacontas)
    cabecalho('Deletar Meio de Transação Financeira')
    while True:
        idtransacao = leiaint('Digite ID da Transação que deseja deletar ou -1 para desistir: ', 0)
        if -1 <= idtransacao <= len(listatrans) - 1:
            break
        else:
            print(f'ID Inválido !')
    if idtransacao >= 0:
        vlrtrans = listatrans[idtransacao]['valor']
        meiotrans = listatrans[idtransacao]['meio']

        saldofim = ler_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano)
        print(f'Saldo Inicial do Meio {meiotrans}: {saldofim}')
        saldofim -= vlrtrans
        print(f'Saldo Final do Meio {meiotrans}: {saldofim}')
        grava_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano, saldofim)
        del listatrans[idtransacao]
        print(f'ID DELETADO !')
    else:
        print(f'Deleção CANCELADA !')
    aguardaenter()


def exibetransmeio(listatrans, mes, ano, meiotrans, listameiossaldo, listameios):
    nomemeio = ''
    if meiotrans != '*':
        nomemeio = list(filter(lambda meio: meio['cod'] == meiotrans, listameios))[0]['nome'].upper()
        textocab = f'LANCAMENTOS - {nomemeio}'
    else:
        textocab = f'TODOS OS LANCAMENTOS DO MÊS'
    cabecalho(f'{textocab:^150}', 150, 0)
    saldofim = 0
    if meiotrans != '*':
        for y in listameiossaldo:
            if y["cod"] == meiotrans and y["ano"] == ano and y["mes"] == mes:
                saldofim = y["saldo"]
                break
    print(f'   ID {"DATA":^10} {"VALOR":>10} {"CONTA":<25} {"DESCRIÇÃO":<50} {"MEIO PGTO":<16} '
          f'{"EMPRESTIMO":<15} {"SALDO MEIO"}')
    print(linha(150, 0))
    nomemeio = nomemeio.lower()
    for c, x in enumerate(listatrans):
        if x["mes"] == mes and x["ano"] == ano and (x["meio"] == meiotrans or meiotrans == '*'):
            nomeemprest = ' '
            if x['conta'] == 'Empréstimo':
                nomeemprest = x['nomeemprest']
            if meiotrans != '*':
                saldofim = saldofim + x["valor"]
            else:
                nomemeio = list(filter(lambda meio: meio['cod'] == x["meio"], listameios))[0]['nome']
            if len(x['descr']) > 50:
                descr = x['descr'][:50]
            else:
                descr = x['descr']
            print(f' {c:4} {x["dia"]:2}/{x["mes"]:2}/{x["ano"]} {x["valor"]:>10,.2f} '
                  f'{x["conta"]:<25} {descr:<50} {nomemeio:<16} {nomeemprest:<15} '
                  f'{saldofim:>10.2f}')
    return saldofim


def trans(listatrans, mes, ano, listacontas, listameiossaldo, listameios, listaemprest):
    system("cls")
    cabecalho('GERENCIAR TRANSAÇÕES', 42, 0)
    meiotrans = leiameio(' Meio de Pagamento ou * : ', listameios, 0)
    while True:
        system("cls")
        saldofim = exibetransmeio(listatrans, mes, ano, meiotrans, listameiossaldo, listameios)
        print(linha(150, 0))
        opcao = leiaint(' 1-Nova Transação    2-Deletar    3-Trocar Meio    9-Sair: ', 0)
        if opcao == 1:
            bordasup(3)
            nomemeio = list(filter(lambda meio: meio['cod'] == meiotrans, listameios))[0]['nome'].upper()
            if meiotrans == "*":
                meiotrans = leiameio(' Meio de Pagamento: ', listameios, 0)
                saldofim = ler_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano)
            cabecalho(f' NOVA TRANSAÇÃO - {nomemeio} - SALDO: {saldofim:>10,.2f}', 46, 0)
            nomeemprest = ''
            diatrans = leiadia(' Dia: ', mes, ano, 0)
            valortrans = leiafloat(' Valor: ', 0)
            contatrans = leiaconta(' Conta: ', listacontas, 0)
            descrtrans = input(f' Descrição: ')
            if descrtrans == '':
                descrtrans = contatrans
            if contatrans == 'Empréstimo':
                nomeemprest = leiaemprestimo(' Nome do Empréstimo: ', listaemprest, mes, ano, 0)
            cabecalho(' CONFIRMA REGISTRO ? ', 46, 0)
            opcao = input(f' Sim (S) ou Não (N) ? ')
            if opcao in 'Ss':
                registrotrans = {'ano': ano,
                                 'mes': mes,
                                 'dia': diatrans,
                                 'valor': valortrans,
                                 'conta': contatrans,
                                 'descr': descrtrans,
                                 'meio': meiotrans,
                                 'nomeemprest': nomeemprest}
                listatrans.append(registrotrans.copy())
                saldofim += valortrans
                grava_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano, saldofim)
                if contatrans == 'Empréstimo':
                    registrotrans = {'ano': ano,
                                     'mes': mes,
                                     'dia': diatrans,
                                     'valor': valortrans * -1,
                                     'conta': contatrans,
                                     'descr': descrtrans,
                                     'meio': 'PR',
                                     'nomeemprest': 'Provisão'
                                     }
                    listatrans.append(registrotrans.copy())
                    saldofim += valortrans * -1
                    grava_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano, saldofim)
        elif opcao == 2:
            bordasup(3)
            cabecalho(' DELETAR TRANSAÇÃO', 46, 0)
            while True:
                idtransacao = leiaint(' ID da Transação ou -1 para desistir: ', 0)
                if -1 <= idtransacao <= len(listatrans) - 1:
                    break
                else:
                    print(f' ID Inválido !')
                    aguardaenter()
            if idtransacao >= 0:
                vlrtrans = listatrans[idtransacao]['valor']
                meiotrans = listatrans[idtransacao]['meio']

                saldofim = ler_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano)
                saldofim -= vlrtrans
                grava_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano, saldofim)

                del listatrans[idtransacao]
        elif opcao == 3:
            bordasup(3)
            cabecalho(' MUDAR MEIO DE PAGAMENTO', 46, 0)
            meiotrans = leiameio(' Meio de Pagamento ou * : ', listameios, 0)
        elif opcao == 9:
            break
