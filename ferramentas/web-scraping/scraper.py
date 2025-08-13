import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL da página
url = "https://dinkum.fandom.com/wiki/Fish"

# Faz a requisição HTTP
response = requests.get(url)
response.raise_for_status()

# Analisa o conteúdo HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra as tabelas com a classe 'wikitable'
tables = soup.find_all('table', {'class': 'fandom-table'})

# Lista para armazenar os DataFrames
dfs = []

# Itera por todas as tabelas encontradas
for i, table in enumerate(tables):
    headers = []
    rows = []

    for th in table.find_all('th'):
        headers.append(th.text.strip())

    for tr in table.find_all('tr')[1:]:
        cells = tr.find_all(['td', 'th'])
        row = [cell.get_text(strip=True) for cell in cells]
        if row:
            rows.append(row)

    # Cria o DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Converte todos os dados para string e minúsculo
    df = df.applymap(lambda x: str(x).lower())

    dfs.append(df)

# Salva no Excel com uma aba para cada tabela
caminho = os.path.join("ferramentas", "web-scraping", "dinkum-pesca.xlsx")
with pd.ExcelWriter(caminho, engine='openpyxl') as writer:
    for idx, df in enumerate(dfs):
        sheet_name = f'Tabela_{idx+1}'
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Tabelas salvas!")
