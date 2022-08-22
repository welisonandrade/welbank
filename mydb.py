import mysql.connector
class My_db:
    def __init__(self):

        self.con = mysql.connector.connect(host='localhost', database='bank_db', user='root',password='youtubercg13')

    def inicia (self):
        sql = '''CREATE DATABASE IF NOT EXISTS bank_db;'''
        sql2 = '''CREATE TABLE IF NOT EXISTS bank_account(cpf VARCHAR(11) PRIMARY KEY, nome VARCHAR(16), senha VARCHAR(15), saldo VARCHAR(15), nmr_conta VARCHAR(15));'''
        
        self.cursor = self.con.cursor()
        self.cursor.execute(sql)
        self.cursor.execute(sql2)

    def executa(self):
        if self.con.is_connected():
            db_info = self.con.get_server_info()
            print("Conectado ao servidor MySQL versão ", db_info)

        else:
            print("Erro")
    
    def insere(self,cpf, nome, senha, saldo, n_conta):
        try:
            sql = '''INSERT INTO bank_account (cpf, nome, senha, saldo, nmr_conta) VALUES (%s, %s, %s, %s, %s);'''
            '''a = str(p.titular.cpf)
            b = str(p.titular.nome)
            c = str(p.titular.senha)
            d = str(p.saldo)
            e = str(p.numero_conta)'''

            val = (cpf, nome, senha, saldo, n_conta)
            self.cursor.execute(sql,val)
            self.con.commit()

        except:
            return False

    def selecionaCPF(self,cpf):
         self.cursor.execute('SELECT * FROM Cadastro WHERE cpf = {};'.format(str(cpf)))
         try:
            result = self.cursor.fetchone()
            return result
         except:
             return False

    def fecha(self):
        self.cursor.close()
        self.con.close()