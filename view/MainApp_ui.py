# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import resources.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(965, 605)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #ffffff\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame_title = QFrame(self.left_container)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 9)
        self.lbl_title = QLabel(self.frame_title)
        self.lbl_title.setObjectName(u"lbl_title")

        self.horizontalLayout_4.addWidget(self.lbl_title)


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_menu = QFrame(self.left_container)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: #656565;\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"\n"
"	text-align: left;\n"
"	background-color: rgb(228, 254, 255)\n"
"\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(194, 232, 255);\n"
"	text-align: left;	\n"
"	\n"
"	color: #000000																						\n"
"\n"
"}")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_menu)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMaximumSize(QSize(200, 16777215))
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	background-color: #656565;\n"
"	border-top-left-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"color: #ffffff\n"
"\n"
"}")
        self.pg_menu = QWidget()
        self.pg_menu.setObjectName(u"pg_menu")
        self.pg_menu.setGeometry(QRect(0, 0, 63, 467))
        self.verticalLayout_4 = QVBoxLayout(self.pg_menu)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.pg_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.pg_menu)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.pg_menu)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setFont(font)
        self.btn_contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.pg_menu)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.pg_menu, u"Menu")
        self.pg_informacoes = QWidget()
        self.pg_informacoes.setObjectName(u"pg_informacoes")
        self.pg_informacoes.setGeometry(QRect(0, 0, 100, 467))
        self.verticalLayout_5 = QVBoxLayout(self.pg_informacoes)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 9, 0, -1)
        self.lbl_informacoes = QLabel(self.pg_informacoes)
        self.lbl_informacoes.setObjectName(u"lbl_informacoes")
        self.lbl_informacoes.setMouseTracking(True)
        self.lbl_informacoes.setAutoFillBackground(False)

        self.verticalLayout_5.addWidget(self.lbl_informacoes)

        self.toolBox.addItem(self.pg_informacoes, u"Informa\u00e7\u00f5es")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_menu)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 9, 9)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/imgs/icons/menu_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(62, 62, 62)")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pages_frame = QStackedWidget(self.main_frame)
        self.pages_frame.setObjectName(u"pages_frame")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.img_logo = QLabel(self.pg_home)
        self.img_logo.setObjectName(u"img_logo")

        self.verticalLayout_7.addWidget(self.img_logo)

        self.pages_frame.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_cadastro = QWidget()
        self.tab_cadastro.setObjectName(u"tab_cadastro")
        self.verticalLayout_11 = QVBoxLayout(self.tab_cadastro)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_4 = QFrame(self.tab_cadastro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	color: #000000\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"	background-color: rgb(231, 231, 231)\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.let_cnpj = QLineEdit(self.frame_4)
        self.let_cnpj.setObjectName(u"let_cnpj")
        self.let_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_cnpj, 1, 0, 1, 1)

        self.let_nome_empresarial = QLineEdit(self.frame_4)
        self.let_nome_empresarial.setObjectName(u"let_nome_empresarial")
        self.let_nome_empresarial.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_nome_empresarial, 1, 1, 1, 2)

        self.let_logradouro = QLineEdit(self.frame_4)
        self.let_logradouro.setObjectName(u"let_logradouro")
        self.let_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_logradouro, 2, 0, 1, 3)

        self.let_numero = QLineEdit(self.frame_4)
        self.let_numero.setObjectName(u"let_numero")
        self.let_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_numero, 3, 0, 1, 1)

        self.let_complemento = QLineEdit(self.frame_4)
        self.let_complemento.setObjectName(u"let_complemento")
        self.let_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_complemento, 3, 1, 1, 1)

        self.let_bairro = QLineEdit(self.frame_4)
        self.let_bairro.setObjectName(u"let_bairro")
        self.let_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_bairro, 3, 2, 1, 1)

        self.let_municipio = QLineEdit(self.frame_4)
        self.let_municipio.setObjectName(u"let_municipio")
        self.let_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_municipio, 4, 0, 1, 1)

        self.let_uf = QLineEdit(self.frame_4)
        self.let_uf.setObjectName(u"let_uf")
        self.let_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_uf, 4, 1, 1, 1)

        self.let_cep = QLineEdit(self.frame_4)
        self.let_cep.setObjectName(u"let_cep")
        self.let_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_cep, 4, 2, 1, 1)

        self.let_telefone = QLineEdit(self.frame_4)
        self.let_telefone.setObjectName(u"let_telefone")
        self.let_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_telefone, 5, 0, 1, 1)

        self.let_email = QLineEdit(self.frame_4)
        self.let_email.setObjectName(u"let_email")
        self.let_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.let_email, 5, 1, 1, 2)

        self.lbl_enterprises_title = QLabel(self.frame_4)
        self.lbl_enterprises_title.setObjectName(u"lbl_enterprises_title")
        self.lbl_enterprises_title.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.gridLayout.addWidget(self.lbl_enterprises_title, 0, 0, 1, 3)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.btn_cadastrar_2 = QPushButton(self.tab_cadastro)
        self.btn_cadastrar_2.setObjectName(u"btn_cadastrar_2")
        self.btn_cadastrar_2.setMinimumSize(QSize(160, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_cadastrar_2.setFont(font1)
        self.btn_cadastrar_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_2.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color: #000000\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	color: #000000\n"
"\n"
"}")

        self.verticalLayout_11.addWidget(self.btn_cadastrar_2, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_cadastro, "")
        self.tab_empresas_cadastradas = QWidget()
        self.tab_empresas_cadastradas.setObjectName(u"tab_empresas_cadastradas")
        self.verticalLayout_10 = QVBoxLayout(self.tab_empresas_cadastradas)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lbl_empresas = QLabel(self.tab_empresas_cadastradas)
        self.lbl_empresas.setObjectName(u"lbl_empresas")
        self.lbl_empresas.setMinimumSize(QSize(0, 80))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.lbl_empresas.setFont(font2)
        self.lbl_empresas.setAutoFillBackground(False)
        self.lbl_empresas.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.verticalLayout_10.addWidget(self.lbl_empresas)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tb_empresas = QTableWidget(self.tab_empresas_cadastradas)
        if (self.tb_empresas.columnCount() < 11):
            self.tb_empresas.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_empresas.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tb_empresas.setObjectName(u"tb_empresas")
        self.tb_empresas.setStyleSheet(u"	QHeaderView::section {\n"
"\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: #ffffff;\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"\n"
"	background-color: rgb(252, 252, 252);\n"
"	color: #000\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.tb_empresas)

        self.frame_3 = QFrame(self.tab_empresas_cadastradas)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 15px;\n"
"	background-color: #ffffff;\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 24, 74);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"	background-color: rgb(230, 230, 230)\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: #ffffff;\n"
"	background-color: rgb(49, 147, 0);\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: #ffffff;\n"
"	background-color: rgb(255, 170, 0);\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: #ffffff;\n"
"	background-color: rgb(199, 66, 0);\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_empresas_cadastradas, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.pages_frame.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lbl_contatos_title = QLabel(self.pg_contatos)
        self.lbl_contatos_title.setObjectName(u"lbl_contatos_title")
        self.lbl_contatos_title.setAutoFillBackground(False)

        self.verticalLayout_12.addWidget(self.lbl_contatos_title)

        self.lbl_whatsapp = QLabel(self.pg_contatos)
        self.lbl_whatsapp.setObjectName(u"lbl_whatsapp")

        self.verticalLayout_12.addWidget(self.lbl_whatsapp)

        self.lbl_email = QLabel(self.pg_contatos)
        self.lbl_email.setObjectName(u"lbl_email")

        self.verticalLayout_12.addWidget(self.lbl_email)

        self.lbl_instagram = QLabel(self.pg_contatos)
        self.lbl_instagram.setObjectName(u"lbl_instagram")

        self.verticalLayout_12.addWidget(self.lbl_instagram)

        self.lbl_github = QLabel(self.pg_contatos)
        self.lbl_github.setObjectName(u"lbl_github")

        self.verticalLayout_12.addWidget(self.lbl_github)

        self.pages_frame.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_13 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lbl_sobre_title = QLabel(self.pg_sobre)
        self.lbl_sobre_title.setObjectName(u"lbl_sobre_title")
        self.lbl_sobre_title.setAutoFillBackground(False)

        self.verticalLayout_13.addWidget(self.lbl_sobre_title)

        self.lbl_sobre_descricao = QLabel(self.pg_sobre)
        self.lbl_sobre_descricao.setObjectName(u"lbl_sobre_descricao")
        self.lbl_sobre_descricao.setAutoFillBackground(False)
        self.lbl_sobre_descricao.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.lbl_sobre_descricao)

        self.pages_frame.addWidget(self.pg_sobre)

        self.verticalLayout_6.addWidget(self.pages_frame)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.lbl_footer = QLabel(self.footer_frame)
        self.lbl_footer.setObjectName(u"lbl_footer")

        self.horizontalLayout_3.addWidget(self.lbl_footer)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages_frame.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"InventoPy - Cadastro de Empresas", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"InventoPy - Gerenciador de estoque", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pg_menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.lbl_informacoes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Usu\u00e1rio:</span> Admin</p><p align=\"center\"><span style=\" font-weight:600;\">Sistema:</span> Cadatro</p><p align=\"center\"><span style=\" font-weight:600;\">Status:</span> Ativo</p><p align=\"center\"><span style=\" font-weight:600;\">Venc:</span> 12/12/2099</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pg_informacoes), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sistema de Cadastro</span></p></body></html>", None))
        self.img_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/window/imgs/icons/app/app_icon.png\"/></p></body></html>", None))
        self.let_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.let_nome_empresarial.setText("")
        self.let_nome_empresarial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Empresarial", None))
        self.let_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.let_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.let_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.let_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.let_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.let_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.let_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.let_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.let_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lbl_enterprises_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CADASTRO DE EMPRESAS</span></p></body></html>", None))
        self.btn_cadastrar_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lbl_empresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#006394;\">EMPRESAS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_empresas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tb_empresas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tb_empresas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tb_empresas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem4 = self.tb_empresas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tb_empresas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tb_empresas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem7 = self.tb_empresas.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tb_empresas.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tb_empresas.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tb_empresas.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_empresas_cadastradas), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.lbl_contatos_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">CONTATOS</span></p></body></html>", None))
        self.lbl_whatsapp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/white_information/imgs/icons/info_icons/white_whatsapp_icon.png\"/><span style=\" font-size:26pt; font-weight:600; vertical-align:super;\">WhastApp</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lbl_email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/white_information/imgs/icons/info_icons/white_email_icon.png\"/><span style=\" font-size:26pt; font-weight:600; vertical-align:super;\">Email</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.lbl_instagram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/white_information/imgs/icons/info_icons/white_instagram_icon.png\"/><span style=\" font-size:26pt; font-weight:600; vertical-align:super;\">Instagram</span></p></body></html>", None))
        self.lbl_github.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/white_information/imgs/icons/info_icons/white_github_icon.png\"/><span style=\" font-size:26pt; font-weight:600; vertical-align:super;\">GitHub</span></p></body></html>", None))
        self.lbl_sobre_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.lbl_sobre_descricao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">Este sistema faz consulta do CNPJ utilizando API da Receita Federal e faz o cadastro em um banco de dados SQLITE3. Objetivo desse sistema \u00e9 aprender a usar Python e o PySide6 para o desenvolvimento de aplica\u00e7\u00f5es modernas.</span></p></body></html>", None))
        self.lbl_footer.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u00a9 Auris 2024</span></p></body></html>", None))
    # retranslateUi

