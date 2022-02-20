############################################################
#
#           TRABALHO DE CONCLUSÃO DE CURSO - TCC
#           GUILHERME HOSODA SOUZA REIS
#           UNIVERSIDADE FEDERAL DE SANTA CATARINA
#           2021-2
#
############################################################
#           IMPORTAÇÃO DAS BIBLIOTECAS
############################################################
# %%
#from PySide2 import QtCore
import numpy as np
import pandas as pd
from copy import deepcopy
import dic_equip
import funcoes
import statsmodels.api as sm
from ui_interface import Ui_MainWindow
from interface_cadastrar import Ui_Cadastro
from interface_nova import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from datetime import date
from pathlib import Path
from inspect import getmembers, isfunction


############################################################
#           CRIAÇÃO DA CLASSE
############################################################
# %%
class Plot:
    def __init__(self, dfs, tipo_plot, **kwargs):
        self.__dfs = dfs
        self.__tipo_plot = tipo_plot


############################################################
# %%
class Interface(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.b_start.clicked.connect(self.rodar)
        self.b_arquivo.clicked.connect(self.aba_abrir)
        self.b_maquina.clicked.connect(self.aba_cadastrar)
        self.b_ensaio.clicked.connect(self.indicar_col_abas)
        self.set_comboboxes()

    def rodar(self):
        inputs, abas, checkboxes_config, checkboxes_results, comboboxes, dia, pontos = self.dicionario_dados()
        if inputs['Arquivo'] == '' or inputs['Operador'] == '':
            msg = QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setText(
                'Deve preencher corretamente o local do arquivo e o nome do Operador')
            msg.exec()
            return
        #print(f'{inputs} \n{abas}\n{checkboxes_config}\n{checkboxes_results}\n{comboboxes}\n{dia}\nPontos: {pontos}')
        saida = FEIMC(inputs, abas, checkboxes_config, comboboxes, dia, pontos)

    def set_comboboxes(self):
        maquinas = pd.read_csv('Maquinas\maquinas.csv', sep=';', index_col=None)
        functions = [i[0] for i in (getmembers(funcoes, isfunction))]

        self.c_ensaio.addItems(functions),
        self.c_maquina.addItems(list(maquinas['id'])),
        self.c_corrente.addItems(['WT500']),
        self.c_frequencia.addItems(['WT500']),
        self.c_potencia.addItems(['WT500']),
        self.c_resistencia.addItems(['Agilent34410A']),
        self.c_rpm.addItems(['HBMTB40']),
        self.c_temperatura.addItems(['YokogawaGP10']),
        self.c_tensao.addItems(['WT500']),
        self.c_torque.addItems(['HBMTB40'])

        dia = (int(x) for x in str(date.today()).split('-'))
        self.dateEdit.setDate(QDate(*dia))

    def indicar_col_abas(self):
        pass

    def aba_cadastrar(self):
        cadastro = NovoCadastro(self)
        cadastro.exec_()
    
    def aba_abrir(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', r'C:\Users\guilh\Desktop\TCC VSCode', 'Images (*.png, *.xmp *.jpg)')
        self.filename.setText(fname[0])

    def nova_maquina(self):
        dicionario = {'id': ['MIT NOVA 5 cv 2'],
                      'Potência (kW)': ['3.7'],
                      'Tensão (V)': ['380'],
                      'Corrente (A)': ['8.2'],
                      'Frequência (Hz)': ['60'],
                      'Rotação (RPM)': ['1740'],
                      'cos fi': ['0.78'],
                      'Polos': ['4']}

        antigo = pd.read_csv('Maquinas\maquinas.csv', sep=';', index_col=None)
        novo = pd.DataFrame(dicionario)
        final = pd.concat([antigo, novo])
        final.reset_index(drop=True, inplace=True)
        final.drop_duplicates(subset=['id'], inplace=True, keep='last')
        final.to_csv('Maquinas\maquinas.csv', sep=';', index=False)

    def dicionario_dados(self):
        """_summary_: Converte todos as entradas do usuário para dicionarios
        para facilitar a manipulação dos dados
        """
        inputs = {'Arquivo': self.i_arquivo.text(),
                  'Corrente': self.i_corrente.text(),
                  'Frequencia': self.i_frequencia.text(),
                  'Operador': self.i_operador.text(),
                  'Potencia': self.i_potencia.text(),
                  'Resistencia': self.i_resistencia.text(),
                  'RPM': self.i_rpm.text(),
                  'Temperatura': self.i_temperatura.text(),
                  'Tensao': self.i_tensao.text(),
                  'Torque': self.i_torque.text()}

        abas = {'Ensaio_Vazio': self.i_aba.text(),
                'Ensaio_Termico_Vazio': self.i_aba_2.text(),
                'Ensaio_Carga': self.i_aba_3.text(),
                'Ensaio_Termico_Carga': self.i_aba_4.text()}

        checkboxes_config = {'Escalas': self.cb_escalas.isChecked(),
                             'Corrente': self.cb_corrente.isChecked(),
                             'Tensao': self.cb_tensao.isChecked(),
                             'Frequencia': self.cb_frequencia.isChecked(),
                             'Potencia': self.cb_potencia.isChecked(),
                             'Resistencia': self.cb_resistencia.isChecked(),
                             'RPM': self.cb_rpm.isChecked(),
                             'Temperatura': self.cb_temperatura.isChecked(),
                             'Torque': self.cb_torque.isChecked()}

        checkboxes_results = {'boxplot': self.cb_boxplot.isChecked(),
                              'desvio_padrao': self.cb_desvio_padrao.isChecked(),
                              'histograma': self.cb_histograma.isChecked(),
                              'histograma_nominal': self.cb_histograma_nominal.isChecked(),
                              'max_min': self.cb_max_min.isChecked(),
                              'media': self.cb_media.isChecked(),
                              'mediana': self.cb_mediana.isChecked(),
                              'moda': self.cb_moda.isChecked(),
                              'quartis': self.cb_quartis.isChecked(),
                              'variancia': self.cb_variancia.isChecked(),
                              'violino': self.cb_violino.isChecked()}

        comboboxes = {'Ensaio': self.c_ensaio.currentText(),
                      'Maquina': self.c_maquina.currentText(),
                      'Corrente': self.c_corrente.currentText(),
                      'Frequencia': self.c_frequencia.currentText(),
                      'Potencia': self.c_potencia.currentText(),
                      'Resistencia': self.c_resistencia.currentText(),
                      'RPM': self.c_rpm.currentText(),
                      'Temperatura': self.c_temperatura.currentText(),
                      'Tensao': self.c_tensao.currentText(),
                      'Torque': self.c_torque.currentText()}
        dia = self.dateEdit.date()
        pontos = self.s_pontos.value()

        return(inputs, abas, checkboxes_config, checkboxes_results, comboboxes, dia, pontos)
    pass


class NovoCadastro(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Cadastro()
        
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
    

############################################################
# %%
class FEIMC:
    def __init__(self, inputs, abas, checkboxes_config, comboboxes, dia, pontos, **kwargs):
        func = {'IEEE112_Metodo_A': funcoes.IEEE112_Metodo_A,
                'IEEE112_Metodo_B': funcoes.IEEE112_Metodo_B}
        self.__arquivo = inputs['Arquivo']
        self.__pontos = pontos
        self.__funcao = func[comboboxes['Ensaio']]
        self.__maquina = comboboxes['Maquina']
        comboboxes.pop('Maquina', None)
        comboboxes.pop('Ensaio', None)
        self.__equipamentos = comboboxes
        self.__bool_incertezas = checkboxes_config
        self.__temperatura = 25
        self.__dia = dia
        self.dataframes(inputs, abas, **kwargs)
        #self.incertezas()
        #self.sep_dataframes()
        #self.__resultado = self.calculo(**kwargs)


    @property
    def resultado(self):
        return self.__resultado

    def dataframes(self, inputs, abas, **kwargs):
        dfs = pd.read_excel(self.__arquivo, sheet_name=None)
        usadas = []
        dici = {}

        print(inputs)
        inputs = {key: value.split(';') for (key, value) in inputs.items()}
        print(inputs)
        for chave, df in dfs.items():
            # Renomeando as colunas conforme padrão
            mapa_colunas = dict(zip(df.columns, df.columns))
            mapa_colunas.update(dict(zip(kwargs.values(), kwargs.keys())))
            mapa_colunas = {k: mapa_colunas[k] for k in df.columns}
            dfs[chave].rename(columns=mapa_colunas, inplace=True)

            # Renomeando os dataframes conforme padrão
            for key, valor in kwargs.items():
                if chave == valor:
                    dici[key] = df
                    usadas.append(chave)
        for usada in usadas:
            del dfs[usada]
        dfs.update(dici)
        self.__dfs = dfs

    def incertezas(self):
        dfs = self.__dfs
        for sheet, df in dfs.items():
            df = df.astype(object)
            # df = df.applymap(lambda x: np.ones(self.__pontos+1)*x)
            for row in df.index:
                df.at[row, :] = dic_equip.equipamentos(df.loc[row, :].to_dict(
                ), self.__equipamentos, self.__bool_incertezas, self.__pontos)
            dfs[sheet] = deepcopy(df)
        self.__dfs = dfs

    def sep_dataframes(self):
        dici = {}
        dici = {k: (self.__pontos + 1)*[None] for k in self.__dfs.keys()}
        for chave in self.__dfs.keys():
            for i in range(self.__pontos+1):
                dici[chave][i] = self.__dfs[chave].applymap(lambda x: x[i])
        self.__dfs = dici

    def calculo(self, **kwargs):
        for i in range(self.__pontos+1):
            dicionario = {chave: valor[i]
                          for chave, valor in self.__dfs.items()}
            resultado = self.__funcao(dicionario, **kwargs)
            for chave in dicionario.keys():
                self.__dfs[chave][i] = resultado[chave]
        return self.__dfs


############################################################
# %%
class Maquina:
    def __init__(self, nome, potencia, tensao, corrente, frequencia, rpm, cos_phi, polos):
        self.__nome = nome
        self.__potencia = potencia
        self.__tensao = tensao
        self.__corrente = corrente
        self.__frequencia = frequencia
        self.__rpm = rpm
        self.__cos_phi = cos_phi
        self.__polos = polos


############################################################
#           INÍCIO DO PROGRAMA
############################################################
# %%

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Principal = QMainWindow()
    ui = Interface(Principal)
    Principal.show()
    sys.exit(app.exec_())
    
'''
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Principal = QMainWindow()
    ui = Interface(Principal)
    Principal.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    inputs = {'Arquivo': u'Ensaios\Ensaio_Rendimento.xlsx',
              'Corrente': '',
              'Frequencia': '',
              'Operador': 'Gui',
              'Potencia': '',
              'Resistencia': 'RS;RT;ST',
              'RPM': '',
              'Temperatura': '',
              'Tensao': '',
              'Torque': ''}
    
    abas = {'Ensaio_Vazio': '',
            'Ensaio_Termico_Vazio': '',
            'Ensaio_Carga': '',
            'Ensaio_Termico_Carga': ''}
    
    checkboxes_config = {'Escalas': False,
                         'Corrente': False,
                         'Tensao': False,
                         'Frequencia': False,
                         'Potencia': False,
                         'Resistencia': False,
                         'RPM': False,
                         'Temperatura': False,
                         'Torque': False}
    
    checkboxes_results = {'boxplot': False,
                          'desvio_padrao': False,
                          'histograma': False,
                          'histograma_nominal': False,
                          'max_min': False,
                          'media': False,
                          'mediana': False,
                          'moda': False,
                          'quartis': False,
                          'variancia': False,
                          'violino': False}
    
    comboboxes = {'Ensaio': 'IEEE112_Metodo_A',
                  'Maquina': 'MIT NOVA 5 cv 2',
                  'Corrente': 'WT500',
                  'Frequencia': 'WT500',
                  'Potencia': 'WT500',
                  'Resistencia': 'Agilent34410A',
                  'RPM': 'HBMTB40',
                  'Temperatura': 'YokogawaGP10',
                  'Tensao': 'WT500',
                  'Torque': 'HBMTB40'}
    
    dia = QDate(2022, 2, 19)
    
    pontos = 2

    teste = FEIMC(inputs, abas, checkboxes_config, comboboxes, dia, pontos)
'''