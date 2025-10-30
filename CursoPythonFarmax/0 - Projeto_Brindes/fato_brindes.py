
# ==========================================================
# IMPORTAÇÃO DOS RECURSOS
# ==========================================================

# Biblioteca para trabalhar com caminhos de arquivos. Permite manipulação de caminhos de forma orientada a objetos.
from pathlib import Path

# Biblioteca oferece estruturas de dados flexíveis (como DataFrame e Series) e ferramentas para manipulação, limpeza e análise de dados tabulares.
import pandas as pd

# ====================================================================================
# CRIAÇÃO DA FUNÇÃO QUE GERA O DF
# ====================================================================================


def get_fato_brindes():

    # Retorna o caminho de onde estão os arquivos do projeto
    dataPath = Path(__file__).resolve().parent

    # Carregar os dados - para este propósito vamos definir uma variavel para receber como valor o arquivo de dados
    dfBrindes = pd.read_excel(
        dataPath / 'fBrindes.xlsx')

    # Converte para o Período Mensal (01/mês/ano)
    dfBrindes['data'] = dfBrindes['data'].dt.to_period('M').dt.to_timestamp()

    # Criar uma coluna (mes) com o número do mês em relação a coluna (data)
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
    print('🔗 Primeiras 5 linhas do dfBrindes')
    print('='*120 + "\n")
    print(dfBrindes.head(5))
    print("\n")

    print('='*120)
    print('🔗 Últimas 5 linhas do dfBrindes')
    print('='*120 + "\n")
    print(dfBrindes.tail(5))
    print("\n")

    # Exibir os nomes das colunas e o tipo dos dados
    print('='*120)
    print('🔗 Nome das colunas do dfBrindes')
    print('='*120 + "\n")
    print('Colunas: ', dfBrindes.dtypes)
    print("\n")

    # Exibir o resumo estatístico
    print('='*120)
    print('🔗 Resumo estatístico do dfBrindes')
    print('='*120 + "\n")
    print(dfBrindes.describe())
    print("\n")
