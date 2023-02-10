""" 
Segundo exemplo de manipulação de dados usando Python Pandas 
Veremos inserção de dados, remoção de colunas, merge e gráficos.

Autor: Túlio Correia Rocha

Data: 9 e 10 de fevereiro de 2023
"""
# Importando biblioteca pandas no Python
import pandas as pd
from IPython.display import display
from openpyxl import Workbook

combustiveis_df = pd.read_excel(r"C:\Users\tulio\Documents\ArquivosGIt\PythonPandas\ca-2021-02.xlsx")
display(combustiveis_df.head())

#Inserção simples de dado
combustiveis_df['Ativo'] = True

display(combustiveis_df.head())

# Criar uma coluna "Obs" que tenha nela escrito "MELHOR CIDADE" quando a coluna Municipio for igual a SAO PAULO
combustiveis_df['Obs'] = ["MELHOR CIDADE" if municipio == 'SAO PAULO' else None for municipio in combustiveis_df['Municipio']]
display(combustiveis_df.loc[combustiveis_df['Municipio'].isin(['SAO PAULO','INDAIATUBA', 'CAMPINAS', 'SALTO']), ['Municipio', 'Obs']])

# (por Leandro Rodrigues)
# como preencher uma coluna 'Valor de Venda - Status' que verifica o seguinte:
# se o valor de venda for maior que 6,5 reais, ele fala que tá Caro..caso contrário, está barato
import numpy as np

combustiveis_df['Status do Valor de Venda'] = np.where(combustiveis_df['Valor de Venda'] > 6.5, 'Caro', 'Barato')
display(combustiveis_df[['Revenda', 'Valor de Venda', 'Status do Valor de Venda']])

# Calcular postos de gasolina por habitante temos na amostragem de 
# combustiveis nov/2021
num_habitantes_df = pd.read_csv(r"C:\Users\tulio\Documents\ArquivosGIt\PythonPandas\ibge_num_habitantes_estimado.csv", sep=";")
display(num_habitantes_df)

num_habitantes_df.rename(columns={"Estado":"Estado - Sigla"}, inplace=True)
display(num_habitantes_df)

# Faz um MERGE dos dois dataframes
colunas = ['Municipio', 'Estado - Sigla']
merge_df = combustiveis_df.merge(num_habitantes_df, how="inner", on=colunas)
display(merge_df)
print(merge_df.info())

# Destruir coluna completamente vazia (todas as linhas são nulas)
merge_df.dropna(axis='columns', inplace=True)
print(merge_df.info())

colunas=['Regiao - Sigla', 'Nome da Rua', 'Numero Rua', 
         'Bairro', 'Cep', 'Produto', 'Data da Coleta', 'Valor de Venda',
         'Unidade de Medida', 'Bandeira', 'Ativo', 'Status do Valor de Venda']
merge_df.drop(labels=colunas, axis=1, inplace=True)
print(merge_df.info())

# Remover a linhas duplicadas
merge_df.drop_duplicates(inplace=True)
display(merge_df.head(100))

#Agrupar e contar quantos postos tem na cidade..
postos_por_municipio_df = merge_df.groupby(by=['Estado - Sigla', 'Municipio', 'NumHabitantes2021']).count()
postos_por_municipio_df.drop('CNPJ da Revenda', axis=1, inplace=True)
postos_por_municipio_df.rename(columns={"Revenda": "Número de Postos"}, inplace=True)
display(postos_por_municipio_df)

# Agrupar e contar quantos postos tem na cidade..
postos_por_municipio_df = merge_df.groupby(by=['Estado - Sigla', 'Municipio', 'NumHabitantes2021']).count()
postos_por_municipio_df.reset_index(inplace=True)
#display(postos_por_municipio_df.info())
postos_por_municipio_df.drop('CNPJ da Revenda', axis=1, inplace=True)
postos_por_municipio_df.rename(columns={"Revenda": "NumPostos"}, inplace=True)

postos_por_municipio_df['PostosPorHabitante'] = postos_por_municipio_df['NumPostos'] / postos_por_municipio_df['NumHabitantes2021']
display(postos_por_municipio_df.info())
display(postos_por_municipio_df)