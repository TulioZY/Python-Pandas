# Primeiro exemplo de manipulação do Pandas
# Autor: Túlio Correia
# Data: 6 de Fevereiro de 2023


# Função para exportar em .xlsx
import os
    
def save_xls(list_dfs, xls_path):
    with pd.ExcelWriter(xls_path) as writer:
        for n, df in enumerate(list_dfs):
            df.to_excel(writer,'sheet%s' % n)
        writer.save()

# Importando biblioteca Pandas no Python
import pandas as pd
from IPython.display import display
from openpyxl import Workbook

combustiveis_df = pd.read_excel(r"C:\Users\tulio\Documents\ArquivosGIt\PythonPandas\ca-2021-02.xlsx")

# Mostra o DataFrame na tela
display(combustiveis_df.head(15))

# Comandos shape() e describe()
print(combustiveis_df.describe())

# Quais são as colunas e que tipo cada um tem
print(combustiveis_df.info())

# Filtrar apenas por uma coluna
display(combustiveis_df['Revenda'].head(10))

# Criando dataframe com as colunas que eu quero
ca_df = combustiveis_df[['Revenda', 'Municipio', 'Produto', 'Valor de Venda']]
display(ca_df)

# Exibe a 4ª linha.
display(ca_df.loc[3])

# Exibir da 10a. linha até a 20a. linha
display(ca_df.loc[9:19])