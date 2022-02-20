# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_nova.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#import imagens_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 918)
        icon = QIcon()
        icon.addFile("Imagens/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionSalvar = QAction(MainWindow)
        self.actionSalvar.setObjectName(u"actionSalvar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionNovo = QAction(MainWindow)
        self.actionNovo.setObjectName(u"actionNovo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cabecalho = QFrame(self.centralwidget)
        self.cabecalho.setObjectName(u"cabecalho")
        self.cabecalho.setEnabled(True)
        self.cabecalho.setMinimumSize(QSize(0, 120))
        self.cabecalho.setMaximumSize(QSize(16777215, 120))
        self.cabecalho.setAutoFillBackground(False)
        self.cabecalho.setStyleSheet(u"background-color: rgb(132, 153, 165);")
        self.cabecalho.setFrameShape(QFrame.NoFrame)
        self.cabecalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.cabecalho)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.logo = QLabel(self.cabecalho)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(300, 100))
        self.logo.setMaximumSize(QSize(300, 100))
        self.logo.setPixmap(QPixmap(u"Imagens/logo-feimc-escrita.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.logo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.logo_2 = QLabel(self.cabecalho)
        self.logo_2.setObjectName(u"logo_2")
        sizePolicy.setHeightForWidth(self.logo_2.sizePolicy().hasHeightForWidth())
        self.logo_2.setSizePolicy(sizePolicy)
        self.logo_2.setMinimumSize(QSize(300, 100))
        self.logo_2.setMaximumSize(QSize(300, 100))
        self.logo_2.setPixmap(QPixmap(u"Imagens/grucad-01.png"))
        self.logo_2.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.logo_2)


        self.verticalLayout.addWidget(self.cabecalho)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(132, 153, 165);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self.horizontalLayout_2 = QHBoxLayout(self.config)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_config = QFrame(self.config)
        self.frame_config.setObjectName(u"frame_config")
        sizePolicy1.setHeightForWidth(self.frame_config.sizePolicy().hasHeightForWidth())
        self.frame_config.setSizePolicy(sizePolicy1)
        self.frame_config.setMinimumSize(QSize(200, 300))
        self.frame_config.setStyleSheet(u"")
        self.frame_config.setFrameShape(QFrame.StyledPanel)
        self.frame_config.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_config)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.config_gerais = QFrame(self.frame_config)
        self.config_gerais.setObjectName(u"config_gerais")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.config_gerais.sizePolicy().hasHeightForWidth())
        self.config_gerais.setSizePolicy(sizePolicy2)
        self.config_gerais.setMinimumSize(QSize(200, 0))
        self.config_gerais.setMaximumSize(QSize(16777215, 16777215))
        self.config_gerais.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.config_gerais.setFrameShape(QFrame.StyledPanel)
        self.config_gerais.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.config_gerais)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.l_geral = QLabel(self.config_gerais)
        self.l_geral.setObjectName(u"l_geral")

        self.verticalLayout_2.addWidget(self.l_geral)

        self.operador = QLabel(self.config_gerais)
        self.operador.setObjectName(u"operador")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.operador.sizePolicy().hasHeightForWidth())
        self.operador.setSizePolicy(sizePolicy3)
        self.operador.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.operador)

        self.i_operador = QLineEdit(self.config_gerais)
        self.i_operador.setObjectName(u"i_operador")

        self.verticalLayout_2.addWidget(self.i_operador)

        self.l_ensaio = QLabel(self.config_gerais)
        self.l_ensaio.setObjectName(u"l_ensaio")
        sizePolicy3.setHeightForWidth(self.l_ensaio.sizePolicy().hasHeightForWidth())
        self.l_ensaio.setSizePolicy(sizePolicy3)
        self.l_ensaio.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.l_ensaio)

        self.c_ensaio = QComboBox(self.config_gerais)
        self.c_ensaio.setObjectName(u"c_ensaio")

        self.verticalLayout_2.addWidget(self.c_ensaio)

        self.b_ensaio = QPushButton(self.config_gerais)
        self.b_ensaio.setObjectName(u"b_ensaio")

        self.verticalLayout_2.addWidget(self.b_ensaio)

        self.l_arquivo = QLabel(self.config_gerais)
        self.l_arquivo.setObjectName(u"l_arquivo")
        sizePolicy3.setHeightForWidth(self.l_arquivo.sizePolicy().hasHeightForWidth())
        self.l_arquivo.setSizePolicy(sizePolicy3)
        self.l_arquivo.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.l_arquivo)

        self.i_arquivo = QLineEdit(self.config_gerais)
        self.i_arquivo.setObjectName(u"i_arquivo")

        self.verticalLayout_2.addWidget(self.i_arquivo)

        self.b_arquivo = QPushButton(self.config_gerais)
        self.b_arquivo.setObjectName(u"b_arquivo")

        self.verticalLayout_2.addWidget(self.b_arquivo)

        self.label = QLabel(self.config_gerais)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.dateEdit = QDateEdit(self.config_gerais)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setMaximumDateTime(QDateTime(QDate(9999, 12, 31), QTime(23, 59, 59)))
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.dateEdit)

        self.l_pontos = QLabel(self.config_gerais)
        self.l_pontos.setObjectName(u"l_pontos")
        sizePolicy3.setHeightForWidth(self.l_pontos.sizePolicy().hasHeightForWidth())
        self.l_pontos.setSizePolicy(sizePolicy3)
        self.l_pontos.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.l_pontos)

        self.s_pontos = QSpinBox(self.config_gerais)
        self.s_pontos.setObjectName(u"s_pontos")
        self.s_pontos.setMinimum(1)
        self.s_pontos.setMaximum(10000)
        self.s_pontos.setValue(1000)

        self.verticalLayout_2.addWidget(self.s_pontos)

        self.cb_escalas = QCheckBox(self.config_gerais)
        self.cb_escalas.setObjectName(u"cb_escalas")

        self.verticalLayout_2.addWidget(self.cb_escalas)

        self.l_maquinas = QLabel(self.config_gerais)
        self.l_maquinas.setObjectName(u"l_maquinas")
        self.l_maquinas.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.l_maquinas)

        self.c_maquina = QComboBox(self.config_gerais)
        self.c_maquina.setObjectName(u"c_maquina")

        self.verticalLayout_2.addWidget(self.c_maquina)

        self.b_maquina = QPushButton(self.config_gerais)
        self.b_maquina.setObjectName(u"b_maquina")

        self.verticalLayout_2.addWidget(self.b_maquina)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.b_start = QPushButton(self.config_gerais)
        self.b_start.setObjectName(u"b_start")

        self.verticalLayout_2.addWidget(self.b_start)


        self.horizontalLayout.addWidget(self.config_gerais)

        self.espaco_1 = QFrame(self.frame_config)
        self.espaco_1.setObjectName(u"espaco_1")
        self.espaco_1.setFrameShape(QFrame.VLine)
        self.espaco_1.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.espaco_1)

        self.config_equip = QFrame(self.frame_config)
        self.config_equip.setObjectName(u"config_equip")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.config_equip.sizePolicy().hasHeightForWidth())
        self.config_equip.setSizePolicy(sizePolicy4)
        self.config_equip.setMinimumSize(QSize(200, 0))
        self.config_equip.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.config_equip.setFrameShape(QFrame.StyledPanel)
        self.config_equip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.config_equip)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.l_grandezas = QLabel(self.config_equip)
        self.l_grandezas.setObjectName(u"l_grandezas")

        self.verticalLayout_3.addWidget(self.l_grandezas)

        self.cb_corrente = QCheckBox(self.config_equip)
        self.cb_corrente.setObjectName(u"cb_corrente")

        self.verticalLayout_3.addWidget(self.cb_corrente)

        self.c_corrente = QComboBox(self.config_equip)
        self.c_corrente.setObjectName(u"c_corrente")

        self.verticalLayout_3.addWidget(self.c_corrente)

        self.cb_tensao = QCheckBox(self.config_equip)
        self.cb_tensao.setObjectName(u"cb_tensao")

        self.verticalLayout_3.addWidget(self.cb_tensao)

        self.c_tensao = QComboBox(self.config_equip)
        self.c_tensao.setObjectName(u"c_tensao")

        self.verticalLayout_3.addWidget(self.c_tensao)

        self.cb_potencia = QCheckBox(self.config_equip)
        self.cb_potencia.setObjectName(u"cb_potencia")

        self.verticalLayout_3.addWidget(self.cb_potencia)

        self.c_potencia = QComboBox(self.config_equip)
        self.c_potencia.setObjectName(u"c_potencia")

        self.verticalLayout_3.addWidget(self.c_potencia)

        self.cb_frequencia = QCheckBox(self.config_equip)
        self.cb_frequencia.setObjectName(u"cb_frequencia")

        self.verticalLayout_3.addWidget(self.cb_frequencia)

        self.c_frequencia = QComboBox(self.config_equip)
        self.c_frequencia.setObjectName(u"c_frequencia")

        self.verticalLayout_3.addWidget(self.c_frequencia)

        self.cb_resistencia = QCheckBox(self.config_equip)
        self.cb_resistencia.setObjectName(u"cb_resistencia")

        self.verticalLayout_3.addWidget(self.cb_resistencia)

        self.c_resistencia = QComboBox(self.config_equip)
        self.c_resistencia.setObjectName(u"c_resistencia")

        self.verticalLayout_3.addWidget(self.c_resistencia)

        self.cb_torque = QCheckBox(self.config_equip)
        self.cb_torque.setObjectName(u"cb_torque")

        self.verticalLayout_3.addWidget(self.cb_torque)

        self.c_torque = QComboBox(self.config_equip)
        self.c_torque.setObjectName(u"c_torque")

        self.verticalLayout_3.addWidget(self.c_torque)

        self.cb_rpm = QCheckBox(self.config_equip)
        self.cb_rpm.setObjectName(u"cb_rpm")

        self.verticalLayout_3.addWidget(self.cb_rpm)

        self.c_rpm = QComboBox(self.config_equip)
        self.c_rpm.setObjectName(u"c_rpm")

        self.verticalLayout_3.addWidget(self.c_rpm)

        self.cb_temperatura = QCheckBox(self.config_equip)
        self.cb_temperatura.setObjectName(u"cb_temperatura")

        self.verticalLayout_3.addWidget(self.cb_temperatura)

        self.c_temperatura = QComboBox(self.config_equip)
        self.c_temperatura.setObjectName(u"c_temperatura")

        self.verticalLayout_3.addWidget(self.c_temperatura)

        self.verticalSpacer_2 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.config_equip)

        self.espaco_2 = QFrame(self.frame_config)
        self.espaco_2.setObjectName(u"espaco_2")
        self.espaco_2.setFrameShape(QFrame.VLine)
        self.espaco_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.espaco_2)

        self.config_dados = QFrame(self.frame_config)
        self.config_dados.setObjectName(u"config_dados")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.config_dados.sizePolicy().hasHeightForWidth())
        self.config_dados.setSizePolicy(sizePolicy5)
        self.config_dados.setMinimumSize(QSize(200, 0))
        self.config_dados.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.config_dados.setFrameShape(QFrame.StyledPanel)
        self.config_dados.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.config_dados)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea = QScrollArea(self.config_dados)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 296, 623))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.l_at_col = QLabel(self.scrollAreaWidgetContents)
        self.l_at_col.setObjectName(u"l_at_col")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.l_at_col.sizePolicy().hasHeightForWidth())
        self.l_at_col.setSizePolicy(sizePolicy6)

        self.verticalLayout_10.addWidget(self.l_at_col)

        self.w_colunas = QWidget(self.scrollAreaWidgetContents)
        self.w_colunas.setObjectName(u"w_colunas")

        self.verticalLayout_10.addWidget(self.w_colunas)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_2)

        self.l_at_abas = QLabel(self.scrollAreaWidgetContents)
        self.l_at_abas.setObjectName(u"l_at_abas")
        sizePolicy6.setHeightForWidth(self.l_at_abas.sizePolicy().hasHeightForWidth())
        self.l_at_abas.setSizePolicy(sizePolicy6)

        self.verticalLayout_10.addWidget(self.l_at_abas)

        self.w_abas = QWidget(self.scrollAreaWidgetContents)
        self.w_abas.setObjectName(u"w_abas")

        self.verticalLayout_10.addWidget(self.w_abas)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.config_dados)


        self.horizontalLayout_2.addWidget(self.frame_config)

        self.tabWidget.addTab(self.config, "")
        self.resultados = QWidget()
        self.resultados.setObjectName(u"resultados")
        self.verticalLayout_6 = QVBoxLayout(self.resultados)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.resultados)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(200, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.l_resultados = QLabel(self.frame_2)
        self.l_resultados.setObjectName(u"l_resultados")

        self.verticalLayout_7.addWidget(self.l_resultados)

        self.cb_violino = QCheckBox(self.frame_2)
        self.cb_violino.setObjectName(u"cb_violino")

        self.verticalLayout_7.addWidget(self.cb_violino)

        self.cb_boxplot = QCheckBox(self.frame_2)
        self.cb_boxplot.setObjectName(u"cb_boxplot")

        self.verticalLayout_7.addWidget(self.cb_boxplot)

        self.cb_histograma_nominal = QCheckBox(self.frame_2)
        self.cb_histograma_nominal.setObjectName(u"cb_histograma_nominal")

        self.verticalLayout_7.addWidget(self.cb_histograma_nominal)

        self.cb_histograma = QCheckBox(self.frame_2)
        self.cb_histograma.setObjectName(u"cb_histograma")

        self.verticalLayout_7.addWidget(self.cb_histograma)

        self.cb_max_min = QCheckBox(self.frame_2)
        self.cb_max_min.setObjectName(u"cb_max_min")

        self.verticalLayout_7.addWidget(self.cb_max_min)

        self.cb_media = QCheckBox(self.frame_2)
        self.cb_media.setObjectName(u"cb_media")

        self.verticalLayout_7.addWidget(self.cb_media)

        self.cb_moda = QCheckBox(self.frame_2)
        self.cb_moda.setObjectName(u"cb_moda")

        self.verticalLayout_7.addWidget(self.cb_moda)

        self.cb_mediana = QCheckBox(self.frame_2)
        self.cb_mediana.setObjectName(u"cb_mediana")

        self.verticalLayout_7.addWidget(self.cb_mediana)

        self.cb_desvio_padrao = QCheckBox(self.frame_2)
        self.cb_desvio_padrao.setObjectName(u"cb_desvio_padrao")

        self.verticalLayout_7.addWidget(self.cb_desvio_padrao)

        self.cb_variancia = QCheckBox(self.frame_2)
        self.cb_variancia.setObjectName(u"cb_variancia")

        self.verticalLayout_7.addWidget(self.cb_variancia)

        self.cb_quartis = QCheckBox(self.frame_2)
        self.cb_quartis.setObjectName(u"cb_quartis")

        self.verticalLayout_7.addWidget(self.cb_quartis)

        self.verticalSpacer_4 = QSpacerItem(20, 344, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.cb_todos_resultados = QCheckBox(self.frame_2)
        self.cb_todos_resultados.setObjectName(u"cb_todos_resultados")

        self.verticalLayout_7.addWidget(self.cb_todos_resultados)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_7.addWidget(self.pushButton)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.w_resultado = QWidget(self.frame_3)
        self.w_resultado.setObjectName(u"w_resultado")

        self.verticalLayout_9.addWidget(self.w_resultado)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.tabWidget.addTab(self.resultados, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame)

        self.rodape = QFrame(self.centralwidget)
        self.rodape.setObjectName(u"rodape")
        self.rodape.setMinimumSize(QSize(0, 70))
        self.rodape.setMaximumSize(QSize(16777215, 70))
        self.rodape.setStyleSheet(u"background-color: rgb(132, 153, 165);")
        self.rodape.setFrameShape(QFrame.StyledPanel)
        self.rodape.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.rodape)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.rodape)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.l_rodape = QLabel(self.frame_6)
        self.l_rodape.setObjectName(u"l_rodape")

        self.verticalLayout_8.addWidget(self.l_rodape)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)


        self.horizontalLayout_9.addWidget(self.frame_6)

        self.logo_3 = QLabel(self.rodape)
        self.logo_3.setObjectName(u"logo_3")
        sizePolicy.setHeightForWidth(self.logo_3.sizePolicy().hasHeightForWidth())
        self.logo_3.setSizePolicy(sizePolicy)
        self.logo_3.setMinimumSize(QSize(40, 50))
        self.logo_3.setMaximumSize(QSize(40, 50))
        self.logo_3.setPixmap(QPixmap(u"Imagens/ufsc.png"))
        self.logo_3.setScaledContents(True)
        self.logo_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_9.addWidget(self.logo_3)

        self.frame_5 = QFrame(self.rodape)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.rodape)

        MainWindow.setCentralWidget(self.centralwidget)
        self.rodape.raise_()
        self.frame.raise_()
        self.cabecalho.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 998, 21))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionNovo)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FEIMC", None))
        self.actionSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionNovo.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.logo.setText("")
        self.logo_2.setText("")
