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
from os import path
import numpy as np
import pandas as pd
from copy import deepcopy
from funcoes import *
from datetime import date
from dic_equip import Sensores
from scipy import stats
import seaborn as sns
from functools import partial


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

    def incertezas(self, pontos, dici_bool, equipamentos, escalas_auto = True, **kwargs):
        classe = self._classe
        dfs = self._dfs
        g_colunas = classe.incertezas()
        g_colunas = {chave: valor for chave, valor in g_colunas if dici_bool[chave]}
        
        for aba, df in dfs.items():
            for coluna in df.columns:
                for grandeza, colunas in g_colunas:
                    if coluna in colunas:
                        df[coluna] = Sensores(df, coluna, grandeza, equipamentos, escalas_auto)
        
            df = df.applymap(lambda x: self.placebo(x, pontos))

    def placebo(self, valor, pontos):
        if isinstance(valor, list):
            return valor
        list_valor = [valor for k in range(pontos+1)]
        return list_valor

    def calculo(self, **kwargs):
        metodo = self._classe
        dfs_mc = metodo.calculo(dfs_mc, **kwargs)
        
    def list2df(self, lista):
        dfs = deepcopy(lista[0])
        pontos = len(lista) - 1
        for aba, df in dfs.items():
            for coluna in df.columns:
                dfs[aba][coluna] = dfs[aba][coluna].astype('object')
                for index in df.index:
                    aux = []
                    for i in range(pontos):
                        aux.append(lista[i][aba].loc[index, coluna])
                    dfs[aba].at[index, coluna] = deepcopy(aux)
        return dfs
        
    def saidas(self, lista, prints):
        dfs = self.list2df(self, lista)
        df = dfs['Resultado']
        x = 'Potencia [pu]'
        y = 'Rendimento'
        
        #Calculo dos dataframes de saída
        dados = {'desvio_padrao': df.applymap(lambda x: np.std(x)),
                 'max_min': [df.applymap(lambda x: np.max(x)), df.applymap(lambda x: np.min(x))],
                 'media': df.applymap(lambda x: np.mean(x)),
                 'mediana': df.applymap(lambda x: np.median(x)),
                 'moda': df.applymap(lambda x: stats.mode(x)),
                 'quartis': [df.applymap(lambda x: stats.scoreatpercentile(x, 25)), df.applymap(lambda x: stats.scoreatpercentile(x, 75))],
                 'variancia': df.applymap(lambda x: np.var(x))}
        
        nomes = {'max_min': ['máximo', 'mínimo'],
                 'quartis': ['1_4', '3_4']}
        
        #Salvar os dataframes
        with pd.ExcelWriter('Resumo.xlsx') as writer:
            for chave, valor in dados.items():
                if prints[chave]:
                    if isinstance(valor, list):
                        for i, pedaco in enumerate(valor):
                            pedaco.to_excel(writer, nomes[chave][i])
                    else:
                        valor.to_excel(writer, chave)
                         
        #Configuração plots
        df_plots = df[[x, y]]
        df_plots[x] = df_plots[x].map(lambda k: np.mean(k))
        eixo_y = list(df_plots[y])
        yy = []
        tamanho = len(eixo_y[0]) 
        list_x = list(df_plots[x])
        eixo_x = [f'{x:.3f}' for x in list_x]
        eixo_x = [[x]*tamanho for x in eixo_x]
        xx = []
        
        for i in range(len(eixo_x)):
            for j in range(tamanho):
                xx.append(eixo_x[i][j])
                yy.append(eixo_y[i][j])
        
        dados = {x: xx, y: yy}
        dados = pd.DataFrame(dados)
        
        absolute_difference = lambda lista : abs(lista - 1)
        prox_nominal =  f'{min(list_x , key=absolute_difference):.3f}'
        dados_nom = dados[dados[x] == prox_nominal]
        
        plots = {'boxplot': partial(sns.boxplot, x = x, y = y, data = dados),
                 'histograma': partial(sns.histplot, x = x, y = y, data = dados, element = 'poly'),
                 'violino': partial(sns.violinplot, x = x, y = y, data = dados, inner = 'stick'),
                 'histograma_nominal': partial(sns.histplot, x = y, y = x, data = dados_nom, kde = True)}
        
        ax = plots['histograma_nominal']  
        
        #Salvar os plots
        for chave, valor in plots.items():
            if prints[chave]:
                ax = plots[chave]
                plot = ax()
                local = path.join('Plots', f'{chave}.svg')
                plot.figure.savefig(local)

        return dados


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
    
    prints = {'boxplot': True,
              'desvio_padrao': False,
              'histograma': False,
              'histograma_nominal': False,
              'max_min': True,
              'media': True,
              'mediana': False,
              'moda': False,
              'quartis': False,
              'variancia': True,
              'violino': True}

if __name__ == '__main__':
    k = [dfs, dfs, dfs]
    classe = IEEE112MetodoB()
    incertezas = classe.incertezas()
    #print(incertezas)
    dfs = classe.calculo(k, **kwargs)
    dfs2 = FEIMC.saidas(FEIMC, dfs, prints)
