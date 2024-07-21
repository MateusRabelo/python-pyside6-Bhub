import sys

# from PySide6 import QtCore
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox


from view.MainApp_ui import Ui_MainWindow
from controllers.ui_functions import consulta_cnpj
from database.database import Database

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

        self.btn_cadastrar_2.clicked.connect(self.cadastrar_empresas)




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
        # print(type(campos[0]))
        self.let_logradouro.setText(campos[1])
        # print(type(campos[1]))
        self.let_numero.setText(campos[2])
        # print(type(campos[2]))
        self.let_complemento.setText(campos[3])
        # print(type(campos[3]))
        self.let_bairro.setText(campos[4])
        # print(type(campos[4]))
        self.let_municipio.setText(campos[5])
        # print(type(campos[5]))
        self.let_uf.setText(campos[6])
        # print(type(campos[6]))
        self.let_cep.setText(campos[7].replace(".", "").replace("-", ""))
        # print(type(campos[7]))
        self.let_telefone.setText(campos[8].replace("(", "").replace(")", "").replace("-", ""))
        # print(type(campos[8]))
        self.let_email.setText(campos[9])
        # print(type(campos[9]))
        



    def cadastrar_empresas(self):
        db = Database()
        db.connect()

        fullDataSet = (
            self.let_cnpj.text(),
            self.let_nome_empresarial.text(),
            self.let_logradouro.text(),
            self.let_numero.text(),
            self.let_complemento.text(),
            self.let_bairro.text(),
            self.let_municipio.text(),
            self.let_uf.text(),
            self.let_cep.text(),
            self.let_telefone.text().strip(),
            self.let_email.text()
        )

        # cadasrando no banco de dados
        response = db.register_company(fullDataSet)

        if response == 'Ok':
            msg = QMessageBox()

            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Empresa cadastrada com sucesso!")

            msg.exec()

            db.close_connection()
            
            return
        else:
            msg = QMessageBox()

            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")

            msg.exec()

            db.close_connection()
            
            return




if __name__ == "__main__":

    db = Database()

    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

