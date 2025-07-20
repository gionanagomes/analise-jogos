import pandas as pd 

def remover_linhas_vazias(df):
    df_limpo = df.dropna(how='all')
    print(f"removidas {len(df) - len(df_limpo)} linhas vazias.")
    return df_limpo 

def converter_para_numerico(df, colunas):
    df_copia = df.copy() 
    for coluna in colunas:
        if coluna in df_copia.columns:
            df_copia[coluna] = pd.to_numeric(df_copia[coluna], errors='coerce')
            print(f"coluna '{coluna}' convertida para numérico.")
        else:
            print(f"aviso: coluna '{coluna}' não encontrada no DataFrame para conversão.")
    return df_copia 

def padronizar_nomes_colunas(df):
    df_copia = df.copy()
    novas_colunas = []
    for col in df_copia.columns:
        nova_col = str(col).lower()
        nova_col = nova_col.replace(' ', '_')
        nova_col = ''.join(e for e in nova_col if e.isalnum() or e == '_') 
        from unicodedata import normalize
        nova_col = normalize('NFKD', nova_col).encode('ascii', 'ignore').decode('utf-8')
        novas_colunas.append(nova_col)
    
    df_copia.columns = novas_colunas
    print("nomes das colunas padronizados.")
    return df_copia