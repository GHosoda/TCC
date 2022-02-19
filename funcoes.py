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
#           FUNÇÕES
############################################################
def ensaio_termico(df,**kwargs):    
    #Atualização dos kwargs
    dici = {'material_estator': 'Cobre', 'aba_termico': 'Ensaio_Termico_Vazio'}
    k_estator = {'Cobre': 234.5, 'Alumínio': 225.0}
    dici.update(kwargs)
    k_estator = k_estator[dici['material_estator']]
    dft = deepcopy(df[dici['aba_termico']])
    #cálculo de R1 Inicial e final
    
    dft['D - R1'] = (dft['RS']+dft['RT']+dft['ST'])/(6)
    dft.set_index(['Tipo'], inplace = True)
    
    #Cálculo R1@25ºC
    dft['D - R1@25C'] = dft['D - R1']*(25+k_estator)/(dft['Temperatura'] + k_estator)
    
    #Cálculo T Final
    aux = dft.loc['Final', 'D - R1']*(25+k_estator)/dft.loc['Inicial', 'D - R1@25C'] - k_estator
    dft['E - T Final'] = deepcopy(aux)
    
    #Cálculo dT
    aux = dft.loc['Final', 'E - T Final'] - dft.loc['Final', 'Temperatura']
    dft['E - dT'] = deepcopy(aux)
    
    #Cálculo Ts
    aux = dft.loc['Final', 'E - dT'] + 25
    dft['E - TS'] = deepcopy(aux)
    df[dici['aba_termico']] = deepcopy(dft)
    return df
    
##############################
def ensaio_vazio(df, **kwargs):
    #Inicializando os kwargs
    dici = {'aba_vazio': 'Ensaio_Vazio',
            'fora': [420],
            'pu': 380}
    
    #Variáveis auxiliares
    v2 = []
    pin_pj1 = []
    vcore = []
    
    dfv = deepcopy(df[dici['aba_vazio']])
    
    #Cálculo das resistências
    termico = ensaio_termico(df, aba_termico='Ensaio_Termico_Vazio')
    r1_inicial = termico['Ensaio_Termico_Vazio'].loc['Inicial', 'D - R1']
    r1_final = termico['Ensaio_Termico_Vazio'].loc['Final', 'D - R1']
    r1 = (r1_inicial+r1_final)/2
    
    #Cálculo V^2
    dfv['D - V^2'] = dfv['Tensao']*dfv['Tensao']
    
    #Cálculo FP
    dfv['D - FP'] = dfv['Potencia']/(dfv['Corrente']*dfv['Tensao']*np.sqrt(3))
    
    #Cálculo Pin - Pj1
    dfv['D - Pin - Pj1'] = dfv['Potencia'] - 3*r1*(dfv['Corrente']**2)
    
    #Cálculo VCore
    dfv['D - VCore'] = (dfv['Tensao'] - np.sqrt(3)*r1_inicial*dfv['Corrente']*dfv['D - FP'])**2
    dfv['D - VCore'] += (np.sqrt(3)*dfv['Corrente']*r1_inicial*np.sqrt(1-dfv['D - FP']**2))**2
    dfv['D - VCore'] = np.sqrt(dfv['D - VCore'])
    
    #Definindo Vref como indice
    dfv.set_index('Vref', inplace = True)
    
    v2 = [dfv.loc[vref, 'D - V^2'] for vref in dfv.index if not(vref in dici['fora'])]
    pin_pj1 = [dfv.loc[vref, 'D - Pin - Pj1'] for vref in dfv.index if not(vref in dici['fora'])]
    # vcore = [dfv.loc[vref, 'D - VCore'] for vref in dfv.index if not(vref in dici['fora'])]

    #Cálculo das regressões lineares de V^2 e Pin - Pj1
    v2 = sm.add_constant(v2)
    
    resultado_regressao = sm.OLS(pin_pj1, v2).fit()
    
    #Perdas Atrito e ventilação
    dfv['E - Perdas Atrito Vent.'] = deepcopy(resultado_regressao.params[0])
    
    #Cálculo Perdas Ferro
    dfv['D - Perdas Ferro'] = dfv['D - Pin - Pj1'] - dfv['E - Perdas Atrito Vent.']
    dfv['E - Perdas Ferro Cond Ensaio'] = float(dfv.loc[dici['pu'], 'D - Pin - Pj1'] - dfv.loc[dici['pu'], 'E - Perdas Atrito Vent.'])
    dfv['E - Perdas Ferro Tensao Nominal'] = float(dfv.loc[dici['pu'], 'E - Perdas Ferro Cond Ensaio']*(dici['pu']/dfv.loc[dici['pu'], 'Tensao'])**2)
    
    df[dici['aba_vazio']] = dfv
    return df

