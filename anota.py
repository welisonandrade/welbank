'''
#sintaxe de get e set

class Conta:
    def __init__(self,saldo=0.0)

    @property
    def saldo(self,saldo)

    @saldo.setter
    def saldo (self,saldo):
        if(saldo<0):
            print('saldo n pode ser negativo')
        else:
            self._saldo = saldo
'''

'''
#é um metodo da classe e n do objeto
@staticmethod
'''

'''
limita quais atributos serão criados numa classe.

class Conta:
    __slots__ = ['_numero','_titular', '_saldo', '_limite']
'''
