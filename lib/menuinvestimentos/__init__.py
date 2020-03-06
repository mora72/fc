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


def exibeinvestnew(listainvest, mes, ano, tipoinvest=''):
    system("cls")
    if tipoinvest != '*':
        textocab = f'INVESTIMENTOS - {tipoinvest}'
    else:
        textocab = f'TODOS OS INVESTIMENTOS DO MÊS'
    margem = 3
    cabecalho(textocab, 160, margem)
    vlrtotini = 0
    vlrtotfim = 0
    print(f'{espacos(margem)} ID {"DATA":^10} {"TIPO":<30} {"NOME":<50} {"VLR UNI INI"} {"QTD INI"} '
          f'{"VLR TOT INI"} {"VLR UNI FIM"} {"QTD FIM"} {"VLR TOT FIM"}')
    print(linha(160, margem))
    for c, x in enumerate(listainvest):
        if x["mes"] == mes and x["ano"] == ano and (x["tipoinvest"] == tipoinvest or tipoinvest == '*'):
            if x["tipoinvest"] != 'Fundo Provisão':
                vlrtotini += x["vlrtotini"]
                vlrtotfim += x["vlrtotfim"]
            print(f'{espacos(margem)}{c:3} {x["diainiinvest"]:2}/{x["mesiniinvest"]:2}/{x["anoiniinvest"]} '
                  f'{x["tipoinvest"]:<30} {x["nomeinvest"]:<50} '
                  f'{x["vlruniini"]:>11,.2f} {x["qtdeini"]:>7,} {x["vlrtotini"]:>11,.2f} '
                  f'{x["vlrunifim"]:>11,.2f} {x["qtdefim"]:>7,} {x["vlrtotfim"]:>11,.2f} ')
    print(linha(160, margem))
    print(f'{espacos(margem)}VALOR TOTAL INICIAL.: {vlrtotini:>10,.2f}')
    print(f'{espacos(margem)}VALOR TOTAL FINAL...: {vlrtotfim:>10,.2f}')
    print(linha(160, margem))


def invest(listainvest, mes, ano):
    system("cls")
    margem = 3
    cabecalho('GERENCIAR INVESTIMENTOS', 42, margem)
    tipoinvest = input(f'{espacos(margem)}Tipo do investimento ou * : ')
    while True:
        system("cls")
        exibeinvestnew(listainvest, mes, ano, tipoinvest)
        opcao = leiaint(' 1-Novo    2-Deletar    3-Trocar Tipo   4-Alterar Saldo    9-Sair: ', margem)
        if opcao == 1:
            bordasup(3)
            if tipoinvest == "*":
                tipoinvest = input(f'{espacos(margem)}Tipo do investimento: ')
            cabecalho(f' NOVA TRANSAÇÃO - {tipoinvest}', 46, margem)
            nomeinvest = input(f'{espacos(margem)}Nome: ')
            diainiinvest = leiaint('Dia do investimento: ', margem)
            mesiniinvest = leiaint('Mês do investimento: ', margem)
            anoiniinvest = leiaint('Ano do investimento: ', margem)
            qtdeini = leiaint('Quantidade: ', margem)
            vlruniini = leiafloat('Valor unitário: ', margem)
            vlrtotini = vlruniini * qtdeini
            cabecalho(f'CONFIRMA REGISTRO ? ', 42, margem)
            opcao = input(f'{espacos(margem)}Sim (S) ou Não (N) ? ')
            if opcao in 'Ss':
                registro = {'ano': ano,
                            'mes': mes,
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
                listainvest.append(registro.copy())
        elif opcao == 2:
            bordasup(3)
            cabecalho('Deletar Investimento', 42, margem)
            while True:
                idtransacao = leiaint('ID do Investimento ou -1 para desistir: ', margem)
                if -1 <= idtransacao <= len(listainvest) - 1:
                    break
                else:
                    print(f'{espacos(margem)}ID Inválido !')
            if idtransacao >= 0:
                del listainvest[idtransacao]
        elif opcao == 3:
            bordasup(3)
            cabecalho(' MUDAR TIPO DE INVESTIMENTO', 42, margem)
            tipoinvest = input(f'{espacos(margem)}Tipo do investimento ou * : ')
        elif opcao == 4:
            print(linha(160, margem))
            while True:
                idtrans = leiaint('ID do Investimento ou -1 para finalizar: ', margem)
                if -1 <= idtrans <= len(listainvest) - 1:
                    break
                else:
                    print(f'{espacos(margem)}ID Inválido !')
            if idtrans >= 0:
                listainvest[idtrans]["vlrunifim"] = leiafloat('Valor unitário final: ', margem)
                listainvest[idtrans]["qtdefim"] = leiaint('Qtde final: (-1 para = inicial)', margem)
                if listainvest[idtrans]["qtdefim"] == -1:
                    listainvest[idtrans]["qtdefim"] = listainvest[idtrans]["qtdeini"]
                listainvest[idtrans]["vlrtotfim"] = listainvest[idtrans]["vlrunifim"] * listainvest[idtrans]["qtdefim"]
        elif opcao == 9:
            break