##############################
def ensaio_carga(df, **kwargs):
    #Inicializando os kwargs
    dici = {'material_estator': 'Cobre',
            'aba_carga': 'Ensaio_Carga',
            'ta': 25, 'polos': 4}
    k_estator = {'Cobre': 234.5, 'Alumínio': 225.0}
    dici.update(kwargs)
    k_estator = k_estator[dici['material_estator']]
    k_rotor = 225.0
    dfc = deepcopy(df[dici['aba_carga']])
    
    #Cálculo das resistências
    termico = ensaio_termico(df, aba_termico='Ensaio_Termico_Carga')
    dfc['D - T1@Temp OP'] = termico['Ensaio_Termico_Carga'].loc['Inicial', 'D - R1@25C']*(dfc['Temperatura']+ k_estator)/(dici['ta']+k_estator)
    
    #Cálculo do escorregamento
    Ns = dfc['Frequencia']*120/dici['polos']
    dfc['D - Escorregamento'] = (Ns - dfc['RPM'])/Ns
    dfc['D - Escorregamento'] = dfc['D - Escorregamento']*(dfc['Temperatura']+k_rotor)/(dici['ta']+ k_rotor)
    
    #Cálculo da Potência Mecânica
    dfc['D - Potencia Mecanica'] = (2*pi)/60*dfc['Torque']*dfc['RPM']
    
    #Cálculo Pj1
    dfc['D - Pj1'] = 3*dfc['D - T1@Temp OP']*dfc['Corrente']*dfc['Corrente']
    
    #Cálculo Cos(phi)
    dfc['D - Cos(phi)'] = dfc['Potencia']/(dfc['Corrente']*dfc['Tensao']*np.sqrt(3))
    
    #Cálculo de E
    dfc['D - E'] = np.sqrt((dfc['Tensao'] - (np.sqrt(3)/2)*dfc['Corrente']*dfc['D - T1@Temp OP']*dfc['D - Cos(phi)'])**2 + ((np.sqrt(3)/2*dfc['Corrente']*dfc['D - T1@Temp OP'])*np.sqrt(1 - dfc['D - Cos(phi)']**2))**2)
    
    
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
    
    #Perdas no Ferro - Correção E
    dfc['D - Perdas Ferro'] = dfv.loc[dici['pu'], 'E - Perdas Ferro Tensao Nominal']*(dfc['D - E']/dici['pu'])**2
    
    #Atribuição das Perdas de Atrito e Ventilação no Dataframe da 
    dfc['E - Perdas Atrito Vent.'] = float(dfv.loc[dici['pu'], 'E - Perdas Atrito Vent.'])
    
    #Cálculo Pj2
    dfc['D - Pj2'] = dfc['D - Escorregamento']*(dfc['Potencia'] - dfc['D - Pj1'] - dfc['D - Perdas Ferro'])
    
    #Determinação Perdas Suplementares
    dfc['D - Perdas Suplementares'] = dfc['Potencia'] - dfc['D - Pj1'] - dfc['D - Pj2'] - dfc['D - Perdas Ferro'] - dfc['E - Perdas Atrito Vent.'] - dfc['D - Potencia Mecanica']
    print(dfc['D - Perdas Suplementares'])
    T2 = list(dfc['Torque']**2)
    Psup = list(dfc['D - Perdas Suplementares'])
    
    #Configuração regressão linear
    T2 = sm.add_constant(T2)
    resultado_regressao = sm.OLS(Psup, T2).fit()
    dfc['D - Perdas Suplementares'] = resultado_regressao.params[1]
    dfc['D - Perdas Suplementares'] = dfc['D - Perdas Suplementares']*(dfc['Torque']**2)
    
    #Correção perdas joule do estator
    #dfc['D - Pj1'] = 1.5*dfc['Corrente']**2*dfc('D - T1@Temp OP')
    
    #Determinação Rendimento
    dfc['Rendimento'] = (dfc['Potencia'] - dfc['D - Pj1'] - dfc['D - Pj2'] - dfc['D - Perdas Ferro'] - dfc['E - Perdas Atrito Vent.'] - dfc['D - Potencia Mecanica'] - dfc['D - Perdas Suplementares'])/dfc['Potencia']
    
    #Correção do escorregamento
    
    #Correção da velocidade
    dfc['RPM'] = (1 - dfc['D - Escorregamento'])*120*dfc['Frequencia']/dici['polos']
    
    #Correção perdas joule do rotor
    dfc['D - Pj2'] = dfc['D - Escorregamento']*(dfc['Potencia'] - dfc['D - Perdas Ferro'] - dfc['D - Pj1'])
    
    #Correção potência mecânica
    dfc['D - Potencia Mecanica'] = dfc['D - Pj1'] + dfc['D - Pj2'] + dfc['D - Perdas Ferro'] + dfc['E - Perdas Atrito Vent.'] + dfc['D - Perdas Suplementares']
    
    #Correção Rendimento
    dfc['Rendimento'] = (dfc['Potencia'] - dfc['D - Pj1'] - dfc['D - Pj2'] - dfc['D - Perdas Ferro'] - dfc['E - Perdas Atrito Vent.'] - dfc['D - Perdas Suplementares'])/dfc['Potencia']
    
    df[dici['aba_carga']] = dfc
    return df
