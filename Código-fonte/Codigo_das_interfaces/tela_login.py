from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from componente import imagens

class Ui_Janela_Principal(object):
    def setupUi(self, Janela_Principal):
        if not Janela_Principal.objectName():
            Janela_Principal.setObjectName(u"Janela_Principal")
        Janela_Principal.resize(400, 400)
        Janela_Principal.setMinimumSize(QSize(400, 400))
        Janela_Principal.setMaximumSize(QSize(400, 400))
        Janela_Principal.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowShadeButtonHint | Qt.CustomizeWindowHint)
        icon = QIcon()
        icon.addFile(u":/imagens/icone_login.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/imagens/icone_login.png", QSize(), QIcon.Active, QIcon.Off)
        Janela_Principal.setWindowIcon(icon)
        Janela_Principal.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(27, 27, 27, 255), stop:0.994318 rgba(143, 143, 215, 255));\n"
"border: null;")
        self.centralwidget = QWidget(Janela_Principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 111, 51))
        font = QFont()
        font.setFamily(u"Berlin Sans FB")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 72, 311, 16))
        font1 = QFont()
        font1.setFamily(u"Berlin Sans FB")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background:transparent;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 87, 281, 16))
        font2 = QFont()
        font2.setFamily(u"Berlin Sans FB")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background:transparent;")
        self.lbl_email = QLineEdit(self.frame)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(120, 134, 250, 30))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(8)
        self.lbl_email.setFont(font3)
        self.lbl_email.setCursor(QCursor(Qt.ArrowCursor))
        self.lbl_email.setStyleSheet(u"QLineEdit{\n"
"	border-radius:15px;\n"
"	border: 2px solid rgb(77, 77, 115);\n"
"	background-color:rgb(170, 85, 255);\n"
"	color: rgb(44, 0, 66);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color:rgb(160, 80, 240);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(77, 77, 115);\n"
"}")
        self.lbl_email.setMaxLength(45)
        self.lbl_email.setReadOnly(False)
        self.lbl_email.setClearButtonEnabled(True)
        self.lbl_senha = QLineEdit(self.frame)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setGeometry(QRect(120, 174, 250, 30))
        self.lbl_senha.setCursor(QCursor(Qt.ArrowCursor))
        self.lbl_senha.setStyleSheet(u"QLineEdit{\n"
"	border-radius:15px;\n"
"	border: 2px solid rgb(77, 77, 115);\n"
"	background-color:rgb(170, 85, 255);\n"
"	color: rgb(44, 0, 66);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color:rgb(160, 80, 240);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(77, 77, 115);\n"
"}")
        self.lbl_senha.setMaxLength(10)
        self.lbl_senha.setEchoMode(QLineEdit.Password)
        self.lbl_senha.setDragEnabled(False)
        self.lbl_senha.setReadOnly(False)
        self.lbl_senha.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lbl_senha.setClearButtonEnabled(True)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 133, 81, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	background:rgb(85, 85, 127)\n"
