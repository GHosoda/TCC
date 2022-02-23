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
# %%         CLASSE PAI
############################################################
class Ensaio:
    def __init__(self):
        self._colunas = []
        self._tabelas = {}
        self._dfs = {}
        self._incertezas = {}
    
    @property
    def tabelas(self):
        return self._tabelas
    
    @property
    def colunas(self):
        return self._colunas
    
    @property
    def dfs(self):
        return self._dfs
 
    @property
    def incertezas(self):
        return self._incertezas
    
############################################################
# %%          CLASSE IEEE112
############################################################
class IEEE112(Ensaio):
    def __init__(self):
        super().__init__()
        self._tabelas = ['Resistencias', 'Ensaio de Carga', 'Ensaio a Vazio']
        self._colunas = {'Resistencias': ['RS', 'RT', 'ST', 'T_amb', 'T_res'],
                          'Ensaio de Carga': ['Tensao', 'Corrente', 'Potencia', 'Frequencia', 'Temperatura', 'Torque', 'RPM'],
                          'Ensaio a Vazio': ['Tensao', 'Corrente', 'Potencia', 'Frequencia']}  
     
    def drop_ensaios(self, ensaios_manter):
        self._tabelas = ensaios_manter
        self._colunas = {chave:valor for chave, valor in self._colunas.items() if chave in ensaios_manter}

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

    def ensaio_carga(self, df, **kwargs):
        #Configuração KWARGS
        dici = {'Material Estator': 'Cobre',
                'Material Rotor': 'Alumínio',
                'Polos': 4}
        dici.update(kwargs)
        k = {'Cobre': 234.5,
             'Alumínio': 225.0}
        k_estator = k[dici['Material Estator']]
        k_rotor = k[dici['Material Rotor']]
        
        #Inicializando os dfs
        tab_resist = deepcopy(df['Resistencias'])
        tab_carga = deepcopy(df['Ensaio com Carga'])
        
        #Configurando as temperaturas
        tt = tab_carga['Temperatura']
        ts = tab_resist.loc[2, 'Ts']
        
        #Velocidade Sincrona
        tab_carga['Velocidade_Sinc'] = 120*tab_carga['Frequencia']/dici['Polos']
        
        #Escorregamento
        tab_carga['Escorregamento'] = (tab_carga['Velocidade_Sinc'] - tab_carga['Velocidade'])/tab_carga['Velocidade_Sinc']
        fator = (ts+k_rotor)/(tt+k_rotor)
        tab_carga['C-Escorregamento'] = tab_carga['Escorregamento']*fator
        
        #Velocidade Corrigida
        tab_carga['C-Velocidade'] = tab_carga['Velocidade_Sinc']*(1 - tab_carga['C-Escorregamento'])
        
        #Correcao Dinamometro
        tab_carga['C-Dinamometro'] = 0
        
        #Torque Corrigido
        tab_carga['C-Torque'] = tab_carga['Torque'] + tab_carga['C-Dinamometro']
        
        #Potencia saida
        tab_carga['P_out'] = 2*np.pi*tab_carga['C-Torque']*tab_carga['C-Velocidade']/60

        df['Ensaio com Carga'] = tab_carga
        return df
    
    def ensaio_vazio(self, df, **kwargs):
        #Configuração KWARGS
        dici = {'Material Estator': 'Cobre',
                'Material Rotor': 'Alumínio',
                'polos': 4,
                'Tensão Nominal': 380}
        dici.update(kwargs)
        k = {'Cobre': 234.5,
             'Alumínio': 225.0}
        k_estator = k[dici['Material Estator']]
        k_rotor = k[dici['Material Rotor']]
        
        #Inicializando os dfs
        tab_resist = deepcopy(df['Resistencias'])
        tab_vazio = deepcopy(df['Ensaio a Vazio'])
        
        #Cálculo Iniciais
        tab_vazio['V^2'] = tab_vazio['Tensao']**2
        tab_vazio['FP'] = tab_vazio['Potencia']/(np.sqrt(3)*tab_vazio['Corrente']*tab_vazio['Tensao'])        
        r1_medio = float(tab_resist.loc[4, 'R1'] + tab_resist.loc[3,'R1'])/2
        
        #Cálculo Pin - Pj1
        tab_vazio['Pin-Pj1'] = tab_vazio['Potencia'] -3*r1_medio*tab_vazio['Corrente']**2
        
        #Cálculo P_fw - Corrigir escolha das listas
        pin_pj1 = list(tab_vazio['Pin-Pj1'])
        v2 = list(tab_vazio['V^2'])
        v2 = sm.add_constant(v2)
        resultado_regressao = sm.OLS(pin_pj1, v2).fit()
        tab_vazio['P_fw'] = float(resultado_regressao.params[0])
        
        #Cálculo P_ferro
        tab_vazio['P_fe'] = tab_vazio['Pin-Pj1'] - tab_vazio['P_fw']
        
        #Voltando pra variável inicial
        df['Ensaio a Vazio'] = tab_vazio
        return df
  
    def perdas_suplementares(self, p_sup, t2):
        while True:
            t2 = sm.add_constant(t2)
            resultado_regressao = sm.OLS(p_sup, t2).fit()
            coeff_ang = resultado_regressao.params[1]
            rsquared = resultado_regressao.rsquared
            if coeff_ang < 0 or rsquared < .9:
                aux = {}
                for i in range(len(p_sup)):
                    p_sup_aux = list(p_sup)
                    p_sup_aux.pop(i)
                    t2_aux = list(t2)
                    t2_aux.pop(i)
                    t2_aux = sm.add_constant(t2_aux)
                    resultado_regressao = sm.OLS(p_sup_aux, t2_aux).fit()
                    coef_ang = resultado_regressao.params[1]
                    if coef_ang > 0:
                        aux[i] = [resultado_regressao.rsquared]                   
            else:
                return coeff_ang
            return coeff_ang
