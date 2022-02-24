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
from funcoes import *
from datetime import date
from dic_equip import (equipamentos_corrente,
                       equipamentos_frequencia,
                       equipamentos_potencia,
                       equipamentos_resistencia,
                       equipamentos_rpm,
                       equipamentos_temperatura,
                       equipamentos_tensao,
                       equipamentos_torque)


############################################################
# %%
class FEIMC:
    def __init__(self, dfs, classe, **kwargs):
        self._dfs = dfs
        self._classe = classe

    @property
    def resultado(self):
        return self.__resultado

    def remapeamento(self, wt_abas, wt_colunas={}):  # Corrigir
        wt_abas = {valor: chave for chave,
                   valor in wt_abas.items() if not(valor == '')}
        wt_colunas = {valor[:valor.find(
            '##')]: chave for chave, valor in wt_colunas.items() if not(valor == '')}
        for aba, df in self.__dfs.items():
            pass

    def incertezas(self, series, pontos, dici_bool, equipamentos, escalas_auto = True, **kwargs):
        classe = self._classe
        g_colunas = classe.incertezas()
        funcoes = {'Corrente': equipamentos_corrente,
                   'Tensao': equipamentos_tensao,
                   'Potencia': equipamentos_potencia,
                   'Frequencia': equipamentos_frequencia,
                   'Resistencia': equipamentos_resistencia,
                   'Torque': equipamentos_torque,
                   'RPM': equipamentos_rpm,
                   'Temperatura': equipamentos_temperatura}
        
        coluna = series.name
        grandeza = ''
        for chave, colunas in g_colunas:
            if coluna in colunas:
                grandeza = chave
        
        if grandeza == '':
            series_mc = self.placebo(series, pontos)
        
        if dici_bool[grandeza]:
            funcao = funcoes[grandeza]
            series_mc = funcao(series, equipamentos, pontos, escalas_auto, **kwargs)
        series_mc = series
        return series_mc

    def placebo(self, series, pontos):
        series_mc = series.map(lambda x: [k for k in range(pontos+1)])
        return series_mc

    def calculo(self, **kwargs):
        metodo = self._classe
        dfs_mc = metodo.calculo(dfs_mc, **kwargs)


############################################################
# %%          INÍCIO DO PROGRAMA
############################################################
if True:
    dfs = pd.read_excel(
        'Ensaios\\7 - MIT NOVA 15 cv (14-02-2019).xlsx', sheet_name=None)
    abas = ['Resistências', 'de Carga', 'a Vazio']
    abas_excel = ['Ensaio_Vazio', 'Ensaio_Carga',
                  'Ensaio_Termico_Carga', 'Ensaio_Termico_Vazio']
    colunas_excel = {'Resistencias': ['RS', 'RT', 'ST', 'T_amb', 'T_res'],
                     'de Carga': ['Tensao', 'Corrente', 'Potencia', 'Frequencia', 'Temperatura', 'Torque', 'RPM'],
                     'a Vazio': ['Tensao', 'Corrente', 'Potencia', 'Frequencia']
                     }

    kwargs = {'Material Estator': 'Cobre',
              'Material Rotor': 'Alumínio',
              'Potencia Nominal': 11000,
              'Polos': 4,
              'Tensao Nominal': 380}

if __name__ == '__main__':
    k = [dfs]
    classe = IEEE112MetodoB()
    incertezas = classe.incertezas()
    print(incertezas)
    dfs = classe.calculo(k, **kwargs)
