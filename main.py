#import weakref
#from matplotlib.animation import AbstractMovieWriter
import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from tela_inicio import Tela_Inicio
from tela_cadastro import Tela_Cadastro
from tela_login import Tela_Login
from tela_depositar import Tela_Depositar
from tela_sacar import Tela_Sacar
from tela_transferir import Tela_Transferir
from tela_usuario import Tela_Usuario
from tela_historico import Tela_Historico
from mydb import My_db

class Ui_main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.tela_inicio = Tela_Inicio()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack2)

        self.tela_usuario = Tela_Usuario()
        self.tela_usuario.setupUi(self.stack3)

        self.tela_sacar = Tela_Sacar()
        self.tela_sacar.setupUi(self.stack4)

        self.tela_depositar = Tela_Depositar()
        self.tela_depositar.setupUi(self.stack5)

        self.tela_transferir = Tela_Transferir()
        self.tela_transferir.setupUi(self.stack6)

        self.tela_historico = Tela_Historico()
        self.tela_historico.setupUi(self.stack7)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)


class Main(QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        

        #self.welbank = Banco()
        self.db = My_db()
        self.db.inicia()
        self.db.executa()

        self.tela_inicio.criar_conta_button.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicio.logar_conta_button.clicked.connect(self.abrirTelaLogin)
        self.tela_inicio.sair_inicio_button.clicked.connect(self.sair)

        self.tela_cadastro.cad_cad_button.clicked.connect(self.botaoCadastrar)
        self.tela_cadastro.voltar_cad_button.clicked.connect(self.voltarInicio)

        self.tela_login.entrar_login_button.clicked.connect(self.botaoLogar)
        self.tela_login.voltar_login_button.clicked.connect(self.voltarInicio)

        self.tela_usuario.sair_user_button.clicked.connect(self.abrirTelaInicio)
        self.tela_usuario.sacar_user_button.clicked.connect(self.abrirTelaSacar)
        self.tela_usuario.depositar_user_button.clicked.connect(self.abrirTelaDepositar)

        self.tela_sacar.sacar_sacar_button.clicked.connect(self.botaoSacar)
        self.tela_sacar.voltar_sacar_button.clicked.connect(self.voltarUsuario)

        self.tela_depositar.depositar_dep_button.clicked.connect(self.botaoDepositar)
        self.tela_depositar.voltar_dep_button.clicked.connect(self.voltarUsuario)

        self.tela_usuario.transferir_user_button.clicked.connect(self.abrirTelaTransferir)
        self.tela_usuario.historico_user_button.clicked.connect(self.abrirTelaHistorico)

        self.tela_transferir.transferir_dep_button.clicked.connect(self.botaoTransferir)
        self.tela_transferir.voltar_trans_button.clicked.connect(self.voltarUsuario)

        self.tela_historico.voltar_dep_button.clicked.connect(self.voltarUsuario)


    def botaoCadastrar(self):
        nome = self.tela_cadastro.nome_cad_edit.text()
        cpf = self.tela_cadastro.cpf_cad_edit.text()
        senha = self.tela_cadastro.senha_cad_edit.text()

        if not (nome == '' or cpf == '' or senha == ''):

            if (cpf.isnumeric()):
                saldo = 10.0
                n_conta = random.randint(100000,999999)

                if(self.db.insere(cpf, nome, senha, saldo, n_conta)!= False):
                    QMessageBox.information(None,'WELBANK', 'Cadastro realizado!')
                    self.tela_cadastro.nome_cad_edit.setText('')
                    self.tela_cadastro.cpf_cad_edit.setText('')
                    self.tela_cadastro.senha_cad_edit.setText('')
                    self.abrirTelaInicio()
                else:
                    QMessageBox.information(None, 'WELBANK', 'Esse CPF já está cadastrado!')
                    self.tela_cadastro.nome_cad_edit.setText('')
                    self.tela_cadastro.cpf_cad_edit.setText('')
                    self.tela_cadastro.senha_cad_edit.setText('')
            else:
                QMessageBox.information(None, 'WELBANK', 'CPF deve conter apenas números!')
                self.tela_cadastro.nome_cad_edit.setText('')
                self.tela_cadastro.cpf_cad_edit.setText('')
                self.tela_cadastro.senha_cad_edit.setText('')

        else:
            QMessageBox.information(None, 'Welison', 'Todos os campos precisam ser preenchidos!')
            self.tela_cadastro.nome_cad_edit.setText('')
            self.tela_cadastro.cpf_cad_edit.setText('')
            self.tela_cadastro.senha_cad_edit.setText('')


    def botaoLogar(self):
        self.cpf = self.tela_login.cpf_login_edit.text()
        self.senha = self.tela_login.senha_login_edit.text()
        
        try:
            self.usuario = self.db.selecionaBD("*", self.cpf)
            self.user = list(self.usuario)
            
            if not (self.cpf == ''  or self.senha == ''):

                if((self.cpf == self.user[0]) and (self.senha == self.user[2])):            
                    QMessageBox.information(None, 'WELBANK', 'Login realizado!')
                    self.tela_cadastro.nome_cad_edit.setText('')
                    self.tela_cadastro.cpf_cad_edit.setText('')
                    self.tela_cadastro.senha_cad_edit.setText('')
                    self.abrirTelaUsuario()
                else:
                    QMessageBox.information(None, 'WELBANK', 'CPF e/ou senha incorreto(s)!')
                    self.tela_login.cpf_login_edit.setText('')
                    self.tela_login.senha_login_edit.setText('')

            else:
                QMessageBox.information(None, 'Welison', 'Todos os campos precisam ser preenchidos!')
                self.tela_login.cpf_login_edit.setText('')
                self.tela_login.senha_login_edit.setText('')
        except:
            QMessageBox.information(None, 'Welison', 'Usuário inexistente!')
            self.tela_login.cpf_login_edit.setText('')
            self.tela_login.senha_login_edit.setText('')

    
    def botaoSacar(self):
        valor = self.tela_sacar.valor_sacar_edit.text()
        try:
            valor = float(valor)
            if(valor > 0):
                verifica = self.saca(valor, self.user)
                if(verifica):
                    string = 'Saque de R$:' + str(valor) + ' realizado!'
                    QMessageBox.information(None, 'WELBANK', string)
                    self.tela_sacar.valor_sacar_edit.setText('')
                else:
                    QMessageBox.information(None, 'WELBANK', 'Valor informado é maior que saldo!')
                    self.tela_sacar.valor_sacar_edit.setText('')
            else:
                QMessageBox.information(None, 'WELBANK', 'Digite apenas valores positivos maiores que zero!')
                self.tela_sacar.valor_sacar_edit.setText('')
        except:
            QMessageBox.information(None, 'WELBANK', 'Informe apenas números!')
            self.tela_sacar.valor_sacar_edit.setText('')


    def botaoDepositar(self):
        valor = self.tela_depositar.valor_dep_edit.text()
        try:
            valor = float(valor)
            float(self.user[3])
            if(valor > 0):
                if(self.deposita(valor, self.user)):
                    string = 'Valor de R$: ' + str(valor) + ' depositado'
                    QMessageBox.information(None, 'WELBANK', string)
                    self.tela_depositar.valor_dep_edit.setText('')
            else:
                QMessageBox.information(None, 'WELBANK', 'Digite apenas valores positivos maiores que zero!')
                self.tela_depositar.valor_dep_edit.setText('')        
        except:
            QMessageBox.information(None, 'WELBANK', 'Informe apenas números!')
            self.tela_depositar.valor_dep_edit.setText('')

    def botaoTransferir(self):
        self.cpfDestino = self.tela_transferir.cpfdestino_trans_edit.text()
        self.valorTransf = self.tela_transferir.valor_trans_edit.text()
        self.usuarioDestino = self.db.selecionaBD("*", str(self.cpfDestino))
        verifica = isinstance(self.usuarioDestino, tuple)
        
        try:
            self.valorTransf = float(self.valorTransf)

            if (verifica):
                self.userDestino = list(self.usuarioDestino)
                if (self.userDestino[0] != self.user[0]):
                    if (self.valorTransf > 0):
                        if(self.transfere(self.valorTransf, self.user, self.userDestino)):
                            string = 'Transferência de R$: ' + str(self.valorTransf) + ' realizada!'
                            QMessageBox.information(None, 'WELBANK', string)
                            self.tela_transferir.cpfdestino_trans_edit.setText('')
                            self.tela_transferir.valor_trans_edit.setText('')
                        else:
                            QMessageBox.information(None, 'WELBANK', 'Erro na transferência. Valor maior que saldo!')
                            self.tela_transferir.cpfdestino_trans_edit.setText('')
                            self.tela_transferir.valor_trans_edit.setText('')
                    else:
                        QMessageBox.information(None, 'WELBANK', 'Erro na transferência. Valor negativo digitado.')
                        self.tela_transferir.cpfdestino_trans_edit.setText('')
                        self.tela_transferir.valor_trans_edit.setText('')
                else:
                    QMessageBox.information(None, 'WELBANK', 'Impossível transferir pra mesma conta!')
                    self.tela_transferir.cpfdestino_trans_edit.setText('')
                    self.tela_transferir.valor_trans_edit.setText('')
            else:
                QMessageBox.information(None, 'WELBANK', 'Erro na transferência. Conta inexistente!')
                self.tela_transferir.cpfdestino_trans_edit.setText('')
                self.tela_transferir.valor_trans_edit.setText('')
        except:
            QMessageBox.information(None, 'WELBANK', 'Informe apenas números!')
            self.tela_transferir.cpfdestino_trans_edit.setText('')
            self.tela_transferir.valor_trans_edit.setText('')

    def abrirTelaInicio(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaLogin(self):
        self.tela_login.cpf_login_edit.setText('')
        self.tela_login.senha_login_edit.setText('')
        self.QtStack.setCurrentIndex(2)

    def abrirTelaUsuario(self):
        '''for item in self.welbank._contasLogaveis:
            if (item._titular._cpf == conta._titular._cpf):
                numero_conta = str(item._numero_conta)     '''
        
        self.QtStack.setCurrentIndex(3)
        self.tela_usuario.nconta_user_edit.setText(str(self.user[4]))
        self.tela_usuario.nome_user_edit.setText(str(self.user[1]))
        self.tela_usuario.cpf_user_edit.setText(str(self.user[0]))
        self.tela_usuario.saldo_user_edit.setText('R$: ' + str(self.user[3]))

    def abrirTelaSacar(self):
        self.QtStack.setCurrentIndex(4)

    def abrirTelaDepositar(self):
        self.QtStack.setCurrentIndex(5)

    def abrirTelaTransferir(self):
        self.QtStack.setCurrentIndex(6)

    def abrirTelaHistorico(self):
        QMessageBox.information(None, 'WELBANK', 'Essa opção ainda não está disponível.')
        '''self.QtStack.setCurrentIndex(7)
        for item  in self.user.historico.transacoes:
            self.tela_historico.hist_hist_listwidget.addItem(item)'''

    def voltarInicio(self):
        self.QtStack.setCurrentIndex(0)

    def voltarUsuario(self):
        self.abrirTelaUsuario()
        self.QtStack.setCurrentIndex(3)

    def saca(self,valor,conta):
        conta[3] = float(conta[3])

        if(valor > conta[3]):
            return False
        else:
            conta[3] -= valor
            saldo = str(conta[3])
            cpf = str(conta[0])
            self.db.updateSaldo(saldo,cpf)
            return True


    def deposita(self, valor,conta):
        float(valor)
        conta[3] += valor
        self.db.updateSaldo(conta[3],conta[0])
        return True

    
    def transfere(self, valor, conta, contaDestino):
        retirou = self.saca(valor, conta)
        if (retirou):
            self.deposita(valor, contaDestino)
            return True
        else:
            return False

    def sair(self):
        sys.exit(app.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec())