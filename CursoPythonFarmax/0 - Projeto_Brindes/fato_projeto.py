# projeto_brindes.py


# Importa as funções de carregamento dos seus módulos
from fato_brindes import get_fato_brindes
from dimensao_produto import get_dimensao_produto
from fato_impostos import get_fato_impostos
import pandas as pd
import numpy as np
import calendar as cl

# ===============================
# 1. CARREGAR E PREPARAR OS DATAFRAMES
# ===============================

print("Iniciando o Projeto Brindes: Carregando Fato e Dimensões...")
dfBrindes = get_fato_brindes()
dfCadprod = get_dimensao_produto()
dfImpostos = get_fato_impostos()
print("Bases de dados carregadas com sucesso.")

# =======================================================
# 1.1. INICIALIZAÇÃO DE VARIÁVEIS PARA ANÁLISE MENSAL
# (Essa inicialização precisa ser antes do bloco 'if __name__ == "__main__":')
# =======================================================

# A variável 'meses' é inicializada no início do seu código, fora do if __name__ == '__main__':,
# para garantir que esteja no escopo de todo o módulo, mas para os loops ela será
# inicializada dentro do if __name__ == '__main__': (onde ela estava antes).
# Vamos manter a inicialização que estava no código anterior, fora do if:
meses = sorted(dfBrindes['mes'].dropna().unique())


# --------------------------------------------------------------------------
# PASSO 1: SELECIONAR APENAS AS COLUNAS NECESSÁRIAS DA DIMENSÃO (dfCadprod)
# --------------------------------------------------------------------------
COLUNAS_DIMENSAO = ['cod_produto', 'nivel_1', 'nivel_2']
dfCadprod_reduzido = dfCadprod[COLUNAS_DIMENSAO].copy()

# ... (Seu código de merge 1 e 2 permanece o mesmo) ...

# ===============================
# 2. PRIMEIRO MERGE (Fato Brindes + Dimensão Produto)
# ===============================

print("\nExecutando 1º LEFT MERGE (Brindes + Produto).")

df_analise = pd.merge(
    left=dfBrindes,
    right=dfCadprod_reduzido,
    left_on='cod_sku',
    right_on='cod_produto',
    how='left'
)

# Remoção da coluna redundante 'cod_produto'
df_analise.drop(columns=['cod_produto'], inplace=True)

# --------------------------------------------------------------------------
# PASSO 2: PREPARAR dfImpostos PARA O SEGUNDO MERGE
# --------------------------------------------------------------------------
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
dfImpostos_reduzido = dfImpostos[COLUNAS_IMPOSTOS].drop_duplicates(
    subset=['nota_fiscal', 'cod_sku'])

# ===============================
# 3. SEGUNDO MERGE (df_analise + Fato Impostos)
# ===============================

print("Executando 2º LEFT MERGE (Análise + Impostos) nas chaves: 'nota_fiscal' e 'cod_sku'.")

df_analise_final = pd.merge(
    left=df_analise,
    right=dfImpostos_reduzido,
    on=['nota_fiscal', 'cod_sku'],
    how='left'
)
# Atualiza o nome da variável principal para uso nas análises subsequentes
df_analise_final_projeto = df_analise_final

# ================================================================================================================================
# INÍCIO DAS ANÁLISES (TUDO ABAIXO ESTÁ DENTRO DO BLOCO IF)
# ================================================================================================================================

if __name__ == '__main__':

   # Exibir um determinado intervalo dos dados a partir do dataset
    print('Primeiras 10 linhas do df_analise_final_projeto')
    print(df_analise_final_projeto.head(10))
    print("\n" + "-"*150)

    # Exibir os nomes das colunas
    print('Nome das colunas da fato df_analise_final_projeto')
    print('Colunas: ', df_analise_final_projeto.dtypes)
    print("\n" + "-"*150)

    # Exibir o resumo estatístico
    print('Resumo estatístico da fato df_analise_final_projeto')
    print(df_analise_final_projeto.describe())
    print('-'*150)
    print()

    COLUNAS_IMPOSTOS_VISUALIZACAO = [
        'data', 'nota_fiscal', 'cod_sku', 'custo_total', 'impostos_total']

    # CORREÇÃO: Usar df_analise_final_projeto que contém a coluna 'impostos_total'
    print('Primeiras 10 linhas das colunas de Nota Fiscal, SKU e Imposto Total')
    print('-'*150)
    print(df_analise_final_projeto[COLUNAS_IMPOSTOS_VISUALIZACAO].head(10))
    print("\n" + '-'*150)

    meses = sorted(df_analise_final_projeto['mes'].dropna().unique())
