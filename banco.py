class Banco:
    
    def __init__(self):
        self._contasLogaveis = []

    def imprime(self):
        for item in self._contasLogaveis:
            print(item._nome)

    def cadastra(self,conta):

        existe = self.busca(conta._titular._cpf,conta._titular._senha)

        if (existe==None):
            self._contasLogaveis.append(conta)
            return True
        else:
            return False

    def busca(self,cpf,senha):
        for lp in self._contasLogaveis:
            if lp._titular._cpf == cpf:
                if lp._titular._senha == senha:
                    return lp
        return None

    def loga(self,obj):
        for conta in self._contasLogaveis:
            if obj._titular._cpf == conta._cpf:
                if obj._titular._senha == conta._senha:
                    return obj
                else:
                    return False

    def existeCPF(self, cpf):
        for item in self._contasLogaveis:
            if item._titular._cpf == cpf:
                return item
        else:
            False
