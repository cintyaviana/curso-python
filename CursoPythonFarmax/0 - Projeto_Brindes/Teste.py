
# ====================================================================================
# IMPORTAÇÃO DOS RECURSOS
# ====================================================================================

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

import datetime as dt

import locale

# ====================================================================================
# CRIAÇÃO DA FUNÇÃO QUE GERA O DF
# ====================================================================================


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
# BLOCO DE ANÁLISE: Executado apenas se o arquivo for rodado diretamente
# ====================================================================================


if __name__ == '__main__':

    # Carrega o DataFrame através da função
    dfBrindes = get_fato_brindes()

    # Exibir um determinado intervalo dos dados a partir do método head: primeiras linhas e o método tail: últimas linhas.
    print('='*120)
    print('Primeiras 5 linhas do dfBrindes')
    print('='*120 + "\n")
    print(dfBrindes.head(5))
    print("\n")

    print('='*120)
    print('Últimas 5 linhas do dfBrindes')
    print('='*120 + "\n")
    print(dfBrindes.tail(5))
    print("\n")

    # Exibir os nomes das colunas e o tipo dos dados
    print('='*120)
    print('Nome das colunas do dfBrindes')
    print('='*120 + "\n")
    print('Colunas: ', dfBrindes.dtypes)
    print("\n")

    # Exibir o resumo estatístico
    print('='*120)
    print('Resumo estatístico do dfBrindes')
    print('='*120 + "\n")
    print(dfBrindes.describe())
    print("\n")

    # Variável de controle para as análises mensais
    meses = sorted(dfBrindes['mes'].dropna().unique())

    # Dicionário para armazenar os resultados mensais
    dados_mensais = {}

