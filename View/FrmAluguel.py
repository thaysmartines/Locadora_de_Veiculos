from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Controller.AluguelCTR import AluguelCTR
from Controller.ClienteCTR import ClienteCTR
from Controller.VeiculoCTR import VeiculoCTR
from PyQt5.QtWidgets import QAbstractItemView


class Ui_FrmAluguel(object):
    # CLICK BTN_SALVAR
    def btnSalvar_Click(self):
        linha = self.gridCliente.currentItem().row()
        codigoCli = self.gridCliente.item(linha, 0).text()
        linha = self.gridVeiculo.currentItem().row()
        codigoVeic = self.gridVeiculo.item(linha, 0).text()

        DataAluguel = self.EdtDataAluguel.text()
        DataPrazo = self.EdtPrazo.text()
        DataDevolucao = self.EdtDataDev.text()
        ValorAluguel = self.EdtValor.text()
        ValorMulta = self.EdtMulta.text()
        KmEntrada = self.EdtkmEntrada.text()
        KmSaida = self.EdtKmSaida.text()

        aluguel = AluguelCTR()
        aluguel.CadastrarAluguel(DataAluguel, DataPrazo, DataDevolucao, ValorAluguel,
                      ValorMulta, KmEntrada, KmSaida, codigoCli, codigoVeic)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Aluguel cadastrado com sucesso!")
        msg.setWindowTitle("Cadastro de  Aluguel")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        self.EdtDataAluguel.setText('')
        self.EdtPrazo.setText('')
        self.EdtDataDev.setText('')
        self.EdtValor.setText('')
        self.EdtMulta.setText('')
        self.EdtkmEntrada.setText('')
        self.EdtKmSaida.setText('')

    def PesquisarTodosClientes(self):
        cliente = ClienteCTR()
        query = cliente.PesquisarTodosClientes()

        while self.gridCliente.rowCount() > 0:
            self.gridCliente.removeRow(0)

        row = 0
        while query.next():
            self.gridCliente.insertRow(row)
            codCli = QtWidgets.QTableWidgetItem(str(query.value(0)))
            nome = QtWidgets.QTableWidgetItem(str(query.value(1)))
            cpf = QtWidgets.QTableWidgetItem(str(query.value(2)))
            endereco = QtWidgets.QTableWidgetItem(str(query.value(3)))
            email = QtWidgets.QTableWidgetItem(str(query.value(4)))
            telefone = QtWidgets.QTableWidgetItem(str(query.value(5)))

            self.gridCliente.setItem(row, 0, codCli)
            self.gridCliente.setItem(row, 1, nome)
            self.gridCliente.setItem(row, 2, cpf)
            self.gridCliente.setItem(row, 3, endereco)
            self.gridCliente.setItem(row, 4, email)
            self.gridCliente.setItem(row, 5, telefone)

            row = row + 1

    def PesquisarCliente(self, valor, tipo):
        if valor == '':
            self.PesquisarTodosClientes()
        else:
            cliente = ClienteCTR()
            query = cliente.PesquisarCliente(valor, tipo)

            while self.gridCliente.rowCount() > 0:
                self.gridCliente.removeRow(0)

            row = 0
            while query.next():
                self.gridCliente.insertRow(row)
                codCli = QtWidgets.QTableWidgetItem(str(query.value(0)))
                nome = QtWidgets.QTableWidgetItem(str(query.value(1)))
                cpf = QtWidgets.QTableWidgetItem(str(query.value(2)))
                endereco = QtWidgets.QTableWidgetItem(str(query.value(3)))
                email = QtWidgets.QTableWidgetItem(str(query.value(4)))
                telefone = QtWidgets.QTableWidgetItem(str(query.value(5)))

                self.gridCliente.setItem(row, 0, codCli)
                self.gridCliente.setItem(row, 1, nome)
                self.gridCliente.setItem(row, 2, cpf)
                self.gridCliente.setItem(row, 3, endereco)
                self.gridCliente.setItem(row, 4, email)
                self.gridCliente.setItem(row, 5, telefone)

                row = row + 1

    def PesquisarVeiculo(self, valor, tipo):
        if valor == '':
            self.PesquisarVeiculosDisponiveis()
        else:
            veiculo = VeiculoCTR()
            query = veiculo.PesquisarVeiculo(valor, tipo)

            while self.gridVeiculo.rowCount() > 0:
                self.gridVeiculo.removeRow(0)

            row = 0
            while query.next():
                self.gridVeiculo.insertRow(row)
                codigoVeic = QtWidgets.QTableWidgetItem(str(query.value(0)))
                modelo = QtWidgets.QTableWidgetItem(str(query.value(1)))
                marca = QtWidgets.QTableWidgetItem(str(query.value(2)))
                anoModelo = QtWidgets.QTableWidgetItem(str(query.value(3)))
                placa = QtWidgets.QTableWidgetItem(str(query.value(4)))
                alugado = QtWidgets.QTableWidgetItem(str(query.value(5)))
                batido = QtWidgets.QTableWidgetItem(str(query.value(6)))
                kmAtual = QtWidgets.QTableWidgetItem(str(query.value(7)))
                valorDiaria = QtWidgets.QTableWidgetItem(str(query.value(8)))
                descricao = QtWidgets.QTableWidgetItem(str(query.value(9)))
                tipoVeiculo = QtWidgets.QTableWidgetItem(str(query.value(10)))

                self.gridVeiculo.setItem(row, 0, codigoVeic)
                self.gridVeiculo.setItem(row, 1, modelo)
                self.gridVeiculo.setItem(row, 2, marca)
                self.gridVeiculo.setItem(row, 3, anoModelo)
                self.gridVeiculo.setItem(row, 4, placa)
                self.gridVeiculo.setItem(row, 5, alugado)
                self.gridVeiculo.setItem(row, 6, batido)
                self.gridVeiculo.setItem(row, 7, kmAtual)
                self.gridVeiculo.setItem(row, 8, valorDiaria)
                self.gridVeiculo.setItem(row, 9, descricao)
                self.gridVeiculo.setItem(row, 10, tipoVeiculo)

                row = row + 1

    def PesquisarVeiculosDisponiveis(self):
        veiculo = VeiculoCTR()
        query = veiculo.PesquisarVeiculosDisponiveis()

        while self.gridVeiculo.rowCount() > 0:
            self.gridVeiculo.removeRow(0)

        row = 0
        while query.next():
            self.gridVeiculo.insertRow(row)
            codigoVeic = QtWidgets.QTableWidgetItem(str(query.value(0)))
            modelo = QtWidgets.QTableWidgetItem(str(query.value(1)))
            marca = QtWidgets.QTableWidgetItem(str(query.value(2)))
            anoModelo = QtWidgets.QTableWidgetItem(str(query.value(3)))
            placa = QtWidgets.QTableWidgetItem(str(query.value(4)))
            alugado = QtWidgets.QTableWidgetItem(str(query.value(5)))
            batido = QtWidgets.QTableWidgetItem(str(query.value(6)))
            kmAtual = QtWidgets.QTableWidgetItem(str(query.value(7)))
            valorDiaria = QtWidgets.QTableWidgetItem(str(query.value(8)))
            descricao = QtWidgets.QTableWidgetItem(str(query.value(9)))
            tipoVeiculo = QtWidgets.QTableWidgetItem(str(query.value(10)))

            self.gridVeiculo.setItem(row, 0, codigoVeic)
            self.gridVeiculo.setItem(row, 1, modelo)
            self.gridVeiculo.setItem(row, 2, marca)
            self.gridVeiculo.setItem(row, 3, anoModelo)
            self.gridVeiculo.setItem(row, 4, placa)
            self.gridVeiculo.setItem(row, 5, alugado)
            self.gridVeiculo.setItem(row, 6, batido)
            self.gridVeiculo.setItem(row, 7, kmAtual)
            self.gridVeiculo.setItem(row, 8, valorDiaria)
            self.gridVeiculo.setItem(row, 9, descricao)
            self.gridVeiculo.setItem(row, 10, tipoVeiculo)

            row = row + 1

    def setupUi(self, FrmAluguel):
        FrmAluguel.setObjectName("FrmAluguel")
        FrmAluguel.setFixedSize(521, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/btnAlugaVeiculo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmAluguel.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(FrmAluguel)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 501, 60))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(380, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(140, 60, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(260, 60, 91, 16))
        self.label_7.setObjectName("label_7")

        self.EdtDataAluguel = QtWidgets.QLineEdit(self.groupBox)
        self.EdtDataAluguel.setGeometry(QtCore.QRect(20, 30, 111, 20))
        self.EdtDataAluguel.setObjectName("EdtDataAluguel")

        self.EdtPrazo = QtWidgets.QLineEdit(self.groupBox)
        self.EdtPrazo.setGeometry(QtCore.QRect(140, 30, 113, 20))
        self.EdtPrazo.setObjectName("EdtPrazo")

        self.EdtDataDev = QtWidgets.QLineEdit(self.groupBox)
        self.EdtDataDev.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.EdtDataDev.setObjectName("EdtDataDev")
        self.EdtDataDev.setDisabled(True)

        self.EdtValor = QtWidgets.QLineEdit(self.groupBox)
        self.EdtValor.setGeometry(QtCore.QRect(260, 30, 113, 20))
        self.EdtValor.setObjectName("EdtValor")

        self.EdtMulta = QtWidgets.QLineEdit(self.groupBox)
        self.EdtMulta.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.EdtMulta.setObjectName("EdtMulta")
        self.EdtMulta.setDisabled(True)

        self.EdtkmEntrada = QtWidgets.QLineEdit(self.groupBox)
        self.EdtkmEntrada.setGeometry(QtCore.QRect(380, 30, 113, 20))
        self.EdtkmEntrada.setObjectName("EdtkmEntrada")

        self.EdtKmSaida = QtWidgets.QLineEdit(self.groupBox)
        self.EdtKmSaida.setGeometry(QtCore.QRect(260, 80, 113, 20))
        self.EdtKmSaida.setObjectName("EdtKmSaida")
        self.EdtKmSaida.setDisabled(True)

        self.groupBox_2 = QtWidgets.QGroupBox(FrmAluguel)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 501, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_8.setObjectName("label_8")
        self.cbPesqCliente = QtWidgets.QComboBox(self.groupBox_2)

        # cb Pesquisar Cliente
        self.cbPesqCliente.setGeometry(QtCore.QRect(10, 40, 111, 22))
        self.cbPesqCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesqCliente.setObjectName("cbPesqCliente")
        self.cbPesqCliente.addItem("")
        self.cbPesqCliente.addItem("")
        self.cbPesqCliente.addItem("")
        self.EdtPesqCliente = QtWidgets.QLineEdit(self.groupBox_2)
        self.EdtPesqCliente.setGeometry(QtCore.QRect(130, 40, 261, 20))
        self.EdtPesqCliente.setObjectName("EdtPesqCliente")

        # BTN PESQ CLIENTE
        self.btnPesqCliente = QtWidgets.QPushButton(self.groupBox_2)
        self.btnPesqCliente.setGeometry(QtCore.QRect(400, 30, 91, 31))
        self.btnPesqCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesqCliente.setIcon(icon1)
        self.btnPesqCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnPesqCliente.setObjectName("btnPesqCliente")
        # BTN PESQ CLIENTE CLICK
        self.btnPesqCliente.clicked.connect(lambda: self.PesquisarCliente(self.EdtPesqCliente.text(), self.cbPesqCliente.currentText()))

        # GRID CLIENTE
        self.gridCliente = QtWidgets.QTableWidget(self.groupBox_2)
        self.gridCliente.setGeometry(QtCore.QRect(10, 70, 481, 96))
        self.gridCliente.setObjectName("gridCliente")
        self.gridCliente.setColumnCount(6)
        self.gridCliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(5, item)
        # AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desabilitar editar
        self.gridCliente.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridCliente.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.gridCliente.setSelectionMode(QAbstractItemView.SingleSelection)

        self.groupBox_3 = QtWidgets.QGroupBox(FrmAluguel)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 250, 501, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_9.setObjectName("label_9")
        self.cbPesqVeic = QtWidgets.QComboBox(self.groupBox_3)

        # cb Pesquisar Veiculo
        self.cbPesqVeic.setGeometry(QtCore.QRect(10, 40, 111, 22))
        self.cbPesqVeic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesqVeic.setObjectName("cbPesqVeic")
        self.cbPesqVeic.addItem("")
        self.cbPesqVeic.addItem("")
        self.cbPesqVeic.addItem("")
        self.EdtPesqVeiculo = QtWidgets.QLineEdit(self.groupBox_3)
        self.EdtPesqVeiculo.setGeometry(QtCore.QRect(130, 40, 261, 20))
        self.EdtPesqVeiculo.setObjectName("EdtPesqVeiculo")

        # BTN PESQUISAR VEICULO
        self.btnPesqVeic = QtWidgets.QPushButton(self.groupBox_3)
        self.btnPesqVeic.setGeometry(QtCore.QRect(400, 30, 91, 31))
        self.btnPesqVeic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPesqVeic.setIcon(icon1)
        self.btnPesqVeic.setIconSize(QtCore.QSize(30, 30))
        self.btnPesqVeic.setObjectName("btnPesqVeic")
        # BTN PESQ VEIC CLICK
        self.btnPesqVeic.clicked.connect(lambda: self.PesquisarVeiculo(self.EdtPesqVeiculo.text(), self.cbPesqVeic.currentText()))

        # GRID VEICULO
        self.gridVeiculo = QtWidgets.QTableWidget(self.groupBox_3)
        self.gridVeiculo.setGeometry(QtCore.QRect(10, 70, 481, 96))
        self.gridVeiculo.setObjectName("gridVeiculo")
        self.gridVeiculo.setColumnCount(11)
        self.gridVeiculo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(10, item)
        # AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desabilitar editar
        self.gridVeiculo.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridVeiculo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.gridVeiculo.setSelectionMode(QAbstractItemView.SingleSelection)

        self.pushButton = QtWidgets.QPushButton(FrmAluguel)
        self.pushButton.setGeometry(QtCore.QRect(10, 430, 91, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagens/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.btnSalvar_Click)

        self.retranslateUi(FrmAluguel)
        QtCore.QMetaObject.connectSlotsByName(FrmAluguel)

    def retranslateUi(self, FrmAluguel):
        _translate = QtCore.QCoreApplication.translate
        FrmAluguel.setWindowTitle(_translate("FrmAluguel", "Aluguel de Veículos"))
        self.label.setText(_translate("FrmAluguel", "Data de Aluguel:"))
        self.label_2.setText(_translate("FrmAluguel", "Prazo de Devolução:"))
        self.label_3.setText(_translate("FrmAluguel", "Valor do Aluguel:"))
        self.label_4.setText(_translate("FrmAluguel", "KM de Entrada:"))
        self.label_5.setText(_translate("FrmAluguel", "Multa:"))
        self.label_6.setText(_translate("FrmAluguel", "KM de Saída:"))
        self.label_7.setText(_translate("FrmAluguel", "Data Devolução:"))
        self.label_8.setText(_translate("FrmAluguel", "Pesquisar Cliente:"))
        self.cbPesqCliente.setItemText(0, _translate("FrmAluguel", "Código"))
        self.cbPesqCliente.setItemText(1, _translate("FrmAluguel", "Nome"))
        self.cbPesqCliente.setItemText(2, _translate("FrmAluguel", "CPF"))
        self.btnPesqCliente.setText(_translate("FrmAluguel", "Pesquisar"))
        item = self.gridCliente.horizontalHeaderItem(0)
        item.setText(_translate("FrmAluguel", "Código"))
        item = self.gridCliente.horizontalHeaderItem(1)
        item.setText(_translate("FrmAluguel", "Nome"))
        item = self.gridCliente.horizontalHeaderItem(2)
        item.setText(_translate("FrmAluguel", "CPF"))
        item = self.gridCliente.horizontalHeaderItem(3)
        item.setText(_translate("FrmAluguel", "Endereço"))
        item = self.gridCliente.horizontalHeaderItem(4)
        item.setText(_translate("FrmAluguel", "Email"))
        item = self.gridCliente.horizontalHeaderItem(5)
        item.setText(_translate("FrmAluguel", "Telefone"))
        self.label_9.setText(_translate("FrmAluguel", "Pesquisar Veículo:"))
        self.cbPesqVeic.setItemText(0, _translate("FrmAluguel", "Código"))
        self.cbPesqVeic.setItemText(1, _translate("FrmAluguel", "Modelo"))
        self.cbPesqVeic.setItemText(2, _translate("FrmAluguel", "Marca"))
        self.btnPesqVeic.setText(_translate("FrmAluguel", "Pesquisar"))
        item = self.gridVeiculo.horizontalHeaderItem(0)
        item.setText(_translate("FrmAluguel", "Código"))
        item = self.gridVeiculo.horizontalHeaderItem(1)
        item.setText(_translate("FrmAluguel", "Modelo"))
        item = self.gridVeiculo.horizontalHeaderItem(2)
        item.setText(_translate("FrmAluguel", "Marca"))
        item = self.gridVeiculo.horizontalHeaderItem(3)
        item.setText(_translate("FrmAluguel", "Ano/Modelo"))
        item = self.gridVeiculo.horizontalHeaderItem(4)
        item.setText(_translate("FrmAluguel", "Placa"))
        item = self.gridVeiculo.horizontalHeaderItem(5)
        item.setText(_translate("FrmAluguel", "Alugado"))
        item = self.gridVeiculo.horizontalHeaderItem(6)
        item.setText(_translate("FrmAluguel", "Batido"))
        item = self.gridVeiculo.horizontalHeaderItem(7)
        item.setText(_translate("FrmAluguel", "KM Atual"))
        item = self.gridVeiculo.horizontalHeaderItem(8)
        item.setText(_translate("FrmAluguel", "Valor da Diária"))
        item = self.gridVeiculo.horizontalHeaderItem(9)
        item.setText(_translate("FrmAluguel", "Descrição"))
        item = self.gridVeiculo.horizontalHeaderItem(10)
        item.setText(_translate("FrmAluguel", "Tipo Veículo"))

# Executar o aplicativo
if __name__ == "__main__":
    import sys
    app = QtWidgets.QGuiApplication(sys.argv)
    FrmAluguel = QtWidgets.QWidget()
    ui = Ui_FrmAluguel()
    ui.setupUi(FrmAluguel)
    FrmAluguel.show()
    sys.exit(app.exec_())
