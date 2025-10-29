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


def get_fato_impostos():

    # Retorna o caminho de onde estão os arquivos do projeto

    dataPath = Path(__file__).resolve().parent

    # Carregar os dados - para este propósito vamos definir uma variavel para receber como valor o arquivo de dados

    dfImpostos = pd.read_excel(

        dataPath / 'fImpostos.xlsx')

    dfImpostos['impostos_total'] = (

        dfImpostos['valor_icms'] +

        dfImpostos['valor_icms_st'] +

        dfImpostos['valor_fcp_st'] +

        dfImpostos['icms_interestadual_uf_destino'] +

        dfImpostos['valor_icms_fcp_uf_destino'] +

        dfImpostos['valor_pis'] +

        dfImpostos['valor_cofins']

    )

    # Converte para o Período Mensal (M) e depois de volta para Timestamp,

    # garantindo que o dia seja sempre '01'.

    dfImpostos['data'] = dfImpostos['data'].dt.to_period('M').dt.to_timestamp()

    # Criar uma coluna com o número do mês

    dfImpostos['mes'] = dfImpostos['data'].dt.month

    # Agrupamos pela Nota Fiscal para somar todos os impostos relacionados a ela.

    dfImpostos_consolidado = (

        dfImpostos

        .groupby(['nota_fiscal', 'cod_sku', 'data'])

        .agg(

            impostos_total=('impostos_total', 'sum'),

            # Se você precisar de outros campos da nota (ex: total de itens), adicione aqui

            # Ex: total_itens=('cod_sku', 'nunique')

        )

        .reset_index()  # Transforma os índices 'nota_fiscal', 'data', 'mes' em colunas

    )

    # Retorna o DataFrame

    return dfImpostos


# ====================================================================================

# BLOCO DE ANÁLISE (Executado apenas se o arquivo for rodado diretamente)

# ====================================================================================