"""
    # ============================= EXIBIR OS 5 SKU's QUE MAIS FORAM DADOS DE BRINDE ============================================

    # Certifique-se de que a biblioteca Pandas e NumPy estão instaladas e importadas!

    # =================================================================
    # 0. PRÉ-PROCESSAMENTO: CARREGAMENTO E NORMALIZAÇÃO DE COLUNAS
    # =================================================================

    # IMPORTANTE: Substitua esta linha pela sua forma real de carregar os dados
    # Exemplo de carregamento:
    # dfBrindes = pd.read_excel('caminho/para/seu/arquivo.xlsx')
    # Substitua o placeholder 'dfBrindes' pelo nome real do seu DataFrame se for diferente.

    # 0.1. Normalização de Colunas (SOLUÇÃO para o erro de nome e case)
    # Isso garante que a coluna 'CENTRO_CUSTO_AJUSTADO' seja lida como 'centro_custo_ajustado'
    dfBrindes.columns = dfBrindes.columns.str.lower()
    dfBrindes.columns = dfBrindes.columns.str.replace(' ', '_')

    # 0.2. Garantir que a coluna 'data' esteja no formato datetime (necessário para month_name)
    dfBrindes['data'] = pd.to_datetime(dfBrindes['data'])

    # 0.3. Obter a lista de meses únicos para o loop
    meses = dfBrindes['data'].dt.month.unique()
    meses.sort()

    dados_mensais = {}  # Dicionário para armazenar os resultados consolidados

    print('='*120)
    print('Análise Mensal dos Top SKUs, Custo Unitário, Participação e Curva ABC')
    print('='*120 + "\n")

    # =================================================================
    # 1. LOOP PRINCIPAL DE ANÁLISES
    # =================================================================

    for mes in meses:
        # FILTRAGEM DO MÊS
        df_mes = dfBrindes[dfBrindes['data'].dt.month == mes].copy()

        # --- CÁLCULOS TOTAIS DO MÊS ---
        total_quantidade_mes = df_mes['quantidade'].sum()
        total_custo_mes = df_mes['custo_total'].sum()

        # Transforma o número mês em nome
        nome_mes = df_mes['data'].dt.month_name(
            locale='pt_BR').iloc[0].capitalize()

        # --- AGRUPAMENTO GERAL POR SKU (ESTE CRIA O df_agrupado_sku) ---
        df_agrupado_sku = df_mes.groupby(['cod_sku', 'descricao'])[
            ['quantidade', 'custo_total']].sum()

        # CÁLCULO DAS ANÁLISES VERTICAIS (AV)
        df_agrupado_sku['AV S/ Qt Mensal (%)'] = (
            df_agrupado_sku['quantidade'] / total_quantidade_mes) * 100
        df_agrupado_sku['AV S/ Custo Mensal (%)'] = (
            df_agrupado_sku['custo_total'] / total_custo_mes) * 100

        # CÁLCULO DO CUSTO UNITÁRIO MÉDIO (CUM)
        df_agrupado_sku['custo_unitario_medio'] = (
            df_agrupado_sku['custo_total'] / df_agrupado_sku['quantidade']
        )

        dados_mensais[mes] = df_agrupado_sku

        print(f'*** 📅 {nome_mes} ***')

        # -----------------------------------------------------------------
        # A. RANKINGS TOP 5 ORIGINAIS
        # -----------------------------------------------------------------

        # 1. TOP 5 POR QUANTIDADE (BRINDE)
        top_5_quantidade = df_agrupado_sku.sort_values(
            by='quantidade', ascending=False).head(5).round(2)
        print('\n🥇 **TOP 5 POR QUANTIDADE (BRINDES):**')
        print(top_5_quantidade[['quantidade', 'AV S/ Qt Mensal (%)']])

        # 2. TOP 5 POR CUSTO
        top_5_custo = df_agrupado_sku.sort_values(
            by='custo_total', ascending=False).head(5).round(2)
        print('\n💲 **TOP 5 POR CUSTO TOTAL:**')
        print(top_5_custo[['quantidade', 'AV S/ Custo Mensal (%)']])

        # Seu código ANTES do loop principal deve terminar com a definição de 'meses'
# Ex: meses.sort()

dados_mensais = {}

print('='*120)
print('Análise Mensal dos Top SKUs, Custo Unitário, Participação e Curva ABC')
print('='*120 + "\n")

# =================================================================
# 1. LOOP PRINCIPAL DE ANÁLISES (INÍCIO DA INDENTAÇÃO)
# =================================================================

for mes in meses:
    # ----------------------------------------------------
    # NÍVEL DE INDENTAÇÃO 1 (Dentro do loop for)
    # ----------------------------------------------------

    # FILTRAGEM DO MÊS
    df_mes = dfBrindes[dfBrindes['data'].dt.month == mes].copy()

    # --- CÁLCULOS TOTAIS DO MÊS ---
    total_quantidade_mes = df_mes['quantidade'].sum()
    total_custo_mes = df_mes['custo_total'].sum()

    # Transforma o número mês em nome
    nome_mes = df_mes['data'].dt.month_name(
        locale='pt_BR').iloc[0].capitalize()

    # --- AGRUPAMENTO GERAL POR SKU (CRIA O df_agrupado_sku) ---
    df_agrupado_sku = df_mes.groupby(['cod_sku', 'descricao'])[
        ['quantidade', 'custo_total']].sum()

    # CÁLCULO DAS ANÁLISES VERTICAIS (AV)
    df_agrupado_sku['AV S/ Qt Mensal (%)'] = (
        df_agrupado_sku['quantidade'] / total_quantidade_mes) * 100
    df_agrupado_sku['AV S/ Custo Mensal (%)'] = (
        df_agrupado_sku['custo_total'] / total_custo_mes) * 100

    # CÁLCULO DO CUSTO UNITÁRIO MÉDIO (CUM)
    df_agrupado_sku['custo_unitario_medio'] = (
        df_agrupado_sku['custo_total'] / df_agrupado_sku['quantidade']
    )

    dados_mensais[mes] = df_agrupado_sku

    print(f'*** 📅 {nome_mes} ***')

    # -----------------------------------------------------------------
    # A. RANKINGS TOP 5 ORIGINAIS
    # -----------------------------------------------------------------

    # 1. TOP 5 POR QUANTIDADE (BRINDE)
    top_5_quantidade = df_agrupado_sku.sort_values(
        by='quantidade', ascending=False).head(5).round(2)
    print('\n🥇 **TOP 5 POR QUANTIDADE (BRINDES):**')
    print(top_5_quantidade[['quantidade', 'AV S/ Qt Mensal (%)']])

    # 2. TOP 5 POR CUSTO
    top_5_custo = df_agrupado_sku.sort_values(
        by='custo_total', ascending=False).head(5).round(2)
    print('\n💲 **TOP 5 POR CUSTO TOTAL:**')
    print(top_5_custo[['quantidade', 'AV S/ Custo Mensal (%)']])

    # -----------------------------------------------------------------
    # B. NOVAS ANÁLISES PERCENTUAIS SOLICITADAS
    # -----------------------------------------------------------------

    # 3. TOP 5 POR MAIOR CUSTO UNITÁRIO MÉDIO (CUM)
    top_5_cum = df_agrupado_sku.sort_values(
        by='custo_unitario_medio', ascending=False
    ).head(5).round(2)
    print(f'\n💰 **TOP 5 SKUS POR MAIOR CUSTO UNITÁRIO MÉDIO:**')
    print('*(Classificado por CUM, valor mostrado é a AV sobre o Custo Total Mensal)*')
    print(top_5_cum[['quantidade', 'AV S/ Custo Mensal (%)']])

    # 4. PARTICIPAÇÃO DE CUSTO POR TIPO (USANDO CENTRO_CUSTO_AJUSTADO)
    df_agrupado_tipo = df_mes.groupby('centro_custo_ajustado')[
        'custo_total'].sum().reset_index()

    total_custo_tipo = df_agrupado_tipo['custo_total'].sum()
    df_agrupado_tipo['AV S/ Custo Mensal (%)'] = (
        df_agrupado_tipo['custo_total'] / total_custo_tipo) * 100
    df_agrupado_tipo = df_agrupado_tipo.sort_values(
        by='AV S/ Custo Mensal (%)', ascending=False).round(2)

    print(f'\n📊 **PARTICIPAÇÃO DE CUSTO POR TIPO:**')
    print(
        df_agrupado_tipo[['centro_custo_ajustado', 'AV S/ Custo Mensal (%)']])

    # 5. COMPARAÇÃO AVs (CUSTO vs. QUANTIDADE)
    top_5_comparacao = df_agrupado_sku.sort_values(
        by='AV S/ Custo Mensal (%)', ascending=False
    ).head(5).round(2)
    print('\n⚖️ **COMPARAÇÃO AVs (CUSTO vs. QUANTIDADE):**')
    print('*(Top 5 classificado por % Custo. Analise o % Qt correspondente)*')
    print(top_5_comparacao[['AV S/ Custo Mensal (%)', 'AV S/ Qt Mensal (%)']])

    # -----------------------------------------------------------------
    # C. ANÁLISE DE CURVA ABC
    # -----------------------------------------------------------------
    print('\n⭐ **ANÁLISE CURVA ABC POR CUSTO TOTAL:**')

    # A. Prepara o DataFrame: Usa o df_agrupado_sku
    df_abc = df_agrupado_sku.copy()

    # B. Ordena e Calcula o Custo Acumulado
    df_abc = df_abc.sort_values(by='custo_total', ascending=False)
    df_abc['Custo Acumulado'] = df_abc['custo_total'].cumsum()

    # C. Calcula o Percentual Acumulado do Custo
    total_custo_mes = df_abc['custo_total'].sum()
    df_abc['% Acumulado Custo'] = (
        df_abc['Custo Acumulado'] / total_custo_mes) * 100

    # D. Define as Classes A, B e C
    df_abc['Curva ABC'] = np.where(
        df_abc['% Acumulado Custo'] <= 80,
        'A',
        np.where(
            df_abc['% Acumulado Custo'] <= 95,
            'B',
            'C'
        )
    )

    # E. Exibe o Resumo da Curva ABC
    resumo_abc = df_abc.groupby('Curva ABC').agg(
        'size'
    ).to_frame(name='Nº de SKUs')

    total_skus = len(df_abc)
    resumo_abc['% SKUs'] = (resumo_abc['Nº de SKUs'] / total_skus) * 100
    resumo_abc['% Custo Total'] = df_abc.groupby(
        'Curva ABC')['custo_total'].sum() / total_custo_mes * 100

    print(resumo_abc.round(2))

    # F. Opcional: Detalhe Top 3 SKUs de cada classe
    print('\nDetalhe Top 3 SKUs por Classe:')
    for classe in ['A', 'B', 'C']:
        top_3_classe = df_abc[df_abc['Curva ABC'] == classe].head(3)
        print(f"\n--- Classe {classe} (Top 3 Custo) ---")
        print(top_3_classe[['quantidade', 'custo_total', '% Acumulado Custo']])

    print('\n' + '=' * 120 + '\n')
"""
# -----------------------------------------------------------------
# B. NOVAS ANÁLISES PERCENTUAIS SOLICITADAS
# -----------------------------------------------------------------