#if QT_CONFIG(whatsthis)
        self.l_geral.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Grandezas</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.l_geral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Geral</span></p></body></html>", None))
        self.operador.setText(QCoreApplication.translate("MainWindow", u"Operador", None))
        self.l_ensaio.setText(QCoreApplication.translate("MainWindow", u"Ensaio", None))
        self.b_ensaio.setText(QCoreApplication.translate("MainWindow", u"Configurar Ensaio", None))
        self.l_arquivo.setText(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.b_arquivo.setText(QCoreApplication.translate("MainWindow", u"Selecionar Arquivo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.l_pontos.setText(QCoreApplication.translate("MainWindow", u"Pontos Monte Carlo", None))
        self.cb_escalas.setText(QCoreApplication.translate("MainWindow", u"Escalas Autom\u00e1ticas", None))
        self.l_maquinas.setText(QCoreApplication.translate("MainWindow", u"M\u00e1quina", None))
        self.b_maquina.setText(QCoreApplication.translate("MainWindow", u"Adicionar nova", None))
        self.b_start.setText(QCoreApplication.translate("MainWindow", u"Rodar Simula\u00e7\u00e3o", None))
#if QT_CONFIG(whatsthis)
        self.l_grandezas.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Grandezas</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.l_grandezas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Grandezas</span></p></body></html>", None))
        self.cb_corrente.setText(QCoreApplication.translate("MainWindow", u"Corrente", None))
        self.cb_tensao.setText(QCoreApplication.translate("MainWindow", u"Tens\u00e3o", None))
        self.cb_potencia.setText(QCoreApplication.translate("MainWindow", u"Pot\u00eancia", None))
        self.cb_frequencia.setText(QCoreApplication.translate("MainWindow", u"Frequ\u00eancia", None))
        self.cb_resistencia.setText(QCoreApplication.translate("MainWindow", u"Resist\u00eancia", None))
        self.cb_torque.setText(QCoreApplication.translate("MainWindow", u"Torque", None))
        self.cb_rpm.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.cb_temperatura.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
#if QT_CONFIG(whatsthis)
        self.l_at_col.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Grandezas</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.l_at_col.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Atribuir Colunas</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.l_at_abas.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Grandezas</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.l_at_abas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Atribuir Abas</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
#if QT_CONFIG(whatsthis)
        self.l_resultados.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Grandezas</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.l_resultados.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Apresentar no relat\u00f3rio</span></p></body></html>", None))
        self.cb_violino.setText(QCoreApplication.translate("MainWindow", u"ViollinPlot", None))
        self.cb_boxplot.setText(QCoreApplication.translate("MainWindow", u"BoxPlot", None))
        self.cb_histograma_nominal.setText(QCoreApplication.translate("MainWindow", u"Histograma (nominal apenas)", None))
        self.cb_histograma.setText(QCoreApplication.translate("MainWindow", u"Histograma (todos)", None))
        self.cb_max_min.setText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo e m\u00ednimo", None))
        self.cb_media.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia", None))
        self.cb_moda.setText(QCoreApplication.translate("MainWindow", u"Moda", None))
        self.cb_mediana.setText(QCoreApplication.translate("MainWindow", u"Mediana", None))
        self.cb_desvio_padrao.setText(QCoreApplication.translate("MainWindow", u"Desvio Padr\u00e3o", None))
        self.cb_variancia.setText(QCoreApplication.translate("MainWindow", u"Vari\u00e2ncia", None))
        self.cb_quartis.setText(QCoreApplication.translate("MainWindow", u"Quartis", None))
        self.cb_todos_resultados.setText(QCoreApplication.translate("MainWindow", u"Selecionar todos", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Gerar Relat\u00f3rio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resultados), QCoreApplication.translate("MainWindow", u"Resultados", None))
#if QT_CONFIG(whatsthis)
        self.l_rodape.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Guilherme Hosoda Souza Reis</span></p><p><span style=\" font-weight:600; color:#ffffff;\">Trabalho de Conclus\u00e3o de Curso 2021-2</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.l_rodape.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Trabalho de Conclus\u00e3o de Curso 2021-2</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Guilherme Hosoda Souza Reis</span></p></body></html>", None))
        self.logo_3.setText("")
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
    # retranslateUi

