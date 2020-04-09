# Programa Principal
from sys import path
from lib.menusetup import *
from lib.menutransacoes import *
from lib.menuresumos import *
from lib.menuinvestimentos import *
from lib.newmonth import *
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
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

basemesano = Arquivolista('/Users/carlo/PycharmProjects/fc/basemesano.pck1', 'MesAno').ler()

mesatual = date.today().month
anoatual = date.today().year

if len(basemesano) == 0:
    mestrabalho = mesatual
    anotrabalho = anoatual
    basemesano.append({'mes': mesatual, 'ano': anoatual})
else:
    mestrabalho = basemesano[0]['mes']
    anotrabalho = basemesano[0]['ano']

while True:
    system("cls")
    bordasup(1)
    cabecalho(f'                                                          GESTÃO  DE  FINANÇAS  PESSOAIS'
              f'                                                        {mestrabalho}/{anotrabalho}', 172, 0)
    exiberesumomeiossaldo(listameios, listameiossaldo, listacontasprevisto, listacontas, listatrans,
                          listacontaprovisaosaldo, listainvest, mestrabalho, anotrabalho)
    opcao = main_menu()
    if opcao == 'F':
        system("cls")
        break
    if opcao == 'S':
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
                anotrabalho, mestrabalho, basemesano = alteramesanotrabalho()
            if opcao1 == 8:
                meiossaldo(listameios, listameiossaldo, mestrabalho, anotrabalho)
            if opcao1 == 9:
                contasprevisto(listacontas, listacontasprevisto, mestrabalho, anotrabalho)
            if opcao1 == 10:
                mestrabalho, anotrabalho = gonewmonth(listameios, listameiossaldo, listacontaprovisaosaldo,
                                                      listainvest, listaemprest, listacontasprevisto, mestrabalho,
                                                      anotrabalho)

    if opcao == 'T':
        trans(listatrans, mestrabalho, anotrabalho, listacontas, listameiossaldo, listameios, listaemprest)
    if opcao == 'A':
        resumomes(listatrans, mestrabalho, anotrabalho, listacontas, listacontasprevisto)
    if opcao == 'P':
        contaprovisaosaldo(listacontas, listacontaprovisaosaldo, mestrabalho, anotrabalho, listatrans)
    if opcao == 'I':
        invest(listainvest, mestrabalho, anotrabalho)
    if opcao == 'E':
        emprestsaldo(listaemprest, mestrabalho, anotrabalho, listatrans)
    if opcao == 'B':
        resumo_patrimonio(listameios, listameiossaldo, listainvest, listacontaprovisaosaldo, mestrabalho, anotrabalho)


arqlistameios.gravar(listameios)
arqlistameiossaldo.gravar(listameiossaldo)
arqlistacontas.gravar(listacontas)
arqlistacontasprevisto.gravar(listacontasprevisto)
arqlistacontaprovisaosaldo.gravar(listacontaprovisaosaldo)
arqlistatrans.gravar(listatrans)
arqlistainvest.gravar(listainvest)
arqlistaemprest.gravar(listaemprest)
Arquivolista('/Users/carlo/PycharmProjects/fc/basemesano.pck1', 'MesAno').gravar(basemesano)