"""
    print('='*120)
    print('Análise Mensal dos Top 5 SKUs por Quantidade e por Custo')
    print('='*120 + "\n")

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]

        # --- CÁLCULOS TOTAIS DO MÊS ---
        total_quantidade_mes = df_mes['quantidade'].sum()
        total_custo_mes = df_mes['custo_total'].sum()

        # Transforma o número mês em nome
        nome_mes = df_mes['data'].dt.month_name(
            locale='pt_BR').iloc[0].capitalize()

        # --- AGRUPAMENTO E CÁLCULO DOS DOIS AVs ---
        df_agrupado_sku = df_mes.groupby(['cod_sku', 'descricao'])[
            ['quantidade', 'custo_total']].sum()

        df_agrupado_sku['AV S/ Qt Mensal (%)'] = (
            df_agrupado_sku['quantidade'] / total_quantidade_mes) * 100

        df_agrupado_sku['AV S/ Custo Mensal (%)'] = (
            df_agrupado_sku['custo_total'] / total_custo_mes) * 100

        # Insere os dados consolidados na lista
        dados_mensais[mes] = df_agrupado_sku

        # =================================================================
        # --- 1. RANKING TOP 5 POR QUANTIDADE (BRINDE) ---
        # =================================================================
        top_5_quantidade = df_agrupado_sku.sort_values(
            by='quantidade', ascending=False)

        top_5_quantidade = top_5_quantidade.head(5).round(2)

        print(f'*** 📅 {nome_mes} ***')
        print('\n🥇 **TOP 5 POR QUANTIDADE (BRINDES):**')
        # Exibe SOMENTE a coluna AV S/ Qt Mensal (%)
        print(top_5_quantidade[[
              'quantidade', 'AV S/ Qt Mensal (%)', 'AV S/ Custo Mensal (%)']])

        # =================================================================
        # --- 2. RANKING TOP 5 POR CUSTO ---
        # =================================================================
        top_5_custo = df_agrupado_sku.sort_values(
            by='custo_total', ascending=False)

        top_5_custo = top_5_custo.head(5).round(2)

        print('\n💲 **TOP 5 POR CUSTO TOTAL:**')
        # Exibe SOMENTE a coluna AV S/ Custo Mensal (%)
        print(top_5_custo[['quantidade', 'AV S/ Custo Mensal (%)']])

        print('-' * 50)
        """


