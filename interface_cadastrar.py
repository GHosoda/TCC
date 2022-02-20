# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_cadastrar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Cadastro(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(472, 539)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cm_cabecalho = QFrame(Dialog)
        self.cm_cabecalho.setObjectName(u"cm_cabecalho")
        self.cm_cabecalho.setEnabled(True)
        self.cm_cabecalho.setMinimumSize(QSize(0, 120))
        self.cm_cabecalho.setMaximumSize(QSize(16777215, 120))
        self.cm_cabecalho.setAutoFillBackground(False)
        self.cm_cabecalho.setStyleSheet(u"background-color: rgb(132, 153, 165);")
        self.cm_cabecalho.setFrameShape(QFrame.NoFrame)
        self.cm_cabecalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.cm_cabecalho)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cm_logo = QLabel(self.cm_cabecalho)
        self.cm_logo.setObjectName(u"cm_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cm_logo.sizePolicy().hasHeightForWidth())
        self.cm_logo.setSizePolicy(sizePolicy)
        self.cm_logo.setMinimumSize(QSize(300, 100))
        self.cm_logo.setMaximumSize(QSize(300, 100))
        self.cm_logo.setPixmap(QPixmap(u":/newPrefix/logo-feimc-escrita.png"))
        self.cm_logo.setScaledContents(True)
        self.cm_logo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.cm_logo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.l_cm_cabecalho = QLabel(self.cm_cabecalho)
        self.l_cm_cabecalho.setObjectName(u"l_cm_cabecalho")

        self.horizontalLayout_8.addWidget(self.l_cm_cabecalho)


        self.verticalLayout.addWidget(self.cm_cabecalho)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 2, 0)
        self.l_cm_nome = QLabel(self.frame_3)
        self.l_cm_nome.setObjectName(u"l_cm_nome")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.l_cm_nome.sizePolicy().hasHeightForWidth())
        self.l_cm_nome.setSizePolicy(sizePolicy2)
        self.l_cm_nome.setMinimumSize(QSize(0, 20))
        self.l_cm_nome.setMaximumSize(QSize(16777215, 20))
        self.l_cm_nome.setText(u"Nome")
        self.l_cm_nome.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.l_cm_nome)

        self.l_cm_potencia = QLabel(self.frame_3)
        self.l_cm_potencia.setObjectName(u"l_cm_potencia")
        sizePolicy2.setHeightForWidth(self.l_cm_potencia.sizePolicy().hasHeightForWidth())
        self.l_cm_potencia.setSizePolicy(sizePolicy2)
        self.l_cm_potencia.setMinimumSize(QSize(0, 20))
        self.l_cm_potencia.setMaximumSize(QSize(16777215, 20))
        self.l_cm_potencia.setText(u"Pot\u00eancia (kW)")
        self.l_cm_potencia.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.l_cm_potencia)

        self.l_cm_tensao = QLabel(self.frame_3)
        self.l_cm_tensao.setObjectName(u"l_cm_tensao")
        sizePolicy2.setHeightForWidth(self.l_cm_tensao.sizePolicy().hasHeightForWidth())
        self.l_cm_tensao.setSizePolicy(sizePolicy2)
        self.l_cm_tensao.setMinimumSize(QSize(0, 20))
        self.l_cm_tensao.setMaximumSize(QSize(16777215, 20))
        self.l_cm_tensao.setText(u"Tens\u00e3o (V)")
        self.l_cm_tensao.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.l_cm_tensao)

        self.l_cm_corrente = QLabel(self.frame_3)
        self.l_cm_corrente.setObjectName(u"l_cm_corrente")
        self.l_cm_corrente.setMinimumSize(QSize(0, 20))
        self.l_cm_corrente.setMaximumSize(QSize(16777215, 20))
        self.l_cm_corrente.setText(u"Corrente (A)")
        self.l_cm_corrente.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.l_cm_corrente)

        self.l_cm_frequencia = QLabel(self.frame_3)
        self.l_cm_frequencia.setObjectName(u"l_cm_frequencia")
        self.l_cm_frequencia.setMinimumSize(QSize(0, 20))
        self.l_cm_frequencia.setMaximumSize(QSize(16777215, 20))
        self.l_cm_frequencia.setText(u"Frequ\u00eancia (Hz)")
        self.l_cm_frequencia.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.l_cm_frequencia)

        self.l_cm_rpm = QLabel(self.frame_3)
        self.l_cm_rpm.setObjectName(u"l_cm_rpm")
        self.l_cm_rpm.setMinimumSize(QSize(0, 20))
        self.l_cm_rpm.setMaximumSize(QSize(16777215, 20))
        self.l_cm_rpm.setText(u"Rota\u00e7\u00e3o (RPM)")
        self.l_cm_rpm.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.l_cm_rpm)

        self.l_cm_cos = QLabel(self.frame_3)
        self.l_cm_cos.setObjectName(u"l_cm_cos")
        self.l_cm_cos.setMinimumSize(QSize(0, 20))
        self.l_cm_cos.setMaximumSize(QSize(16777215, 20))
        self.l_cm_cos.setText(u"Cos(phi)")
        self.l_cm_cos.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.l_cm_cos)

        self.l_cm_polos = QLabel(self.frame_3)
        self.l_cm_polos.setObjectName(u"l_cm_polos")
        self.l_cm_polos.setMinimumSize(QSize(0, 20))
        self.l_cm_polos.setMaximumSize(QSize(16777215, 20))
        self.l_cm_polos.setText(u"Polos")
        self.l_cm_polos.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.l_cm_polos)

        self.l_cm_outros = QLabel(self.frame_3)
        self.l_cm_outros.setObjectName(u"l_cm_outros")
        self.l_cm_outros.setMinimumSize(QSize(0, 20))
        self.l_cm_outros.setMaximumSize(QSize(16777215, 20))
        self.l_cm_outros.setText(u"Outros")
        self.l_cm_outros.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.l_cm_outros)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.i_cm_nome = QLineEdit(self.frame_2)
        self.i_cm_nome.setObjectName(u"i_cm_nome")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.i_cm_nome.sizePolicy().hasHeightForWidth())
        self.i_cm_nome.setSizePolicy(sizePolicy3)
        self.i_cm_nome.setMinimumSize(QSize(0, 20))
        self.i_cm_nome.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.i_cm_nome)

        self.i_cm_potencia = QLineEdit(self.frame_2)
        self.i_cm_potencia.setObjectName(u"i_cm_potencia")
        sizePolicy3.setHeightForWidth(self.i_cm_potencia.sizePolicy().hasHeightForWidth())
        self.i_cm_potencia.setSizePolicy(sizePolicy3)
        self.i_cm_potencia.setMinimumSize(QSize(0, 20))
        self.i_cm_potencia.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.i_cm_potencia)

        self.i_cm_tensao = QLineEdit(self.frame_2)
        self.i_cm_tensao.setObjectName(u"i_cm_tensao")
        sizePolicy3.setHeightForWidth(self.i_cm_tensao.sizePolicy().hasHeightForWidth())
        self.i_cm_tensao.setSizePolicy(sizePolicy3)
        self.i_cm_tensao.setMinimumSize(QSize(0, 20))
        self.i_cm_tensao.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.i_cm_tensao)

        self.i_cm_corrente = QLineEdit(self.frame_2)
        self.i_cm_corrente.setObjectName(u"i_cm_corrente")
        sizePolicy3.setHeightForWidth(self.i_cm_corrente.sizePolicy().hasHeightForWidth())
        self.i_cm_corrente.setSizePolicy(sizePolicy3)
        self.i_cm_corrente.setMinimumSize(QSize(0, 20))
        self.i_cm_corrente.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.i_cm_corrente)

        self.i_cm_frequencia = QLineEdit(self.frame_2)
        self.i_cm_frequencia.setObjectName(u"i_cm_frequencia")
        sizePolicy3.setHeightForWidth(self.i_cm_frequencia.sizePolicy().hasHeightForWidth())
        self.i_cm_frequencia.setSizePolicy(sizePolicy3)
        self.i_cm_frequencia.setMinimumSize(QSize(0, 20))
        self.i_cm_frequencia.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.i_cm_frequencia)

        self.i_cm_rpm = QLineEdit(self.frame_2)
        self.i_cm_rpm.setObjectName(u"i_cm_rpm")
        sizePolicy3.setHeightForWidth(self.i_cm_rpm.sizePolicy().hasHeightForWidth())
        self.i_cm_rpm.setSizePolicy(sizePolicy3)
        self.i_cm_rpm.setMinimumSize(QSize(0, 20))
        self.i_cm_rpm.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.i_cm_rpm)

        self.i_cm_cos = QLineEdit(self.frame_2)
        self.i_cm_cos.setObjectName(u"i_cm_cos")
        sizePolicy3.setHeightForWidth(self.i_cm_cos.sizePolicy().hasHeightForWidth())
        self.i_cm_cos.setSizePolicy(sizePolicy3)
        self.i_cm_cos.setMinimumSize(QSize(0, 20))
        self.i_cm_cos.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.i_cm_cos)

        self.i_cm_polos = QLineEdit(self.frame_2)
        self.i_cm_polos.setObjectName(u"i_cm_polos")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.i_cm_polos.sizePolicy().hasHeightForWidth())
        self.i_cm_polos.setSizePolicy(sizePolicy4)
        self.i_cm_polos.setMinimumSize(QSize(0, 20))
        self.i_cm_polos.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.i_cm_polos)

        self.i_cm_outros = QLineEdit(self.frame_2)
        self.i_cm_outros.setObjectName(u"i_cm_outros")
        sizePolicy3.setHeightForWidth(self.i_cm_outros.sizePolicy().hasHeightForWidth())
        self.i_cm_outros.setSizePolicy(sizePolicy3)
        self.i_cm_outros.setMinimumSize(QSize(0, 80))
        self.i_cm_outros.setMaximumSize(QSize(16777215, 80))
        self.i_cm_outros.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.i_cm_outros)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        self.b_cm_cadastrar = QPushButton(Dialog)
        self.b_cm_cadastrar.setObjectName(u"b_cm_cadastrar")

        self.verticalLayout.addWidget(self.b_cm_cadastrar)


        self.retranslateUi(Dialog)
        self.b_cm_cadastrar.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cadastrar Maquina", None))
        self.cm_logo.setText("")
#if QT_CONFIG(whatsthis)
        self.l_cm_cabecalho.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"right\"><span style=\" font-size:18pt; color:#ffffff;\">Cadastrar</span></p><p align=\"right\"><span style=\" font-size:18pt; color:#ffffff;\">M\u00e1quina</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.l_cm_cabecalho.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"right\"><span style=\" font-size:18pt; color:#ffffff;\">Cadastrar</span></p><p align=\"right\"><span style=\" font-size:18pt; color:#ffffff;\">M\u00e1quina</span></p></body></html>", None))
        self.i_cm_outros.setText("")
        self.b_cm_cadastrar.setText(QCoreApplication.translate("Dialog", u"Cadastrar", None))
    # retranslateUi

