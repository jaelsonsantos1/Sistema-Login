from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from componente import imagens

class Ui_janela_2(object):
    def setupUi(self, janela_2):
        if not janela_2.objectName():
            janela_2.setObjectName(u"janela_2")
        janela_2.resize(400, 400)
        janela_2.setMinimumSize(QSize(400, 400))
        janela_2.setMaximumSize(QSize(400, 400))
        janela_2.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowShadeButtonHint | Qt.CustomizeWindowHint)
        icon = QIcon()
        icon.addFile(u":/imagens/icone_login.png", QSize(), QIcon.Normal, QIcon.Off)
        janela_2.setWindowIcon(icon)
        janela_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(27, 27, 27, 255), stop:0.994318 rgba(143, 143, 215, 255));\n"
"border: null;")
        self.widget = QWidget(janela_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(34, 10, 321, 41))
        self.label_2.setStyleSheet(u"background: transparent;")
        self.lbl_nome1 = QLineEdit(self.frame)
        self.lbl_nome1.setObjectName(u"lbl_nome1")
        self.lbl_nome1.setGeometry(QRect(40, 140, 320, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(8)
        self.lbl_nome1.setFont(font1)
        self.lbl_nome1.setCursor(QCursor(Qt.ArrowCursor))
        self.lbl_nome1.setStyleSheet(u"QLineEdit{\n"
"	border-radius:15px;\n"
"	background-color:rgb(170, 85, 255);\n"
"	color: rgb(44, 0, 66);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color:rgb(160, 80, 240);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(77, 77, 115);\n"
"}")
        self.lbl_nome1.setMaxLength(10)
        self.lbl_nome1.setClearButtonEnabled(True)
        self.lbl_nome2 = QLineEdit(self.frame)
        self.lbl_nome2.setObjectName(u"lbl_nome2")
        self.lbl_nome2.setGeometry(QRect(40, 180, 320, 30))
        self.lbl_nome2.setFont(font1)
        self.lbl_nome2.setCursor(QCursor(Qt.ArrowCursor))
        self.lbl_nome2.setStyleSheet(u"QLineEdit{\n"
"	border-radius:15px;\n"
"	background-color:rgb(170, 85, 255);\n"
"	color: rgb(44, 0, 66);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color:rgb(160, 80, 240);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(77, 77, 115);\n"
"}")
        self.lbl_nome2.setInputMethodHints(Qt.ImhNone)
        self.lbl_nome2.setMaxLength(10)
        self.lbl_nome2.setClearButtonEnabled(True)
        self.lbl_senha2 = QLineEdit(self.frame)
        self.lbl_senha2.setObjectName(u"lbl_senha2")
        self.lbl_senha2.setGeometry(QRect(40, 289, 320, 30))
        self.lbl_senha2.setFont(font1)
        self.lbl_senha2.setCursor(QCursor(Qt.ArrowCursor))
        self.lbl_senha2.setStyleSheet(u"QLineEdit{\n"
"	border-radius:15px;\n"
"	background-color:rgb(170, 85, 255);\n"
"	color: rgb(44, 0, 66);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color:rgb(160, 80, 240);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(77, 77, 115);\n"
"}")
        self.lbl_senha2.setMaxLength(10)
        self.lbl_senha2.setClearButtonEnabled(True)
        self.lbl_senha1 = QLineEdit(self.frame)
        self.lbl_senha1.setObjectName(u"lbl_senha1")
        self.lbl_senha1.setGeometry(QRect(40, 254, 320, 30))
        self.lbl_senha1.setFont(font1)
        self.lbl_senha1.setCursor(QCursor(Qt.ArrowCursor))
        self.lbl_senha1.setStyleSheet(u"QLineEdit{\n"
"	border-radius:15px;\n"
"	background-color:rgb(170, 85, 255);\n"
"	color: rgb(44, 0, 66);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color:rgb(160, 80, 240);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(77, 77, 115);\n"
"}")
        self.lbl_senha1.setMaxLength(10)
        self.lbl_senha1.setClearButtonEnabled(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 40, 121, 101))
        self.label.setStyleSheet(u"background:transparent;\n"
"image: url(:/imagens/icone_cadastro.png);")
        self.btn_verificar = QToolButton(self.frame)
        self.btn_verificar.setObjectName(u"btn_verificar")
        self.btn_verificar.setGeometry(QRect(260, 344, 130, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_verificar.setFont(font2)
        self.btn_verificar.setStyleSheet(u"QToolButton{\n"
"	background:rgb(69, 69, 103);\n"
"	border-radius: 20px;\n"
"	border: 2px solid rgb(60, 60, 89);		\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QToolButton:hover{\n"
"	color:rgb(211, 141, 211);\n"
"	background:rgb(99, 99, 147);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(60, 60, 89);\n"
"}")
        self.btn_gerar = QToolButton(self.frame)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setGeometry(QRect(40, 220, 85, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.btn_gerar.setFont(font3)
        self.btn_gerar.setStyleSheet(u"QToolButton{\n"
"	background:rgb(69, 69, 103);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(60, 60, 89);\n"
"		\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QToolButton:hover{\n"
"	color:rgb(211, 141, 211);\n"
"	background:rgb(99, 99, 147);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(60, 60, 89);\n"
"	font: 87 8pt \"Arial Black\";\n"
"}")
        self.btn_copiar = QToolButton(self.frame)
        self.btn_copiar.setObjectName(u"btn_copiar")
        self.btn_copiar.setGeometry(QRect(365, 225, 21, 21))
        self.btn_copiar.setStyleSheet(u"QToolButton{\n"
"\n"
"	image: url(:/imagens/icone_copiar.png);\n"
"}\n"
"QToolButton:hover{\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QToolButton:pressed{\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 340, 241, 51))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(9)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"	color: rgb(255, 170, 255);\n"
"	font: 75 9pt \"Consolas\";\n"
"	border: 0.5px solid rgb(121, 121, 180);\n"
"	border-radius: 5px;\n"
"}")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.lbl_email = QLineEdit(self.frame)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(129, 220, 231, 31))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.lbl_email.setFont(font5)
        self.lbl_email.setStyleSheet(u"QLineEdit{\n"
"	background-color:rgb(170, 85, 255);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(77, 77, 115);\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color:rgb(160, 80, 240);\n"
"	color: rgb(39, 0, 58);\n"
"}\n"
"")
        self.lbl_email.setMaxLength(50)
        self.lbl_email.setAlignment(Qt.AlignCenter)
        self.lbl_email.setDragEnabled(True)
        self.lbl_email.setReadOnly(True)
        self.lbl_mostraSenha2 = QCheckBox(self.frame)
        self.lbl_mostraSenha2.setObjectName(u"lbl_mostraSenha2")
        self.lbl_mostraSenha2.setGeometry(QRect(230, 319, 130, 16))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(9)
        font6.setBold(False)
        font6.setUnderline(False)
        font6.setWeight(50)
        self.lbl_mostraSenha2.setFont(font6)
        self.lbl_mostraSenha2.setLayoutDirection(Qt.RightToLeft)
        self.lbl_mostraSenha2.setStyleSheet(u"QCheckBox{\n"
"	background-color:transparent;\n"
"	color: rgb(255, 170, 255);\n"
"}")
        self.lbl_mostraSenha2.setChecked(False)
        self.lbl_mostraSenha2.setAutoRepeat(False)
        self.lbl_mostraSenha2.setAutoRepeatDelay(300)
        self.lbl_mostraSenha2.setAutoRepeatInterval(100)
        self.lbl_mostraSenha2.setTristate(False)

        self.verticalLayout.addWidget(self.frame)

        janela_2.setCentralWidget(self.widget)

        self.retranslateUi(janela_2)

        QMetaObject.connectSlotsByName(janela_2)
    # setupUi

    def retranslateUi(self, janela_2):
        janela_2.setWindowTitle(QCoreApplication.translate("janela_2", u" Cadastrar-se", None))
        self.label_2.setText(QCoreApplication.translate("janela_2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffaaff;\">Cadastrar-se</span></p></body></html>", None))
        self.lbl_nome1.setText("")
        self.lbl_nome1.setPlaceholderText(QCoreApplication.translate("janela_2", u"Insira seu primeiro nome", None))
        self.lbl_nome2.setText("")
        self.lbl_nome2.setPlaceholderText(QCoreApplication.translate("janela_2", u"Insira seu segundo nome", None))
        self.lbl_senha2.setPlaceholderText(QCoreApplication.translate("janela_2", u"Insira sua senha novamente", None))
        self.lbl_senha1.setPlaceholderText(QCoreApplication.translate("janela_2", u"Senha", None))
        self.label.setText("")
        self.btn_verificar.setText(QCoreApplication.translate("janela_2", u"Verificar", None))
#if QT_CONFIG(shortcut)
        self.btn_verificar.setShortcut(QCoreApplication.translate("janela_2", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_gerar.setText(QCoreApplication.translate("janela_2", u"Gerar email", None))
#if QT_CONFIG(shortcut)
        self.btn_gerar.setShortcut(QCoreApplication.translate("janela_2", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_copiar.setText(QCoreApplication.translate("janela_2", u"...", None))
        self.label_7.setText(QCoreApplication.translate("janela_2", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lbl_email.setInputMask("")
        self.lbl_email.setText(QCoreApplication.translate("janela_2", u"Seu email aparecer\u00e1 aqui!", None))
        self.lbl_email.setPlaceholderText("")
        self.lbl_mostraSenha2.setText(QCoreApplication.translate("janela_2", u"Não mostrar senha", None))
    # retranslateUi

