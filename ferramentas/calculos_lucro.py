import pandas as pd

def calcular_lucro_pesca(df, colunas_venda):
    df_copy = df.copy()

    for col_venda in colunas_venda:
        df_copy[col_venda] = pd.to_numeric(df_copy[col_venda], errors='coerce').fillna(0)

        suffix = col_venda.replace('preço venda ', '').replace('preço ', '').replace(' ', '_').capitalize()
        if suffix == 'normal':
            suffix = 'normal'
        elif suffix == 'prata':
            suffix = 'prata'
        elif suffix == 'ouro':
            suffix = 'ouro'
        elif suffix == 'irídio':
            suffix = 'iridio'

        df_copy[f'lucro_por_peixe_{suffix}'] = df_copy[col_venda]

    return df_copy