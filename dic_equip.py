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
from copy import deepcopy
import pandas as pd
import numpy as np
from math import pi


############################################################
#           FUNÇÕES
############################################################
def melhor_escala(valor, escalas):
    '''
    Define a melhor escala com base no valor de entrada

    Parameters
    ----------
    valor : Medida realizada
    escalas : lista com todas as escalas do equipamento para determinada grandeza

    Returns
    -------
    melhor_escala : Retorna a melhor escala disponível do equipamento
    '''
    escalas = escalas.sort()
    try:
        melhor_escala = escalas[0]
    except TypeError:
        return 0
        
    for escala in escalas:
        if valor < escala:
            return melhor_escala
        else:
            melhor_escala = escala
    return melhor_escala

##############################
def distribuicoes(valor, retangulares:list, normais:list, incertezas:dict, bool_incertezas:dict, pontos:int):
    ret = 1.4
    parcial = np.ones(pontos+1)*valor
    
    for retangular in retangulares:
        # if bool_incertezas[retangular]:
        parcial += np.random.uniform(-incertezas[retangular]*ret, incertezas[retangular]*ret, pontos+1)
    
    for normal in normais:
        # if bool_incertezas[normal]:
        parcial += np.random.normal(valor, incertezas[normal], pontos+1)
    
    parcial[pontos] = valor
    return parcial

##############################
class Equipamentos:
    def __init__(self, series, equipamento, pontos, escala_auto, **kwargs):
        self._series = series
        self._equipamento = equipamento
        self._pontos = pontos
        self._escala_auto = escala_auto
        
    def tensao(self, **kwargs):
        pass


def equipamentos(linha: dict, equipamentos:dict, bool_incertezas:dict, pontos = 1000):
    dicionario_funcoes = {
        'Corrente': equipamentos_corrente,
        'Tensao': equipamentos_tensao,
        'Potencia': equipamentos_potencia,
        'Frequencia': equipamentos_frequencia,
        'Resistencia': equipamentos_resistencia,
        'Temperatura': equipamentos_temperatura,
        'Torque': equipamentos_torque,
        'RPM': equipamentos_rpm}
    
    dici_parc = deepcopy(linha)
    
    for grandeza, funcao in dicionario_funcoes.items():
        if grandeza in linha.keys():    
            dici_parc.update({grandeza: funcao(linha[grandeza], equipamentos[grandeza], bool_incertezas, pontos, **linha)})
    series = pd.Series(dici_parc, dtype = object)    
    
    for chave, valor in linha.items():
        if not(chave in dicionario_funcoes.keys()):
            series[chave] = [series[chave] for i in range(pontos+1)]
    return series  

##############################


##############################
def equipamentos_tensao(valor: float, equipamento: str, bool_incertezas:dict, pontos: int, **kwargs):        
    #Inicialização valores
    retangulares = []
    normais = []
    incertezas = {}
    
    #Inicialização dos Kwargs
    dicionario = {'Temperatura': 25}
    dicionario.update(kwargs)
    
    #Cálculo da temperatura
    if dicionario['Temperatura'] < 28 and dicionario['Temperatura'] >18:
        dicionario['Temperatura'] = 0
    else:
        dicionario['Temperatura'] = abs(dicionario['Temperatura'] - 23) - 5
    
    ###############
    #WT500
    if equipamento == 'WT500':
        retangulares = ['Incerteza Leitura', 'Incerteza Escala', 'Incerteza Temperatura', 'Incerteza Resolução']
        normais = []
        escalas = [15, 30, 60, 100, 150, 300, 600, 1000]
        consts = {
            'Incerteza Leitura': 0.001,
            'Incerteza Escala': 0.001,
            'Incerteza Temperatura': 0.0003,
            'Incerteza Resolução': 0
            }
        
        escala = melhor_escala(valor, escalas)
        incertezas = {
            'Incerteza Leitura': consts['Incerteza Leitura']*valor,
            'Incerteza Escala': consts['Incerteza Escala']*escala,
            'Incerteza Temperatura': consts['Incerteza Temperatura']*dicionario['Temperatura'],
            'Incerteza Resolução': 0
            }
        
    return distribuicoes(valor, retangulares, normais, incertezas, bool_incertezas, pontos)

