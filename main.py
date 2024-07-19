import sys

from PySide6.QtCore import QCoreApplication, QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow


from view.MainApp_ui import Ui_MainWindow
from controllers.ui_functions import consulta_cnpj

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.setWindowTitle("BHub - Sistema de Cadastro de Empresas")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)


        # ----------------------------------------------------- TOGGLE BUTTON --------------------------------------------------------
        self.btn_toggle.clicked.connect(self.LeftMenuAnimation)

        # --------------------------------------------------------- PAGES ------------------------------------------------------------
        self.btn_home.clicked.connect(lambda: self.pages_frame.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.pages_frame.setCurrentWidget(self.pg_cadastrar))
        self.btn_contatos.clicked.connect(lambda: self.pages_frame.setCurrentWidget(self.pg_contatos))
        self.btn_sobre.clicked.connect(lambda: self.pages_frame.setCurrentWidget(self.pg_sobre))


        # preencher dados automaticmente a partir do CNPJ
        self.let_cnpj.editingFinished.connect(self.api_consumer)



    def LeftMenuAnimation(self):

        width = self.left_container.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()



    def api_consumer(self):
        campos = consulta_cnpj(self.let_cnpj.text())

        self.let_nome_empresarial.setText(campos[0])
        self.let_logradouro.setText(campos[1])
        self.let_numero.setText(campos[2])
        self.let_complemento.setText(campos[3])
        self.let_bairro.setText(campos[4])
        self.let_municipio.setText(campos[5])
        self.let_uf.setText(campos[6])
        self.let_cep.setText(campos[7]).replace(".", "").replace("-", "")
        self.let_telefone.setText(campos[8]).replace("(", "").replace(")", "").replace("-", "")
        self.let_email.setText(campos[9])
        



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

