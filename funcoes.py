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
import pandas as pd
import numpy as np
from copy import deepcopy
import statsmodels.api as sm
from math import pi


############################################################
# %%          CLASSE PAI
############################################################
class Ensaio:
    def __init__(self):
        self.__colunas = []
        self.__tabelas = {}
        self.__dfs = {}
    
    @property
    def tabelas(self):
        return self.__tabelas
    
    @property
    def colunas(self):
        return self.__colunas
    
    @property
    def dfs(self):
        return self.__dfs
 
    
############################################################
# %%          CLASSE IEEE112
############################################################
class IEEE112(Ensaio):
    def __init__(self):
        super().__init__()
        self.__tabelas = ['Resistencias', 'Ensaio de Carga', 'Ensaio a Vazio']
        self.__colunas = {'Resistencias': ['RS', 'RT', 'ST', 'T_amb', 'T_res'],
                          'Ensaio de Carga': ['Tensao', 'Corrente', 'Potencia', 'Frequencia', 'Temperatura', 'Torque', 'RPM'],
                          'Ensaio a Vazio': ['Tensao', 'Corrente', 'Potencia', 'Frequencia']}
    
    def drop_ensaios(self, ensaios_manter):
        self.__tabelas = ensaios_manter
        self.__colunas = {chave:valor for chave, valor in self.__colunas.items() if chave in ensaios_manter}
            
    def ensaio_resistencia(self, df, **kwargs):
        #Configuração KWARGS
        dici = {'Material Estator': 'Cobre'}
        dici.update(kwargs)
        k = {'Cobre': 234.5,
             'Alumínio': 225.0}
        k_estator = k[dici['Material Estator']]
        
        #Início cálculos
        tab_resist = deepcopy(df['Resistencias'])
        tab_resist['dT'] = deepcopy('T_res')
        tab_resist['dT'] = tab_resist['T_res'] - tab_resist['T_res'].shift(1)
        tab_resist.at[0,'dT'] =  0
        tab_resist['Ts'] = tab_resist['dT'] + 25
        tab_resist['R1'] = (tab_resist['RS']+tab_resist['RT']+tab_resist['ST'])/6
        tab_resist['R1@25'] = tab_resist['R1']*(25+k_estator)/(tab_resist['T_res']+k_estator)
        #Inserir cálculo do T Final??
        df['Resistencias'] = tab_resist
        return df
    
    def ensaio_carga(self, df, *kwargs):
        #Configuração KWARGS
        dici = {'Material Estator': 'Cobre',
                'Material Rotor': 'Alumínio',
                'polos': 4}
        dici.update(kwargs)
        k = {'Cobre': 234.5,
             'Alumínio': 225.0}
        k_estator = k[dici['Material Estator']]
        k_rotor = k[dici['Material Rotor']]
        
        #Inicializando os dfs
        tab_resist = deepcopy(df['Resistencias'])
        tab_carga = deepcopy(df['Ensaio com Carga'])

    def ensaio_vazio(self, df, **kwargs):
        #Configuração KWARGS
        dici = {'Material Estator': 'Cobre',
                'Material Rotor': 'Alumínio',
                'polos': 4,
                'Tensão (V)': 380}
        dici.update(kwargs)
        k = {'Cobre': 234.5,
             'Alumínio': 225.0}
        k_estator = k[dici['Material Estator']]
        k_rotor = k[dici['Material Rotor']]
        
        #Inicializando os dfs
        tab_resist = deepcopy(df['Resistencias'])
        tab_carga = deepcopy(df['Ensaio a Vazio'])
        pass
    
############################################################
# %%          CLASSE IEEE 112 MÉTODO A
############################################################
class IEEE112MetodoA(IEEE112):
    def __init__(self):
        super().__init__()
        ensaios_manter = ['Resistências', 'Ensaio de Carga']
        self.drop_ensaios(ensaios_manter)
        print(self.__tabelas)
        print(self.__colunas)
          
    def incertezas(self, dfs, dicionario_incertezas):
        pass
    
    def calculo(self, dfs):
        pass


