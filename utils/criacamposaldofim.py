from sys import path
from lib.arquivos import *
from lib.interface import aguardaenter
path.append('C:/Users/carlo/PycharmProjects/fc)')

arqlistameiossaldo = Arquivolista('/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1', 'Meios Saldo')
listameiossaldo = arqlistameiossaldo.ler()
print(listameiossaldo[0])
print(listameiossaldo[1])
print(listameiossaldo[2])
print(listameiossaldo[3])
print(len(listameiossaldo))
listanova = []
for c, x in enumerate(listameiossaldo):
    x['saldofim'] = 0
    listanova.append(x.copy())
    print(f'REG {c} ALTERADO')

print(listanova[0])
print(listanova[1])
print(listanova[2])
print(listanova[3])
print(len(listanova))
opcao = int(input('Digite 1 para confirmar ou 2 para abortar'))
if opcao == 1:
    arqlistameiossaldo.gravar(listanova)
    print('FEITO')
else:
    print('ABORTADO')
aguardaenter()
