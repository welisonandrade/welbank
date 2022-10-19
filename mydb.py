from click import command
import mysql.connector
class My_db:
    def __init__(self):

        self.con = mysql.connector.connect(host='localhost', database='bank_db', user='root',password='youtubercg13')

    def inicia (self):
        sql = '''CREATE DATABASE IF NOT EXISTS bank_db;'''
        sql2 = '''USE bank_db;'''
        sql3 = '''CREATE TABLE IF NOT EXISTS bank_account(cpf VARCHAR(11) PRIMARY KEY, nome VARCHAR(16), senha VARCHAR(15), saldo VARCHAR(15), nmr_conta VARCHAR(15));'''
        
        self.cursor = self.con.cursor()
        self.cursor.execute(sql)
        self.cursor.execute(sql2)
        self.cursor.execute(sql3)
        self.cursor = self.con.cursor(buffered=True)

    def executa(self):
        if self.con.is_connected():
            db_info = self.con.get_server_info()
            print("Conectado ao servidor MySQL versão ", db_info)

        else:
            print("Erro")
    
    def insere(self,cpf, nome, senha, saldo, n_conta):
        try:
            sql = '''INSERT INTO bank_account (cpf, nome, senha, saldo, nmr_conta) VALUES (%s, %s, %s, %s, %s);'''

            val = (cpf, nome, senha, saldo, n_conta)
            self.cursor.execute(sql,val)
            self.con.commit()

        except:
            return False

    def selecionaBD(self,coluna,cpf):
        try:
            string = 'SELECT {} FROM bank_account WHERE cpf = "{}";'.format(str(coluna),str(cpf))
            self.cursor.execute(string)
            result = self.cursor.fetchone()
            return result
        except:
            print("false")
            return False

    def updateSaldo(self, saldo, cpf):
        string = 'UPDATE bank_account SET saldo = "{}" WHERE cpf = "{}";'.format(str(saldo),str(cpf))

        self.cursor.execute(string)
        self.con.commit()

    def fecha(self):
        self.cursor.close()
        self.con.close()