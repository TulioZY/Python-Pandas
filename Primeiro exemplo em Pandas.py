# Primeiro exemplo de manipulação do Pandas
# Autor: Túlio Correia
# Data: 6 de Fevereiro de 2023

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
# display(combustiveis_df.head(15))

# Comandos shape() e describe()
# print(combustiveis_df.describe())

# Quais são as colunas e que tipo cada um tem
# print(combustiveis_df.info())

# Filtrar apenas por uma coluna
# display(combustiveis_df['Revenda'].head(10))

# Criando dataframe com as colunas que eu quero
ca_df = combustiveis_df[['Revenda', 'Municipio', 'Produto', 'Valor de Venda']]
# display(ca_df)

# Exibe a 4ª linha.
# display(ca_df.loc[3])

# Exibir da 10a. linha até a 20a. linha
# display(ca_df.loc[9:19])

gas_df = ca_df.loc[ca_df['Produto'] == 'GASOLINA']
# display(gas_df)

# display(gas_df['Valor de Venda'].max())
# display(gas_df[['Revenda', 'Municipio', 'Valor de Venda']].max())

# DataFrame.loc[] com múltiplas condições para filtragem
# Quais são so preços do ETANOL na minha cidade
# Ordenado do menor valor de venda para o maior
etanol_indaiatuba_df = ca_df.loc[(ca_df['Produto'] == 'ETANOL') & (ca_df['Municipio'] == 'INDAIATUBA')]
#etanol_indaiatuba_df.sort_values(by='Valor de Venda', inplace=True)
#display(etanol_indaiatuba_df)

# Qual a média de preços dos combustíveis GASOLINA e GASOLINA ADITIVADA do Bairro MOOCA em SÃO PAULO?
#display(combustiveis_df.loc[(combustiveis_df['Bairro'] == 'MOOCA') & 
#                            (combustiveis_df['Municipio'] == 'SAO PAULO') & 
#                            ((combustiveis_df['Produto'] == 'GASOLINA') | (combustiveis_df['Produto'] == 'GASOLINA ADITIVADA')), 
#                            ['Valor de Venda']].mean())


# Como mostrar média de valor de venda POR COMBUSTÍVEL Brasil todo?
#media_por_combustivel_df = ca_df[['Produto', 'Valor de Venda']].groupby(by='Produto').mean().round(2)
#display(media_por_combustivel_df)

# Quero adicionar uma coluna de valor booleano no combustiveis_df 
# Chamada "Ativo" que, por padrão, vai ser True para 
# TODAS as linhas

#combustiveis_df['Ativo'] = True
#print(combustiveis_df.info())
#display(combustiveis_df.head())

# Exportar para Excel o dataframe com etanol em Indaiatuba....
#save_xls([etanol_indaiatuba_df], 'EtanolIndaiatuba.xlsx')