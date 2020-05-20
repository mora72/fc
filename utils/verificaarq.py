# zera valor, qtde de investimentos iniciados no mês

from lib.arquivos import *


arqlistainvest = Arquivolista('/Users/carlo/PycharmProjects/fc/baseinvest.pck1', 'Investimentos')
listainvest = arqlistainvest.ler()
for i, x in enumerate(listainvest):
    if x['mesiniinvest'] == 3 and x['anoiniinvest'] == 2020 and x['vlruniini'] > 0:
        print(i, x)
        x['vlrtotini'] = 0
        x['qtdeini'] = 0
        x['vlruniini'] = 0
arqlistainvest.gravar(listainvest)
