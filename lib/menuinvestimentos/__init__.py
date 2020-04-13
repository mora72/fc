# Funções do Menu INVESTIMENTOS
from lib.interface import *
from lib.arquivos import *


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
                arqlistainvest = Arquivolista('/Users/carlo/PycharmProjects/fc/baseinvest.pck1', 'Investimentos')
                arqlistainvest.gravar(listainvest)
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
                cabecalho(f'CONFIRMA ALTERAÇÃO ? ', 42, margem)
                opcao = input(f'{espacos(margem)}Sim (S) ou Não (N) ? ')
                if opcao in 'Ss':
                    del listainvest[idtransacao]
                    arqlistainvest = Arquivolista('/Users/carlo/PycharmProjects/fc/baseinvest.pck1', 'Investimentos')
                    arqlistainvest.gravar(listainvest)
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
                new_vl = leiafloat('Valor unitário final: ', margem)
                new_qt = leiaint('Qtde final: (-1 para = inicial)', margem)
                cabecalho(f'CONFIRMA ALTERAÇÃO ? ', 42, margem)
                opcao = input(f'{espacos(margem)}Sim (S) ou Não (N) ? ')
                if opcao in 'Ss':
                    listainvest[idtrans]["vlrunifim"] = new_vl
                    if new_qt == -1:
                        listainvest[idtrans]["qtdefim"] = listainvest[idtrans]["qtdeini"]
                    else:
                        listainvest[idtrans]["qtdefim"] = new_qt
                    listainvest[idtrans]["vlrtotfim"] = listainvest[idtrans]["vlrunifim"] * \
                                                        listainvest[idtrans]["qtdefim"]
                    arqlistainvest = Arquivolista('/Users/carlo/PycharmProjects/fc/baseinvest.pck1', 'Investimentos')
                    arqlistainvest.gravar(listainvest)
        elif opcao == 9:
            break
