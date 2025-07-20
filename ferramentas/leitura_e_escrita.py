import pandas as pd 
import os

def ler_dados_brutos(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None

    try:
        if caminho_arquivo.endswith('.csv'):
            df = pd.read_csv(caminho_arquivo)
            print(f"arquivo CSV '{caminho_arquivo}' lido com sucesso.")
        elif caminho_arquivo.endswith('.xlsx'):
            df = pd.read_excel(caminho_arquivo)
            print(f"arquivo Excel '{caminho_arquivo}' lido com sucesso.")
        else:
            print(f"erro: formato de arquivo não suportado para leitura: '{caminho_arquivo}'. use .csv ou .xlsx.")
            return None
        
        return df 
    
    except pd.errors.EmptyDataError:
        print(f"erro: o arquivo '{caminho_arquivo}' está vazio.")
        return None
    except Exception as e:
        print(f"erro ao ler o arquivo '{caminho_arquivo}': {e}")
        return None

def salvar_dados_processados(df, caminho_arquivo):
    diretorio = os.path.dirname(caminho_arquivo)
    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio) 

    try:
        if caminho_arquivo.endswith('.csv'):
            df.to_csv(caminho_arquivo, index=False)
            print(f"DataFrame salvo como CSV em '{caminho_arquivo}' com sucesso.")
        elif caminho_arquivo.endswith('.xlsx'):
            df.to_excel(caminho_arquivo, index=False)
            print(f"DataFrame salvo como Excel em '{caminho_arquivo}' com sucesso.")
        else:
            print(f"erro: formato de arquivo não suportado para escrita: '{caminho_arquivo}'. use .csv ou .xlsx.")
    except Exception as e:
        print(f"erro ao salvar o arquivo '{caminho_arquivo}': {e}")