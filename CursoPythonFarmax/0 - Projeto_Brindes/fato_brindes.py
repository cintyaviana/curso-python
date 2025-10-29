# importar os recursos necessarios

# Biblioteca para trabalhar com caminhos de arquivos
from pathlib import Path

# Biblioteca
import numpy as np

# Biblioteca
import pandas as pd

# Biblioteca para a plotagem de graficos
import matplotlib as plt

# Biblioteca para a plotagem de graficos
import seaborn as sb

import calendar as cl

# Retorna o caminho de onde estão os arquivos do projeto
dataPath = Path(__file__).resolve().parent

# Carregar os dados - para este proposito vamos definir uma variavel para receber como valor o arquivo de dados
dfBrindes = pd.read_excel(
    dataPath / 'fBrindes.xlsx')

# Exibir um determinado intervalo dos dados a partir do dataset
print('Primeiras 10 linhas do dfBrindes')
print(dfBrindes.head(10))
print()
print("-"*150)

# Exibir os nomes das colunas
print('Nome das colunas da fato dfBrindes')
print('Colunas: ', dfBrindes.dtypes)
print()
print("-"*150)

# Exibir o resumo estatístico
print('Resumo estatístico da fato dfBrindes')
print(dfBrindes.describe())
print('-'*150)
print()

# ============================= EXIBIR OS 20 SKU'S QUE MAIS FORAM DADOS DE BRINDE ============================================

print('Top 20 SKUs que mais foram dados como brindes')
print('-'*150)

# Criar uma coluna com o número do mês
dfBrindes['mes'] = dfBrindes['data'].dt.month

# Pegar todos os meses distintos da base (ordenados)
meses = sorted(dfBrindes['mes'].dropna().unique())

# Dicionário para armazenar os dados mensais de cada mês
dados_mensais = {}

# Loop para cada mês encontrado
for mes in meses:
    # Filtrar o DataFrame apenas para o mês atual
    df_mes = dfBrindes[dfBrindes['mes'] == mes]

    total_mes = df_mes['quantidade'].sum()

    # Obter o nome do mês por extenso (em português)
    nome_mes = df_mes['data'].dt.month_name(
        locale='pt_BR').iloc[0].capitalize()

    # Agrupar e somar as quantidades de brindes por SKU e descrição
    total_brindes_sku = df_mes.groupby(['cod_sku', 'descricao'])[
        ['quantidade']].sum()

    total_brindes_sku['AV S/ Qt mensal'] = (
        total_brindes_sku['quantidade'] / total_mes
    ) * 100

    # Salvar o resultado do mês atual no dicionário
    dados_mensais[mes] = total_brindes_sku

    # Ordenar e pegar os top 20 daquele mês
    top_20_brindes = total_brindes_sku.sort_values(
        by='quantidade', ascending=False).head(20)

    print(f'\n📅 Mês: {nome_mes}')
    print(top_20_brindes.round(2))
    print()
    print('-'*150)

# ====================================== IDENTIFICAR SKUS COMUNS A TODOS OS MESES ===================================

# Extrair e ordenar os nomes dos meses analisados
meses_numeros = sorted(dados_mensais.keys())

# Obter o nome do mês por extenso (em português)
nomes_meses = ', '.join([
    cl.month_name[m].capitalize()
    for m in meses_numeros
])

print(
    f'\n🔁 Top 20 SKUs comuns em todos os meses analisados ({nomes_meses}) e soma total:\n')

# Interseção dos índices (cod_sku, descricao) de todos os DataFrames mensais
skus_comuns = set.intersection(*[
    set(df.index.get_level_values(0))  # Pega APENAS o cod_sku (nível 0)
    for df in dados_mensais.values()
])

# Se não houver SKUs comuns, informar e sair
if not skus_comuns:
    print('⚠️ Nenhum SKU está presente em todos os meses analisados.')