# +++++++++++++++==================================================+++++++++++++++++++++++
"""
print('='*120)
print('Análise Mensal dos Top 5 SKUs por Quantidade e por Custo (Original)')
print('='*120 + "\n")

# Reutilizando a estrutura FOR que você já tem
for mes in meses:
    # dfBrindes agora tem as colunas padronizadas em minúsculas
    # Use .copy() para evitar SettingWithCopyWarning
    df_mes = dfBrindes[dfBrindes['mes'] == mes].copy()

    # --- CÁLCULOS TOTAIS DO MÊS ---
    total_quantidade_mes = df_mes['quantidade'].sum()
    total_custo_mes = df_mes['custo_total'].sum()

    # Transforma o número mês em nome
    nome_mes = df_mes['data'].dt.month_name(
        locale='pt_BR').iloc[0].capitalize()

    # --- AGRUPAMENTO E CÁLCULO DOS AVs ---
    # As colunas 'cod_sku' e 'descricao' agora também estão em minúsculas
    df_agrupado_sku = df_mes.groupby(['cod_sku', 'descricao'])[
        ['quantidade', 'custo_total']].sum()

    df_agrupado_sku['AV S/ Qt Mensal (%)'] = (
        df_agrupado_sku['quantidade'] / total_quantidade_mes) * 100

    df_agrupado_sku['AV S/ Custo Mensal (%)'] = (
        df_agrupado_sku['custo_total'] / total_custo_mes) * 100

    # =================================================================
    # --- NOVOS CÁLCULOS SOLICITADOS ---
    # =================================================================

    # 1. CUSTO UNITÁRIO MÉDIO (CUM) por SKU
    df_agrupado_sku['custo_unitario_medio'] = (
        df_agrupado_sku['custo_total'] / df_agrupado_sku['quantidade']
    )

    # =================================================================
    # --- 4. RANKING TOP 5 POR CUSTO UNITÁRIO MÉDIO (CUM) ---
    # =================================================================

    top_5_cum = df_agrupado_sku.sort_values(
        by='custo_unitario_medio', ascending=False
    ).head(5).round(2)

    print(f'\n💰 **TOP 5 SKUS POR MAIOR CUSTO UNITÁRIO MÉDIO ({nome_mes}):**')
    print('*(Classificado por Custo Unitário, valor mostrado é a AV sobre o Custo Total Mensal)*')
    print(top_5_cum[['quantidade', 'AV S/ Custo Mensal (%)']])

    # =================================================================
    # --- 5. RANKING POR PARTICIPAÇÃO DE CUSTO POR TIPO (AGORA FUNCIONA) ---
    # =================================================================
    # Usa a coluna 'custo_ajustado' (que agora está padronizada em minúsculas)

    # 5.1. Agrupamento
    df_agrupado_tipo = df_mes.groupby('centro_custo_ajustado')[
        'custo_total'].sum().reset_index()

    # 5.2. Cálculo do Percentual
    total_custo_tipo = df_agrupado_tipo['custo_total'].sum()
    df_agrupado_tipo['AV S/ Custo Mensal (%)'] = (
        df_agrupado_tipo['custo_total'] / total_custo_tipo) * 100

    # 5.3. Exibição
    df_agrupado_tipo = df_agrupado_tipo.sort_values(
        by='AV S/ Custo Mensal (%)', ascending=False).round(2)

    print(f'\n📊 **PARTICIPAÇÃO DE CUSTO POR TIPO ({nome_mes}):**')
    # Exibe o Tipo e o Percentual (AV)
    print(
        df_agrupado_tipo[['centro_custo_ajustado', 'AV S/ Custo Mensal (%)']])

    # =================================================================
    # --- 6. COMPARAÇÃO: TOP 5 SKUS QUE PESAM NO CUSTO VS. QUANTIDADE ---
    # =================================================================

    top_5_comparacao = df_agrupado_sku.sort_values(
        by='AV S/ Custo Mensal (%)', ascending=False
    ).head(5).round(2)

    print('\n⚖️ **COMPARAÇÃO AVs (CUSTO vs. QUANTIDADE):**')
    print('*(Top 5 classificado por % Custo. Analise o % Qt correspondente)*')
    print(top_5_comparacao[['AV S/ Custo Mensal (%)', 'AV S/ Qt Mensal (%)']])

    print('\n' + '-' * 120 + '\n')
"""

"""
   

    

   

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
"""
