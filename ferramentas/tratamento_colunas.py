import pandas as pd
import numpy as np

def extrair_hora_inicio(texto_horario):
    if pd.isna(texto_horario):
        return np.nan
        
    texto_horario = str(texto_horario).strip().lower()

    if '-' in texto_horario:
        try:
            return float(texto_horario.split('-')[0].split(':')[0])
        except (ValueError, IndexError):
            return np.nan
    elif texto_horario == 'qualquer hora':
        return np.nan
    else:
        return np.nan

def converter_hora_para_periodo(hora_numerica):
    if pd.isna(hora_numerica):
        return 'qualquer hora'
    elif 6 <= hora_numerica < 12:
        return 'manhã'
    elif 12 <= hora_numerica < 18:
        return 'tarde'
    else:
        return 'noite'

def processar_localizacao(df):
    df_copia = df.copy()

    df_copia['localizacao_individual'] = df_copia['localizacao'].str.split(',').str[0].str.strip().str.lower()
    
    df_copia['localizacao_individual'] = df_copia['localizacao_individual'].str.replace('floresta', 'lago_floresta')
    df_copia['localizacao_individual'] = df_copia['localizacao_individual'].str.replace('montanha', 'lago_montanha')
    
    return df_copia