# ============================= EXIBIR TOP 5 SKU'S QUE MAIS FORAM DADOS COMO BRINDES ============================================

    # Análise mensal
    # Variável de controle para as análises mensais
    meses = sorted(dfBrindes['mes'].dropna().unique())

    # Dicionário para armazenar os resultados mensais
    dados_mensais_sku = {}

    print('='*120)
    print('🔗 Top 5 SKUs que mais foram dados como brindes no mês')
    print('='*120 + "\n")

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]

        # Soma a coluna quantidade de acordo com o mês sendo analisado
        total_mes = df_mes['quantidade'].sum()

        # Transforma o número mês em nome
        nome_mes = df_mes['data'].dt.month_name(
            locale='pt_BR').iloc[0].capitalize()

        # Soma a coluna quantidade de acordo com o SKU e o mês sendo analisado
        total_brindes_sku = df_mes.groupby(['cod_sku', 'descricao'])[
            ['quantidade']].sum()

        # Cria a coluna AV (Total por SKU / Total geral no mês em análise)
        total_brindes_sku['(%) S/Qt mensal'] = (
            total_brindes_sku['quantidade'] / total_mes) * 100

        # Insere os dados na lista
        dados_mensais_sku[mes] = total_brindes_sku

        # Seleciona os 5 maiores SKU
        top_brindes = total_brindes_sku.sort_values(
            by='quantidade', ascending=False).head(5).round(2)

        # Exibição dos dados
        print(f'\n📅 Mês: {nome_mes}')
        print(top_brindes[['(%) S/Qt mensal']])
        print("\n")

    # Análise geral
    # Concatena todos os DataFrames mensais em um único DataFrame
    df_consolidado = pd.concat(dados_mensais_sku.values())

    # Agrupa o consolidado para obter a soma TOTAL de quantidade por SKU
    total_brindes_base_completa = df_consolidado.groupby(
        level=[0, 1])['quantidade'].sum().reset_index()
    # Note que o 'level=[0, 1]' agrupa pelos índices de 'cod_sku' e 'descricao'

    # Soma total de brindes em toda a base
    total_geral = total_brindes_base_completa['quantidade'].sum()

    # Cria a coluna AV S/ Qt Total (participação na base completa)
    total_brindes_base_completa['(%) S/Qt mensal'] = (
        total_brindes_base_completa['quantidade'] / total_geral) * 100

    # Seleciona o Top 5 da base completa
    top_5_geral = total_brindes_base_completa.sort_values(
        by='quantidade', ascending=False).head(5).round(2)

    # Exibição dos dados
    print('='*120)
    print('🏆 TOP 5 GERAL: SKUs que mais foram dados como brinde')
    print('='*120 + "\n")
    print(top_5_geral[['cod_sku', 'descricao', '(%) S/Qt mensal']
                      ].set_index(['cod_sku', 'descricao']))
    print("\n" + "="*120 + "\n")

    # ============================= EXIBIR OS CENTROS DE CUSTO QUE MAIS DERAM BRINDE ============================================

    # Dicionário para armazenar os resultados mensais (CC)
    dados_mensais_cc = {}

    print('='*120)
    print('🔗 Top 5 Centros de Custos que mais deram brindes no mês')
    print('='*120 + "\n")

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes].copy()

        # Soma a coluna quantidade de acordo com o mês sendo analisado
        total_mes = df_mes['quantidade'].sum()

        # Transforma o número mês em nome
        nome_mes = df_mes['data'].dt.month_name(
            locale='pt_BR').iloc[0].capitalize()

        # Soma a coluna quantidade de acordo com o CC e o mês sendo analisado
        total_brindes_cc = df_mes.groupby(['centro_custo_ajustado'])[
            ['quantidade']].sum()

        # Cria a coluna AV (Total por CC / Total geral no mês em análise)
        total_brindes_cc['(%) S/Qt mensal'] = (
            total_brindes_cc['quantidade'] / total_mes) * 100

        # Insere os dados na lista
        dados_mensais_cc[mes] = total_brindes_cc

        # Seleciona o Top 5 da base
        top_5_brindes_cc = total_brindes_cc.sort_values(
            by='quantidade', ascending=False).head(5).round(2)

        # Exibição dos dados
        print(f'\n📅 Mês: {nome_mes}')
        # Exibe apenas a coluna AV S/ Qt mensal
        print(top_5_brindes_cc[['(%) S/Qt mensal']])
        print("\n")

    # Análise geral
    # Concatena todos os DataFrames CC mensais
    df_consolidado_cc = pd.concat(dados_mensais_cc.values())

    # Agrupa o consolidado para obter a soma TOTAL de quantidade por CC
    total_brindes_base_completa_cc = df_consolidado_cc.groupby(
        level=[0])['quantidade'].sum().reset_index()

    # Reutiliza o total geral de quantidade calculado no Bloco 1
    total_geral_cc = total_brindes_base_completa_cc['quantidade'].sum()

    # Cria a coluna AV S/ Qt Total (participação na base completa)
    total_brindes_base_completa_cc['(%) S/Qt mensal'] = (
        total_brindes_base_completa_cc['quantidade'] / total_geral_cc) * 100

    # Seleciona o Top 5 da base completa
    top_5_geral_cc = total_brindes_base_completa_cc.sort_values(
        by='quantidade', ascending=False).head(5).round(2)

    # Exibição dos dados
    print('='*120)
    print('🏆 TOP 5 GERAL: Centros de Custos que mais deram brindes')
    print('='*120 + "\n")
    print(top_5_geral_cc[['centro_custo_ajustado', '(%) S/Qt mensal']
                         ].set_index('centro_custo_ajustado'))
    print("\n")

    # ============================= EXIBIR TOP 5 CLIENTE QUE MAIS RECEBERAM BRINDES ============================================
    print("="*120)
    print('Top 5 Clientes que mais receberam brindes')
    print("="*120)

    # Redefinir dados_mensais para a análise de Clientes
    dados_mensais_cliente = {}

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]

        # Soma a coluna quantidade de acordo com o mês sendo analisado
        total_mes = df_mes['quantidade'].sum()

        # Transforma o número mês em nome
        nome_mes = df_mes['data'].dt.month_name(
            locale='pt_BR').iloc[0].capitalize()

        # Soma a coluna quantidade de acordo com o Cliente e o mês sendo analisado
        total_brindes_cliente = df_mes.groupby(['cod_cliente', 'cliente'])[
            ['quantidade']].sum()

        # Cria a coluna AV (Total por Cliente / Total geral no mês em análise)
        total_brindes_cliente['(%) S/Qt mensal'] = (
            total_brindes_cliente['quantidade'] / total_mes) * 100

        # Insere os dados na lista
        dados_mensais_cliente[mes] = total_brindes_cliente

        # Seleciona o Top 5 da base
        top_5_brindes = total_brindes_cliente.sort_values(
            by='quantidade', ascending=False).head(5).round(2)

        # Exibição dos dados
        print(f'\n📅 Mês: {nome_mes}')
        print(top_5_brindes[['(%) S/Qt mensal']])
        print("\n")

    # Análise Geral
    # Concatena todos os DataFrames CC mensais
    df_consolidado_cliente = pd.concat(dados_mensais_cliente.values())

    # Agrupa o consolidado para obter a soma TOTAL de quantidade por Cliente
    total_brindes_base_completa_cliente = df_consolidado_cliente.groupby(
        level=[0, 1])['quantidade'].sum().reset_index()

    # Reutiliza o total geral de quantidade calculado
    total_geral_cliente = total_brindes_base_completa_cliente['quantidade'].sum(
    )

    # Cria a coluna AV S/ Qt Total (participação na base completa)
    total_brindes_base_completa_cliente['(%) S/Qt mensal'] = (
        total_brindes_base_completa_cliente['quantidade'] / total_geral_cliente) * 100

    # Seleciona o Top 5 da base completa
    top_5_geral_cli = total_brindes_base_completa_cliente.sort_values(
        by='quantidade', ascending=False).head(5).round(2)

    # Exibição dos dados
    print('='*120)
    print('🏆 TOP 5 GERAL: Clientes que mais receberam brindes (Consolidado)')
    print('='*120 + "\n")
    print(top_5_geral_cli[['cod_cliente', 'cliente', '(%) S/Qt mensal']
                          ].set_index(['cod_cliente', 'cliente']))
    print("\n" + "="*120 + "\n")
