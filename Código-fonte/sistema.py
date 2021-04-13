import sys
from PySide2 import QtCore, QtGui, QtWidgets
from Codigo_das_interfaces.tela_login import Ui_Janela_Principal
from cadastro import janela_cadastro
from Codigo_das_interfaces.tela_final import Ui_janela_final
from time import sleep
import webbrowser as web

# Classe que herda todos os componentes da janela final
class janela_final(QtWidgets.QMainWindow, Ui_janela_final):
    def __init__(self):
        super(janela_final, self).__init__()
        self.setupUi(self)

        def click_btnLink():
            web.open('https://www.instagram.com/_jaelson1/')
        
        def fechar_tela():
            self.close()

        self.btn_link.clicked.connect(click_btnLink)
        self.btn_fechar.clicked.connect(fechar_tela)


# Classe que herda todos os componentes da janela de login
class Janela_prinipal(QtWidgets.QMainWindow, Ui_Janela_Principal):
    def __init__(self):
        super(Janela_prinipal, self).__init__()
        self.setupUi(self)
        
        janela2 = janela_cadastro()
        janela_fim_programa = janela_final()


        global tentativa
        tentativa = 0
        self.label_7.setText("Você tem apenas 3 tentativas para efetuar o login corretamente!")

        # ============================================ #
        # ÁREA DE FUNÇÕES DO SISTEMA DE LOGIN

        def bloquear_campos():
            self.lbl_email.setReadOnly(True)
            self.lbl_senha.setReadOnly(True)
            self.btn_entrar.setEnabled(False)
            self.lbl_mostraSenha1.setEnabled(False)

        def ativar_campos():
            self.lbl_email.setReadOnly(False)
            self.lbl_senha.setReadOnly(False)
            self.btn_entrar.setEnabled(True)
            self.lbl_mostraSenha1.setEnabled(True)

        
        def procurar_conta(usuario, senha):
            contas_cadastradas = janela2.contas

            analizador = False

            for conta in contas_cadastradas:
                if usuario == conta['email'] and senha == conta['senha']:
                    analizador = True
            return analizador
                            

        def click_btnCadastrar():
            zerar_tentativa()
            self.lbl_email.setText("")
            self.lbl_senha.setText("")
            ativar_campos()
            janela2.lbl_mostraSenha2.setChecked(False)
            self.lbl_mostraSenha1.setChecked(False)
            notificacao("Você tem apenas 3 tentativas para efetuar o login corretamente!")
            janela2.btn_gerar.setEnabled(True)
            janela2.lbl_email.setText("Seu email aparecerá aqui!")
            janela2.show()


        def caracteres_invalidos(frase=''):
            caractere = ['', '!', ' ', '¹', '²', '#', '%', '¬','¨', '&', '*', '(', ')', '/', '|', '"', "'", '-', '+', '=', '§', '?', '°', '´', '`', '{', '}', 'ª', '[', ']', 'º', '~', '^', ';', ':', ',', '.', 'ç', 'Ç']
            contem = False
            for letra in frase:
                if letra in caractere:
                    contem = True
                else:
                    False
            return contem
        
        def notificacao(msg=''):
            campo_notif = self.label_7
            campo_notif.setText(msg)

        def zerar_tentativa():
            global tentativa
            campo_tentativas = self.label_5
            tentativa = 0
            campo_tentativas.setText(f"{tentativa}")
        
        def login_errado():
            global tentativa
            notificacao("Login errado!\nSeu email ou senha estão errados\nTente novamente...")
            self.lbl_senha.setText("")
            campo_tentativas = self.label_5

            if tentativa < 3:
                tentativa+=1

            campo_tentativas.setText(f"{tentativa}")

            if tentativa == 3:
                self.lbl_email.setText("")
                self.lbl_senha.setText("")
                campo_tentativas.setText("3")
                notificacao("Você atingiu o número máximo de tentativas.\ntente cadastrar outra conta!")
                bloquear_campos()
        
        def mostra_senha():
            if self.lbl_mostraSenha1.isChecked() == True:
                self.lbl_senha.setEchoMode(QtWidgets.QLineEdit.Normal)
            else:
                self.lbl_senha.setEchoMode(QtWidgets.QLineEdit.Password)

        def fechar_tela():
            janela2.close()
            self.close()

        def click_Entrar():
            campo_email = self.lbl_email
            campo_senha = self.lbl_senha
            

            notificacao("")
        
            if campo_email.text() == "" or campo_senha.text() == "":
                notificacao('Tenha ceteza de que todos os campos estejão preenchidos!')
            else:
                if caracteres_invalidos(campo_email.text()) == True or caracteres_invalidos(campo_senha.text()) == True:
                    notificacao("Caracteres válidos: ( _ , @ )\nNúmeros(1,2,3,4,5,6,7,8,9,0)\nLetras Maiúsculas ou Minúsculas.")
                else:

                    teste = procurar_conta(campo_email.text(), campo_senha.text())

                    if teste == True:
                        fechar_tela()
                        janela_fim_programa.show()
                    else:
                        login_errado()

                    # Verificar tentativas
                
        
        # ============================================ #
        
        # Atribuindo as funções aos botões
        self.btn_entrar.clicked.connect(click_Entrar)
        self.btn_cadastrar.clicked.connect(click_btnCadastrar)
        self.lbl_mostraSenha1.clicked.connect(mostra_senha)
        self.btn_fechar.clicked.connect(fechar_tela)
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Janela_prinipal()
    window.show()
    sys.exit(app.exec_())