# Funções do Menu SETUP
from lib.interface import *
from lib.arquivos import *


def cadmeios(lista):
    system("cls")
    cabecalho('Cadastro de Meios de Transação', 40, 30)
    codmeio = input(f'{espacos(30)}Digite código do Meio de Transação (2 letras): ').upper()
    nomemeio = input(f'{espacos(30)}Digite o nome do Meio de Transacao: ')
    while True:
        tipomeio = input(f'{espacos(30)}Digite tipo do Meio de Transação'
                         ' (CC - Conta Corrente; DI - Dinheiro; CA - Cartão; PR - Provisão; CO - Conta Corretora): ')
        if tipomeio in ('CC', 'cc', 'DI', 'di', 'CA', 'ca', 'PR', 'pr', 'CO', 'co'):
            break
        print(f'{espacos(30)}Tipo Inválido !')
    registromeio = {'cod': codmeio, 'nome': nomemeio, 'tipo': tipomeio}
    lista.append(registromeio.copy())
    Arquivolista('/Users/carlo/PycharmProjects/fc/basemeios.pck1', 'Meios').gravar(lista)
    print(f'{espacos(30)}REGISTRO INSERIDO')
    aguardaenter()


def exibemeios(lista):
    system("cls")
    cabecalho('MEIOS DE TRANSAÇÃO CADASTRADOS')
    for x in lista:
        print(f'{espacos(50)}{x["cod"]} - {x["nome"]:<20} - {x["tipo"]}')
    aguardaenter()


def deletameio(lista):
    system("cls")
    cabecalho('Deletar Meio de Transação Financeira')
    codmeiotransacao = input(f'{espacos()}Digite código do Meio de Transação (2 letras) que deseja deletar: ')
    achou = False
    posregistro = -1
    nomemeiotransacao = ''
    tipomeio = ''
    for c, x in enumerate(lista):
        if x["cod"] == codmeiotransacao:
            achou = True
            nomemeiotransacao = x["nome"]
            tipomeio = x["tipo"]
            posregistro = c
            break
    if achou:
        print(f'{espacos()}Registro código: {codmeiotransacao}, nome: {nomemeiotransacao}, tipo: {tipomeio} DELETADO !')
        del lista[posregistro]
        Arquivolista('/Users/carlo/PycharmProjects/fc/basemeios.pck1', 'Meios').gravar(lista)
    else:
        print(f'{espacos()}Registro código: {codmeiotransacao} não encontrado!')
    aguardaenter()


def cadcontas(lista):
    while True:
        system("cls")
        cabecalho('Cadastro de tipos de conta de receita ou despesa', 42, 0)
        nomeconta = input(f'{espacos(0)}Digite o nome da conta de receita ou despesa ou "Sair" para SAIR : ')
        if nomeconta in ('Sair', 'SAIR', 'sair'):
            break
        tipoconta = input(f'{espacos(0)}Digite o tipo da conta (R = Receita; D = Despesa; T = Transferência; '
                          'E = Empréstimo; C = PagtoCartão; RI = Receita Investimento;'
                          ' DI = Despesa Investimento ').upper()
        registroconta = {'nome': nomeconta, 'tipo': tipoconta}
        lista.append(registroconta.copy())
        Arquivolista('/Users/carlo/PycharmProjects/fc/basecontas.pck1', 'Contas').gravar(lista)
        print(f'{espacos(0)}REGISTRO INSERIDO')
        aguardaenter(0)


def deletaconta(lista):
    system("cls")
    cabecalho('Deletar Conta de Receita ou Despesa')
    nomeconta = input(f'{espacos()}Digite nome da conta que deseja deletar: ')
    achou = False
    posregistro = -1
    for c, x in enumerate(lista):
        if x["nome"] == nomeconta:
            achou = True
            posregistro = c
            break
    if achou:
        print(f'{espacos()}Registro nome: {nomeconta} DELETADO !')
        del lista[posregistro]
        Arquivolista('/Users/carlo/PycharmProjects/fc/basecontas.pck1', 'Contas').gravar(lista)
    else:
        print(f'{espacos()}Registro nome: {nomeconta} não encontrado!')
    aguardaenter()


def alteramesanotrabalho():
    system("cls")
    cabecalho('Alteração do Ano e/ou Mes de Trabalho')
    mes = leiaint('Digite mes de trabalho: ')
    ano = leiaint('Digite ano de trabalho: ')
    basemesano = list()
    basemesano.append({'mes': mes, 'ano': ano})
    Arquivolista('/Users/carlo/PycharmProjects/fc/basemesano.pck1', 'MesAno').gravar(basemesano)
    print(f'{espacos()}OK. Alterado.')
    aguardaenter()
    return ano, mes, basemesano


