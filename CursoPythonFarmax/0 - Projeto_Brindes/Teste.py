
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


def get_py_fBrinde():

    # Retorna o caminho de onde estão os arquivos do projeto
    dataPath = Path(__file__).resolve().parent

    # Carregar os dados - para este propósito vamos definir uma variavel para receber como valor o arquivo de dados
    dfBrindes = pd.read_excel(
        dataPath / 'Ex_fBrindes_Impostos.xlsx')

    # Converte para o Período Mensal (01/mês/ano)
    dfBrindes['data'] = dfBrindes['data'].dt.to_period('M').dt.to_timestamp()

    # Criar a coluna (mes) com o número do mês em relação a coluna (data)
    dfBrindes['mes'] = dfBrindes['data'].dt.month

    # # Criar a coluna (menome_mes) com o nome do mês em relação a coluna (data)
    dfBrindes['nome_mes'] = dfBrindes['data'].dt.month_name(
        locale='pt_BR').str.capitalize()

    dfBrindes['total_impostos'] = (
        dfBrindes['valor_icms'].fillna(0) +
        dfBrindes['valor_icms_st'].fillna(0) +
        dfBrindes['difal'].fillna(0))

    dfBrindes['custo_final'] = (
        dfBrindes['custo_unitario_total'].fillna(0) +
        dfBrindes['total_impostos'].fillna(0))

    # Retorna o DataFrame
    return dfBrindes

# ====================================================================================
# BLOCO DE ANÁLISE: Executado apenas se o arquivo for rodado diretamente
# ====================================================================================


if __name__ == '__main__':

    # Carrega o DataFrame através da função
    dfBrindes = get_py_fBrinde()

# ========================================= EXIBIR TOP 5 SKU'S COM MAIOR CUSTO =================================================

    # ---------------------------------------------------- Análise Mensal ------------------------------------------------------

    # Variável de controle para as análises mensais
    meses = sorted(dfBrindes['mes'].dropna().unique())

    # Dicionário para armazenar os resultados mensais
    dados_mensais_sku = {}

    print('='*120)
    print('🏆 TOP 5 SKUs COM MAIORES CUSTOS NO MÊS')

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]

        # Nome do mês correto
        nome_mes = df_mes['nome_mes'].iloc[0]

        # Soma a coluna custos de acordo com o mês sendo analisado
        total_custo_mes = df_mes['custo_unitario_total'].sum()

        # Soma a coluna custos de acordo com o SKU e o mês sendo analisado
        total_custo_sku = df_mes.groupby(['cod_sku', 'descricao_sku'])[
            ['custo_unitario_total']].sum()

        # Cria a coluna AV (Total por SKU / Total geral no mês em análise)
        total_custo_sku['(%) S/Custo mensal'] = (
            total_custo_sku['custo_unitario_total'] / total_custo_mes) * 100

        # Insere os dados na lista
        dados_mensais_sku[mes] = total_custo_sku

        # Seleciona os 5 maiores custos
        top_custo_mes = total_custo_sku.sort_values(
            by='custo_unitario_total', ascending=False).head(5).round(1)

        # Exibição dos dados
        print(f'\n📅 Mês: {nome_mes}')
        print(top_custo_mes[['(%) S/Custo mensal']])
        print("\n")

    # ---------------------------------------- Análise Geral -------------------------------------------

    # Soma a coluna custos de acordo com o SKU e o mês sendo analisado
    total_custo_sku = dfBrindes.groupby(['cod_sku', 'descricao_sku'])[
        ['custo_unitario_total']].sum()

    # Soma a coluna custos do dfBrindes
    total_custo = dfBrindes['custo_unitario_total'].sum()

    # Cria a coluna AV (Total por SKU / Total geral)
    total_custo_sku['(%) S/Custo total'] = (
        total_custo_sku['custo_unitario_total'] / total_custo) * 100

    # Seleciona os 5 maiores SKU
    top_custo_total = total_custo_sku.sort_values(
        by='custo_unitario_total', ascending=False).head(5).round(1)

    # Exibição dos dado
    print('='*120)
    print('🏆 TOP 5 SKUs COM MAIORES CUSTOS TOTAL')
    print('='*120 + "\n")
    print(top_custo_total[['(%) S/Custo total']])
    print("\n" + "="*120 + "\n")
