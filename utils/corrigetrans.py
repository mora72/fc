from sys import path
from lib.arquivos import *
from lib.interface import aguardaenter
path.append('C:/Users/carlo/PycharmProjects/fc)')

arqlistatrans = Arquivolista('/Users/carlo/PycharmProjects/fc/basetrans.pck1', 'Transações')
listatrans = arqlistatrans.ler()

for i, x in enumerate(listatrans):
    # listatrans[126]['nomeemprest'] = 'Provisão'
    print(i, x)
opcao = int(input('Digite 1 para confirmar ou 2 para abortar'))
if opcao == 1:
    del listatrans[404]
    del listatrans[403]
    arqlistatrans.gravar(listatrans)
    print('FEITO')
else:
    print('ABORTADO')
aguardaenter()