"}")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 173, 81, 31))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	background:rgb(85, 85, 127)\n"
"}")
        self.btn_entrar = QToolButton(self.frame)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(132, 298, 130, 41))
        self.btn_entrar.setFont(font4)
        self.btn_entrar.setStyleSheet(u"QToolButton{\n"
"	background:rgb(69, 69, 103);\n"
"	border-radius: 20px;\n"
"	border: 2px solid rgb(60, 60, 89);\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QToolButton:hover{\n"
"	color:rgb(211, 141, 211);\n"
"	background:rgb(99, 99, 147);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(60, 60, 89);\n"
"}")
        self.btn_cadastrar = QToolButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(60, 350, 281, 31))
        self.btn_cadastrar.setFont(font4)
        self.btn_cadastrar.setStyleSheet(u"QToolButton{\n"
"	background:rgb(69, 69, 103);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(60, 60, 89);\n"
"	\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QToolButton:hover{\n"
"	color:rgb(211, 141, 211);\n"
"	background:rgb(99, 99, 147);\n"
"	color: rgb(39, 0, 58);\n"
"	border: 3px solid rgb(60, 60, 89);\n"
"}")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(339, 242, 31, 31))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"QLabel{\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(77, 77, 115);\n"
"	background-color: rgb(170, 85, 255);\n"
"}\n"
"QLabel:hover{\n"
"	background-color:rgb(160, 80, 240);\n"
"	color: rgb(39, 0, 58);\n"
"}\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(31, 234, 297, 51))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(9)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(9)
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"	color: rgb(255, 170, 255);\n"
"	font: 75 9pt \"Consolas\";\n"
"	border: 0.5px solid rgb(121, 121, 180);\n"
"	border-radius: 5px;\n"
"}")
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.btn_fechar = QToolButton(self.frame)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setGeometry(QRect(363, 7, 31, 31))
        self.btn_fechar.setStyleSheet(u"QToolButton{\n"
"	image: url(:/imagens/icone_fechar.png);\n"
"	background-color:rgb(255, 170, 255);\n"
"	border: 1.5px solid  rgb(255, 170, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"QToolButton:hover{\n"
"	background-color:rgb(255, 170, 255);\n"
"	border: 3px solid  rgb(255, 170, 255);\n"
"}\n"
"QToolButton:pressed{\n"
"	background-color: rgb(255, 85, 255);\n"
"	border: 2px solid rgb(255, 85, 255);\n"
"}	\n"
"")
        self.lbl_mostraSenha1 = QCheckBox(self.frame)
        self.lbl_mostraSenha1.setObjectName(u"lbl_mostraSenha1")
        self.lbl_mostraSenha1.setGeometry(QRect(267, 204, 101, 16))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(9)
        font7.setBold(False)
        font7.setUnderline(False)
        font7.setWeight(50)
        self.lbl_mostraSenha1.setFont(font7)
        self.lbl_mostraSenha1.setLayoutDirection(Qt.RightToLeft)
        self.lbl_mostraSenha1.setStyleSheet(u"QCheckBox{\n"
"	background-color:transparent;\n"
"	color: rgb(255, 170, 255);\n"
"}")
        self.lbl_mostraSenha1.setChecked(False)
        self.lbl_mostraSenha1.setAutoRepeat(False)
        self.lbl_mostraSenha1.setAutoRepeatDelay(300)
        self.lbl_mostraSenha1.setAutoRepeatInterval(100)
        self.lbl_mostraSenha1.setTristate(False)

        self.verticalLayout.addWidget(self.frame)

        Janela_Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela_Principal)

        QMetaObject.connectSlotsByName(Janela_Principal)
    # setupUi

    def retranslateUi(self, Janela_Principal):
        Janela_Principal.setWindowTitle(QCoreApplication.translate("Janela_Principal", u" Loggin", None))
        self.label.setText(QCoreApplication.translate("Janela_Principal", u"<html><head/><body><p><span style=\" font-size:36pt; color:#d68fd6;\">Login</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Janela_Principal", u"<html><head/><body><p><span style=\" font-size:10pt; color:#d68fd6;\">Entre com seus dados corretamente para acessar o sistema,</span></p><p><span style=\" font-size:10pt; color:#c785c7;\"><br/></span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Janela_Principal", u"<html><head/><body><p><span style=\" font-size:10pt; color:#d672d6;\">caso n\u00e3o </span><span style=\" font-size:9pt; color:#d672d6;\">tenha cadastro ainda, clique em Cadastrar-se</span></p></body></html>", None))
        self.lbl_email.setPlaceholderText(QCoreApplication.translate("Janela_Principal", u"Email do usu\u00e1rio", None))
        self.lbl_senha.setPlaceholderText(QCoreApplication.translate("Janela_Principal", u"Senha do usu\u00e1rio", None))
        self.label_4.setText(QCoreApplication.translate("Janela_Principal", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffaaff;\">Email:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Janela_Principal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffaaff;\">Senha:</span></p></body></html>", None))
        self.btn_entrar.setText(QCoreApplication.translate("Janela_Principal", u"Entrar", None))
#if QT_CONFIG(shortcut)
        self.btn_entrar.setShortcut(QCoreApplication.translate("Janela_Principal", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cadastrar.setText(QCoreApplication.translate("Janela_Principal", u"Cadastrar-se", None))
        self.label_5.setText(QCoreApplication.translate("Janela_Principal", u"<html><head/><body><p><span style=\" color:#4d4d73;\">0</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Janela_Principal", u"<html><head/><body><p><br/></p></body></html>", None))
        self.btn_fechar.setText("")
        self.lbl_mostraSenha1.setText(QCoreApplication.translate("Janela_Principal", u"Mostrar senha", None))
    # retranslateUi

