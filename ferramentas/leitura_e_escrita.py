import pandas as pd # importa a biblioteca pandas, essencial para trabalhar com DataFrames
import os # importa a biblioteca os, usada para interagir com o sistema operacional (ex: verificar se um arquivo existe)

def ler_dados_brutos(caminho_arquivo):
    """
    lê um arquivo de dados brutos (CSV ou XLSX) e retorna um DataFrame do Pandas.
    args:
        caminho_arquivo (str): O caminho completo para o arquivo (ex: 'dados_brutos/minhas_culturas.xlsx').
    returns:
        pd.DataFrame: um DataFrame contendo os dados do arquivo. retorna None se houver erro.
    """
    # verifica se o arquivo existe no caminho especificado
    if not os.path.exists(caminho_arquivo):
        # se o arquivo não for encontrado, imprime uma mensagem de erro e retorna None
        print(f"erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None

    # tenta ler o arquivo
    try:
        # verifica a extensão do arquivo para saber como lê-lo
        if caminho_arquivo.endswith('.csv'):
            # se for CSV, usa read_csv do pandas
            df = pd.read_csv(caminho_arquivo)
            print(f"arquivo CSV '{caminho_arquivo}' lido com sucesso.")
        elif caminho_arquivo.endswith('.xlsx'):
            # se for XLSX (Excel), usa read_excel do pandas
            df = pd.read_excel(caminho_arquivo)
            print(f"arquivo Excel '{caminho_arquivo}' lido com sucesso.")
        else:
            # se a extensão não for suportada, imprime um erro
            print(f"erro: formato de arquivo não suportado para leitura: '{caminho_arquivo}'. use .csv ou .xlsx.")
            return None
        
        return df # retorna o DataFrame lido
    
    # captura possíveis erros durante a leitura do arquivo
    except pd.errors.EmptyDataError:
        # erro se o arquivo CSV estiver vazio
        print(f"erro: o arquivo '{caminho_arquivo}' está vazio.")
        return None
    except Exception as e:
        # captura qualquer outro erro inesperado na leitura
        print(f"erro ao ler o arquivo '{caminho_arquivo}': {e}")
        return None

def salvar_dados_processados(df, caminho_arquivo):
    """
    salva um DataFrame processado em um arquivo (CSV ou XLSX).
    args:
        df (pd.DataFrame): o DataFrame a ser salvo.
        caminho_arquivo (str): o caminho completo para o arquivo de saída.
    """
    # garante que o diretório de destino existe. ex: se for 'dados_processados/arquivo.xlsx',
    # ele cria a pasta 'dados_processados' se ela não existir.
    diretorio = os.path.dirname(caminho_arquivo)
    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio) # cria a pasta

    # tenta salvar o DataFrame
    try:
        if caminho_arquivo.endswith('.csv'):
            # salva como CSV, sem o índice (index=False) para não criar uma coluna numérica extra no CSV
            df.to_csv(caminho_arquivo, index=False)
            print(f"DataFrame salvo como CSV em '{caminho_arquivo}' com sucesso.")
        elif caminho_arquivo.endswith('.xlsx'):
            # salva como XLSX, também sem o índice
            df.to_excel(caminho_arquivo, index=False)
            print(f"DataFrame salvo como Excel em '{caminho_arquivo}' com sucesso.")
        else:
            print(f"erro: formato de arquivo não suportado para escrita: '{caminho_arquivo}'. use .csv ou .xlsx.")
    except Exception as e:
        print(f"erro ao salvar o arquivo '{caminho_arquivo}': {e}")