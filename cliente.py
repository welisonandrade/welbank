class Cliente():
    __slots__= ['_nome','_sobrenome', '_cpf', '_senha']

    def __init__(self, nome, sobrenome, cpf, senha ='pass'):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._senha = senha

    def __str__(self):
        pass