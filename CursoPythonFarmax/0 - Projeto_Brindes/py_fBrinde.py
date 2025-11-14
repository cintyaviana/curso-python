
# ==========================================================
# IMPORTAÇÃO DOS RECURSOS
# ==========================================================

# Biblioteca para trabalhar com caminhos de arquivos. Permite manipulação de caminhos de forma orientada a objetos.
from pathlib import Path

# Biblioteca oferece estruturas de dados flexíveis (como DataFrame e Series) e ferramentas para manipulação, limpeza e análise de dados tabulares.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    # =============================== EXIBIR TOP 5 CENTROS DE CUSTOS COM MAIOR CUSTO COM BRINDES ======================================

    # ---------------------------------------------------- Análise Mensal ------------------------------------------------------

    # Dicionário para armazenar os resultados mensais
    dados_mensais_cc = {}

    print('='*120)
    print('🏆 TOP 5 CC COM MAIORES CUSTOS NO MÊS')

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]

        # Nome do mês correto
        nome_mes = df_mes['nome_mes'].iloc[0]

        # Soma a coluna custos de acordo com o mês sendo analisado
        total_custo_mes = df_mes['custo_unitario_total'].sum()

        # Soma a coluna custos de acordo com o SKU e o mês sendo analisado
        total_custo_cc = df_mes.groupby(['centro_custo'])[
            ['custo_unitario_total']].sum()

        # Cria a coluna AV (Total por SKU / Total geral no mês em análise)
        total_custo_cc['(%) S/Custo mensal'] = (
            total_custo_cc['custo_unitario_total'] / total_custo_mes) * 100

        # Insere os dados na lista
        dados_mensais_cc[mes] = total_custo_cc

        # Seleciona os 5 maiores custos
        top_custo_mes = total_custo_cc.sort_values(
            by='custo_unitario_total', ascending=False).head(5).round(1)

        # Exibição dos dados
        print(f'\n📅 Mês: {nome_mes}')
        print(top_custo_mes[['(%) S/Custo mensal']])
        print("\n")

    # ---------------------------------------- Análise Geral -------------------------------------------

    # Soma a coluna custos de acordo com o SKU e o mês sendo analisado
    total_custo_cc = dfBrindes.groupby(['centro_custo'])[
        ['custo_unitario_total']].sum()

    # Soma a coluna custos do dfBrindes
    total_custo = dfBrindes['custo_unitario_total'].sum()

    # Cria a coluna AV (Total por SKU / Total geral)
    total_custo_cc['(%) S/Custo total'] = (
        total_custo_cc['custo_unitario_total'] / total_custo) * 100

    # Seleciona os 5 maiores SKU
    top_custo_total = total_custo_cc.sort_values(
        by='custo_unitario_total', ascending=False).head(5).round(1)

    # Exibição dos dado
    print('='*120)
    print('🏆 TOP 5 CC COM MAIORES CUSTOS DE BRINDES TOTAL')
    print('='*120 + "\n")
    print(top_custo_total[['(%) S/Custo total']])
    print("\n" + "="*120 + "\n")

    # ==================================== EXIBIR TOP 5 CLIENTES COM MAIOR CUSTO COM BRINDES ========================================

    # ---------------------------------------------------- Análise Mensal ------------------------------------------------------

    # Variável de controle para as análises mensais
    meses = sorted(dfBrindes['mes'].dropna().unique())

    # Dicionário para armazenar os resultados mensais
    dados_mensais_cliente = {}

    print('='*120)
    print('🏆 TOP 5 CLIENTES COM MAIOR CUSTO NO MÊS COM BRINDES')

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        df_mes = dfBrindes[dfBrindes['mes'] == mes]

        # Nome do mês correto
        nome_mes = df_mes['nome_mes'].iloc[0]

        # Soma a coluna custos de acordo com o mês sendo analisado
        total_custo_mes = df_mes['custo_unitario_total'].sum()

        # Soma a coluna custos de acordo com o SKU e o mês sendo analisado
        total_custo_cliente = df_mes.groupby(['cod_cliente', 'descricao_cliente'])[
            ['custo_unitario_total']].sum()

        # Cria a coluna AV (Total por SKU / Total geral no mês em análise)
        total_custo_cliente['(%) S/Custo mensal'] = (
            total_custo_cliente['custo_unitario_total'] / total_custo_mes) * 100

        # Insere os dados na lista
        dados_mensais_cliente[mes] = total_custo_cliente

        # Seleciona os 5 maiores custos
        top_custo_mes = total_custo_cliente.sort_values(
            by='custo_unitario_total', ascending=False).head(5).round(1)

        # Exibição dos dados
        print(f'\n📅 Mês: {nome_mes}')
        print(top_custo_mes[['(%) S/Custo mensal']])
        print("\n")

    # ---------------------------------------- Análise Geral -------------------------------------------

    # Soma a coluna custos de acordo com o SKU e o mês sendo analisado
    total_custo_cliente = dfBrindes.groupby(['cod_cliente', 'descricao_cliente'])[
        ['custo_unitario_total']].sum()

    # Soma a coluna custos do dfBrindes
    total_custo = dfBrindes['custo_unitario_total'].sum()

    # Cria a coluna AV (Total por SKU / Total geral)
    total_custo_cliente['(%) S/Custo total'] = (
        total_custo_cliente['custo_unitario_total'] / total_custo) * 100

    # Seleciona os 5 maiores SKU
    top_custo_total = total_custo_cliente.sort_values(
        by='custo_unitario_total', ascending=False).head(5).round(1)

    # Exibição dos dado
    print('='*120)
    print('🏆 TOP 5 CLIENTES COM MAIOR CUSTO TOTAL COM BRINDES')
    print('='*120 + "\n")
    print(top_custo_total[['(%) S/Custo total']])

    # ========================================= CURVA ABC: estado vs. custo_final ========================================

    print('='*120)
    print('📈 ANÁLISE DA CURVA ABC: estado vs. custo_final')
    print('='*120)

    # 1. Agregação do custo_final por estado
    df_abc_final = dfBrindes.groupby('estado').agg(
        total_valor=('custo_final', 'sum')
    ).reset_index()

    # 2. Ordenação (do maior para o menor custo)
    df_abc_final = df_abc_final.sort_values(
        by='total_valor',
        ascending=False
    ).reset_index(drop=True)

    # 3. Cálculo da Participação Relativa e Acumulada
    total_geral = df_abc_final['total_valor'].sum()
    df_abc_final['participacao_relativa_%'] = (
        df_abc_final['total_valor'] / total_geral
    ) * 100
    df_abc_final['participacao_acumulada_%'] = (
        df_abc_final['participacao_relativa_%'].cumsum()
    )

    # 4. Classificação ABC (80/15/5)

    # Usando np.select para classificação direta
    # É necessário que o 'numpy as np' esteja importado no cabeçalho do seu script.
    condicoes = [
        df_abc_final['participacao_acumulada_%'] <= 80,
        df_abc_final['participacao_acumulada_%'] <= 95
    ]
    escolhas = ['A', 'B']
    df_abc_final['classe_abc'] = np.select(condicoes, escolhas, default='C')

    # 5. Resumo da Classificação (Título 2 ajustado para 5)
    resumo_abc = df_abc_final.groupby('classe_abc').agg(
        num_estados=('estado', 'count'),  # Corrigido para contar 'estado'
        total_custo=('total_valor', 'sum'),
        participacao_custo=('participacao_relativa_%', 'sum')
    ).round(2).sort_values(by='participacao_custo', ascending=False)

    # Cálculo da porcentagem de Estados
    total_estados = resumo_abc['num_estados'].sum()
    resumo_abc['(%) S/Total Estados'] = (
        # AQUI FOI CORRIGIDO: de 'num_skus' para 'num_estados'
        resumo_abc['num_estados'] / total_estados
    ) * 100

    resumo_abc = resumo_abc.rename(columns={
        'num_estados': 'Qtd. Estados',
        'total_custo': 'Custo Total (R$)',
        'participacao_custo': '(%) Custo Total'
    })

    print("\n### Resumo da Classificação")
    print(resumo_abc[['Qtd. Estados', '(%) S/Total Estados',  # Corrigido o nome da coluna de exibição
          'Custo Total (R$)', '(%) Custo Total']])

    print("\n" + "="*120)

    # ========================================= PLOTAGEM (APENAS CLASSE A) - COMPOSIÇÃO DE CUSTO EMPILHADA COM NOVAS CORES ========================================

    print('\n📊 Gerando Gráfico Empilhado: Composição do Custo Final nos Estados Classe A (Novas Cores)...')

    # 1. Filtrar apenas a Classe A e o DataFrame original para agrupar as colunas de custo
    estados_classe_a = df_abc_final[df_abc_final['classe_abc']
                                    == 'A']['estado'].tolist()

    # Filtrar o DataFrame original para incluir apenas os estados da Classe A
    df_classe_a_detalhe = dfBrindes[dfBrindes['estado'].isin(estados_classe_a)]

    # 2. Agrupar os componentes do custo por estado (apenas Classe A)
    df_composicao = df_classe_a_detalhe.groupby('estado').agg({
        'custo_unitario_total': 'sum',
        'valor_icms': 'sum',
        'valor_icms_st': 'sum',
        'difal': 'sum'
        # Mantém a ordem decrescente de custo
    }).sort_values(by='custo_unitario_total', ascending=False)

    # 3. Preparar os dados para o plot
    estados = df_composicao.index
    custo_base = df_composicao['custo_unitario_total']
    icms = df_composicao['valor_icms']
    icms_st = df_composicao['valor_icms_st']
    difal = df_composicao['difal']

    # Calcular o valor total de cada barra para os rótulos
    total_custo = custo_base + icms + icms_st + difal

    # Definição das novas cores
    COR_AZUL_ESCURO = '#003366'
    COR_AZUL_CLARO = '#66A3D2'
    COR_VERDE_ESCURO = '#006400'
    COR_VERDE_CLARO = '#66CDAA'

    # 4. Criar a figura e os eixos
    plt.figure(figsize=(12, 7))

    # 5. Plotar o gráfico de barras empilhadas com as novas cores
    # Custo Unitário Total (Azul Escuro)
    p1 = plt.bar(estados, custo_base, color=COR_AZUL_ESCURO,
                 label='Custo Unitário Total')
    # Valor ICMS (Azul Claro)
    p2 = plt.bar(estados, icms, bottom=custo_base,
                 color=COR_AZUL_CLARO, label='Valor ICMS')
    # Valor ICMS ST (Verde Escuro)
    p3 = plt.bar(estados, icms_st, bottom=custo_base + icms,
                 color=COR_VERDE_ESCURO, label='Valor ICMS ST')
    # DIFAL (Verde Claro)
    p4 = plt.bar(estados, difal, bottom=custo_base + icms +
                 icms_st, color=COR_VERDE_CLARO, label='DIFAL')

    # 6. Adicionar Títulos e Rótulos
    plt.title('Composição do Custo Final nos Estados da Classe A', fontsize=16)
    plt.xlabel('Estado', fontsize=12)
    plt.ylabel('Custo Final Total (R$)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 7. Adicionar rótulos de dados (Valor Total da Barra)
    for i, total in enumerate(total_custo):
        plt.text(i, total + (total * 0.01),  # Posição no topo da barra
                 f'R${total:,.0f}',  # Formato R$ sem decimais
                 ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Adicionar legenda
    plt.legend()

    plt.tight_layout()
    plt.show()

    print("\n" + "="*120 + "\n")


# ========================================= CURVA ABC: centro_custo vs. custo_final ========================================

    print('\n' + '='*120)
    print('📈 ANÁLISE DA CURVA ABC: centro_custo vs. custo_final')
    print('='*120)

    # 1. Agregação do custo_final por centro_custo
    df_abc_cc = dfBrindes.groupby('centro_custo').agg(
        total_valor=('custo_final', 'sum')
    ).reset_index()

    # 2. Ordenação (do maior para o menor custo)
    df_abc_cc = df_abc_cc.sort_values(
        by='total_valor',
        ascending=False
    ).reset_index(drop=True)

    # 3. Cálculo da Participação Relativa e Acumulada
    total_geral_cc = df_abc_cc['total_valor'].sum()
    df_abc_cc['participacao_relativa_%'] = (
        df_abc_cc['total_valor'] / total_geral_cc
    ) * 100
    df_abc_cc['participacao_acumulada_%'] = (
        df_abc_cc['participacao_relativa_%'].cumsum()
    )

    # 4. Classificação ABC (80/15/5)
    condicoes_cc = [
        df_abc_cc['participacao_acumulada_%'] <= 80,
        df_abc_cc['participacao_acumulada_%'] <= 95
    ]
    escolhas = ['A', 'B']
    df_abc_cc['classe_abc'] = np.select(condicoes_cc, escolhas, default='C')

    # 5. Resumo da Classificação
    resumo_abc_cc = df_abc_cc.groupby('classe_abc').agg(
        num_ccs=('centro_custo', 'count'),
        total_custo=('total_valor', 'sum'),
        participacao_custo=('participacao_relativa_%', 'sum')
    ).round(2).sort_values(by='participacao_custo', ascending=False)

    # Cálculo da porcentagem de Centros de Custo
    total_ccs = resumo_abc_cc['num_ccs'].sum()
    resumo_abc_cc['(%) S/Total CCs'] = (
        resumo_abc_cc['num_ccs'] / total_ccs
    ) * 100

    resumo_abc_cc = resumo_abc_cc.rename(columns={
        'num_ccs': 'Qtd. Centros Custo',
        'total_custo': 'Custo Total (R$)',
        'participacao_custo': '(%) Custo Total'
    })

    print("\n### Resumo da Classificação")
    print(resumo_abc_cc[['Qtd. Centros Custo', '(%) S/Total CCs',
          'Custo Total (R$)', '(%) Custo Total']])

    print("\n" + "="*120)

# ========================================= CURVA ABC: centro_custo vs. custo_final ========================================

    print('\n' + '='*120)
    print('📈 ANÁLISE DA CURVA ABC: centro_custo vs. custo_final')
    print('='*120)

    # 1. Agregação do custo_final por centro_custo
    df_abc_cc = dfBrindes.groupby('centro_custo').agg(
        total_valor=('custo_final', 'sum')
    ).reset_index()

    # 2. Ordenação (do maior para o menor custo)
    df_abc_cc = df_abc_cc.sort_values(
        by='total_valor',
        ascending=False
    ).reset_index(drop=True)

    # 3. Cálculo da Participação Relativa e Acumulada
    total_geral_cc = df_abc_cc['total_valor'].sum()
    df_abc_cc['participacao_relativa_%'] = (
        df_abc_cc['total_valor'] / total_geral_cc
    ) * 100
    df_abc_cc['participacao_acumulada_%'] = (
        df_abc_cc['participacao_relativa_%'].cumsum()
    )

    # 4. Classificação ABC (80/15/5)
    condicoes_cc = [
        df_abc_cc['participacao_acumulada_%'] <= 80,
        df_abc_cc['participacao_acumulada_%'] <= 95
    ]
    escolhas = ['A', 'B']
    df_abc_cc['classe_abc'] = np.select(condicoes_cc, escolhas, default='C')

    # 5. Resumo da Classificação
    resumo_abc_cc = df_abc_cc.groupby('classe_abc').agg(
        num_ccs=('centro_custo', 'count'),
        total_custo=('total_valor', 'sum'),
        participacao_custo=('participacao_relativa_%', 'sum')
    ).round(2).sort_values(by='participacao_custo', ascending=False)

    # Cálculo da porcentagem de Centros de Custo
    total_ccs = resumo_abc_cc['num_ccs'].sum()
    resumo_abc_cc['(%) S/Total CCs'] = (
        resumo_abc_cc['num_ccs'] / total_ccs
    ) * 100

    resumo_abc_cc = resumo_abc_cc.rename(columns={
        'num_ccs': 'Qtd. Centros Custo',
        'total_custo': 'Custo Total (R$)',
        'participacao_custo': '(%) Custo Total'
    })

    print("\n### Resumo da Classificação")
    print(resumo_abc_cc[['Qtd. Centros Custo', '(%) S/Total CCs',
          'Custo Total (R$)', '(%) Custo Total']])

    print("\n" + "="*120)

# ========================================= PLOTAGEM (APENAS CLASSE A) - COMPOSIÇÃO DE CUSTO EMPILHADA ========================================

    print('\n📊 Gerando Gráfico Empilhado: Composição do Custo Final nos Centros de Custo Classe A...')

    # 6. Filtrar apenas a Classe A
    ccs_classe_a = df_abc_cc[df_abc_cc['classe_abc']
                             == 'A']['centro_custo'].tolist()

    # Filtrar o DataFrame original para incluir apenas os centros de custo da Classe A
    df_classe_a_detalhe_cc = dfBrindes[dfBrindes['centro_custo'].isin(
        ccs_classe_a)]

    # 7. Agrupar os componentes do custo por centro_custo (apenas Classe A)
    df_composicao_cc = df_classe_a_detalhe_cc.groupby('centro_custo').agg({
        'custo_unitario_total': 'sum',
        'valor_icms': 'sum',
        'valor_icms_st': 'sum',
        'difal': 'sum'
    }).sort_values(by='custo_unitario_total', ascending=False)

    # 8. Preparar os dados para o plot
    centros_custo = df_composicao_cc.index
    custo_base = df_composicao_cc['custo_unitario_total']
    icms = df_composicao_cc['valor_icms']
    icms_st = df_composicao_cc['valor_icms_st']
    difal = df_composicao_cc['difal']

    # Calcular o valor total de cada barra para os rótulos
    total_custo_cc = custo_base + icms + icms_st + difal

    # Cores (Mantendo a paleta de azul e verde)
    COR_AZUL_ESCURO = '#003366'
    COR_AZUL_CLARO = '#66A3D2'
    COR_VERDE_ESCURO = '#006400'
    COR_VERDE_CLARO = '#66CDAA'

    # 9. Criar a figura e os eixos
    plt.figure(figsize=(12, 7))

    # 10. Plotar o gráfico de barras empilhadas
    p1 = plt.bar(centros_custo, custo_base, color=COR_AZUL_ESCURO,
                 label='Custo Unitário Total')
    p2 = plt.bar(centros_custo, icms, bottom=custo_base,
                 color=COR_AZUL_CLARO, label='Valor ICMS')
    p3 = plt.bar(centros_custo, icms_st, bottom=custo_base + icms,
                 color=COR_VERDE_ESCURO, label='Valor ICMS ST')
    p4 = plt.bar(centros_custo, difal, bottom=custo_base + icms +
                 icms_st, color=COR_VERDE_CLARO, label='DIFAL')

    # 11. Adicionar Títulos e Rótulos
    plt.title(
        'Composição do Custo Final nos Centros de Custo da Classe A', fontsize=16)
    plt.xlabel('Centro de Custo', fontsize=12)
    plt.ylabel('Custo Final Total (R$)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 12. Adicionar rótulos de dados (Valor Total da Barra)
    for i, total in enumerate(total_custo_cc):
        plt.text(i, total + (total * 0.01),
                 f'R${total:,.0f}',
                 ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Adicionar legenda
    plt.legend()

    plt.tight_layout()
    plt.show()

    print("\n" + "="*120 + "\n")