##############################
def equipamentos_corrente(valor: float, equipamento: str, bool_incertezas:dict, pontos: int, **kwargs):
    #Inicialização valores
    retangulares = []
    normais = []
    incertezas = {}
    
    #Inicialização dos Kwargs
    dicionario = {'Temperatura': 25}
    dicionario.update(kwargs)
    
    #Cálculo da temperatura
    if dicionario['Temperatura'] < 28 and dicionario['Temperatura'] >18:
        dicionario['Temperatura'] = 0
    else:
        dicionario['Temperatura'] = abs(dicionario['Temperatura'] - 23) - 5
    
    #WT500
    if equipamento == 'WT500':
        retangulares = ['Incerteza Leitura', 'Incerteza Escala', 'Incerteza Temperatura', 'Incerteza Resolução', 'Incerteza Posição Sensor', 'Incerteza Precisão do Sensor', 'Incerteza TC']
        normais = []
        escalas = [.5, 1, 2, 5, 10, 20, 40]
        consts = {
            'Incerteza Leitura': 0.001,
            'Incerteza Escala': 0.001,
            'Incerteza Temperatura': 0.0003,
            'Incerteza Resolução': 0,
            'Incerteza Posição Sensor': 0.005,
            'Incerteza Precisão do Sensor': [0.005, .1/10],
            'Incerteza TC': 0.007
            }
    
        escala = melhor_escala(valor, escalas)
        incertezas = {
            'Incerteza Leitura': consts['Incerteza Leitura']*valor,
            'Incerteza Escala': consts['Incerteza Escala']*escala,
            'Incerteza Temperatura': consts['Incerteza Temperatura']*dicionario['Temperatura'],
            'Incerteza Resolução': consts['Incerteza Resolução'],
            'Incerteza Posição Sensor': consts['Incerteza Posição Sensor']*valor,
            'Incerteza Precisão do Sensor': consts['Incerteza Precisão do Sensor'][1] + consts['Incerteza Precisão do Sensor'][0]*valor,
            'Incerteza TC': consts['Incerteza TC']*valor}
        
    return distribuicoes(valor, retangulares, normais, incertezas, bool_incertezas, pontos)

##############################
def equipamentos_potencia(valor: float, equipamento: str, bool_incertezas:dict, pontos: int, **kwargs):
    #Inicialização valores
    retangulares = []
    normais = []
    incertezas = {}
    
    #Inicialização dos Kwargs
    dicionario = {'Temperatura': 25, 'Corrente': 0, 'Tensao': 0}
    dicionario.update(kwargs)
    
    #Cálculo da temperatura
    if dicionario['Temperatura'] < 28 and dicionario['Temperatura'] >18:
        dicionario['Temperatura'] = 0
    else:
        dicionario['Temperatura'] = abs(dicionario['Temperatura'] - 23) - 5
    
    #WT500
    if equipamento == 'WT500':
        retangulares = ['Incerteza Leitura', 'Incerteza Escala', 'Incerteza Temperatura','Incerteza Resolução', 'Incerteza FP']
        normais = []
        escalas = []
        consts = {
            'Incerteza Leitura': 0.001,
            'Incerteza Escala': 0.001,
            'Incerteza Temperatura': 0.0003,
            'Incerteza Resolução': 0,
            'Incerteza FP': 0.002
            }
        
        #Cálculo valor do ângulo phi
        phi = valor/(dicionario['Corrente']*dicionario['Tensao']*(3**0.5))
        
        escala = melhor_escala(valor, escalas)
        incertezas = {
            'Incerteza Leitura': consts['Incerteza Leitura']*valor,
            'Incerteza Escala': consts['Incerteza Escala']*escala*np.cos(phi),
            'Incerteza Temperatura': consts['Incerteza Temperatura']*dicionario['Temperatura'],
            'Incerteza Resolução': consts['Incerteza Resolução'],
            'Incerteza FP': consts['Incerteza FP']*valor*np.tan(phi)
            }
    
    return distribuicoes(valor, retangulares, normais, incertezas, bool_incertezas, pontos)

