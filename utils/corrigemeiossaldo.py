from sys import path
from lib.arquivos import *
from lib.interface import aguardaenter
path.append('C:/Users/carlo/PycharmProjects/fc)')

arqlistameiossaldo = Arquivolista('/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1', 'Meios Saldo')
listameiossaldo = arqlistameiossaldo.ler()


for c, x in enumerate(listameiossaldo):
    print(f'{c} {x}')

opcao = int(input('Digite 1 para confirmar ou 2 para abortar'))
if opcao == 1:
    arqlistameiossaldo.gravar(listameiossaldo)
    print('FEITO')
else:
    print('ABORTADO')
aguardaenter()