######################################
# %%    CLASSE IEEE112 - PROPERTIES
###################################### 
    @property
    def tabelas(self):
        return self._tabelas
    
    @property
    def colunas(self):
        return self._colunas
    

############################################################
# %%          CLASSE IEEE 112 MÉTODO A
############################################################
class IEEE112MetodoA(IEEE112):
    def __init__(self):
        super().__init__()
        ensaios_manter = ['Resistencias', 'Ensaio de Carga']
        self.drop_ensaios(ensaios_manter)
        self._incertezas = {'Corrente': ['Corrente'],
                 'Tensao': ['Tensao'],
                 'Potencia': ['Potencia'],
                 'Frequencia': ['Frequencia'],
                 'Resistencia': ['RS', 'RT', 'ST'],
                 'Torque': ['Torque'],
                 'RPM': ['Velocidade'],
                 'Temperatura': ['Temperatura', 'T_amb', 'T_res']}
          
    def incertezas(self):
        dici  = {'Corrente': ['Corrente'],
                 'Tensao': ['Tensao'],
                 'Potencia': ['Potencia'],
                 'Frequencia': ['Frequencia'],
                 'Resistencia': ['RS', 'RT', 'ST'],
                 'Torque': ['Torque'],
                 'RPM': ['Velocidade'],
                 'Temperatura': ['Temperatura', 'T_amb', 'T_res']}
        return dici
    
    def calculo(self, dfs_mc, **kwargs):
        for dfs in dfs_mc:
            dfs = self.ensaio_resistencia(dfs, **kwargs)
            dfs = self.ensaio_carga(dfs, **kwargs)
            dfs = self.rendimento(dfs, **kwargs)
        return dfs
    
    def rendimento(self, dfs, **kwargs):
        #Inicializando os KWARGS
        dici = {'Material Estator': 'Cobre',
                'Potencia Nominal': 1}
        dici.update(kwargs)
        k = {'Cobre': 234.5,
             'Alumínio': 225.0}
        k_estator = k[dici['Material Estator']]
        p_nominal = dici['Potencia Nominal']
        
        #Inicializando os dfs
        tab_resist = deepcopy(dfs['Resistencias'])
        tab_carga = deepcopy(dfs['Ensaio com Carga'])
        
        #Variáveis
        tf = tab_resist.loc[0,'T_amb']
        ts = tab_resist.loc[1, 'Ts']
        R1 = tab_resist.loc[0, 'R1']
        
        #Cálculo Pj1 -> Tt
        tab_carga['Pj1 - Tt'] = 1.5*tab_carga['Corrente']**2*R1*(k_estator+tab_carga['Temperatura'])/(k_estator+tf)
        
        #Calculo Pj1 -> Ts
        tab_carga['Pj1 - Ts'] = 1.5*tab_carga['Corrente']**2*R1*(k_estator+ts)/(k_estator+tf)
        dfs['Ensaio com Carga'] = tab_carga
        #Correção Pj1
        tab_carga['C-Pj1'] = tab_carga['Pj1 - Ts'] - tab_carga['Pj1 - Tt']
        
        #Correção Pin
        tab_carga['C-Pin'] = tab_carga['Potencia'] + tab_carga['C-Pj1']
        
        #Cálculo rendimento
        tab_carga['Rendimento'] = tab_carga['P_out']/tab_carga['C-Pin']
        
        #Criação novo Df com o resultado
        resultado = tab_carga[['Potencia', 'C-Escorregamento', 'C-Pj1', 'C-Pin', 'P_out', 'Rendimento']]
        resultado['Potencia'] = resultado['Potencia']/p_nominal
        dfs['Resultado'] = resultado
        return dfs
    

