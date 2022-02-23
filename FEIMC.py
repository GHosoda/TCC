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
from funcoes import *
import statsmodels.api as sm
from datetime import date


############################################################
# %%
class FEIMC:
    def __init__(self, dfs, **kwargs):
        self.__dfs = dfs

    @property
    def resultado(self):
        return self.__resultado

    def remapeamento(self, wt_abas, wt_colunas={}):
        print('#'*30)
        print('ANTES')
        print('#'*30)
        print(wt_abas)
        print(wt_colunas)
        wt_abas = {valor: chave for chave,
                   valor in wt_abas.items() if not(valor == '')}
        wt_colunas = {valor[:valor.find('##')]: chave for chave, valor in wt_colunas.items() if not(valor == '')}
        print('#'*30)
        print('DEPOIS')
        print('#'*30)
        print(wt_abas)
        print(wt_colunas)
        for aba, df in self.__dfs.items():
            pass

    def dataframes(self, inputs, abas, **kwargs):
        dfs = pd.read_excel(self.__arquivo, sheet_name=None)
        usadas = []
        dici = {}

        inputs = {key: value.split(';') for (key, value) in inputs.items()}
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
        dfs = self.__funcao()


############################################################
# %%          INÍCIO DO PROGRAMA
############################################################
if __name__ == '__main__':
    dfs = pd.read_excel('Ensaios\\7 - MIT NOVA 15 cv (14-02-2019).xlsx', sheet_name=None)
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

    k = [dfs]
    classe = IEEE112MetodoB()
    dfs = classe.calculo(k, **kwargs)
    for resultado in dfs:
        with pd.ExcelWriter('Resultado.xlsx') as writer:
            for chave, valor in resultado.items():
                print('\n\n\n\n')
                print(chave)
                print(100*'#')
                print(valor)
                valor.to_excel(writer, sheet_name = chave, index = False)