else:
    # Concatena todos os DataFrames mensais
    df_todos = pd.concat(dados_mensais.values())

    # Soma a coluna 'quantidade' do DataFrame concatenado
    total_geral_brindes = df_todos['quantidade'].sum()

    # Filtrar apenas SKUs comuns
    df_filtrado = df_todos[df_todos.index.get_level_values(
        0).isin(skus_comuns)]

    # Agrupar e somar as quantidades de todos os meses
    df_comuns_soma = (
        df_filtrado
        .groupby(level=[0, 1])['quantidade']
        .sum()
    )

    # Converter a Series de soma em DataFrame para adicionar a nova coluna
    df_comuns = df_comuns_soma.to_frame()

    # Calcular a AV S/ Qt total dos meses analisados
    df_comuns['AV S/ Qt total'] = (
        df_comuns['quantidade'] / total_geral_brindes
    ) * 100

    # Ordenar e pegar os top 20
    df_comuns_top_20 = (
        df_comuns
        .sort_values(by='quantidade', ascending=False)
        .head(20)
    )

    print(df_comuns_top_20.round(2))
    print('-' * 150)

# ============================= EXIBIR OS CENTROS DE CUSTO QUE MAIS DERAM BRINDE ============================================

print('Top Centros de Custos que mais deram brindes')
print('-'*150)

# Criar uma coluna com o número do mês
dfBrindes['mes'] = dfBrindes['data'].dt.month

# Pegar todos os meses distintos da base (ordenados)
meses = sorted(dfBrindes['mes'].dropna().unique())

# Dicionário para armazenar os dados mensais de cada mês
dados_mensais = {}

# Loop para cada mês encontrado
for mes in meses:
    # Filtrar o DataFrame apenas para o mês atual
    df_mes = dfBrindes[dfBrindes['mes'] == mes]

    total_mes = df_mes['quantidade'].sum()

    # Obter o nome do mês por extenso (em português)
    nome_mes = df_mes['data'].dt.month_name(
        locale='pt_BR').iloc[0].capitalize()

    # Agrupar e somar as quantidades de brindes por SKU e descrição
    total_brindes_sku = df_mes.groupby(['centro_custo_ajustado'])[
        ['quantidade']].sum()

    total_brindes_sku['AV S/ Qt mensal'] = (
        total_brindes_sku['quantidade'] / total_mes
    ) * 100

    # Salvar o resultado do mês atual no dicionário
    dados_mensais[mes] = total_brindes_sku

    # Ordenar e pegar os top 20 daquele mês
    top_20_brindes = total_brindes_sku.sort_values(
        by='quantidade', ascending=False).head(20)

    print(f'\n📅 Mês: {nome_mes}')
    print(top_20_brindes.round(2))
    print()
    print('-'*150)

# ====================================== IDENTIFICAR CENTROS DE CUSTO COMUNS A TODOS OS MESES ===================================

# Extrair e ordenar os nomes dos meses analisados
meses_numeros = sorted(dados_mensais.keys())

# Obter o nome do mês por extenso (em português)
nomes_meses = ', '.join([
    cl.month_name[m].capitalize()
    for m in meses_numeros
])

print(
    f'\n🔁 Top Centros de Custo comuns em todos os meses analisados ({nomes_meses}) e soma total:\n')

# Interseção dos índices (cod_sku, descricao) de todos os DataFrames mensais
skus_comuns = set.intersection(*[
    set(df.index.get_level_values(0))  # Pega APENAS o cod_sku (nível 0)
    for df in dados_mensais.values()
])

# Se não houver SKUs comuns, informar e sair
if not skus_comuns:
    print('⚠️ Nenhum SKU está presente em todos os meses analisados.')
else:
    # Concatena todos os DataFrames mensais
    df_todos = pd.concat(dados_mensais.values())

    # Soma a coluna 'quantidade' do DataFrame concatenado
    total_geral_brindes = df_todos['quantidade'].sum()

    # Filtrar apenas SKUs comuns
    df_filtrado = df_todos[df_todos.index.get_level_values(
        0).isin(skus_comuns)]

    # Agrupar e somar as quantidades de todos os meses
    df_comuns_soma = (
        df_filtrado
        .groupby(level=[0])['quantidade']
        .sum()
    )

    # Converter a Series de soma em DataFrame para adicionar a nova coluna
    df_comuns = df_comuns_soma.to_frame()

    # Calcular a AV S/ Qt total dos meses analisados
    df_comuns['AV S/ Qt total'] = (
        df_comuns['quantidade'] / total_geral_brindes
    ) * 100

    # Ordenar e pegar os top 20
    df_comuns_top_20 = (
        df_comuns
        .sort_values(by='quantidade', ascending=False)
        .head(20)
    )

    print(df_comuns_top_20.round(2))
    print('-' * 150)


