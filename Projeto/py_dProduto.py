
# ==========================================================
# IMPORTAÇÃO DOS RECURSOS
# ==========================================================

# Biblioteca para trabalhar com caminhos de arquivos.
from pathlib import Path

# Biblioteca oferece estruturas de dados flexíveis (como DataFrame e Series) e ferramentas para manipulação, limpeza e análise de dados tabulares.
import pandas as pd

# ====================================================================================
# CRIAÇÃO DA FUNÇÃO QUE GERA O DF
# ====================================================================================


def get_dProduto():

    # Retorna o caminho de onde estão os arquivos do projeto
    dataPath = Path(__file__).resolve().parent

    # Carregar os dados
    dfCadprod = pd.read_excel(dataPath / 'Ex_dCadprod.xlsx')

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
