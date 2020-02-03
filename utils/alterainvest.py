from sys import path
from lib.arquivos import *
from lib.interface import aguardaenter
path.append('C:/Users/carlo/PycharmProjects/fc)')

arqlistainvest = Arquivolista('/Users/carlo/PycharmProjects/fc/baseinvest.pck1', 'Investimentos')
listainvest = arqlistainvest.ler()

listainvest[40]['vlruniini'] = 7825.61
listainvest[40]['vlrtotini'] = 7825.61
print(listainvest[40])
opcao = int(input('Digite 1 para confirmar ou 2 para abortar'))
if opcao == 1:
    arqlistainvest.gravar(listainvest)
    print('FEITO')
else:
    print('ABORTADO')
aguardaenter()
