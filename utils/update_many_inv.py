from sys import path
from lib.arquivos import *
from lib.interface import *
path.append('C:/Users/carlo/PycharmProjects/fc)')

arqlistainvest = Arquivolista('/Users/carlo/PycharmProjects/fc/baseinvest.pck1', 'Investimentos')
listainvest = arqlistainvest.ler()

mes = leiaint('digite o mes: ', 0)
ano = leiaint('digite o ano: ', 0)
invest = ''
while True:
    invest = input('Digite nome do investimento ou <SAIR>: ')
    if invest.upper() == 'SAIR':
        break
    valor = leiafloat('Digite o valor unitário final: ', 0)
    for x in listainvest:
        if x['ano'] == ano and x['mes'] == mes and x['nomeinvest'] == invest:
            x['vlrunifim'] = valor
            if x['qtdefim'] == 0:
                x['qtdefim'] = x['qtdeini']
                x['vlrtotfim'] = x['qtdeini'] * valor
            else:
                x['vlrtotfim'] = x['qtdefim'] * valor
            print(x, 'ALTERADO !')
opcao = leiaint('Digite 1 para confirmar ou 2 para abortar', 0)
if opcao == 1:
    arqlistainvest.gravar(listainvest)
    print('FEITO')
else:
    print('ABORTADO')
aguardaenter(0)
