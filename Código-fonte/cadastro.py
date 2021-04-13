from PySide2 import QtCore, QtGui, QtWidgets
from Codigo_das_interfaces.tela_cadastro import Ui_janela_2
from random import sample


# Classe que herda todos os componentes da janela de cadastro
class janela_cadastro(QtWidgets.QMainWindow, Ui_janela_2):
    logados = {}
    contas = []    
    
    def cadastro(self, usuario, senha):
        self.logados['email'] = usuario
        self.logados['senha'] = senha
        self.contas.append(self.logados.copy())


    def __init__(self):
        super(janela_cadastro, self).__init__()
        self.setupUi(self)
        
        def caracteres_invalidos_email(frase=''):
            caractere = ['', '!', ' ', '¹', '²', '#', '%', '¬','¨', '&', '*', '(', ')', '/', '|', '"', "'", '-', '_', '@', '+', '=', '§', '?', '°', '´', '`', '{', '}', 'ª', '[', ']', 'º', '~', '^', ';', ':', ',', '.', 'ç', 'Ç', '1','2','3','4','5','6','7','8','9','0']
            contem = False
            for letra in frase:
                if letra in caractere:
                    contem = True
                else:
                    False
            return contem


        def caracteres_invalidos_senha(frase=''):
            caractere = ['', '!', ' ', '¹', '²', '#', '%', '¬','¨', '&', '*', '(', ')', '/', '|', '"', "'", '-', '_', '@', '+', '=', '§', '?', '°', '´', '`', '{', '}', 'ª', '[', ']', 'º', '~', '^', ';', ':', ',', '.', 'ç', 'Ç']
            contem = False
            for letra in frase:
                if letra in caractere:
                    contem = True
                else:
                    False
            return contem

        def gerar_email(nome1, nome2):
            email_gerado = self.lbl_email

            nums = sample(range(0, 9), 5)
            email_gerado.setText(f"_{nums[0]}{nome1}{nums[1]}{nums[2]}{nums[3]}@{nome2}{nums[4]}")
            campo_notif.setText("Email gerado com sucesso!")


        def notificacao(msg=''):
            global campo_notif
            campo_notif = self.label_7
            campo_notif.setText(msg)

        def click_btnGerar():
            campo_nome1 = self.lbl_nome1.text()
            campo_nome2 = self.lbl_nome2.text()

            notificacao("")
        
            if campo_nome1 == "" or campo_nome2 == "":
                notificacao('Tenha ceteza de que todos os campos estejão preenchidos!')
            else:
                if len(campo_nome1) <= 5 or len(campo_nome2) <= 5:
                    notificacao("Os campos 'Primeiro NOME' e 'Segundo NOME' Devem conter mais do que 5 caracteres")
                else:
                    if campo_nome1 == campo_nome2:
                        notificacao("Os campos 'Nome' e 'Segundo nome' não podem ser iguais!")
                    else:
                        if caracteres_invalidos_email(campo_nome1) == True or caracteres_invalidos_email(campo_nome2) == True:
                            notificacao("Caracteres válidos: \nLetras Maiúsculas ou Minúsculas.")
                        else:
                            gerar_email(campo_nome1, campo_nome2)
                            self.btn_gerar.setEnabled(False)
                
        def cadastro_existente(email, senha):
            verificador = False
            if self.logados == {}:
                pass
            else:
                if email == self.logados['email'] and senha == self.logados['senha']:
                    verificador = True
                else:
                    False
                
            return verificador
            
        def click_btnCopiar():
            if self.lbl_email.text() == "Seu email aparecerá aqui!":
                pass
            else:
                email_gerado = self.lbl_email
                notificacao("Email copiado com sucesso!")
                selecionado = email_gerado.selectAll()
                email_gerado.copy()
        
        def mostra_senha():
            caixa_mostra = self.lbl_mostraSenha2
            if caixa_mostra.isChecked() == True:
                self.lbl_senha1.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lbl_senha2.setEchoMode(QtWidgets.QLineEdit.Password)
            else:
                self.lbl_senha1.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.lbl_senha2.setEchoMode(QtWidgets.QLineEdit.Normal)

        def click_btnValidar():
            email_gerado = self.lbl_email
            campo_senha1 = self.lbl_senha1
            campo_senha2 = self.lbl_senha2
            campo_nome1 = self.lbl_nome1
            campo_nome2 = self.lbl_nome2

            if email_gerado.text() == "Seu email aparecerá aqui!":
                notificacao("Sertifique que seu email foi gerado!")
            else:
                if campo_senha1.text() == "" or campo_senha2.text() == "":
                    notificacao('Tenha ceteza de que os campos de senha estejam preenchidos!')
                else:
                    if len(campo_senha1.text()) < 8 or len(campo_senha2.text()) < 8:
                        notificacao("Os campos 'Senha' e 'Repitir senha'\nDevem conter de 8 a 15 caracteres")
                    else:
                        if caracteres_invalidos_senha(campo_senha1.text()) == True or caracteres_invalidos_senha(campo_senha2.text()) == True:
                            notificacao("Caracteres válidos:\nNúmeros(1,2,3,4,5,6,7,8,9,0)\nLetras Maiúsculas ou Minúsculas.")
                        else:
                            if campo_senha2.text() != campo_senha1.text():
                                campo_senha2.setText("")
                                notificacao("Insira a mesma senha novamente!")
                            else:
                                if cadastro_existente(email_gerado.text(), campo_senha1.text()) == True:
                                    notificacao("Essa conta já existe no sistema!")
                                else:
                                    self.cadastro(email_gerado.text(), campo_senha1.text())

                                    fonte = QtGui.QFont()
                                    fonte.setFamily(u"Berlin Sans FB")
                                    fonte.setPointSize(14)
                                    fonte.setBold(True)
                                    fonte.setItalic(False)
                                    fonte.setWeight(50)
                                    msg = QtWidgets.QMessageBox(self)
                                    msg.setIcon(msg.Information)
                                    msg.setFont(fonte)
                                    msg.setText("Cadastro efetuado\ncom sucesso!")
                                    msg.exec_()

                                    campo_nome1.setText("")
                                    campo_nome2.setText("")
                                    campo_senha1.setText("")
                                    campo_senha2.setText("")
                                    email_gerado.setText("")
                                    notificacao("")

                                    self.close()

        
        # Atribuindo funções aos botões
        self.btn_gerar.clicked.connect(click_btnGerar)
        self.btn_copiar.clicked.connect(click_btnCopiar)
        self.btn_verificar.clicked.connect(click_btnValidar)
        self.lbl_mostraSenha2.clicked.connect(mostra_senha)


