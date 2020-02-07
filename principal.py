# Programa Principal
# from datetime import date
from sys import path
from lib.arquivos import *
from lib.menusetup import *
from lib.menutransacoes import *
from lib.menuresumos import *
from lib.menuinvestimentos import *
from lib.newmonth import *
path.append('C:/Users/carlo/PycharmProjects/fc)')

arqlistameios = Arquivolista('/Users/carlo/PycharmProjects/fc/basemeios.pck1', 'Meios')
listameios = arqlistameios.ler()

arqlistameiossaldo = Arquivolista('/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1', 'MeiosSaldo')
listameiossaldo = arqlistameiossaldo.ler()

arqlistacontas = Arquivolista('/Users/carlo/PycharmProjects/fc/basecontas.pck1', 'Contas')
listacontas = arqlistacontas.ler()

arqlistacontasprevisto = Arquivolista('/Users/carlo/PycharmProjects/fc/basecontasprevisto.pck1', 'ContasPrevisto')
listacontasprevisto = arqlistacontasprevisto.ler()

arqlistacontaprovisaosaldo = Arquivolista('/Users/carlo/PycharmProjects/fc/basecontaprovisaosaldo.pck1',
                                          'ContaProvisaoSaldo')
listacontaprovisaosaldo = arqlistacontaprovisaosaldo.ler()

arqlistatrans = Arquivolista('/Users/carlo/PycharmProjects/fc/basetrans.pck1', 'Transações')
listatrans = arqlistatrans.ler()

arqlistainvest = Arquivolista('/Users/carlo/PycharmProjects/fc/baseinvest.pck1', 'Investimentos')
listainvest = arqlistainvest.ler()

arqlistaemprest = Arquivolista('/Users/carlo/PycharmProjects/fc/baseemprest.pck1', 'Emprestimos')
listaemprest = arqlistaemprest.ler()

anoatual = date.today().year
mesatual = date.today().month
anotrabalho = anoatual
mestrabalho = mesatual

while True:
    system("cls")
    bordasup(1)
    cabecalho(f'ANO TRABALHO: {anotrabalho} - MES TRABALHO: {mestrabalho}')
    exiberesumomeiossaldo(listameios, listameiossaldo, listacontasprevisto, listacontas, listatrans,
                          listacontaprovisaosaldo, listainvest, mestrabalho, anotrabalho)
    cabecalho('MENU PRINCIPAL')
    opcao = menu(['MENU SETUP',
                  'MENU TRANSAÇÕES',
                  'Resumo do Mês',
                  'Verificações',
                  'Provisões',
                  'Investimentos',
                  'Empréstimos',
                  'Resumo Patrimonial (local e tipo)',
                  'Sair'])
    if opcao == 9:
        system("cls")
        break
    if opcao == 1:
        while True:
            system("cls")
            cabecalho(f'ANO TRABALHO: {anotrabalho} - MES TRABALHO: {mestrabalho}')
            cabecalho('MENU SETUP')
            opcao1 = menu(['Cadastro de Meios de Transação Financeira',
                           'Listar Meios de Transação Financeira',
                           'Deletar Meio de Transação Financeira',
                           'Cadastro de contas de receita ou despesa',
                           'Listar Tipos de Conta de Receita ou Despesa',
                           'Deletar Tipo de Conta de Receita ou Despesa',
                           'Alterar Mes e/ou Ano de Trabalho',
                           'Saldo de Contas Corrente e Dinheiro',
                           'Gasto Previsto por Tipo de Conta',
                           'Gerar Novo Mes/Ano de Trabalho',
                           'Voltar ao Menu Principal'])
            if opcao1 == 11:
                system("cls")
                break
            if opcao1 == 1:
                cadmeios(listameios)
            if opcao1 == 2:
                exibemeios(listameios)
            if opcao1 == 3:
                deletameio(listameios)
            if opcao1 == 4:
                cadcontas(listacontas)
            if opcao1 == 5:
                exibecontas(listacontas)
            if opcao1 == 6:
                deletaconta(listacontas)
            if opcao1 == 7:
                anotrabalho, mestrabalho = alteramesanotrabalho()
            if opcao1 == 8:
                meiossaldo(listameios, listameiossaldo, mestrabalho, anotrabalho)
            if opcao1 == 9:
                contasprevisto(listacontas, listacontasprevisto, mestrabalho, anotrabalho)
            if opcao1 == 10:
                mestrabalho, anotrabalho = gonewmonth(listameios, listameiossaldo, listacontaprovisaosaldo,
                                                      listainvest, listaemprest, mestrabalho, anotrabalho)

    if opcao == 2:
        while True:
            system("cls")
            cabecalho(f'ANO TRABALHO: {anotrabalho} - MES TRABALHO: {mestrabalho}')
            cabecalho('MENU TRANSAÇÕES')
            opcao2 = menu(['Lançamento de Transações - Bancos, Dinheiro, Cartões',
                           'Listar Transações',
                           'Deletar Transações',
                           'Saldo do Meio',
                           'Voltar ao Menu Principal'])
            if opcao2 == 5:
                system("cls")
                break
            if opcao2 == 1:
                lanctrans(listatrans, anotrabalho, mestrabalho, listameios, listacontas)
            if opcao2 == 2:
                exibetrans(listatrans, mestrabalho, anotrabalho, listacontas)
            if opcao2 == 3:
                deletatrans(listatrans, mestrabalho, anotrabalho, listacontas)
            if opcao2 == 4:
                exibetransmeiosaldo(listatrans, listameios, listameiossaldo, mestrabalho, anotrabalho)
    if opcao == 3:
        resumomes(listatrans, mestrabalho, anotrabalho, listacontas, listacontasprevisto)
    if opcao == 5:
        contaprovisaosaldo(listacontas, listacontaprovisaosaldo, mestrabalho, anotrabalho, listatrans)
    if opcao == 6:
        while True:
            system("cls")
            cabecalho(f'ANO TRABALHO: {anotrabalho} - MES TRABALHO: {mestrabalho}')
            cabecalho('MENU INVESTIMENTOS')
            opcao2 = menu(['Lançamento de novos Investimentos',
                           'Listar Investimentos',
                           'Deletar Investimentos',
                           'Alterar saldo final de Investimento',
                           'Voltar ao Menu Principal'])
            if opcao2 == 5:
                system("cls")
                break
            if opcao2 == 1:
                newinvest(listainvest, mestrabalho, anotrabalho)
            if opcao2 == 2:
                exibeinvest(listainvest, mestrabalho, anotrabalho)
            if opcao2 == 3:
                deletainvest(listainvest, mestrabalho, anotrabalho)
            if opcao2 == 4:
                updateinvest(listainvest, mestrabalho, anotrabalho)
    if opcao == 7:
        emprestsaldo(listaemprest, mestrabalho, anotrabalho, listatrans)
    if opcao == 8:
        resumo_patrimonio(listameios, listameiossaldo, listainvest, listacontaprovisaosaldo, mestrabalho, anotrabalho)

arqlistameios.gravar(listameios)
arqlistameiossaldo.gravar(listameiossaldo)
arqlistacontas.gravar(listacontas)
arqlistacontasprevisto.gravar(listacontasprevisto)
arqlistacontaprovisaosaldo.gravar(listacontaprovisaosaldo)
arqlistatrans.gravar(listatrans)
arqlistainvest.gravar(listainvest)
arqlistaemprest.gravar(listaemprest)
