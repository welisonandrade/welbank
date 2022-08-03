# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_sacar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Sacar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgb(40, 42, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welbank_sacar_label = QtWidgets.QLabel(self.centralwidget)
        self.welbank_sacar_label.setGeometry(QtCore.QRect(235, -15, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.welbank_sacar_label.setFont(font)
        self.welbank_sacar_label.setObjectName("welbank_sacar_label")
        self.sentence = QtWidgets.QLabel(self.centralwidget)
        self.sentence.setGeometry(QtCore.QRect(175, 62, 291, 31))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(21)
        font.setItalic(True)
        self.sentence.setFont(font)
        self.sentence.setObjectName("sentence")
        self.copyr_sacar_label = QtWidgets.QLabel(self.centralwidget)
        self.copyr_sacar_label.setGeometry(QtCore.QRect(10, 429, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(21)
        font.setItalic(False)
        self.copyr_sacar_label.setFont(font)
        self.copyr_sacar_label.setObjectName("copyr_sacar_label")
        self.voltar_sacar_button = QtWidgets.QPushButton(self.centralwidget)
        self.voltar_sacar_button.setGeometry(QtCore.QRect(552, 422, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.voltar_sacar_button.setFont(font)
        self.voltar_sacar_button.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.voltar_sacar_button.setObjectName("voltar_sacar_button")
        self.line_sacar = QtWidgets.QFrame(self.centralwidget)
        self.line_sacar.setGeometry(QtCore.QRect(-23, 99, 711, 20))
        self.line_sacar.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_sacar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_sacar.setObjectName("line_sacar")
        self.valor_sacar_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.valor_sacar_edit.setGeometry(QtCore.QRect(361, 238, 111, 25))
        self.valor_sacar_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valor_sacar_edit.setObjectName("valor_sacar_edit")
        self.valor_sacar_label = QtWidgets.QLabel(self.centralwidget)
        self.valor_sacar_label.setGeometry(QtCore.QRect(159, 240, 171, 21))
        self.valor_sacar_label.setObjectName("valor_sacar_label")
        self.sacar_sacar_button = QtWidgets.QPushButton(self.centralwidget)
        self.sacar_sacar_button.setGeometry(QtCore.QRect(251, 320, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sacar_sacar_button.setFont(font)
        self.sacar_sacar_button.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.sacar_sacar_button.setObjectName("sacar_sacar_button")
        self.telasaque_sacar_label = QtWidgets.QLabel(self.centralwidget)
        self.telasaque_sacar_label.setGeometry(QtCore.QRect(230, 150, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.telasaque_sacar_label.setFont(font)
        self.telasaque_sacar_label.setObjectName("telasaque_sacar_label")
        self.line_sacar_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_sacar_2.setGeometry(QtCore.QRect(0, 402, 711, 20))
        self.line_sacar_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_sacar_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_sacar_2.setObjectName("line_sacar_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welbank_sacar_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f8f8f2;\">WEL</span><span style=\" color:#ffde00;\">BANK</span></p></body></html>"))
        self.sentence.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#f8f8f2;\">Modernidade e simplicidade é aqui.</span></p></body></html>"))
        self.copyr_sacar_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#f8f8f2;\">&copy;welisoncopyright</span></p></body></html>"))
        self.voltar_sacar_button.setText(_translate("MainWindow", "Voltar"))
        self.valor_sacar_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">VALOR DO SAQUE:</span></p></body></html>"))
        self.sacar_sacar_button.setText(_translate("MainWindow", "Confirmar saque"))
        self.telasaque_sacar_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">TELA DE SAQUE</span></p><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Sacar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())