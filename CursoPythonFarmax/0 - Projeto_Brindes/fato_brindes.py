
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


def get_fato_brindes():

    # Retorna o caminho de onde estão os arquivos do projeto
    dataPath = Path(__file__).resolve().parent

    # Carregar os dados - para este propósito vamos definir uma variavel para receber como valor o arquivo de dados
    dfBrindes = pd.read_excel(
        dataPath / 'fBrindes.xlsx')

    # Criar uma coluna com o número do mês
    dfBrindes['mes'] = dfBrindes['data'].dt.month

    # Retorna o DataFrame
    return dfBrindes

# ====================================================================================
# BLOCO DE ANÁLISE (Executado apenas se o arquivo for rodado diretamente)
# ====================================================================================


if __name__ == '__main__':
    # 1. Carrega o DataFrame através da função
    dfBrindes = get_fato_brindes()

    # Exibir um determinado intervalo dos dados a partir do dataset
    print('Primeiras 10 linhas do dfBrindes')
    print(dfBrindes.head(10))
    print("\n" + "-"*150)

    # Exibir os nomes das colunas
    print('Nome das colunas da fato dfBrindes')
    print('Colunas: ', dfBrindes.dtypes)
    print("\n" + "-"*150)

    # Exibir o resumo estatístico
    print('Resumo estatístico da fato dfBrindes')
    print(dfBrindes.describe())
    print('-'*150)
    print()

    # Variável de controle para as análises mensais
    meses = sorted(dfBrindes['mes'].dropna().unique())
    dados_mensais = {}  # Dicionário para armazenar os resultados mensais

    # ============================= EXIBIR OS 20 SKU'S QUE MAIS FORAM DADOS DE BRINDE ============================================

    print('Top 20 SKUs que mais foram dados como brindes')
    print('-'*150)

    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]
        total_mes = df_mes['quantidade'].sum()
        nome_mes = df_mes['data'].dt.month_name(
            locale='pt_BR').iloc[0].capitalize()

        total_brindes_sku = df_mes.groupby(['cod_sku', 'descricao'])[
            ['quantidade']].sum()
        total_brindes_sku['AV S/ Qt mensal'] = (
            total_brindes_sku['quantidade'] / total_mes) * 100
        dados_mensais[mes] = total_brindes_sku

        top_20_brindes = total_brindes_sku.sort_values(
            by='quantidade', ascending=False).head(20)

        print(f'\n📅 Mês: {nome_mes}')
        print(top_20_brindes.round(2))
        print("\n" + '-'*150)

    # ====================================== IDENTIFICAR SKUS COMUNS A TODOS OS MESES ===================================
    # NOTA: O bloco abaixo usa a última versão de 'dados_mensais' do loop acima.

    meses_numeros = sorted(dados_mensais.keys())
    nomes_meses = ', '.join([cl.month_name[m].capitalize()
                            for m in meses_numeros])

    print(
        f'\n🔁 Top 20 SKUs comuns em todos os meses analisados ({nomes_meses}) e soma total:\n')

    skus_comuns = set.intersection(
        *[set(df.index.get_level_values(0)) for df in dados_mensais.values()])

    if not skus_comuns:
        print('⚠️ Nenhum SKU está presente em todos os meses analisados.')
    else:
        df_todos = pd.concat(dados_mensais.values())
        total_geral_brindes = df_todos['quantidade'].sum()
        df_filtrado = df_todos[df_todos.index.get_level_values(
            0).isin(skus_comuns)]

        df_comuns_soma = (df_filtrado.groupby(
            level=[0, 1])['quantidade'].sum())
        df_comuns = df_comuns_soma.to_frame()
        df_comuns['AV S/ Qt total'] = (df_comuns['quantidade'] /
                                       total_geral_brindes) * 100

        df_comuns_top_20 = (df_comuns.sort_values(
            by='quantidade', ascending=False).head(20))

        print(df_comuns_top_20.round(2))
        print('-' * 150)

    # ============================= EXIBIR OS CENTROS DE CUSTO QUE MAIS DERAM BRINDE ============================================

    print('Top Centros de Custos que mais deram brindes')
    print('-'*150)

    # É necessário redefinir 'dados_mensais' para a análise de Centros de Custo
    dados_mensais = {}

    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]
        total_mes = df_mes['quantidade'].sum()
        nome_mes = df_mes['data'].dt.month_name(
            locale='pt_BR').iloc[0].capitalize()

        # Agrupar por Centro de Custo (apenas um nível)
        total_brindes_cc = df_mes.groupby(['centro_custo_ajustado'])[
            ['quantidade']].sum()
        total_brindes_cc['AV S/ Qt mensal'] = (
            total_brindes_cc['quantidade'] / total_mes) * 100
        dados_mensais[mes] = total_brindes_cc  # Salva o resultado do CC

        top_20_brindes = total_brindes_cc.sort_values(
            by='quantidade', ascending=False).head(20)

        print(f'\n📅 Mês: {nome_mes}')
        print(top_20_brindes.round(2))
        print("\n" + '-'*150)

    # ====================================== IDENTIFICAR CENTROS DE CUSTO COMUNS A TODOS OS MESES ===================================
    # NOTA: Este bloco usa a última versão de 'dados_mensais' (Centros de Custo).

    meses_numeros = sorted(dados_mensais.keys())
    nomes_meses = ', '.join([cl.month_name[m].capitalize()
                            for m in meses_numeros])

    print(
        f'\n🔁 Top Centros de Custo comuns em todos os meses analisados ({nomes_meses}) e soma total:\n')

    # A interseção é pelo Nível 0 (centro_custo_ajustado)
    cc_comuns = set.intersection(
        *[set(df.index.get_level_values(0)) for df in dados_mensais.values()])

    if not cc_comuns:
        print('⚠️ Nenhum Centro de Custo está presente em todos os meses analisados.')
    else:
        df_todos = pd.concat(dados_mensais.values())
        total_geral_brindes = df_todos['quantidade'].sum()
        df_filtrado = df_todos[df_todos.index.get_level_values(
            0).isin(cc_comuns)]

        # Agrupar por APENAS o nível 0 (centro_custo_ajustado)
        df_comuns_soma = (df_filtrado.groupby(level=[0])[
                          'quantidade'].sum())  # CORREÇÃO DE NIVEL
        df_comuns = df_comuns_soma.to_frame()
        df_comuns['AV S/ Qt total'] = (df_comuns['quantidade'] /
                                       total_geral_brindes) * 100

        df_comuns_top_20 = (df_comuns.sort_values(
            by='quantidade', ascending=False).head(20))

        print(df_comuns_top_20.round(2))
        print('-' * 150)

    # ============================= EXIBIR TOP 20 CLIENTE QUE MAIS RECEBERAM BRINDES ============================================

    print('Top 20 Clientes que mais receberam brindes')
    print('-'*150)

    # Redefinir dados_mensais para a análise de Clientes
    dados_mensais = {}

    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]
        total_mes = df_mes['quantidade'].sum()
        nome_mes = df_mes['data'].dt.month_name(
            locale='pt_BR').iloc[0].capitalize()

        # Agrupar por Cliente (cod_cliente, cliente)
        total_brindes_cli = df_mes.groupby(['cod_cliente', 'cliente'])[
            ['quantidade']].sum()
        total_brindes_cli['AV S/ Qt mensal'] = (
            total_brindes_cli['quantidade'] / total_mes) * 100
        dados_mensais[mes] = total_brindes_cli  # Salva o resultado do Cliente

        top_20_brindes = total_brindes_cli.sort_values(
            by='quantidade', ascending=False).head(20)

        print(f'\n📅 Mês: {nome_mes}')
        print(top_20_brindes.round(2))
        print("\n" + '-'*150)

    # ====================================== IDENTIFICAR TOP 20 CLIENTES COMUNS A TODOS OS MESES ===================================

    print('Top 20 Clientes que mais receberam brindes em comum aos meses')
    print('-'*150)

    meses_numeros = sorted(dados_mensais.keys())
    nomes_meses = ', '.join([cl.month_name[m].capitalize()
                            for m in meses_numeros])

    print(
        f'\n🔁 Top 20 clientes comuns em todos os meses analisados ({nomes_meses}) e soma total:\n')

    # A interseção é pelo Nível 0 (cod_cliente)
    clientes_comuns = set.intersection(
        *[set(df.index.get_level_values(0)) for df in dados_mensais.values()])

    if not clientes_comuns:
        print('⚠️ Nenhum Cliente está presente em todos os meses analisados.')
    else:
        df_todos = pd.concat(dados_mensais.values())
        total_geral_brindes = df_todos['quantidade'].sum()
        df_filtrado = df_todos[df_todos.index.get_level_values(
            0).isin(clientes_comuns)]

        # Agrupar por ambos os níveis (cod_cliente e cliente)
        df_comuns_soma = (df_filtrado.groupby(
            level=[0, 1])['quantidade'].sum())
        df_comuns = df_comuns_soma.to_frame()
        df_comuns['AV S/ Qt total'] = (df_comuns['quantidade'] /
                                       total_geral_brindes) * 100

        df_comuns_top_20 = (df_comuns.sort_values(
            by='quantidade', ascending=False).head(20))

        print(df_comuns_top_20.round(2))
        print('-' * 150)

    # ============================= NOVO BLOCO: EXIBIR OS 20 SKU'S COM MAIOR CUSTO TOTAL ============================================

    # ============================= NOVO BLOCO: EXIBIR OS 20 SKU'S COM MAIOR CUSTO TOTAL (E CUSTO MÉDIO) =============================

    print('Top 20 SKUs com MAIOR CUSTO TOTAL (Incluindo Custo Médio)')
    print('-'*150)

    # Re-inicializar dados_mensais para esta nova análise
    dados_mensais_custo = {}

    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]
        # Usar a soma do CUSTO TOTAL do mês como base
        total_custo_mes = df_mes['custo_total'].sum()

        # Garantir o nome do mês (reutilizando a lógica existente)
        nome_mes = df_mes['data'].dt.month_name(
            locale='pt_BR').iloc[0].capitalize()

        # Agrupar por SKU, somando o 'custo_total' e a 'quantidade'
        total_custo_sku = df_mes.groupby(['cod_sku', 'descricao']).agg(
            custo_total=('custo_total', 'sum'),
            # Adicionamos 'quantidade' para calcular a média
            quantidade=('quantidade', 'sum')
        )

        # Calcular o CUSTO MÉDIO por SKU: custo_total / quantidade
        # Para evitar divisão por zero, usamos .fillna(0) e tratamos a possibilidade.
        total_custo_sku['custo_medio_sku'] = (
            total_custo_sku['custo_total'] / total_custo_sku['quantidade']
        ).fillna(0)  # Trata casos onde quantidade é zero

        # Calcular a representatividade do custo por SKU no custo total do mês
        total_custo_sku['AV S/ Custo mensal'] = (
            total_custo_sku['custo_total'] / total_custo_mes) * 100

        # Armazenar o resultado, se necessário para análises de custo comuns (Futuro)
        dados_mensais_custo[mes] = total_custo_sku

        # Ordenar pelo 'custo_total' (mantendo o foco no maior gasto total)
        top_20_custo = total_custo_sku.sort_values(
            by='custo_total', ascending=False).head(20)

        print(f'\n📅 Mês: {nome_mes}')
        print(top_20_custo.round(2))
        print("\n" + '-'*150)

    # ... O restante do seu código (SKUs comuns, Centros de Custo, Clientes) segue aqui
