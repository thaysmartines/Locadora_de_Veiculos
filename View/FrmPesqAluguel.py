from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.AluguelCTR import AluguelCTR
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

class Ui_FrmPesqAluguel(object):
    def DevolverVeiculo(self):
        linha = self.gridAluguel.currentItem().row()
        codigoAlug = self.gridAluguel.item(linha, 0).text()
        dataDevol = self.edtDevolucao.text()
        valorMulta = self.edtMulta.text()
        kmSaida = self.edtSaida.text()

        aluguelCTR = AluguelCTR()
        aluguelCTR.DevolverVeiculo(codigoAlug, dataDevol, valorMulta, kmSaida)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Veículo devolvido!")
        msg.setWindowTitle("Devolver Veículo")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        self.edtDevolucao.setText('')
        self.edtMulta.setText('')
        self.edtSaida.setText('')

    def PesquisarAluguel(self, valor, tipo):
        if valor == '':
            self.PesquisarTodosAluguel()
        else:
            aluguel = AluguelCTR()
            query = aluguel.PesquisarAluguel(valor, tipo)

            while self.gridAluguel.rowCount() > 0:
                self.gridAluguel.removeRow(0)

            row = 0
            while query.next():
                self.gridAluguel.insertRow(row)
                codigoAlug = QTableWidgetItem(str(query.value(0)))
                nomecliente = QTableWidgetItem(str(query.value(10)))
                dataAlug = QTableWidgetItem(str(query.value(1)))
                dataPrazo = QTableWidgetItem(str(query.value(2)))
                dataDevolucao = QTableWidgetItem(str(query.value(3)))
                valorAluguel = QTableWidgetItem(str(query.value(4)))
                valorMulta = QTableWidgetItem(str(query.value(5)))
                kmEntrada = QTableWidgetItem(str(query.value(6)))
                kmSaida = QTableWidgetItem(str(query.value(7)))

                self.gridAluguel.setItem(row, 0, codigoAlug)
                self.gridAluguel.setItem(row, 1, nomecliente)
                self.gridAluguel.setItem(row, 2, dataAlug)
                self.gridAluguel.setItem(row, 3, dataPrazo)
                self.gridAluguel.setItem(row, 4, dataDevolucao)
                self.gridAluguel.setItem(row, 5, valorAluguel)
                self.gridAluguel.setItem(row, 6, valorMulta)
                self.gridAluguel.setItem(row, 7, kmEntrada)
                self.gridAluguel.setItem(row, 8, kmSaida)

                row = row + 1

        self.edtPesquisa.setText('')

    def PesquisarTodosAluguel(self):
        aluguel = AluguelCTR()
        query = aluguel.PesquisarTodosAluguel()

        while self.gridAluguel.rowCount() > 0:
            self.gridAluguel.removeRow(0)

        row = 0
        while query.next():
            self.gridAluguel.insertRow(row)
            codigoAlug = QTableWidgetItem(str(query.value(0)))
            nomecliente = QTableWidgetItem(str(query.value(10)))
            dataAlug = QTableWidgetItem(str(query.value(1)))
            dataPrazo = QTableWidgetItem(str(query.value(2)))
            dataDevolucao = QTableWidgetItem(str(query.value(3)))
            valorAluguel = QTableWidgetItem(str(query.value(4)))
            valorMulta = QTableWidgetItem(str(query.value(5)))
            kmEntrada = QTableWidgetItem(str(query.value(6)))
            kmSaida = QTableWidgetItem(str(query.value(7)))

            self.gridAluguel.setItem(row, 0, codigoAlug)
            self.gridAluguel.setItem(row, 1, nomecliente)
            self.gridAluguel.setItem(row, 2, dataAlug)
            self.gridAluguel.setItem(row, 3, dataPrazo)
            self.gridAluguel.setItem(row, 4, dataDevolucao)
            self.gridAluguel.setItem(row, 5, valorAluguel)
            self.gridAluguel.setItem(row, 6, valorMulta)
            self.gridAluguel.setItem(row, 7, kmEntrada)
            self.gridAluguel.setItem(row, 8, kmSaida)

            row = row + 1

    def setupUi(self, FrmPesqAluguel):
        FrmPesqAluguel.setObjectName("FrmPesqAluguel")
        FrmPesqAluguel.setFixedSize(519, 365)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/btnListAluguel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmPesqAluguel.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(FrmPesqAluguel)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 501, 71))
        self.groupBox.setObjectName("groupBox")
        self.cbPesquisa = QtWidgets.QComboBox(self.groupBox)
        self.cbPesquisa.setGeometry(QtCore.QRect(10, 40, 161, 22))
        self.cbPesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesquisa.setObjectName("cbPesquisa")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.edtPesquisa = QtWidgets.QLineEdit(self.groupBox)
        self.edtPesquisa.setGeometry(QtCore.QRect(180, 40, 221, 20))
        self.edtPesquisa.setObjectName("edtPesquisa")

        # BTN PESQUISA
        self.btnPesquisa = QtWidgets.QPushButton(self.groupBox)
        self.btnPesquisa.setGeometry(QtCore.QRect(404, 10, 91, 51))
        self.btnPesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisa.setIcon(icon1)
        self.btnPesquisa.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisa.setObjectName("btnPesquisa")
        # BTN PESQUISAR CLICK #
        self.btnPesquisa.clicked.connect(lambda: self.PesquisarAluguel(self.edtPesquisa.text(), self.cbPesquisa.currentText()))

        self.gridAluguel = QtWidgets.QTableWidget(FrmPesqAluguel)
        self.gridAluguel.setGeometry(QtCore.QRect(10, 80, 501, 192))
        self.gridAluguel.setObjectName("gridAluguel")
        self.gridAluguel.setColumnCount(9)
        self.gridAluguel.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(8, item)

        # AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desalitar editar
        self.gridAluguel.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.gridAluguel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.gridAluguel.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.groupBox_2 = QtWidgets.QGroupBox(FrmPesqAluguel)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 501, 80))
        self.groupBox_2.setObjectName("groupBox_2")

        # BTN DEVOLVER
        self.btnDevolver = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDevolver.setGeometry(QtCore.QRect(394, 10, 101, 61))
        self.btnDevolver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagens/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDevolver.setIcon(icon2)
        self.btnDevolver.setIconSize(QtCore.QSize(30, 30))
        self.btnDevolver.setObjectName("btnDevolver")
        # btn DEVOLVER click
        self.btnDevolver.clicked.connect(lambda: self.DevolverVeiculo())

        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName("label")
        self.edtDevolucao = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtDevolucao.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.edtDevolucao.setObjectName("edtDevolucao")
        self.edtMulta = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtMulta.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.edtMulta.setObjectName("edtMulta")
        self.edtSaida = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtSaida.setGeometry(QtCore.QRect(250, 40, 113, 20))
        self.edtSaida.setObjectName("edtSaida")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 46, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 46, 13))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(FrmPesqAluguel)
        QtCore.QMetaObject.connectSlotsByName(FrmPesqAluguel)

        self.PesquisarTodosAluguel()

    def retranslateUi(self, FrmPesqAluguel):
        FrmPesqAluguel.setWindowTitle("Lista de Aluguéis")
        self.groupBox.setTitle("Selecione o Tipo de Pesquisa")
        self.cbPesquisa.setItemText(0, "Código Aluguel")
        self.cbPesquisa.setItemText(1, "Código Cliente")
        self.cbPesquisa.setItemText(2, "Código Veículo")
        self.cbPesquisa.setItemText(3, "Nome Cliente")
        self.btnPesquisa.setText("Pesquisar")
        item = self.gridAluguel.horizontalHeaderItem(0)
        item.setText("Código Aluguel")
        item = self.gridAluguel.horizontalHeaderItem(1)
        item.setText("Nome Cliente")
        item = self.gridAluguel.horizontalHeaderItem(2)
        item.setText("Data Aluguel")
        item = self.gridAluguel.horizontalHeaderItem(3)
        item.setText("Data Prazo")
        item = self.gridAluguel.horizontalHeaderItem(4)
        item.setText("Data Devolução")
        item = self.gridAluguel.horizontalHeaderItem(5)
        item.setText("Valor Aluguel")
        item = self.gridAluguel.horizontalHeaderItem(6)
        item.setText("Valor Multa")
        item = self.gridAluguel.horizontalHeaderItem(7)
        item.setText("Km Entrada")
        item = self.gridAluguel.horizontalHeaderItem(8)
        item.setText("Km Saída")
        self.groupBox_2.setTitle("Devolver Veículo")
        self.btnDevolver.setText("Devolver")
        self.label.setText("Data Devolução")
        self.label_2.setText("Multa")
        self.label_3.setText("Km Saída")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPesqAluguel = QtWidgets.QDialog()
    ui = Ui_FrmPesqAluguel()
    ui.setupUi(FrmPesqAluguel)
    FrmPesqAluguel.show()
    sys.exit(app.exec_())
