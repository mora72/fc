from lib.arquivos import *

arqlistatrans = Arquivolista('/Users/carlo/PycharmProjects/fc/basetrans.pck1', 'Transações')
listatrans = arqlistatrans.ler()

meios = set(x['meio'] for x in listatrans)
for y in meios:
    print(y)
