from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from componente import imagens

class Ui_janela_final(object):
    def setupUi(self, janela_final):
        if not janela_final.objectName():
            janela_final.setObjectName(u"janela_final")
        janela_final.resize(308, 216)
        janela_final.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowShadeButtonHint | Qt.CustomizeWindowHint)
        janela_final.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.centralwidget = QWidget(janela_final)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 29, 291, 181))
        self.label.setStyleSheet(u"")
        self.label.setWordWrap(True)
        self.btn_link = QPushButton(self.centralwidget)
        self.btn_link.setObjectName(u"btn_link")
        self.btn_link.setGeometry(QRect(6, 180, 294, 28))
        self.btn_link.setStyleSheet(u"QPushButton{	\n"
"	background:transparent;\n"
"	border: 2px solid rgb(66, 66, 98);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 3px solid rgb(42, 42, 62);\n"
"}")
        self.btn_fechar = QToolButton(self.centralwidget)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setGeometry(QRect(272, 4, 31, 31))
        self.btn_fechar.setStyleSheet(u"QToolButton{\n"
"	image: url(:/imagens/icone_fechar.png);\n"
"	background-color: rgb(0, 37, 54);\n"
"	border: 1.5px solid   rgb(0, 37, 54);\n"
"	border-radius: 15px;\n"
"}\n"
"QToolButton:hover{\n"
"	background-color: rgb(0, 16, 24);\n"
"	border: 3px solid   rgb(0, 16, 24);\n"
"}\n"
"QToolButton:pressed{\n"
"	background-color: rgb(0, 60, 88);\n"
"	border: 2px solid rgb(0, 60, 88);\n"
"}	\n"
"")
        janela_final.setCentralWidget(self.centralwidget)

        self.retranslateUi(janela_final)

        QMetaObject.connectSlotsByName(janela_final)
    # setupUi

    def retranslateUi(self, janela_final):
        janela_final.setWindowTitle(QCoreApplication.translate("janela_final", u"FeedBack", None))
        self.label.setText(QCoreApplication.translate("janela_final", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#aaff7f;\">Se gostou do sistema de login, deixe seu feedback para o desenvolvedor!</span></p><p><a href=\"https://www.insm/_jaelson1/?tagram.cohl=pt-br\"><span style=\" font-size:14pt; text-decoration: underline; color:#00aaff;\">\\\\ Link para o instagram do Dev //</span></a></p></body></html>", None))
        self.btn_link.setText("")
        self.btn_fechar.setText("")
    # retranslateUi

