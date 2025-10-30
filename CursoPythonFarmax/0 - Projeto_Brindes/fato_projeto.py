# ==========================================================
# IMPORTAÇÃO DOS RECURSOS
# ==========================================================

from fato_brindes import get_fato_brindes
from dimensao_produto import get_dimensao_produto
from fato_impostos import get_fato_impostos
import pandas as pd
import numpy as np
import calendar as cl

# ==========================================================
# CARREGAR E PREPARAR OS DATAFRAMES
# ==========================================================

print("Iniciando o Projeto Brindes: Carregando Fato e Dimensões...")
dfBrindes = get_fato_brindes()
dfCadprod = get_dimensao_produto()
dfImpostos = get_fato_impostos()
print("Bases de dados carregadas com sucesso.")

# A variável 'meses' é inicializada
meses = sorted(dfBrindes['mes'].dropna().unique())

# ==========================================================
# PRIMEIRO MERGE (Fato Brindes + Dimensão Produto)
# ==========================================================

COLUNAS_DIMENSAO = ['cod_produto', 'nivel_1', 'nivel_2']
dfCadprod = dfCadprod[COLUNAS_DIMENSAO].copy()

print("\nExecutando 1º LEFT MERGE (Brindes + Produto).")

df1 = pd.merge(
    left=dfBrindes,
    right=dfCadprod,
    left_on='cod_sku',
    right_on='cod_produto',
    how='left'
)

# Remoção da coluna redundante 'cod_produto'
df1.drop(columns=['cod_produto'], inplace=True)

# ==========================================================
# SEGUNDO MERGE (df1 + Fato Impostos)
# ==========================================================

# Renomear a coluna de SKU em dfImpostos para 'cod_sku' (para manter o padrão)
dfImpostos.rename(columns={'codigo_sku': 'cod_sku'}, inplace=True)

# Selecionar apenas as colunas de impostos que você precisa, mais as chaves.
COLUNAS_IMPOSTOS = [
    'nota_fiscal',
    'cod_sku',
    'aliq_icms',
    'aliq_pis',
    'aliq_cofins',
    'impostos_total'
]
dfImpostos = dfImpostos[COLUNAS_IMPOSTOS].drop_duplicates(
    subset=['nota_fiscal', 'cod_sku'])

print("Executando 2º LEFT MERGE (df1 + Impostos) nas chaves: 'nota_fiscal' e 'cod_sku'.")

df_analise = pd.merge(
    left=df1,
    right=dfImpostos,
    on=['nota_fiscal', 'cod_sku'],
    how='left'
)
# Atualiza o nome da variável principal para uso nas análises subsequentes
df_analise_final = df_analise

# ================================================================================================================================
# INÍCIO DAS ANÁLISES
# ================================================================================================================================

if __name__ == '__main__':

   # Exibir um determinado intervalo dos dados a partir do dataset
    print('Primeiras 10 linhas do df_analise_final_projeto')
    print(df_analise_final.head(10))
    print("\n" + "-"*150)

    # Exibir os nomes das colunas
    print('Nome das colunas da fato df_analise_final_projeto')
    print('Colunas: ', df_analise_final.dtypes)
    print("\n" + "-"*150)

    # Exibir o resumo estatístico
    print('Resumo estatístico da fato df_analise_final_projeto')
    print(df_analise_final.describe())
    print('-'*150)
    print()

    COLUNAS_IMPOSTOS_VISUALIZACAO = [
        'data', 'nota_fiscal', 'cod_sku', 'custo_total', 'impostos_total']

    # CORREÇÃO: Usar df_analise_final_projeto que contém a coluna 'impostos_total'
    print('Primeiras 10 linhas das colunas de Nota Fiscal, SKU e Imposto Total')
    print('-'*150)
    print(df_analise_final[COLUNAS_IMPOSTOS_VISUALIZACAO].head(10))
    print("\n" + '-'*150)

    meses = sorted(df_analise_final['mes'].dropna().unique())
