from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from Controller.VeiculoCTR import VeiculoCTR
from View.FrmVeiculos import Ui_frmVeiculos

class Ui_frmPesqVeiculos(object):
    def AlterarVeiculo_Click(self):
        linha = self.gridVeiculos.currentItem().row()
        codigoVeic = self.gridVeiculos.item(linha, 0).text()
        modelo = self.gridVeiculos.item(linha, 1).text()
        marca = self.gridVeiculos.item(linha, 2).text()
        anoModelo = self.gridVeiculos.item(linha, 3).text()
        placa = self.gridVeiculos.item(linha, 4).text()
        alugado = self.gridVeiculos.item(linha, 5).text()
        batido = self.gridVeiculos.item(linha, 6).text()
        kmAtual = self.gridVeiculos.item(linha, 7).text()
        valorDiaria = self.gridVeiculos.item(linha, 8).text()
        descricao = self.gridVeiculos.item(linha, 9).text()
        tipoVeiculo = self.gridVeiculos.item(linha, 10).text()

        self.frmVeiculos = QtWidgets.QMainWindow()
        self.ui = Ui_frmVeiculos()
        self.ui.setupUi(self.frmVeiculos, 'alterar', codigoVeic)
        self.ui.PreencherAlterar(modelo, marca, anoModelo, placa, alugado, batido, kmAtual, valorDiaria, descricao, tipoVeiculo)
        self.frmVeiculos.show()

    def ExcluirVeiculo_Click(self):
        linha = self.gridVeiculos.currentItem().row()
        codigoVeic = self.gridVeiculos.item(linha, 0).text()

        self.gridVeiculos.removeRow(linha)
        veiculo = VeiculoCTR()
        veiculo.ExcluirVeiculo(codigoVeic)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Veículo Excluído!")
        msg.setWindowTitle("Excluir Veículo")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def PesquisarVeiculo(self, valor, tipo):
        if (valor == '') and (tipo != 'Disponível') and (tipo != 'Alugado'):
            self.PesquisarTodosVeiculos()
        else:
            veiculo = VeiculoCTR()
            query = veiculo.PesquisarVeiculo(valor, tipo)

            while (self.gridVeiculos.rowCount() > 0):
                self.gridVeiculos.removeRow(0)

            row = 0
            while query.next():
                self.gridVeiculos.insertRow(row)
                codigoVeic = QTableWidgetItem(str(query.value(0)))
                modelo = QTableWidgetItem(str(query.value(1)))
                marca = QTableWidgetItem(str(query.value(2)))
                anoModelo = QTableWidgetItem(str(query.value(3)))
                placa = QTableWidgetItem(str(query.value(4)))
                alugado = QTableWidgetItem(str(query.value(5)))
                batido = QTableWidgetItem(str(query.value(6)))
                kmAtual = QTableWidgetItem(str(query.value(7)))
                valorDiaria = QTableWidgetItem(str(query.value(8)))
                descricao = QTableWidgetItem(str(query.value(9)))
                tipoVeiculo = QTableWidgetItem(str(query.value(10)))

                self.gridVeiculos.setItem(row, 0, codigoVeic)
                self.gridVeiculos.setItem(row, 1, modelo)
                self.gridVeiculos.setItem(row, 2, marca)
                self.gridVeiculos.setItem(row, 3, anoModelo)
                self.gridVeiculos.setItem(row, 4, placa)
                self.gridVeiculos.setItem(row, 5, alugado)
                self.gridVeiculos.setItem(row, 6, batido)
                self.gridVeiculos.setItem(row, 7, kmAtual)
                self.gridVeiculos.setItem(row, 8, valorDiaria)
                self.gridVeiculos.setItem(row, 9, descricao)
                self.gridVeiculos.setItem(row, 10, tipoVeiculo)

                row = row + 1

        self.edtPesquisa.setText('')

    def PesquisarTodosVeiculos(self):
        veiculo = VeiculoCTR()
        query = veiculo.PesquisarTodosVeiculos()

        while (self.gridVeiculos.rowCount() > 0):
            self.gridVeiculos.removeRow(0)

        row = 0
        while query.next():
            self.gridVeiculos.insertRow(row)
            codigoVeic = QTableWidgetItem(str(query.value(0)))
            modelo = QTableWidgetItem(str(query.value(1)))
            marca = QTableWidgetItem(str(query.value(2)))
            anoModelo = QTableWidgetItem(str(query.value(3)))
            placa = QTableWidgetItem(str(query.value(4)))
            alugado = QTableWidgetItem(str(query.value(5)))
            batido = QTableWidgetItem(str(query.value(6)))
            kmAtual = QTableWidgetItem(str(query.value(7)))
            valorDiaria = QTableWidgetItem(str(query.value(8)))
            descricao = QTableWidgetItem(str(query.value(9)))
            tipoVeiculo = QTableWidgetItem(str(query.value(10)))

            self.gridVeiculos.setItem(row, 0, codigoVeic)
            self.gridVeiculos.setItem(row, 1, modelo)
            self.gridVeiculos.setItem(row, 2, marca)
            self.gridVeiculos.setItem(row, 3, anoModelo)
            self.gridVeiculos.setItem(row, 4, placa)
            self.gridVeiculos.setItem(row, 5, alugado)
            self.gridVeiculos.setItem(row, 6, batido)
            self.gridVeiculos.setItem(row, 7, kmAtual)
            self.gridVeiculos.setItem(row, 8, valorDiaria)
            self.gridVeiculos.setItem(row, 9, descricao)
            self.gridVeiculos.setItem(row, 10, tipoVeiculo)

            row = row + 1

    def setupUi(self, frmPesqVeiculos):
        frmPesqVeiculos.setObjectName("frmPesqVeiculos")
        frmPesqVeiculos.setFixedSize(820, 504)

        self.gridVeiculos = QtWidgets.QTableWidget(frmPesqVeiculos)
        self.gridVeiculos.setGeometry(QtCore.QRect(10, 150, 800, 291))
        self.gridVeiculos.setObjectName("gridVeiculos")
        self.gridVeiculos.setColumnCount(11)
        self.gridVeiculos.setRowCount(0)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(7, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(8, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(9, item)
        item = QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(10, item)
        self.gridVeiculos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.gridVeiculos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.gridVeiculos.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.edtPesquisa = QtWidgets.QLineEdit(frmPesqVeiculos)
        self.edtPesquisa.setGeometry(QtCore.QRect(190, 60, 621, 20))
        self.edtPesquisa.setObjectName("edtPesquisa")
        self.cbPesquisa = QtWidgets.QComboBox(frmPesqVeiculos)
        self.cbPesquisa.setGeometry(QtCore.QRect(20, 60, 161, 22))
        self.cbPesquisa.setObjectName("cbPesquisa")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.label = QtWidgets.QLabel(frmPesqVeiculos)
        self.label.setGeometry(QtCore.QRect(20, 30, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnPesquisar = QtWidgets.QPushButton(frmPesqVeiculos)
        self.btnPesquisar.setGeometry(QtCore.QRect(700, 90, 111, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisar.setObjectName("btnPesquisar")
        self.btnPesquisar.clicked.connect(lambda: self.PesquisarVeiculo(self.edtPesquisa.text(), self.cbPesquisa.currentText()))

        self.lblTotal = QtWidgets.QLabel(frmPesqVeiculos)
        self.lblTotal.setGeometry(QtCore.QRect(20, 450, 111, 16))
        self.lblTotal.setObjectName("lblTotal")

        self.btnExcluir = QtWidgets.QPushButton(frmPesqVeiculos)
        self.btnExcluir.setGeometry(QtCore.QRect(720, 450, 91, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagens/excluir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluir.setIcon(icon1)
        self.btnExcluir.setIconSize(QtCore.QSize(30, 30))
        self.btnExcluir.setObjectName("btnExcluir")
        self.btnExcluir.clicked.connect(lambda: self.ExcluirVeiculo_Click())

        self.btnAlterar = QtWidgets.QPushButton(frmPesqVeiculos)
        self.btnAlterar.setGeometry(QtCore.QRect(610, 450, 101, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagens/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlterar.setIcon(icon2)
        self.btnAlterar.setIconSize(QtCore.QSize(35, 35))
        self.btnAlterar.setObjectName("btnAlterar")
        self.btnAlterar.clicked.connect(lambda: self.AlterarVeiculo_Click())

        self.retranslateUi(frmPesqVeiculos)
        QtCore.QMetaObject.connectSlotsByName(frmPesqVeiculos)

        self.PesquisarTodosVeiculos()

    def retranslateUi(self, frmPesqVeiculos):
        frmPesqVeiculos.setWindowTitle("Lista de Veículo")
        item = self.gridVeiculos.horizontalHeaderItem(0)
        item.setText("Código")
        item = self.gridVeiculos.horizontalHeaderItem(1)
        item.setText("Modelo")
        item = self.gridVeiculos.horizontalHeaderItem(2)
        item.setText("Marca")
        item = self.gridVeiculos.horizontalHeaderItem(3)
        item.setText("Ano")
        item = self.gridVeiculos.horizontalHeaderItem(4)
        item.setText("Placa")
        item = self.gridVeiculos.horizontalHeaderItem(5)
        item.setText("Alugado")
        item = self.gridVeiculos.horizontalHeaderItem(6)
        item.setText("Batido")
        item = self.gridVeiculos.horizontalHeaderItem(7)
        item.setText("Quilometragem")
        item = self.gridVeiculos.horizontalHeaderItem(8)
        item.setText("Valor da Diária")
        item = self.gridVeiculos.horizontalHeaderItem(9)
        item.setText("Descrição")
        item = self.gridVeiculos.horizontalHeaderItem(10)
        item.setText("Tipo do Veículo")
        self.cbPesquisa.setItemText(0, "Código")
        self.cbPesquisa.setItemText(1, "Marca")
        self.cbPesquisa.setItemText(2, "Modelo")
        self.cbPesquisa.setItemText(3, "Disponível")
        self.cbPesquisa.setItemText(4, "Alugado")
        self.label.setText("Selecione o Tipo de Pesquisa:")
        self.btnPesquisar.setText("Pesquisar")
        self.lblTotal.setText("TextLabel")
        self.btnExcluir.setText("Excluir")
        self.btnAlterar.setText("Alterar")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmPesqVeiculos = QtWidgets.QMainWindow()
    ui = Ui_frmPesqVeiculos()
    ui.setupUi(frmPesqVeiculos)
    frmPesqVeiculos.show()
    sys.exit(app.exec_())