def meiossaldo(listameios, listameiossaldo, mestrabalho, anotrabalho):
    while True:
        system("cls")
        cabecalho('SALDO DE CONTAS CORRENTE')
        for x in listameiossaldo:
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                print(f'{espacos()}{x["cod"]} - {x["saldo"]:>10,.2f} - {x["saldofim"]:>10,.2f}')
        print(linha())
        opcao = leiaint('Digite 1 - Cadastrar; 2 - Deletar ou 9 - Sair: ')
        if opcao == 1:
            codmeio = leiameio('Digite código do meio: ', listameios)
            saldomeio = leiafloat('Digite o saldo do meio: ')
            registro = {'cod': codmeio, 'saldo': saldomeio, 'mes': mestrabalho, 'ano': anotrabalho, 'saldofim': 0}
            listameiossaldo.append(registro.copy())
            Arquivolista('/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1', 'MeiosSaldo').gravar(listameiossaldo)
            print(f'{espacos(50)}REGISTRO INSERIDO')
            aguardaenter()
        elif opcao == 2:
            codmeio = leiameio('Digite código do meio: ', listameios)
            for c, x in enumerate(listameiossaldo):
                if x["mes"] == mestrabalho and x["ano"] == anotrabalho and x["cod"] == codmeio:
                    print(f'{espacos(50)}REGISTRO REMOVIDO !')
                    del listameiossaldo[c]
                    Arquivolista('/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1',
                                 'MeiosSaldo').gravar(listameiossaldo)
                    aguardaenter()
                    break
        elif opcao == 9:
            break


def contasprevisto(listacontas, listacontasprevisto, mestrabalho, anotrabalho):
    while True:
        system("cls")
        cabecalho('PREVISÃO DE GASTOS POR CONTA')
        for x in listacontasprevisto:
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                print(f'{espacos()}{x["nome"]:<30} {x["valorprevisto"]:>10,.2f}')
        print(linha())
        opcao = leiaint('Digite 1 - Cadastrar; 2 - Deletar ou 9 - Sair: ')
        if opcao == 1:
            nomeconta = leiaconta('Digite nome da conta: ', listacontas)
            valorprevisto = leiafloat('Digite o valor previsto: ')
            registro = {'nome': nomeconta, 'valorprevisto': valorprevisto, 'mes': mestrabalho, 'ano': anotrabalho}
            listacontasprevisto.append(registro.copy())
            Arquivolista('/Users/carlo/PycharmProjects/fc/basecontasprevisto.pck1',
                         'ContasPrevisto').gravar(listacontasprevisto)
            print(f'{espacos()}REGISTRO INSERIDO')
            aguardaenter()
        elif opcao == 2:
            nomeconta = leiaconta('Digite nome da conta: ', listacontas)
            for c, x in enumerate(listacontasprevisto):
                if x["mes"] == mestrabalho and x["ano"] == anotrabalho and x["nome"] == nomeconta:
                    print(f'{espacos()}REGISTRO REMOVIDO !')
                    del listacontasprevisto[c]
                    Arquivolista('/Users/carlo/PycharmProjects/fc/basecontasprevisto.pck1',
                                 'ContasPrevisto').gravar(listacontasprevisto)
                    aguardaenter()
                    break
        elif opcao == 9:
            break


