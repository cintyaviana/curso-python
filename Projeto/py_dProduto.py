
# ==========================================================
# IMPORTAÇÃO DOS RECURSOS
# ==========================================================

# Biblioteca para trabalhar com caminhos de arquivos. Permite manipulação de caminhos de forma orientada a objetos.
from pathlib import Path

# Biblioteca oferece o objeto array de alto desempenho e ferramentas para computação científica e operações numéricas eficientes, especialmente com vetores e matrizes.
import numpy as np

# Biblioteca oferece estruturas de dados flexíveis (como DataFrame e Series) e ferramentas para manipulação, limpeza e análise de dados tabulares.
import pandas as pd

# ====================================================================================
# CRIAÇÃO DA FUNÇÃO QUE GERA O DF
# ====================================================================================


def get_dProduto():

    # Retorna o caminho de onde estão os arquivos do projeto
    dataPath = Path(__file__).resolve().parent

    # Carregar os dados - para este propósito vamos definir uma variavel para receber como valor o arquivo de dados
    dfCadprod = pd.read_excel(
        dataPath / 'Ex_dCadprod.xlsx')

    # Tratamento dos dados divergentes
    dfCadprod['nivel_1'] = (dfCadprod['nivel_1'].str.replace(
        r'ESPORTE\s+FITNESS', 'ESPORTE E FITNESS', regex=True))

    """
    .str: É um acessor do Pandas que permite aplicar funções de manipulação de string (texto) a todos os valores (células) da coluna nivel_1.

    .replace(...): É a função que faz a substituição do texto. Ela procura um padrão e o troca por uma nova string.
    
    regex=True: Este argumento é obrigatório para dizer ao Pandas que o primeiro argumento é uma expressão regular, e não apenas uma string literal simples.
        Comportamento: O padrão de busca ganha poder, pois pode usar metacaracteres (símbolos especiais) para representar classes de caracteres, repetições, ou posições.

        Sua Aplicação Específica:
            Padrão: r'ESPORTE\s+FITNESS'

            Metacaractere Usado:
            \s: Representa qualquer espaço em branco (espaço, tab, nova linha).
            +: Representa uma ou mais ocorrências do que o precede (\s).

            Resultado: O Pandas não procura a string literal \s+. Em vez disso, ele usa a lógica da regex para encontrar ESPORTE seguido por qualquer quantidade de espaços antes de FITNESS.   
    """

    # Retorna o DataFrame tratado
    return dfCadprod

# ====================================================================================
# BLOCO DE ANÁLISE: Executado apenas se o arquivo for rodado diretamente
# ====================================================================================


if __name__ == '__main__':
    # Carrega o DataFrame através da função
    dfCadprod = get_dProduto()

    # Exibir um determinado intervalo dos dados a partir do dataset
    print('='*120)
    print('🔗 Primeiras 5 linhas do dfCadprod')
    print('='*120)
    print(dfCadprod.head(5))
    print("\n")

    print('='*120)
    print('🔗 Últimas 5 linhas do dfCadprod')
    print('='*120 + "\n")
    print(dfCadprod.tail(5))
    print("\n")

    # Exibir os nomes das colunas através do dtypes
    print('='*120)
    print('🔗 Nome das colunas da dimensao  dfCadprod')
    print('='*120 + "\n")
    print('Colunas: ', dfCadprod.dtypes)
    print("\n")

    # Observação de valores unicos da Coluna nível 1 e coluna nível 2 atraves do np.unique
    print('='*120)
    print('🔗 Valores únicos da coluna nível 1')
    print('='*120 + "\n")
    tipo_nivel1 = np.unique(dfCadprod['nivel_1'])
    print(tipo_nivel1)
    print("\n")

    print('='*120)
    print('🔗 Valores únicos da coluna nível 2')
    print('='*120 + "\n")
    tipo_nivel2 = np.unique(dfCadprod['nivel_2'])
    print(tipo_nivel2)
    print("\n")