##############################
def equipamentos_frequencia(valor: float, equipamento: str, bool_incertezas:dict, pontos: int, **kwargs):
    #Inicialização valores
    retangulares = []
    normais = []
    incertezas = {}
    
    #Inicialização dos Kwargs
    dicionario = {'Temperatura': 25}
    dicionario.update(kwargs)
    
    #Cálculo da temperatura
    if dicionario['Temperatura'] < 28 and dicionario['Temperatura'] >18:
        dicionario['Temperatura'] = 0
    else:
        dicionario['Temperatura'] = abs(dicionario['Temperatura'] - 23) - 5
    
    #WT500
    if equipamento == 'WT500':
        
        consts = {
            'Incerteza Leitura': 0.006
            }
        
    return distribuicoes(valor, retangulares, normais, incertezas, bool_incertezas, pontos)

##############################
def equipamentos_resistencia(valor: float, equipamento: str, bool_incertezas:dict, pontos: int, **kwargs):
    #Inicialização valores
    retangulares = []
    normais = []
    incertezas = {}
    
    #Inicialização dos Kwargs
    dicionario = {'Temperatura': 25}
    dicionario.update(kwargs)
    
    #Cálculo da temperatura
    if dicionario['Temperatura'] < 28 and dicionario['Temperatura'] >18:
        dicionario['Temperatura'] = 0
    else:
        dicionario['Temperatura'] = abs(dicionario['Temperatura'] - 23) - 5
    
    if equipamento == 'Agilent34410A':
        retangulares = []
        normais = []
        escalas = []
        E34410A = [10**(j+2) for j in range(8)]
        consts = {
            'Incerteza Leitura': dict(zip(E34410A, [0.01, 0.01, 0.01, 0.01, 0.012, 0.04, 0.8, 8.0])),
            'Incerteza Escala': dict(zip(E34410A, [0.004, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001])),
            'Incerteza Temperatura': dict(zip(E34410A, zip([0.0006, 0.0006, 0.0006, 0.0006, 0.001, 0.003, 0.1, 1.0], [0.0005, 0.0001, 0.0001, 0.0001, 0.0002, 0.0004, 0.0001, 0.0001])))
            }
        
        escala = melhor_escala(valor, escalas)
        incertezas = {
            'Incerteza Leitura':valor*consts['Incerteza Leitura'][escala],
            'Incerteza Escala':escala*consts['Incerteza Escala'][escala],
            'Incerteza Temperatura':valor*consts['Incerteza Temperatura'][escala][0] + escala*consts['Incerteza Temperatura'][escala][1]
            }
    
    return distribuicoes(valor, retangulares, normais, incertezas, bool_incertezas, pontos)

##############################
def equipamentos_temperatura(valor: float, equipamento: str, bool_incertezas:dict, pontos: int, **kwargs):
    #Inicialização valores
    retangulares = []
    normais = []
    incertezas = {}
    
    #Inicialização dos Kwargs
    dicionario = {'Temperatura': 25}
    dicionario.update(kwargs)
    
    #Cálculo da temperatura
    if dicionario['Temperatura'] < 28 and dicionario['Temperatura'] >18:
        dicionario['Temperatura'] = 0
    else:
        dicionario['Temperatura'] = abs(dicionario['Temperatura'] - 23) - 5
    
    if equipamento == 'YokogawaGP10':
        retangulares = []
        normais = []
        escalas = []
        consts = {}
        
        escala = melhor_escala(valor, escalas)
        pass
    return distribuicoes(valor, retangulares, normais, incertezas, bool_incertezas, pontos)