# ============================= EXIBIR TOP 20 CLIENTE QUE MAIS RECEBERAM BRINDES ============================================

print('Top 20 Clientes que mais receberam brindes')
print('-'*150)

# Criar uma coluna com o número do mês
dfBrindes['mes'] = dfBrindes['data'].dt.month

# Pegar todos os meses distintos da base (ordenados)
meses = sorted(dfBrindes['mes'].dropna().unique())

# Dicionário para armazenar os dados mensais de cada mês
dados_mensais = {}

# Loop para cada mês encontrado
for mes in meses:
    # Filtrar o DataFrame apenas para o mês atual
    df_mes = dfBrindes[dfBrindes['mes'] == mes]

    total_mes = df_mes['quantidade'].sum()

    # Obter o nome do mês por extenso (em português)
    nome_mes = df_mes['data'].dt.month_name(
        locale='pt_BR').iloc[0].capitalize()

    # Agrupar e somar as quantidades de brindes por SKU e descrição
    total_brindes_sku = df_mes.groupby(['cod_cliente', 'cliente'])[
        ['quantidade']].sum()

    total_brindes_sku['AV S/ Qt mensal'] = (
        total_brindes_sku['quantidade'] / total_mes
    ) * 100

    # Salvar o resultado do mês atual no dicionário
    dados_mensais[mes] = total_brindes_sku

    # Ordenar e pegar os top 20 daquele mês
    top_20_brindes = total_brindes_sku.sort_values(
        by='quantidade', ascending=False).head(20)

    print(f'\n📅 Mês: {nome_mes}')
    print(top_20_brindes.round(2))
    print()
    print('-'*150)

# ====================================== IDENTIFICAR TOP 20 CLIENTES COMUNS A TODOS OS MESES ===================================

print('Top 20 Clientes que mais receberam brindes em comum aos meses')
print('-'*150)

# Extrair e ordenar os nomes dos meses analisados
meses_numeros = sorted(dados_mensais.keys())

# Obter o nome do mês por extenso (em português)
nomes_meses = ', '.join([
    cl.month_name[m].capitalize()
    for m in meses_numeros
])

print(
    f'\n🔁 Top 20 clientes comuns em todos os meses analisados ({nomes_meses}) e soma total:\n')

# Interseção dos índices (cod_sku, descricao) de todos os DataFrames mensais
skus_comuns = set.intersection(*[
    set(df.index.get_level_values(0))  # Pega APENAS o cod_sku (nível 0)
    for df in dados_mensais.values()
])

# Se não houver SKUs comuns, informar e sair
if not skus_comuns:
    print('⚠️ Nenhum Cliente está presente em todos os meses analisados.')
else:
    # Concatena todos os DataFrames mensais
    df_todos = pd.concat(dados_mensais.values())

    # Soma a coluna 'quantidade' do DataFrame concatenado
    total_geral_brindes = df_todos['quantidade'].sum()

    # Filtrar apenas SKUs comuns
    df_filtrado = df_todos[df_todos.index.get_level_values(
        0).isin(skus_comuns)]

    # Agrupar e somar as quantidades de todos os meses
    df_comuns_soma = (
        df_filtrado
        .groupby(level=[0, 1])['quantidade']
        .sum()
    )

    # Converter a Series de soma em DataFrame para adicionar a nova coluna
    df_comuns = df_comuns_soma.to_frame()

    # Calcular a AV S/ Qt total dos meses analisados
    df_comuns['AV S/ Qt total'] = (
        df_comuns['quantidade'] / total_geral_brindes
    ) * 100

    # Ordenar e pegar os top 20
    df_comuns_top_20 = (
        df_comuns
        .sort_values(by='quantidade', ascending=False)
        .head(20)
    )

    print(df_comuns_top_20.round(2))
    print('-' * 150)
