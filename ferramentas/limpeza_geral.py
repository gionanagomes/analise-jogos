import pandas as pd # importa a biblioteca pandas

def remover_linhas_vazias(df):
    """
    remove linhas que contêm apenas valores vazios (NaN) de um DataFrame.
    args:
        df (pd.DataFrame): o DataFrame original.
    returns:
        pd.DataFrame: um novo DataFrame sem as linhas vazias.
    """
    # df.dropna() remove linhas com valores NaN (Not a Number/Vazio)
    # how='all' significa que só remove a linha se *todos* os valores forem NaN
    df_limpo = df.dropna(how='all')
    print(f"removidas {len(df) - len(df_limpo)} linhas vazias.")
    return df_limpo # retorna o DataFrame limpo

def converter_para_numerico(df, colunas):
    """
    tenta converter colunas específicas de um DataFrame para tipo numérico.
    valores que não puderem ser convertidos serão transformados em NaN.
    args:
        df (pd.DataFrame): o DataFrame original.
        colunas (list): uma lista de nomes de colunas para converter.
    returns:
        pd.DataFrame: um novo DataFrame com as colunas convertidas.
    """
    df_copia = df.copy() # cria uma cópia do DataFrame para não modificar o original diretamente
    for coluna in colunas:
        if coluna in df_copia.columns: # verifica se a coluna realmente existe no DataFrame
            # pd.to_numeric tenta converter a coluna.
            # errors='coerce' faz com que qualquer valor que não seja número vire NaN (em vez de dar erro).
            df_copia[coluna] = pd.to_numeric(df_copia[coluna], errors='coerce')
            print(f"coluna '{coluna}' convertida para numérico.")
        else:
            print(f"aviso: coluna '{coluna}' não encontrada no DataFrame para conversão.")
    return df_copia # retorna o DataFrame com as colunas numéricas

def padronizar_nomes_colunas(df):
    """
    padroniza os nomes das colunas de um DataFrame: minúsculas, espaços por underline, remove acentos e caracteres especiais.
    args:
        df (pd.DataFrame): o DataFrame original.
    returns:
        pd.DataFrame: um novo DataFrame com os nomes das colunas padronizados.
    """
    df_copia = df.copy()
    novas_colunas = []
    for col in df_copia.columns:
        # converte para minúsculas
        nova_col = str(col).lower()
        # substitui espaços por underscores
        nova_col = nova_col.replace(' ', '_')
        # remove caracteres especiais (simples) - você pode expandir isso se precisar
        nova_col = ''.join(e for e in nova_col if e.isalnum() or e == '_') # mantém apenas alfanuméricos e underscore
        # remove acentos (um pouco mais complexo, mas útil)
        from unicodedata import normalize
        nova_col = normalize('NFKD', nova_col).encode('ascii', 'ignore').decode('utf-8')
        novas_colunas.append(nova_col)
    
    df_copia.columns = novas_colunas
    print("nomes das colunas padronizados.")
    return df_copia