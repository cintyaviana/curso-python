# IMPORTAR AS BIBLIOTECAS NECESSÁRIAS
import pandas as pd
import numpy as np
import os  # Necessário para a solução de caminho

# 1 - PASSO: CARREGAR OS DADOS
NOME_DO_ARQUIVO = 'vendas.xlsx'
df = None

# Tenta obter o diretório do script atual.
# ATENÇÃO: Se rodar em um console interativo ou notebook, isso pode FALHAR!
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo
CAMINHO_COMPLETO = os.path.join(DIRETORIO_ATUAL, NOME_DO_ARQUIVO)

# Carrega o DataFrame usando o caminho absoluto.
# O script FALHARÁ se o arquivo não for encontrado.
df = pd.read_excel(CAMINHO_COMPLETO)

# Exibe o resumo
print('Primeiras 5 linhas do df:')
print(df.head(5))

print('\n=========================RESUMO ESTATISTICO===========================')
print(df.describe())
