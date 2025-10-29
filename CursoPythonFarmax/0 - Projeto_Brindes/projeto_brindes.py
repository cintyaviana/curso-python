
# importar os recursos necessarios

# Biblioteca
import numpy as np

# Biblioteca
import pandas as pd

# Biblioteca para a plotagem de graficos
import matplotlib as plt

# Biblioteca para a plotagem de graficos
import seaborn as sb

# Biblioteca para trabalhar com caminhos de arquivos
from pathlib import Path

# Retorna o caminho de onde estão os arquivos do projeto
dataPath = Path(__file__).resolve().parent

# Carregar os dados - para este proposito vamos definir uma variavel para receber como valor o arquivo de dados
dfBrindes = pd.read_excel(
    dataPath / 'fBrindes.xlsx')
print()
print('Primeiras 5 linhas do dfBrindes')
print(dfBrindes.head(5))


"""
print()
juncao = pd.merge(df1, df2, how='left', on='A')
# traz todos os dados dados do df1 e somente os dados de df2 compativeis - em commun - do
# elemente a esquerda da junção
print(juncao)
"""