if __name__ == '__main__':

    # 1. Carrega o DataFrame através da função

    dfImpostos = get_fato_impostos()

    # Exibir um determinado intervalo dos dados a partir do dataset

    print('Primeiras 10 linhas do dfImpostos')

    print(dfImpostos.head(10))

    print("\n" + "-"*150)

    # Exibir os nomes das colunas

    print('Nome das colunas da fato dfImpostos')

    print('Colunas: ', dfImpostos.dtypes)

    print("\n" + "-"*150)

    # Exibir o resumo estatístico

    print('Resumo estatístico da fato dfImpostos')

    print(dfImpostos.describe())

    print('-'*150)

    print()

    # ==============================================================================

    # ANÁLISE DE ASSOCIAÇÃO: Alíquotas por Estado (Variável Categórica)

    # ==============================================================================

    print('\n🔗 Correlação dos Componentes com o Imposto Total (dfImpostos_consolidado)')

    print('-'*100)

    # Lista dos componentes que foram somados para criar 'impostos_total'

    componentes_imposto = [

        'valor_icms',

        'valor_icms_st',

        'valor_fcp_st',

        'icms_interestadual_uf_destino',

        'valor_icms_fcp_uf_destino',

        'valor_pis',

        'valor_cofins'

    ]

    # A função get_fato_impostos já retorna o total calculado

    dfImpostos_original = get_fato_impostos()

    # 2. Selecionar as colunas para o cálculo da correlação

    colunas_corr = componentes_imposto + ['impostos_total']

    # Garantir que só estamos correlacionando colunas numéricas válidas

    df_corr = dfImpostos_original[colunas_corr].dropna()

    # 3. Calcular a correlação da matriz completa

    matriz_corr = df_corr.corr()

    # 4. Selecionar apenas a correlação dos componentes com 'impostos_total'

    corr_com_total = matriz_corr['impostos_total'].drop('impostos_total')

    # 5. Ordenar para ver qual é o mais correlacionado

    corr_ordenada = corr_com_total.sort_values(ascending=False)

    print('Correlação de cada componente com a soma "impostos_total":')

    print(corr_ordenada.round(4))

    print('-'*100)

    # ==============================================================================

    # ANÁLISE DE ASSOCIAÇÃO: Alíquotas por Estado (Variável Categórica)

    # ==============================================================================

    ### ANÁLISE COMPLETA POR ESTADO (ORDENADO PELA MÉDIA DAS ALÍQUOTAS) ###

    print('\n🔗 Análise de Alíquotas e Valores Médios por Estado')

    print('-'*100)

    # 1. Recuperar o DataFrame original

    dfImpostos_original = get_fato_impostos()

    # 2. Definindo os nomes das colunas de interesse

    COLUNA_TOTAL = 'impostos_total'

    COLUNAS_ALIQUOTAS = [

        'aliq_icms',

        'aliq_pis',

        'aliq_cofins'

    ]

    # 3. Agrupar os dados pela coluna 'estado' e calcular as médias

    analise_por_estado = dfImpostos_original.groupby('estado').agg(

        # Médias das Alíquotas Individuais

        media_aliq_icms=('aliq_icms', 'mean'),

        media_aliq_pis=('aliq_pis', 'mean'),

        media_aliq_cofins=('aliq_cofins', 'mean'),



        # Médias dos Valores

        media_valor_unitario=('valor_unitario', 'mean'),

        media_valor_bruto=('valor_bruto', 'mean'),



        # Média do Imposto Total

        media_imposto_total=(COLUNA_TOTAL, 'mean')

    )

    # 4. Calcular a média das 3 alíquotas (icms, pis, cofins) por estado

    analise_por_estado['media_aliquotas'] = analise_por_estado[[

        'media_aliq_icms',

        'media_aliq_pis',

        'media_aliq_cofins'

    ]].mean(axis=1)

    # 5. Ordenar a análise PELA MÉDIA DAS ALÍQUOTAS (maior para menor)

    # Alteração: sort_values(by='media_aliquotas', ascending=False)

    analise_ordenada = analise_por_estado.sort_values(

        by='media_aliquotas', ascending=False)

    print('Médias (Individuais e Agregada) e Valores por Estado (ordenado pela Média das Alíquotas):')

    print(analise_ordenada.round(4))

    print('-'*100)

    # ==============================================================================

    # 5. ANÁLISE: Top SKUs por Alíquota Individual (ICMS, PIS, COFINS)

    # ==============================================================================

    print('\n📈 Top SKUs com Maiores Alíquotas Individuais (Top 20 por Imposto)')

    print('-'*100)

    # Definir a lista de colunas de alíquotas a serem analisadas

    colunas_aliquotas = ['aliq_icms', 'aliq_pis', 'aliq_cofins']

    top_n = 20

    # Iterar sobre cada coluna de alíquota para gerar a análise

    for coluna in colunas_aliquotas:

        # 1. Agrupar por cod_sku e encontrar a alíquota MÁXIMA que ele teve

        #    *** CORREÇÃO APLICADA AQUI: Incluindo 'descricao' com 'first' ***

        df_aliq_sku = (

            dfImpostos

            .groupby('cod_sku')

            .agg(

                # Pega a primeira descrição associada

                descricao=('descricao', 'first'),

                aliquota_max=(coluna, 'max')      # Encontra a alíquota MÁXIMA

            )

            .reset_index()

        )

        # 2. Ordenar o resultado de forma descendente

        df_aliq_sku_ordenado = (

            df_aliq_sku

            .sort_values(by='aliquota_max', ascending=False)

        )

        # 3. Exibir os Top N SKUs para a alíquota atual

        print(

            f'\n*** TOP {top_n} SKUs com a maior alíquota de {coluna.upper()} ***')

        # Reordenar as colunas para a exibição e aplicar o .head(top_n)

        df_resultado = (

            df_aliq_sku_ordenado.head(top_n)

            [['cod_sku', 'descricao', 'aliquota_max']]

        )

        print(df_resultado.round(4))

        print('-'*70)

    print('-'*100)
