import pandas as pd # Importa a biblioteca pandas

def calcular_lucro_por_cultivo(df, col_venda, col_semente):
    """
    calcula o lucro por cultivo (ou por unidade de produto) e adiciona como nova coluna.
    args:
        df (pd.DataFrame): o DataFrame original.
        col_venda (str): nome da coluna que contém o preço de venda.
        col_semente (str): nome da coluna que contém o preço da semente/custo inicial.
    returns:
        pd.DataFrame: um novo DataFrame com a coluna 'lucro_por_cultivo'.
    """
    df_copia = df.copy()
    # verifica se as colunas necessárias existem
    if col_venda not in df_copia.columns or col_semente not in df_copia.columns:
        print(f"erro: colunas '{col_venda}' ou '{col_semente}' não encontradas para calcular o lucro por cultivo.")
        return df_copia # retorna o DataFrame sem a coluna de lucro
        
    df_copia['lucro_por_cultivo'] = df_copia[col_venda] - df_copia[col_semente]
    print("coluna 'lucro_por_cultivo' calculada.")
    return df_copia

def calcular_lucro_por_dia(df, col_lucro_cultivo, col_tempo_crescimento):
    """
    calcula o lucro médio por dia com base no lucro por cultivo e no tempo de crescimento.
    args:
        df (pd.DataFrame): o DataFrame original.
        col_lucro_cultivo (str): nome da coluna que contém o lucro por cultivo.
        col_tempo_crescimento (str): nome da coluna que contém o tempo de crescimento em dias.
    returns:
        pd.DataFrame: um novo DataFrame com a coluna 'lucro_por_dia'.
    """
    df_copia = df.copy()
    if col_lucro_cultivo not in df_copia.columns or col_tempo_crescimento not in df_copia.columns:
        print(f"erro: colunas '{col_lucro_cultivo}' ou '{col_tempo_crescimento}' não encontradas para calcular o lucro por dia.")
        return df_copia

    # para evitar divisão por zero, substituímos 0 por NaN e depois preenchemos com 0 se for o caso
    # ou podemos simplesmente ignorar a divisão onde o tempo de crescimento é 0 ou nulo
    df_copia['lucro_por_dia'] = df_copia[col_lucro_cultivo] / df_copia[col_tempo_crescimento].replace(0, pd.NA)
    # se uma cultura não tem tempo de crescimento (ex: forrageamento, ou tempo zero), seu lucro_por_dia pode ser considerado igual ao lucro_por_cultivo ou 0
    df_copia['lucro_por_dia'] = df_copia['lucro_por_dia'].fillna(df_copia[col_lucro_cultivo]) # se tempo for 0, usa o lucro do cultivo
    
    print("coluna 'lucro_por_dia' calculada.")
    return df_copia

def calcular_roi(df, col_lucro, col_custo_inicial):
    """
    calcula o Retorno sobre o Investimento (ROI).
    args:
        df (pd.DataFrame): o DataFrame original.
        col_lucro (str): nome da coluna que contém o lucro (total ou por cultivo).
        col_custo_inicial (str): nome da coluna que contém o custo inicial (preço da semente, preço do animal).
    returns:
        pd.DataFrame: um novo DataFrame com a coluna 'ROI'.
    """
    df_copia = df.copy()
    if col_lucro not in df_copia.columns or col_custo_inicial not in df_copia.columns:
        print(f"erro: colunas '{col_lucro}' ou '{col_custo_inicial}' não encontradas para calcular o ROI.")
        return df_copia

    # evita divisão por zero para o custo inicial
    df_copia['ROI'] = df_copia[col_lucro] / df_copia[col_custo_inicial].replace(0, pd.NA)
    # se o custo inicial for 0 (ex: sementes grátis), o ROI pode ser infinito ou um valor alto
    df_copia['ROI'] = df_copia['ROI'].fillna(pd.NA) # representa como NA se a divisão for por zero ou se for infinito

    print("coluna 'ROI' calculada.")
    return df_copia