############################################################
# %%          CLASSE IEEE 112 MÉTODO B
############################################################
class IEEE112MetodoB(IEEE112):
    def __init__(self):
        self.__tabelas = ['Resistencias', 'Ensaio de Carga', 'Ensaio a Vazio']
        self.__colunas = {'Resistencias': ['RS', 'RT', 'ST', 'T_amb', 'T_res'],
                          'Ensaio de Carga': ['Tensao', 'Corrente', 'Potencia', 'Frequencia', 'Temperatura', 'Torque', 'RPM'],
                          'Ensaio a Vazio': ['Tensao', 'Corrente', 'Potencia', 'Frequencia']}
    
    def incertezas(self, dfs, dicionario_incertezas):
        pass

    def calculo(self, dfs):
        pass

############################################################
# %%          CÓDIGO ANTIGO
############################################################

def ensaio_termico(df, **kwargs):
    # Atualização dos kwargs
    dici = {'material_estator': 'Cobre', 'aba_termico': 'Ensaio_Termico_Vazio'}
    k_estator = {'Cobre': 234.5, 'Alumínio': 225.0}
    dici.update(kwargs)
    k_estator = k_estator[dici['material_estator']]
    dft = deepcopy(df[dici['aba_termico']])
    # cálculo de R1 Inicial e final

    dft['D - R1'] = (dft['RS']+dft['RT']+dft['ST'])/(6)
    dft.set_index(['Tipo'], inplace=True)

    # Cálculo R1@25ºC
    dft['D - R1@25C'] = dft['D - R1'] * \
        (25+k_estator)/(dft['Temperatura'] + k_estator)

    # Cálculo T Final
    aux = dft.loc['Final', 'D - R1'] * \
        (25+k_estator)/dft.loc['Inicial', 'D - R1@25C'] - k_estator
    dft['E - T Final'] = deepcopy(aux)

    # Cálculo dT
    aux = dft.loc['Final', 'E - T Final'] - dft.loc['Final', 'Temperatura']
    dft['E - dT'] = deepcopy(aux)

    # Cálculo Ts
    aux = dft.loc['Final', 'E - dT'] + 25
    dft['E - TS'] = deepcopy(aux)
    df[dici['aba_termico']] = deepcopy(dft)
    return df

##############################


