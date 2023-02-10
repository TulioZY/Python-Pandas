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
