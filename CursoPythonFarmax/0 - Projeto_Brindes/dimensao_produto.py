
# importar os recursos necessários

# Biblioteca para trabalhar com caminhos de arquivos
from pathlib import Path

# Biblioteca oferece o objeto array de alto desempenho e ferramentas para computação científica e operações numéricas eficientes, especialmente com vetores e matrizes.
import numpy as np

# Biblioteca oferece estruturas de dados flexíveis (como DataFrame e Series) e ferramentas para manipulação, limpeza e análise de dados tabulares.
import pandas as pd

# Biblioteca para a plotagem de graficos
import matplotlib as plt

# Biblioteca para a plotagem de graficos
import seaborn as sb

import calendar as cl

# ====================================================================================
# BLOCO DE ANÁLISE (Executado apenas se o arquivo for rodado diretamente)
# ====================================================================================


def get_dimensao_produto():

    # Retorna o caminho de onde estão os arquivos do projeto
    dataPath = Path(__file__).resolve().parent

    # Carregar os dados - para este proposito vamos definir uma variavel para receber como valor o arquivo de dados
    dfCadprod = pd.read_excel(
        dataPath / 'dCadprod.xlsx')

    # Tratamento dos dados divergentes
    dfCadprod['nivel_1'] = (dfCadprod['nivel_1'].str.replace(
        r'ESPORTE\s+FITNESS', 'ESPORTE E FITNESS', regex=True))

    # Retorna o DataFrame tratado
    return dfCadprod


if __name__ == '__main__':
    df = get_dimensao_produto()

    # Exibir um determinado intervalo dos dados a partir do dataset
    print('Primeiras 10 linhas do dfCadprod')
    print(df.head(10))
    print()
    print("-"*150)

    # Exibir os nomes das colunas
    print('Nome das colunas da dimensao  dfCadprod')
    print('Colunas: ', df.dtypes)
    print()
    print("-"*150)

    # Observação de valores unicos da Coluna nível 1 e coluna nível 2
    print('Valores únicos da coluna nível 1')
    tipo_nivel1 = np.unique(df['nivel_1'])
    print(tipo_nivel1)
    print()
    print("-"*150)

    print('Valores únicos da coluna nível 2')
    tipo_nivel2 = np.unique(df['nivel_2'])
    print(tipo_nivel2)
    print()
    print("-"*150)

    # Observação de valores unicos da Coluna nível 1 e coluna nível 2 após o "Tratamento dos dados divergentes"
    print('Dados divergentes Tratados')
    print("-"*150)

    print('Valores únicos da coluna nível 1')
    tipo_nivel1 = np.unique(df['nivel_1'])
    print(tipo_nivel1)
    print()
    print("-"*150)

    print('Valores únicos da coluna nível 2')
    tipo_nivel2 = np.unique(df['nivel_2'])
    print(tipo_nivel2)
    print()
    print("-"*150)