def ensaio_vazio(df, **kwargs):
    # Inicializando os kwargs
    dici = {'aba_vazio': 'Ensaio_Vazio',
            'fora': [420],
            'pu': 380}

    # Variáveis auxiliares
    v2 = []
    pin_pj1 = []
    vcore = []

    dfv = deepcopy(df[dici['aba_vazio']])

    # Cálculo das resistências
    termico = ensaio_termico(df, aba_termico='Ensaio_Termico_Vazio')
    r1_inicial = termico['Ensaio_Termico_Vazio'].loc['Inicial', 'D - R1']
    r1_final = termico['Ensaio_Termico_Vazio'].loc['Final', 'D - R1']
    r1 = (r1_inicial+r1_final)/2

    # Cálculo V^2
    dfv['D - V^2'] = dfv['Tensao']*dfv['Tensao']

    # Cálculo FP
    dfv['D - FP'] = dfv['Potencia']/(dfv['Corrente']*dfv['Tensao']*np.sqrt(3))

    # Cálculo Pin - Pj1
    dfv['D - Pin - Pj1'] = dfv['Potencia'] - 3*r1*(dfv['Corrente']**2)

    # Cálculo VCore
    dfv['D - VCore'] = (dfv['Tensao'] - np.sqrt(3) *
                        r1_inicial*dfv['Corrente']*dfv['D - FP'])**2
    dfv['D - VCore'] += (np.sqrt(3)*dfv['Corrente'] *
                         r1_inicial*np.sqrt(1-dfv['D - FP']**2))**2
    dfv['D - VCore'] = np.sqrt(dfv['D - VCore'])

    # Definindo Vref como indice
    dfv.set_index('Vref', inplace=True)

    v2 = [dfv.loc[vref, 'D - V^2']
          for vref in dfv.index if not(vref in dici['fora'])]
    pin_pj1 = [dfv.loc[vref, 'D - Pin - Pj1']
               for vref in dfv.index if not(vref in dici['fora'])]
    # vcore = [dfv.loc[vref, 'D - VCore'] for vref in dfv.index if not(vref in dici['fora'])]

    # Cálculo das regressões lineares de V^2 e Pin - Pj1
    v2 = sm.add_constant(v2)

    resultado_regressao = sm.OLS(pin_pj1, v2).fit()

    # Perdas Atrito e ventilação
    dfv['E - Perdas Atrito Vent.'] = deepcopy(resultado_regressao.params[0])

    # Cálculo Perdas Ferro
    dfv['D - Perdas Ferro'] = dfv['D - Pin - Pj1'] - \
        dfv['E - Perdas Atrito Vent.']
    dfv['E - Perdas Ferro Cond Ensaio'] = float(
        dfv.loc[dici['pu'], 'D - Pin - Pj1'] - dfv.loc[dici['pu'], 'E - Perdas Atrito Vent.'])
    dfv['E - Perdas Ferro Tensao Nominal'] = float(
        dfv.loc[dici['pu'], 'E - Perdas Ferro Cond Ensaio']*(dici['pu']/dfv.loc[dici['pu'], 'Tensao'])**2)

    df[dici['aba_vazio']] = dfv
    return df

##############################


def ensaio_carga(df, **kwargs):
    # Inicializando os kwargs
    dici = {'material_estator': 'Cobre',
            'aba_carga': 'Ensaio_Carga',
            'ta': 25, 'polos': 4}
    k_estator = {'Cobre': 234.5, 'Alumínio': 225.0}
    dici.update(kwargs)
    k_estator = k_estator[dici['material_estator']]
    k_rotor = 225.0
    dfc = deepcopy(df[dici['aba_carga']])

    # Cálculo das resistências
    termico = ensaio_termico(df, aba_termico='Ensaio_Termico_Carga')
    dfc['D - T1@Temp OP'] = termico['Ensaio_Termico_Carga'].loc['Inicial',
                                                                'D - R1@25C']*(dfc['Temperatura'] + k_estator)/(dici['ta']+k_estator)

    # Cálculo do escorregamento
    Ns = dfc['Frequencia']*120/dici['polos']
    dfc['D - Escorregamento'] = (Ns - dfc['RPM'])/Ns
    dfc['D - Escorregamento'] = dfc['D - Escorregamento'] * \
        (dfc['Temperatura']+k_rotor)/(dici['ta'] + k_rotor)

    # Cálculo da Potência Mecânica
    dfc['D - Potencia Mecanica'] = (2*pi)/60*dfc['Torque']*dfc['RPM']

    # Cálculo Pj1
    dfc['D - Pj1'] = 3*dfc['D - T1@Temp OP']*dfc['Corrente']*dfc['Corrente']

    # Cálculo Cos(phi)
    dfc['D - Cos(phi)'] = dfc['Potencia'] / \
        (dfc['Corrente']*dfc['Tensao']*np.sqrt(3))

    # Cálculo de E
    dfc['D - E'] = np.sqrt((dfc['Tensao'] - (np.sqrt(3)/2)*dfc['Corrente']*dfc['D - T1@Temp OP']*dfc['D - Cos(phi)'])
                           ** 2 + ((np.sqrt(3)/2*dfc['Corrente']*dfc['D - T1@Temp OP'])*np.sqrt(1 - dfc['D - Cos(phi)']**2))**2)

    df[dici['aba_carga']] = dfc
    return df


def IEEE112_Metodo_A(df, **kwargs):
    pass