##############################
def equipamentos_torque(valor: float, equipamento: str, bool_incertezas:dict, pontos: int, **kwargs):
    #Inicialização valores
    retangulares = []
    normais = []
    incertezas = {}
    
    #Inicialização dos Kwargs
    dicionario = {'Temperatura': 25, 'Tpp': 0, 'Frequencia_Torque': 120, 'Periodo': 1}
    dicionario.update(kwargs)
    
    #Cálculo da temperatura
    if dicionario['Temperatura'] < 28 and dicionario['Temperatura'] >18:
        dicionario['Temperatura'] = 0
    else:
        dicionario['Temperatura'] = abs(dicionario['Temperatura'] - 23) - 5
    
    #HBM TB40
    if equipamento == 'HBMTB40':
        retangulares = ['Incerteza não Linearidade e Histerese',
                        'Incerteza Efeito da Temperatura',
                        'Incerteza Efeito da Temperatura sobre o zero',
                        'Incerteza Tolerância da Sensibilidade',
                        'Incerteza Resolução Limitada',
                        'Incerteza Long Term Drift Over 48h',
                        'Incerteza Tolerância da Frequência',
                        'Incerteza Desvio Integração Numérica']
        
        normais = ['Incerteza Repetibilidade']
        escalas = []
        consts = {
            'Incerteza não Linearidade e Histerese': 0.0001,
            'Incerteza Repetibilidade': 0.0003,
            'Incerteza Efeito da Temperatura': 0.0005/10,
            'Incerteza Efeito da Temperatura sobre o zero': 0.0005,
            'Incerteza Tolerância da Sensibilidade': 0.001,
            'Incerteza Resolução Limitada': 0.016,
            'Incerteza Long Term Drift Over 48h': 0.0003,
            'Incerteza Tolerância da Frequência': 0.0001,
            'Incerteza Desvio Integração Numérica': 0.0
            }
        
        escala = melhor_escala(valor, escalas)
        try:
            perc = valor/escala
        except ZeroDivisionError:
            perc = 1
        fator = 1
        if perc <.6:
            if perc >.2:
                fator = 2
        else:
            fator = 3
        incertezas = {
            'Incerteza não Linearidade e Histerese': valor*fator*consts['Incerteza não Linearidade e Histerese'],
            'Incerteza Repetibilidade': valor*consts['Incerteza Repetibilidade'],
            'Incerteza Efeito da Temperatura': dicionario['Temperatura']*valor*consts['Incerteza Efeito da Temperatura'],
            'Incerteza Efeito da Temperatura sobre o zero': dicionario['Temperatura']*valor*consts['Incerteza Efeito da Temperatura sobre o zero'],
            'Incerteza Tolerância da Sensibilidade': valor*consts['Incerteza Tolerância da Sensibilidade'],
            'Incerteza Resolução Limitada': consts['Incerteza Resolução Limitada'],
            'Incerteza Long Term Drift Over 48h': valor*consts['Incerteza Long Term Drift Over 48h'],
            'Incerteza Tolerância da Frequência': valor*consts['Incerteza Tolerância da Frequência'],
            'Incerteza Desvio Integração Numérica': dicionario['Tpp']/(dicionario['Periodo']*2*pi*dicionario['Frequencia_Torque'])
            }
    
    return distribuicoes(valor, retangulares, normais, incertezas, bool_incertezas, pontos)

##############################
def equipamentos_rpm(valor: float, equipamento: str, bool_incertezas:dict, pontos: int, **kwargs):
    #Inicialização valores
    retangulares = []
    normais = []
    incertezas = {}
    
    #Inicialização dos Kwargs
    dicionario = {'Temperatura': 25, 'Npp': 0, 'Polos': 4}
    dicionario.update(kwargs)
    
    #Cálculo da temperatura
    if dicionario['Temperatura'] < 28 and dicionario['Temperatura'] >18:
        dicionario['Temperatura'] = 0
    else:
        dicionario['Temperatura'] = abs(dicionario['Temperatura'] - 23) - 5
        
    #HBMTB40
    if equipamento == 'HBMTB40':
        retangulares = ['Incerteza Máxima Variação de polos', 'Incerteza Tolerância de Pulso', 'Incerteza Resolução da Medição de Frequência', 'Incerteza Desvio por Integração Numérica']
        normais = []
        escalas = []
        consts = {
            'Incerteza Máxima Variação de polos': 50*pi/(180*60*3600),
            'Incerteza Tolerância de Pulso':  0.05*pi*1024/(20000*180*60),
            'Incerteza Resolução da Medição de Frequência': 0.01*2*pi,
            'Incerteza Desvio por Integração Numérica': 0.0
            }
        
        escala = melhor_escala(valor, escalas)
        incertezas = {
            'Incerteza Máxima Variação de polos': consts['Incerteza Máxima Variação de polos']*valor*dicionario['Polos'],
            'Incerteza Tolerância de Pulso':  valor*consts['Incerteza Tolerância de Pulso'],
            'Incerteza Resolução da Medição de Frequência': consts['Incerteza Resolução da Medição de Frequência'],
            'Incerteza Desvio por Integração Numérica': consts['Incerteza Desvio por Integração Numérica']*dicionario['Npp']/0.9/(2*pi*valor/60)*pi/30
            }
        
    
    return distribuicoes(valor, retangulares, normais, incertezas, bool_incertezas, pontos)
##############################
