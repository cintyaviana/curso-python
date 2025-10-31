# ==========================================================
# IMPORTAÇÃO DOS RECURSOS
# ==========================================================

from pathlib import Path
import pandas as pd

# Carrega o DataFrame de impostos, calcula a coluna 'impostos_total' e consolida os dados por nota fiscal e SKU.


def get_fato_impostos():

    # Retorna o caminho de onde estão os arquivos do projeto
    dataPath = Path(__file__).resolve().parent

    # Carregar os dados
    dfImpostos = pd.read_excel(dataPath / 'fImpostos.xlsx')

    # Cria a coluna de impostos total somando os componentes
    dfImpostos['impostos_total'] = (
        dfImpostos['valor_icms'] +
        dfImpostos['valor_icms_st'] +
        dfImpostos['valor_fcp_st'] +
        dfImpostos['icms_interestadual_uf_destino'] +
        dfImpostos['valor_icms_fcp_uf_destino'] +
        dfImpostos['valor_pis'] +
        dfImpostos['valor_cofins']
    )

    # Converte para o Período Mensal (01/mês/ano)
    dfImpostos['data'] = dfImpostos['data'].dt.to_period('M').dt.to_timestamp()

    # Criar uma coluna com o número do mês
    dfImpostos['mes'] = dfImpostos['data'].dt.month

    # Agrupa pela Nota Fiscal para consolidar os impostos
    dfImpostos_consolidado = (
        dfImpostos
        # Estado também é chave de imposto
        .groupby(['nota_fiscal', 'cod_sku', 'estado'])
        .agg(
            impostos_total=('impostos_total', 'sum'),
            # <--- Incluído para o gráfico de composição
            valor_icms=('valor_icms', 'sum'),
            # <--- Incluído para o gráfico de composição
            valor_pis=('valor_pis', 'sum'),
            # <--- Incluído para o gráfico de composição
            valor_cofins=('valor_cofins', 'sum'),
            # Se a base tiver alíquotas, você pode trazê-las aqui com 'first' ou 'mean'
            # aliq_icms=('aliq_icms', 'first'),
        )
        .reset_index()
    )

    # Retorna o DataFrame
    return dfImpostos

# ====================================================================================
# BLOCO DE ANÁLISE (Executado apenas se o arquivo for rodado diretamente)
# ====================================================================================


if __name__ == '__main__':
    # Carrega o DataFrame através da função
    dfImpostos = get_fato_impostos()

    # Exibir um determinado intervalo dos dados a partir do método head: primeiras linhas e o método tail: últimas linhas.
    print('='*120)
    print('🔗 Primeiras 5 linhas do dfImpostos')
    print('='*120 + "\n")
    print(dfImpostos.head(5))
    print("\n")

    print('='*120)
    print('🔗 Últimas 5 linhas do dfImpostos')
    print('='*120 + "\n")
    print(dfImpostos.tail(5))
    print("\n")

    # Exibir os nomes das colunas e o tipo dos dados
    print('='*120)
    print('🔗 Nome das colunas do dfImpostos')
    print('='*120 + "\n")
    print('Colunas: ', dfImpostos.dtypes)
    print("\n")

    # Exibir o resumo estatístico
    print('='*120)
    print('🔗 Resumo estatístico do dfImpostos')
    print('='*120 + "\n")
    print(dfImpostos.describe())
    print("\n")

    # ==============================================================================
    # ANÁLISE DE CORRELAÇÃO: Componentes (impostos) vs. Imposto Total
    # ==============================================================================
    print('='*120)
    print('🔗 Correlação dos Componentes (impostos) com o Imposto Total')
    print('='*120 + "\n")

    componentes_imposto = [
        'valor_icms',
        'valor_icms_st',
        'valor_fcp_st',
        'icms_interestadual_uf_destino',
        'valor_icms_fcp_uf_destino',
        'valor_pis',
        'valor_cofins'
    ]

    # Selecionar as colunas para o cálculo da correlação
    impostos_corr = componentes_imposto + ['impostos_total']

    # Garantir que só estamos correlacionando colunas numéricas válidas
    df_impostos_corr = dfImpostos[impostos_corr].dropna()

    # Calcular a correlação da matriz completa
    matriz_impostos_corr = df_impostos_corr.corr()

    # Selecionar apenas a correlação dos componentes com 'impostos_total'
    impostos_corr_total = matriz_impostos_corr['impostos_total'].drop(
        'impostos_total')

    # Ordenar para ver qual é o mais correlacionado
    impostos_corr_ordenada = impostos_corr_total.sort_values(
        ascending=False).round(4)

    # Exibição dos dados
    print('Correlação de cada componente (impostos) com o "impostos_total":')
    print(impostos_corr_ordenada)
    print("\n")

    # ==============================================================================
    # ANÁLISE DE ASSOCIAÇÃO: Alíquotas por Estado
    # ==============================================================================

    print('='*120)
    print('🔗 Análise de Alíquotas e Valores Médios por Estado')
    print('='*120 + "\n")

    # Definindo os nomes das colunas de interesse
    COLUNAS_ALIQUOTAS = [
        'aliq_icms',
        'aliq_pis',
        'aliq_cofins'
    ]

    # Agrupar os dados pela coluna 'estado' e calcula as médias
    analise_por_estado = dfImpostos.groupby('estado').agg(
        # Médias das Alíquotas Individuais
        media_aliq_icms=('aliq_icms', 'mean'),
        media_aliq_pis=('aliq_pis', 'mean'),
        media_aliq_cofins=('aliq_cofins', 'mean'),
        media_valor_unitario=('valor_unitario', 'mean'),
        media_valor_bruto=('valor_bruto', 'mean'),
        media_imposto_total=('impostos_total', 'mean')
    )

    # Calcular a média das 3 alíquotas (icms, pis, cofins) por estado
    analise_por_estado['media_aliquotas'] = analise_por_estado[[
        'media_aliq_icms',
        'media_aliq_pis',
        'media_aliq_cofins'
    ]].mean(axis=1)

    # Ordenar a análise pela média das alíquotas
    analise_ordenada = analise_por_estado.sort_values(
        by='media_aliquotas', ascending=False).round(1)

    # Exibição dos dados
    print('Médias (Individuais e Agregada) e Valores por Estado (ordenado pela Média das Alíquotas):')
    print(analise_ordenada)
    print('-'*100)
