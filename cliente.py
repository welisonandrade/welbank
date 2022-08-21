class Cliente():
    __slots__= ['_nome', '_cpf', '_senha']

    def __init__(self, nome, cpf, senha ='pass'):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha

    def __str__(self):
        pass