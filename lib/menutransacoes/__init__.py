# Funções do Menu TRANSACOES
from lib.interface import *
from lib.arquivos import *


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
            arqlistameiossaldo = Arquivolista('/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1', 'MeiosSaldo')
            arqlistameiossaldo.gravar(listameiossaldo)
            break


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
    print(f'   ID {"DATA":^10} {"VALOR":>11} {"CONTA":<25} {"DESCRIÇÃO":<50} {"MEIO PGTO":<16} '
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
            print(f' {c:4} {x["dia"]:2}/{x["mes"]:2}/{x["ano"]} {x["valor"]:>11,.2f} '
                  f'{x["conta"]:<25} {descr:<50} {nomemeio:<16} {nomeemprest:<15} '
                  f'{saldofim:>10,.2f}')
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
            if meiotrans == "*":
                meiotrans = leiameio(' Meio de Pagamento: ', listameios, 0)
                saldofim = ler_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano)
            nomemeio = list(filter(lambda meio: meio['cod'] == meiotrans, listameios))[0]['nome'].upper()
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
                arqlistatrans = Arquivolista('/Users/carlo/PycharmProjects/fc/basetrans.pck1', 'Transações')
                arqlistatrans.gravar(listatrans)
        elif opcao == 2:
            bordasup(3)
            cabecalho(' DELETAR TRANSAÇÃO', 46, 0)
            while True:
                idtransacao = leiaint(' ID da Transação ou -1 para desistir: ', 0)
                if -1 <= idtransacao <= len(listatrans) - 1:
                    break
                else:
                    print(f' ID Inválido !')
            if idtransacao >= 0:
                vlrtrans = listatrans[idtransacao]['valor']
                meiotrans = listatrans[idtransacao]['meio']

                saldofim = ler_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano)
                saldofim -= vlrtrans
                grava_saldo_fim_meio(listameiossaldo, meiotrans, mes, ano, saldofim)

                del listatrans[idtransacao]
                arqlistatrans = Arquivolista('/Users/carlo/PycharmProjects/fc/basetrans.pck1', 'Transações')
                arqlistatrans.gravar(listatrans)
        elif opcao == 3:
            bordasup(3)
            cabecalho(' MUDAR MEIO DE PAGAMENTO', 46, 0)
            meiotrans = leiameio(' Meio de Pagamento ou * : ', listameios, 0)
        elif opcao == 9:
            break