############################################################
# %%          CLASSE IEEE 112 MÉTODO B
############################################################
class IEEE112MetodoB(IEEE112):
    def __init__(self):
        super().__init__()
        ensaios_manter = ['Resistencias', 'Ensaio de Carga', 'Ensaio a Vazio']
        self.drop_ensaios(ensaios_manter)
        
    def incertezas(self):
        dici  = {'Corrente': ['Corrente'],
                 'Tensao': ['Tensao'],
                 'Potencia': ['Potencia'],
                 'Frequencia': ['Frequencia'],
                 'Resistencia': ['RS', 'RT', 'ST'],
                 'Torque': ['Torque'],
                 'RPM': ['Velocidade'],
                 'Temperatura': ['Temperatura', 'T_amb', 'T_res']}
        return dici

    def calculo(self, dfs_mc, **kwargs):
        for dfs in dfs_mc:
            dfs = self.ensaio_resistencia(dfs, **kwargs)
            dfs = self.ensaio_carga(dfs, **kwargs)
            dfs = self.ensaio_vazio(dfs, **kwargs)
            dfs = self.rendimento(dfs, **kwargs)
        return dfs_mc

    def rendimento(self, dfs, **kwargs):
        #Inicializando os KWARGS
        dici = {'Material Estator': 'Cobre',
                'Potencia Nominal': 1,
                'Tensao Nominal': 380}
        dici.update(kwargs)
        k = {'Cobre': 234.5,
             'Alumínio': 225.0}
        k_estator = k[dici['Material Estator']]
        p_nominal = dici['Potencia Nominal']
        t_nominal = dici['Tensao Nominal']
        
        #Inicializando os dfs
        tab_resist = deepcopy(dfs['Resistencias'])
        tab_carga = deepcopy(dfs['Ensaio com Carga'])
        tab_vazio = deepcopy(dfs['Ensaio a Vazio'])
        
        #Variáveis
        t_nom_index = 1#Método para quebrar um galho
        
        #Atribuição das perdas de atrito e ventilação para o dataframe do ensaio de carga
        tab_carga['P_fw'] = float(tab_vazio.loc[0, 'P_fw'])
        
        #Perda no ferro Condicoes de ensaio
        p_fe_ensaio = tab_vazio.loc[t_nom_index, 'P_fe']*(t_nominal/tab_vazio.loc[t_nom_index, 'Tensao'])**2
        tab_carga['P_fe'] = p_fe_ensaio*(tab_carga['Tensao']/t_nominal)**2
        
        #Pj1
        tt = tab_carga['Temperatura']
        tTR = tab_resist.loc[2, 'Ts']
        tTTD = tab_resist.loc[2, 'T_res']
        tA = tTR*tt/tTTD
        R1 = tab_resist.loc[2, 'R1']*(k_estator+tA)/(k_estator+tTR)
        tab_carga['Pj1'] = 1.5*tab_carga['Corrente']**2*R1
        
        #Pj2
        tab_carga['Pj2'] = (tab_carga['Potencia'] - tab_carga['P_fe'] - tab_carga['Pj1'])*tab_carga['Escorregamento']
        
        #Perdas totais converncionais
        tab_carga['P_total_conv'] = tab_carga['Pj1']+tab_carga['Pj2']+tab_carga['P_fe']+tab_carga['P_fw']
        
        #Correção Pout
        tab_carga['C-P_out'] = 2*np.pi*tab_carga['C-Torque']*tab_carga['Velocidade']/60
        
        #Perdas totais
        tab_carga['P_total'] = tab_carga['Potencia'] - tab_carga['C-P_out']
        
        #Perdas suplementares
        tab_carga['P_sup'] = tab_carga['P_total'] - tab_carga['P_total_conv']
        
        #Correção perdas suplementares
        p_sup = list(tab_carga['P_sup'])
        t2 = list(tab_carga['C-Torque']**2)
        coeff = self.perdas_suplementares(p_sup, t2)
        tab_carga['C-P_sup'] = coeff*tab_carga['C-Torque']**2
        
        #Correção Pj1
        ts = tab_resist.loc[1, 'Ts']
        t_res = tab_resist.loc[1, 'T_res']
        tab_carga['C-Pj1'] = 1.5*tab_carga['Corrente']**2*tab_resist.loc[1, 'R1']*(k_estator+ts)/(k_estator+t_res)
        
        #Correção Pj2
        tab_carga['C-Pj2'] = tab_carga['C-Escorregamento']*(tab_carga['Potencia'] - tab_carga['C-Pj1']- tab_carga['P_fe'])
        
        #Perdas totais corrigidas
        tab_carga['C-P_tot'] = tab_carga['C-Pj1']+tab_carga['C-Pj2']+tab_carga['C-P_sup']+tab_carga['P_fe']+tab_carga['P_fw']
        
        #Potencia saida corrigida
        tab_carga['C-P_out'] = tab_carga['Potencia'] - tab_carga['C-P_tot']
        
        #Rendimento
        tab_carga['Rendimento'] = tab_carga['C-P_out']/tab_carga['Potencia']
        
        #Criando novo df com os resultados
        tab_carga['Potencia [pu]'] = tab_carga['Potencia']/p_nominal
        resultado = tab_carga[['Potencia [pu]', 'C-Escorregamento', 'P_out', 'Pj1', 'Pj2', 'P_sup', 'P_fw', 'P_fe', 'C-Pj1', 'C-Pj2', 'C-P_sup', 'C-P_out', 'Rendimento']]
        dfs['Resultado'] = resultado
        
        return dfs

'''
def IEEE112_Metodo_B(df, **kwargs):
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
'''

if __name__ == '__main__':
    a = IEEE112MetodoA()
    print(a.incertezas)
    
# %%
