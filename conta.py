from historico import Historico
from banco import Banco
import random


class Conta:
    _total_conta = 0

    __slots__= ['_titular', '_saldo', '_limite', '_historico', '_senha', '_numero_conta']
    
    def __init__(self, titular, saldo, limite=1000.0):
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._senha = titular._senha
        self._numero_conta = random.randint(10000,99999)
        Conta._total_conta += 1

    #é um metodo da classe e n do objeto
    @staticmethod
    def get_TC():
        return Conta._total_conta

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self,numero):
        self._numero = numero

    
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self,titular):
        self._titular = titular
    

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,saldo):
        self._saldo = saldo

    
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self,limite):
        self._limite = limite


    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self,historico):
        self._historico = historico


    def deposita(self, valor):
        self._saldo += valor
        self.historico.transacoes.append("Depósito de {} foi realizado.".format(valor))
        return True

    def extrato(self):
        print('O seu saldo é de:', self._saldo)

    def saca(self, valor, controle=0):
        if controle != 1:
            if valor > 0:
                if valor > self._saldo:
                    return False
                else:
                    self._saldo -= valor
                    self._historico.transacoes.append(
                        "Saque de {} foi realizado.".format(valor))
                    return True
        else:
            if valor > 0:
                if valor > self._saldo:
                    return False
                else:
                    self._saldo -= valor
                    return True

    def transfere(self, destino, valor):
        controle = 1
        retirou = self.saca(valor, controle)
        if retirou:
            destino.deposita(valor)
            self.historico.transacoes.append(
                'Valor de {} foi transferido para {}'.format(valor, destino.titular._nome))
            return True
        else:
            return False