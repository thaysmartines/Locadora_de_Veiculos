import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# local files
from .FrmCliente import Ui_frmCliente
from .frmPesqCliente import Ui_frmPesqCliente
from .FrmVeiculos import Ui_frmVeiculos
from .frmPesqVeiculos import Ui_frmPesqVeiculos
from .FrmAluguel import Ui_FrmAluguel
from .FrmPesqAluguel import Ui_FrmPesqAluguel

class Ui_FrmPrincipal(object):
    # BTN ALUGUEL.CLICK
    def FrmAluguel_Click(self):
        self.frmAluguel = QtWidgets.QMainWindow()
        self.ui = Ui_FrmAluguel()
        
        self.ui.setupUi(self.frmAluguel)
        self.frmAluguel.show()

    # BTN CLIENTE.CLICK
    def FrmCliente_Click(self):
        self.frmCliente = QtWidgets.QMainWindow()
        self.ui = Ui_frmCliente()
        self.ui.setupUi(self.frmCliente, 'inserir', 0)
        self.frmCliente.show()

    # BTN VEICULO.CLICK
    def FrmVeiculo_Click(self):
        self.frmVeiculo = QtWidgets.QMainWindow()
        self.ui = Ui_frmVeiculos()
        self.ui.setupUi(self.frmVeiculo, 'inserir', 0)
        self.frmVeiculo.show()

    # BTN LISTAR TODOS CLIENTES CLICK
    def btnListarCliente_Click(self):
        self.frmPesqCliente = QtWidgets.QMainWindow()
        self.ui = Ui_frmPesqCliente()
        self.ui.setupUi(self.frmPesqCliente)
        self.frmPesqCliente.show()

    # BTN LISTAR TODOS VEICULOS CLICK
    def btnListarVeiculo_Click(self):
        self.frmPesqVeiculo = QtWidgets.QMainWindow()
        self.ui = Ui_frmPesqVeiculos()
        self.ui.setupUi(self.frmPesqVeiculo)
        self.frmPesqVeiculo.show()

    # BTN LISTAR TODOS ALUGUEIS CLICK
    def btnListarAluguel_Click(self):
        self.frmPesqAluguel = QtWidgets.QMainWindow()
        self.ui = Ui_FrmPesqAluguel()
        self.ui.setupUi(self.frmPesqAluguel)
        self.frmPesqAluguel.show()

    def setupUi(self, FrmPrincipal):
        FrmPrincipal.setObjectName("FrmPrincipal")
        FrmPrincipal.setWindowModality(QtCore.Qt.NonModal)

        # DESABILITAR REDIMENCIONAMENTO DA JANELA
        FrmPrincipal.setFixedSize(803, 422)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/FrmIcon_Car.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmPrincipal.setWindowIcon(icon)
        FrmPrincipal.setAutoFillBackground(True)
        FrmPrincipal.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(FrmPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(0, 0, 801, 101))
        self.columnView.setObjectName("columnView")

        # BTN ALUGAR #############
        self.btnAlugar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlugar.setGeometry(QtCore.QRect(10, 10, 131, 81))
        self.btnAlugar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAlugar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAlugar.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagens/btnAlugaVeiculo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlugar.setIcon(icon1)
        self.btnAlugar.setIconSize(QtCore.QSize(40, 40))
        self.btnAlugar.setObjectName("btnAlugar")
        ## BTN ALUGAR CLICK EVENT ######
        self.btnAlugar.clicked.connect(self.FrmAluguel_Click)

        # BTN CLIENTE ###################
        self.btnCliente = QtWidgets.QPushButton(self.centralwidget)
        self.btnCliente.setGeometry(QtCore.QRect(140, 10, 131, 81))
        self.btnCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagens/btnCadCli.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCliente.setIcon(icon2)
        self.btnCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnCliente.setObjectName("btnCliente")
        ## BTN CLIENTE CLICK EVENT  ###
        self.btnCliente.clicked.connect(self.FrmCliente_Click)

        # BTN VEICULO #################
        self.btnVeiculo = QtWidgets.QPushButton(self.centralwidget)
        self.btnVeiculo.setGeometry(QtCore.QRect(270, 10, 131, 81))
        self.btnVeiculo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Imagens/FrmIcon_Car.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnVeiculo.setIcon(icon3)
        self.btnVeiculo.setIconSize(QtCore.QSize(40, 40))
        self.btnVeiculo.setObjectName("btnVeiculo")
        # BTN VEICULO CLICK EVENT ##
        self.btnVeiculo.clicked.connect(self.FrmVeiculo_Click)

        # BTN LISTAR CLIENTE #####################
        self.btnListCliente = QtWidgets.QPushButton(self.centralwidget)
        self.btnListCliente.setGeometry(QtCore.QRect(400, 10, 131, 81))
        self.btnListCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Imagens/btnListCliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("Imagens/btnListClientes.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnListCliente.setIcon(icon4)
        self.btnListCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnListCliente.setObjectName("btnListCliente")
        # BTN LISTAR CLIENTE CLICK ##
        self.btnListCliente.clicked.connect(self.btnListarCliente_Click)

        # BTN LISTAR VEICULO ################
        self.btnListVeiculo = QtWidgets.QPushButton(self.centralwidget)
        self.btnListVeiculo.setGeometry(QtCore.QRect(530, 10, 131, 81))
        self.btnListVeiculo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Imagens/btnListVeiculo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListVeiculo.setIcon(icon5)
        self.btnListVeiculo.setIconSize(QtCore.QSize(30, 30))
        self.btnListVeiculo.setObjectName("btnListVeiculo")
        # BTN LISTAR VEICULO CLICK
        self.btnListVeiculo.clicked.connect(self.btnListarVeiculo_Click)

        # BTN LISTAR ALUGUEL
        self.btnListAluguel = QtWidgets.QPushButton(self.centralwidget)
        self.btnListAluguel.setGeometry(QtCore.QRect(660, 10, 131, 81))
        self.btnListAluguel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Imagens/btnListAluguel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListAluguel.setIcon(icon6)
        self.btnListAluguel.setIconSize(QtCore.QSize(30, 30))
        self.btnListAluguel.setObjectName("btnListAluguel")
        # BTN LISTAR ALUGUEL CLICK #
        self.btnListAluguel.clicked.connect(self.btnListarAluguel_Click)

        self.lbImg = QtWidgets.QLabel(self.centralwidget)
        self.lbImg.setGeometry(QtCore.QRect(10, 110, 781, 301))
        self.lbImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbImg.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lbImg.setText("")
        self.lbImg.setPixmap(QtGui.QPixmap("Imagens/BGImg.png"))
        self.lbImg.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.lbImg.setObjectName("lbImg")
        FrmPrincipal.setCentralWidget(self.centralwidget)
        self.actionCliente = QtWidgets.QAction(FrmPrincipal)
        self.actionCliente.setObjectName("actionCliente")
        self.actionVe_culo = QtWidgets.QAction(FrmPrincipal)
        self.actionVe_culo.setObjectName("actionVe_culo")
        self.actionAlugar = QtWidgets.QAction(FrmPrincipal)
        self.actionAlugar.setObjectName("actionAlugar")
        self.actionCliente_2 = QtWidgets.QAction(FrmPrincipal)
        self.actionCliente_2.setObjectName("actionCliente_2")
        self.actionVe_culos = QtWidgets.QAction(FrmPrincipal)
        self.actionVe_culos.setObjectName("actionVe_culos")
        self.actionAlugueis = QtWidgets.QAction(FrmPrincipal)
        self.actionAlugueis.setObjectName("actionAlugueis")
        self.actionSair = QtWidgets.QAction(FrmPrincipal)
        self.actionSair.setObjectName("actionSair")

        self.retranslateUi(FrmPrincipal)
        QtCore.QMetaObject.connectSlotsByName(FrmPrincipal)

    def retranslateUi(self, FrmPrincipal):
        FrmPrincipal.setWindowTitle("Locadora de Veículos")
        self.btnAlugar.setText("Alugar Veículo")
        self.btnCliente.setText("Cadastrar Cliente")
        self.btnVeiculo.setText("Cadastrar Veículo")
        self.btnListCliente.setText("Listar Clientes")
        self.btnListVeiculo.setText("Listar Veículos")
        self.btnListAluguel.setText("Listar Alugueis")
        self.actionCliente.setText("Cliente")
        self.actionVe_culo.setText("Veículo")
        self.actionAlugar.setText("Alugar Veículo")
        self.actionCliente_2.setText("Clientes")
        self.actionVe_culos.setText("Veículos")
        self.actionAlugueis.setText("Alugueis")
        self.actionSair.setText("Sair")

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     FrmPrincipal = QtWidgets.QMainWindow()
#     ui = Ui_FrmPrincipal()
#     ui.setupUi(FrmPrincipal)
#     FrmPrincipal.show()
#     sys.exit(app.exec_())