def contaprovisaosaldo(listacontas, listacontaprovisaosaldo, mestrabalho, anotrabalho, listatrans):
    while True:
        system("cls")
        cabecalho('SALDO DE CONTAS PROVISAO')
        saldoinirec = realizadorec = saldofimrec = 0
        saldoinides = realizadodes = saldofimdes = 0
        print(f'{espacos()}{"CONTA":<30} {"SALDO INI":>10} - {"REALIZADO":>10} {"SALDO FIM":>10}')
        for x in listacontaprovisaosaldo:
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                tipoconta = list(filter(lambda conta: conta["nome"] == x["nome"], listacontas))[0]["tipo"]
                if tipoconta in ('R', 'E'):
                    saldoinirec += x["saldoini"]
                    saldofimrec += x["saldofim"]
                    realizadorec += x['realizado']
                elif tipoconta == 'D':
                    saldoinides += x["saldoini"]
                    saldofimdes += x["saldofim"]
                    realizadodes += x['realizado']
                print(f'{espacos()}{x["nome"]:<30} {x["saldoini"]:>10,.2f} {x["realizado"]:>10,.2f}'
                      f' {x["saldofim"]:>10,.2f}')
        print(linha(80))
        print(f'{espacos()}{"TOTAL RECEITAS":<30} {saldoinirec:>10,.2f} {realizadorec:>10,.2f} {saldofimrec:>10,.2f}')
        print(f'{espacos()}{"TOTAL DESPESAS":<30} {saldoinides:>10,.2f} {realizadodes:>10,.2f} {saldofimdes:>10,.2f}')
        print(linha(80))
        print(f'{espacos()}{"TOTAL PROVISAO":<30} {(saldoinirec+saldoinides):>10,.2f}'
              f' {(realizadorec+realizadodes):>10,.2f}'
              f' {(saldofimrec+saldofimdes):>10,.2f}')
        print(linha(80))
        opcao = leiaint('Digite 1 - Cadastrar; 2 - Deletar; 3 - Update ou 9 - Sair: ')
        if opcao == 1:
            nomeconta = leiaconta('Digite nome da conta: ', listacontas)
            saldoconta = leiafloat('Digite o saldo da conta: ')
            registro = {'nome': nomeconta, 'saldoini': saldoconta, 'mes': mestrabalho, 'ano': anotrabalho,
                        'realizado': 0, 'saldofim': 0}
            listacontaprovisaosaldo.append(registro.copy())
            Arquivolista('/Users/carlo/PycharmProjects/fc/basecontaprovisaosaldo.pck1',
                         'ContaProvisaoSaldo').gravar(listacontaprovisaosaldo)
            print(f'{espacos()}REGISTRO INSERIDO')
            aguardaenter()
        elif opcao == 2:
            nomeconta = leiaconta('Digite nome da conta: ', listacontas)
            for c, x in enumerate(listacontaprovisaosaldo):
                if x["mes"] == mestrabalho and x["ano"] == anotrabalho and x["nome"] == nomeconta:
                    print(f'{espacos()}REGISTRO REMOVIDO !')
                    del listacontaprovisaosaldo[c]
                    Arquivolista('/Users/carlo/PycharmProjects/fc/basecontaprovisaosaldo.pck1',
                                 'ContaProvisaoSaldo').gravar(listacontaprovisaosaldo)
                    aguardaenter()
                    break
        elif opcao == 3:
            for x in listacontaprovisaosaldo:
                if x['mes'] == mestrabalho and x['ano'] == anotrabalho:
                    realtemp = 0
                    for y in listatrans:
                        if y['mes'] == mestrabalho and y['ano'] == anotrabalho \
                                and y['conta'] == x['nome'] and y['meio'] == 'PR':
                            realtemp -= y['valor']
                    x['realizado'] = realtemp
                    x['saldofim'] = x['saldoini'] + realtemp
            Arquivolista('/Users/carlo/PycharmProjects/fc/basecontaprovisaosaldo.pck1',
                         'ContaProvisaoSaldo').gravar(listacontaprovisaosaldo)
        elif opcao == 9:
            break


def emprestsaldo(listaemprest, mestrabalho, anotrabalho, listatrans):
    while True:
        system("cls")
        cabecalho('SALDO DE EMPRESTIMOS')
        saldoini = realizado = saldofim = 0
        print(f'{espacos()}{"NOME":<30} {"SALDO INI":>10} - {"REALIZADO":>10} {"SALDO FIM":>10}')
        for x in listaemprest:
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                saldoini += x["saldoini"]
                saldofim += x["saldofim"]
                realizado += x['realizado']
                print(f'{espacos()}{x["nome"]:<30} {x["saldoini"]:>10,.2f}'
                      f' {x["realizado"]:>10,.2f} {x["saldofim"]:>10,.2f}')
        print(linha())
        print(f'{espacos()}{"TOTAL EMPRÉSTIMOS: ":<30} {saldoini:>10,.2f} {realizado:>10,.2f} {saldofim:>10,.2f}')
        print(linha())
        opcao = leiaint('Digite 1 - Cadastrar; 2 - Deletar; 3 - Update ou 9 - Sair: ')
        if opcao == 1:
            nomeemprest = input(f'{espacos()}Digite nome do empréstimo: ')
            saldoemprest = leiafloat('Digite o saldo do empréstimo: ')
            registro = {'nome': nomeemprest, 'saldoini': saldoemprest, 'mes': mestrabalho, 'ano': anotrabalho,
                        'realizado': 0, 'saldofim': 0}
            listaemprest.append(registro.copy())
            Arquivolista('/Users/carlo/PycharmProjects/fc/baseemprest.pck1', 'Emprestimos').gravar(listaemprest)
            print(f'{espacos()}REGISTRO INSERIDO')
            aguardaenter()
        elif opcao == 2:
            nomeemprest = input(f'{espacos()}Digite nome do empréstimo: ')
            for c, x in enumerate(listaemprest):
                if x["mes"] == mestrabalho and x["ano"] == anotrabalho and x["nome"] == nomeemprest:
                    print(f'{espacos()}REGISTRO REMOVIDO !')
                    del listaemprest[c]
                    Arquivolista('/Users/carlo/PycharmProjects/fc/baseemprest.pck1', 'Emprestimos').gravar(listaemprest)
                    aguardaenter()
                    break
        elif opcao == 3:
            for x in listaemprest:
                if x['mes'] == mestrabalho and x['ano'] == anotrabalho:
                    realtemp = 0
                    for y in listatrans:
                        if y['mes'] == mestrabalho and y['ano'] == anotrabalho \
                                and x['nome'] == y['nomeemprest']:
                            realtemp -= y['valor']
                    x['realizado'] = realtemp
                    x['saldofim'] = x['saldoini'] + realtemp
            Arquivolista('/Users/carlo/PycharmProjects/fc/baseemprest.pck1', 'Emprestimos').gravar(listaemprest)
        elif opcao == 9:
            break