def IEEE112_Metodo_B(df, **kwargs):
    df = ensaio_vazio(df, **kwargs)
    df = ensaio_carga(df, **kwargs)

    dici = {'material_estator': 'Cobre',
            'aba_carga': 'Ensaio_Carga',
            'aba_vazio': 'Ensaio_Vazio',
            'ta': 25, 'polos': 4,
            'fora': [420],
            'pu': 380
            }
    k_estator = {'Cobre': 234.5, 'Alumínio': 225.0}
    dici.update(kwargs)
    k_estator = k_estator[dici['material_estator']]
    k_rotor = 225.0

    dfc = deepcopy(df[dici['aba_carga']])
    dfv = deepcopy(df[dici['aba_vazio']])

    # Perdas no Ferro - Correção E
    dfc['D - Perdas Ferro'] = dfv.loc[dici['pu'],
                                      'E - Perdas Ferro Tensao Nominal']*(dfc['D - E']/dici['pu'])**2

    # Atribuição das Perdas de Atrito e Ventilação no Dataframe da
    dfc['E - Perdas Atrito Vent.'] = float(
        dfv.loc[dici['pu'], 'E - Perdas Atrito Vent.'])

    # Cálculo Pj2
    dfc['D - Pj2'] = dfc['D - Escorregamento'] * \
        (dfc['Potencia'] - dfc['D - Pj1'] - dfc['D - Perdas Ferro'])

    # Determinação Perdas Suplementares
    dfc['D - Perdas Suplementares'] = dfc['Potencia'] - dfc['D - Pj1'] - dfc['D - Pj2'] - \
        dfc['D - Perdas Ferro'] - dfc['E - Perdas Atrito Vent.'] - \
        dfc['D - Potencia Mecanica']
    print(dfc['D - Perdas Suplementares'])
    T2 = list(dfc['Torque']**2)
    Psup = list(dfc['D - Perdas Suplementares'])

    # Configuração regressão linear
    T2 = sm.add_constant(T2)
    resultado_regressao = sm.OLS(Psup, T2).fit()
    dfc['D - Perdas Suplementares'] = resultado_regressao.params[1]
    dfc['D - Perdas Suplementares'] = dfc['D - Perdas Suplementares'] * \
        (dfc['Torque']**2)

    # Correção perdas joule do estator
    #dfc['D - Pj1'] = 1.5*dfc['Corrente']**2*dfc('D - T1@Temp OP')

    # Determinação Rendimento
    dfc['Rendimento'] = (dfc['Potencia'] - dfc['D - Pj1'] - dfc['D - Pj2'] - dfc['D - Perdas Ferro'] -
                         dfc['E - Perdas Atrito Vent.'] - dfc['D - Potencia Mecanica'] - dfc['D - Perdas Suplementares'])/dfc['Potencia']

    # Correção do escorregamento

    # Correção da velocidade
    dfc['RPM'] = (1 - dfc['D - Escorregamento']) * \
        120*dfc['Frequencia']/dici['polos']

    # Correção perdas joule do rotor
    dfc['D - Pj2'] = dfc['D - Escorregamento'] * \
        (dfc['Potencia'] - dfc['D - Perdas Ferro'] - dfc['D - Pj1'])

    # Correção potência mecânica
    dfc['D - Potencia Mecanica'] = dfc['D - Pj1'] + dfc['D - Pj2'] + \
        dfc['D - Perdas Ferro'] + dfc['E - Perdas Atrito Vent.'] + \
        dfc['D - Perdas Suplementares']

    # Correção Rendimento
    dfc['Rendimento'] = (dfc['Potencia'] - dfc['D - Pj1'] - dfc['D - Pj2'] - dfc['D - Perdas Ferro'] -
                         dfc['E - Perdas Atrito Vent.'] - dfc['D - Perdas Suplementares'])/dfc['Potencia']

    df[dici['aba_carga']] = dfc
    return df


