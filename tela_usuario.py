# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Usuario(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 480)
        MainWindow.setStyleSheet("background-color: rgb(40, 42, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welbank_user_label = QtWidgets.QLabel(self.centralwidget)
        self.welbank_user_label.setGeometry(QtCore.QRect(235, -15, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.welbank_user_label.setFont(font)
        self.welbank_user_label.setObjectName("welbank_user_label")
        self.sentence_user = QtWidgets.QLabel(self.centralwidget)
        self.sentence_user.setGeometry(QtCore.QRect(175, 62, 291, 31))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(21)
        font.setItalic(True)
        self.sentence_user.setFont(font)
        self.sentence_user.setObjectName("sentence_user")
        self.copyright_user = QtWidgets.QLabel(self.centralwidget)
        self.copyright_user.setGeometry(QtCore.QRect(10, 429, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(21)
        font.setItalic(False)
        self.copyright_user.setFont(font)
        self.copyright_user.setObjectName("copyright_user")
        self.sair_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.sair_user_button.setGeometry(QtCore.QRect(560, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sair_user_button.setFont(font)
        self.sair_user_button.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.sair_user_button.setObjectName("sair_user_button")
        self.line_user = QtWidgets.QFrame(self.centralwidget)
        self.line_user.setGeometry(QtCore.QRect(-23, 110, 711, 20))
        self.line_user.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_user.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_user.setObjectName("line_user")
        self.nome_user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.nome_user_edit.setGeometry(QtCore.QRect(19, 180, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nome_user_edit.setFont(font)
        self.nome_user_edit.setStyleSheet("border: none;\n"
"color: yellow;")
        self.nome_user_edit.setReadOnly(True)
        self.nome_user_edit.setObjectName("nome_user_edit")
        self.welcome_user_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_user_label.setGeometry(QtCore.QRect(19, 145, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_user_label.setFont(font)
        self.welcome_user_label.setObjectName("welcome_user_label")
        self.cpf_user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.cpf_user_edit.setGeometry(QtCore.QRect(170, 340, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cpf_user_edit.setFont(font)
        self.cpf_user_edit.setStyleSheet("color: yellow;")
        self.cpf_user_edit.setReadOnly(True)
        self.cpf_user_edit.setObjectName("cpf_user_edit")
        self.numconta_user_label = QtWidgets.QLabel(self.centralwidget)
        self.numconta_user_label.setGeometry(QtCore.QRect(21, 259, 121, 21))
        self.numconta_user_label.setObjectName("numconta_user_label")
        self.nconta_user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.nconta_user_edit.setGeometry(QtCore.QRect(170, 260, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nconta_user_edit.setFont(font)
        self.nconta_user_edit.setStyleSheet("color: yellow;")
        self.nconta_user_edit.setReadOnly(True)
        self.nconta_user_edit.setObjectName("nconta_user_edit")
        self.cpf_user_label = QtWidgets.QLabel(self.centralwidget)
        self.cpf_user_label.setGeometry(QtCore.QRect(20, 342, 51, 21))
        self.cpf_user_label.setObjectName("cpf_user_label")
        self.tableView_user = QtWidgets.QTableView(self.centralwidget)
        self.tableView_user.setGeometry(QtCore.QRect(415, 119, 231, 291))
        self.tableView_user.setObjectName("tableView_user")
        self.operacoes_user_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.operacoes_user_label_2.setGeometry(QtCore.QRect(460, 145, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.operacoes_user_label_2.setFont(font)
        self.operacoes_user_label_2.setObjectName("operacoes_user_label_2")
        self.saldo_user_label = QtWidgets.QLabel(self.centralwidget)
        self.saldo_user_label.setGeometry(QtCore.QRect(203, 145, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saldo_user_label.setFont(font)
        self.saldo_user_label.setObjectName("saldo_user_label")
        self.depositar_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.depositar_user_button.setGeometry(QtCore.QRect(488, 249, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.depositar_user_button.setFont(font)
        self.depositar_user_button.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.depositar_user_button.setObjectName("depositar_user_button")
        self.transferir_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.transferir_user_button.setGeometry(QtCore.QRect(488, 299, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.transferir_user_button.setFont(font)
        self.transferir_user_button.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.transferir_user_button.setObjectName("transferir_user_button")
        self.sacar_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.sacar_user_button.setGeometry(QtCore.QRect(488, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sacar_user_button.setFont(font)
        self.sacar_user_button.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.sacar_user_button.setObjectName("sacar_user_button")
        self.saldo_user_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.saldo_user_edit.setGeometry(QtCore.QRect(293, 150, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saldo_user_edit.setFont(font)
        self.saldo_user_edit.setStyleSheet("color: yellow;\n border: none")
        self.saldo_user_edit.setFrame(True)
        self.saldo_user_edit.setReadOnly(True)
        self.saldo_user_edit.setObjectName("saldo_user_edit")
        self.line_user_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_user_2.setGeometry(QtCore.QRect(-56, 402, 471, 16))
        self.line_user_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_user_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_user_2.setObjectName("line_user_2")
        self.historico_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.historico_user_button.setGeometry(QtCore.QRect(489, 349, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.historico_user_button.setFont(font)
        self.historico_user_button.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.historico_user_button.setObjectName("historico_user_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welbank_user_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f8f8f2;\">WEL</span><span style=\" color:#ffde00;\">BANK</span></p></body></html>"))
        self.sentence_user.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#f8f8f2;\">Modernidade e simplicidade é aqui.</span></p></body></html>"))
        self.copyright_user.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#f8f8f2;\">&copy;welisoncopyright</span></p></body></html>"))
        self.sair_user_button.setText(_translate("MainWindow", "Sair"))
        self.welcome_user_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">BEM VINDO!</span></p><p><br/></p></body></html>"))
        self.numconta_user_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Nº DA CONTA:</span></p></body></html>"))
        self.cpf_user_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">CPF:</span></p></body></html>"))
        self.operacoes_user_label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">OPERAÇÕES:</span></p><p><br/></p></body></html>"))
        self.saldo_user_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">SALDO:</span></p><p><br/></p></body></html>"))
        self.depositar_user_button.setText(_translate("MainWindow", "Depositar"))
        self.transferir_user_button.setText(_translate("MainWindow", "Transferir"))
        self.sacar_user_button.setText(_translate("MainWindow", "Sacar"))
        self.historico_user_button.setText(_translate("MainWindow", "Histórico"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Usuario()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
