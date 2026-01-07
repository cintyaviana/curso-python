
# ====================================================================================
# IMPORTAÇÃO DOS RECURSOS
# ====================================================================================

from pathlib import Path
import pandas as pd
import numpy as np

# Biblioteca que personaliza a forma como os valores aparecem no eixo do seu gráfico para que ele seja mais claro, como formatar para dinheiro, porcentagem ou usar notação científica.
import matplotlib.ticker as mtick

# Biblioteca oferece estruturas de criação de visualizações estáticas, interativas e animadas em 2D, e até mesmo algumas em 3D.
import matplotlib.pyplot as plt

# Biblioteca que fornece módulos de álgebra linear, integração, interpolação, e, estatística.chi2_contingency. Ela é usada para realizar o Teste Qui-Quadrado de Independência (Chi-Square Test) que é usado para determinar se existe uma relação estatisticamente significativa entre duas variáveis categóricas.
from scipy.stats import chi2_contingency

# ====================================================================================
# CRIAÇÃO DA FUNÇÃO QUE GERA O DF
# ====================================================================================


def get_fBrinde():

    dataPath = Path(__file__).resolve().parent

    dfBrindes = pd.read_excel(dataPath / 'Ex_fBrindes_Impostos.xlsx')

    # Converte para o Período Mensal (01/mês/ano)
    dfBrindes['data'] = dfBrindes['data'].dt.to_period('M').dt.to_timestamp()

    """
    .dt: É o acessor do Pandas para DateTime (data e hora). Ele permite aplicar métodos específicos de manipulação de data/hora aos valores da coluna.

    .to_period('M'): transforma a coluna de um formato de Timestamp (data e hora exata, ex: 2025-01-15 14:30:00) para um formato (Período).

        O argumento 'M' indica que o período deve ser Mensal. Resultado desta etapa: A data 2025-01-15 14:30:00 se torna o período 2025-01.

    .to_timestamp(): Após a conversão para Período, esta função converte o Período de volta para o formato Timestamp.

        A Regra Chave: Ao converter um Período Mensal de volta para um Timestamp, o Pandas define o início desse período como a nova data.

        Resultado Final: O período 2025-01 é transformado na data exata 2025-01-01 00:00:00
    """
    # Criar a coluna (mes) com o número do mês
    # .month: extrai o número inteiro correspondente ao mês
    dfBrindes['mes'] = dfBrindes['data'].dt.month

    # Cria a coluna (nome_mes)
    dfBrindes['nome_mes'] = dfBrindes['data'].dt.month_name(
        locale='pt_BR').str.capitalize()
    """
    .month_name(...): É a função que extrai o nome completo do mês (ex: "janeiro" em vez de "1").

    locale='pt_BR': Ele garante que o nome do mês seja retornado no idioma Português do Brasil ("Janeiro", "Fevereiro", etc.), e não no padrão americano ("January", "February").

    .str: É o acessor de string (texto) do Pandas. Ele é usado porque o resultado da etapa anterior é uma série de (texto).

    .capitalize(): Converte a primeira letra de cada nome em maiúscula e todas as demais em minúscula.

    """
    # Cria a coluna (total_impostos)
    # .fillna: preenche valores ausentes ou nulos (NaN) com zero.
    dfBrindes['total_impostos'] = (
        dfBrindes['valor_icms'].fillna(0) +
        dfBrindes['valor_icms_st'].fillna(0) +
        dfBrindes['icms_interestadual_uf_destino'].fillna(0) +
        dfBrindes['valor_icms_fcp_uf_destino'].fillna(0))

    # Cria a coluna (custo_final)
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
    dfBrindes = get_fBrinde()

    # ---------------------------------------------------------------------------------
    # TOP 5 SKU'S COM MAIOR CUSTO
    # ---------------------------------------------------------------------------------
    # Análise Mensal -----------------------------------------------------------------=

    print('='*120)
    print('TOP 5 SKUs COM MAIOR CUSTO NO MÊS')
    print('='*120)

    # Variável de controle para as análises mensais
    meses = sorted(dfBrindes['mes'].unique())

    """
    .unique(): Este método retorna um array NumPy contendo apenas os valores distintos (únicos).

    sorted(): Ordena a lista

    """

    # Dicionário para armazenar os resultados mensais
    dados_mensais_sku = {}

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        # Cria um novo df, apenas com os dados cujo valor na coluna 'mes' é igual ao mês do loop.
        df_mes = dfBrindes[dfBrindes['mes'] == mes]

        # Retorna o nome do mês da nova df_mes
        nome_mes = df_mes['nome_mes'].iloc[0]
        # iloc[0]: indica que você quer o item que está na posição zero (o primeiro item) da Série.

        # Soma a coluna custo total
        total_custo_mes = df_mes['custo_unitario_total'].sum()

        # Soma a coluna custos total de acordo com o SKU gerando um novo df onde cada linha mostra o custo total acumulado para o SKU.
        total_custo_sku = df_mes.groupby(['cod_sku', 'descricao_sku'])[
            ['custo_unitario_total']].sum()

        # Cria a coluna AV (Total por SKU / Total geral)
        total_custo_sku['(%) S/Custo mensal'] = (
            total_custo_sku['custo_unitario_total'] / total_custo_mes) * 100

        # Insere os dados na lista usando o número do mês como chave. Isso permite acessar esses dados para o mês 1, 2..., posteriormente.
        dados_mensais_sku[mes] = total_custo_sku

        # Seleciona os 5 maiores custos
        top_custo_mes = total_custo_sku.sort_values(
            by='custo_unitario_total', ascending=False).head(5).round(1)

        # Exibição dos dados
        print(f'\n📅 Mês: {nome_mes}')
        print(top_custo_mes[['(%) S/Custo mensal']])
        print("\n")

    # ---------------------------------------------------------------------------------
    # Análise Geral -------------------------------------------------------------------
    # Soma a coluna custos total de acordo com o SKU gerando um novo df onde cada linha mostra o custo total acumulado para o SKU.
    total_custo_sku = dfBrindes.groupby(['cod_sku', 'descricao_sku'])[
        ['custo_unitario_total']].sum()

    # Soma a coluna custos total QUE SERÁ USADO PARA AS DEMAIS ANÁLISES GERAIS DE CC E CLIENTE.
    total_custo = dfBrindes['custo_unitario_total'].sum()

    # Cria a coluna AV (Total por SKU / Total geral)
    total_custo_sku['(%) S/Custo total'] = (
        total_custo_sku['custo_unitario_total'] / total_custo) * 100

    # Seleciona os 5 maiores SKU
    top_custo_total = total_custo_sku.sort_values(
        by='custo_unitario_total', ascending=False).head(5).round(1)

    # Exibição dos dado
    print('='*120)
    print('TOP 5 SKUs COM MAIOR CUSTO GERAL')
    print('='*120 + "\n")
    print(top_custo_total[['(%) S/Custo total']])
    print("\n" + "="*120 + "\n")

    # ---------------------------------------------------------------------------------
    # TOP 5 CENTROS DE CUSTOS COM MAIOR CUSTO
    # ---------------------------------------------------------------------------------
    # Análise Mensal ------------------------------------------------------------------
    # Dicionário para armazenar os resultados mensais

    print('='*120)
    print('TOP 5 CENTRO DE CUSTO COM MAIOR CUSTO NO MÊS')
    print('='*120)

    dados_mensais_cc = {}

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        # Cria um novo df, apenas com os dados cujo valor na coluna 'mes' é igual ao mês do loop.
        df_mes = dfBrindes[dfBrindes['mes'] == mes]

        # Retorna o nome do mês da nova df_mes
        nome_mes = df_mes['nome_mes'].iloc[0]

        # Soma a coluna custos total
        total_custo_mes = df_mes['custo_unitario_total'].sum()

        # Soma a coluna custos total de acordo com o CC gerando um novo df onde cada linha mostra o custo total acumulado para o CC.
        total_custo_cc = df_mes.groupby(['centro_custo'])[
            ['custo_unitario_total']].sum()

        # Cria a coluna AV (Total por CC / Total geral)
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

    # ---------------------------------------------------------------------------------
    #  Análise Geral ------------------------------------------------------------------
    # Soma a coluna custos total de acordo com o CC gerando um novo df onde cada linha mostra o custo total acumulado para o CC.
    total_custo_cc = dfBrindes.groupby(['centro_custo'])[
        ['custo_unitario_total']].sum()

    # Cria a coluna AV (Total por CC / Total geral)
    total_custo_cc['(%) S/Custo total'] = (
        total_custo_cc['custo_unitario_total'] / total_custo) * 100

    # Seleciona os 5 maiores CC
    top_custo_total = total_custo_cc.sort_values(
        by='custo_unitario_total', ascending=False).head(5).round(1)

    # Exibição dos dado
    print('='*120)
    print('TOP 5 CENTRO DE CUSTO COM MAIOR CUSTO GERAL')
    print('='*120 + "\n")
    print(top_custo_total[['(%) S/Custo total']])
    print("\n" + "="*120 + "\n")

    # ---------------------------------------------------------------------------------
    # EXIBIR TOP 5 CLIENTES COM MAIOR CUSTO
    # ---------------------------------------------------------------------------------
    # Análise Mensal -----------------------------------------------------------------

    print('='*120)
    print('TOP 5 CLIENTES COM MAIOR CUSTO NO MÊS')
    print('='*120)

    # Dicionário para armazenar os resultados mensais
    dados_mensais_cliente = {}

    # Condição FOR que vai analisar os dados para cada mês
    for mes in meses:
        # Cria um novo df, apenas com os dados cujo valor na coluna 'mes' é igual ao mês do loop.
        df_mes = dfBrindes[dfBrindes['mes'] == mes]

        # Retorna o nome do mês da nova df_mes
        nome_mes = df_mes['nome_mes'].iloc[0]

        # Soma a coluna custos total
        total_custo_mes = df_mes['custo_unitario_total'].sum()

        # Soma a coluna custos total de acordo com o Cliente gerando um novo df onde cada linha mostra o custo total acumulado para o Cliente.
        total_custo_cliente = df_mes.groupby(['cod_cliente', 'descricao_cliente'])[
            ['custo_unitario_total']].sum()

        # Cria a coluna AV (Total por Cliente / Total geral)
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

    # ---------------------------------------------------------------------------------
    #  Análise Geral ------------------------------------------------------------------
    # Soma a coluna custos total de acordo com o Cliente gerando um novo df onde cada linha mostra o custo total acumulado para o Cliente.
    total_custo_cliente = dfBrindes.groupby(['cod_cliente', 'descricao_cliente'])[
        ['custo_unitario_total']].sum()

    # Cria a coluna AV (Total por Cliente / Total geral)
    total_custo_cliente['(%) S/Custo total'] = (
        total_custo_cliente['custo_unitario_total'] / total_custo) * 100

    # Seleciona os 5 maiores Clientes
    top_custo_total = total_custo_cliente.sort_values(
        by='custo_unitario_total', ascending=False).head(5).round(1)

    # Exibição dos dado
    print('='*120)
    print('TOP 5 CLIENTES COM MAIOR CUSTO GERAL')
    print('='*120 + "\n")
    print(top_custo_total[['(%) S/Custo total']])

    # ---------------------------------------------------------------------------------
    # MATRIZ DE CORRELAÇÃO DE CUSTOS
    # ---------------------------------------------------------------------------------
    # O objetivo é descobrir o quão forte e em que direção cada componente que forma o custo, está relacionado com o custo_final.
    print('\n' + '='*120)
    print('ANÁLISE DE CORRELAÇÃO: Custo Final')
    print('='*120)

    # Variável alvo (target).
    variavel_target = 'custo_final'

    # Determina as variáveis/colunas para análise da correlação.
    variaveis_componentes = [
        'custo_unitario_total',
        'valor_icms',
        'valor_icms_st',
        'icms_interestadual_uf_destino',
        'valor_icms_fcp_uf_destino']

    # Dicionário para armazenar os resultados da correlação.
    correlacoes = {}

    # Calcula a correlação de cada componente com o custo_final
    for var in variaveis_componentes:
        # O método .corr() calcula a correlação entre duas Series
        correlacao_valor = dfBrindes[var].corr(dfBrindes[variavel_target])
        correlacoes[var] = correlacao_valor

    # Converte o resultado para uma Series do Pandas para facilitar a visualização e ordenação
    df_correlacao_final = pd.Series(
        correlacoes).sort_values(ascending=False).round(2)

    # Exibe o resultado formatado
    print(f"\n Correlação com a Variável '{variavel_target}'")
    print("> Valores próximos de 1.0 indicam que a variável cresce junto com o custo_final.")
    print("> Valores próximos de 0.0 indicam pouca relação linear.")
    print(df_correlacao_final)
    print("\n" + "="*120 + "\n")

    # ---------------------------------------------------------------------------------
    # CURVA ABC: ESTADO vs CUSTO FINAL
    # ---------------------------------------------------------------------------------
    # Agregação do custo_final por estado
    df_abc_uf = (
        dfBrindes.groupby('estado').agg(total_valor=('custo_final', 'sum')).sort_values(
            by='total_valor', ascending=False).reset_index())

    """
    .agg(...): Este método aplica uma ou mais funções de agregação (como soma, média, contagem, máximo, etc.) a cada um dos grupos criados.

    total_valor: É o novo nome que você está dando à coluna de resultado.

    reset.index: Reinicialização do Índice

    """

    # Cálculo da Participação Relativa e Acumulada
    total_geral = df_abc_uf['total_valor'].sum()

    df_abc_uf['participacao_relativa_%'] = (
        df_abc_uf['total_valor'] / total_geral) * 100

    df_abc_uf['participacao_acumulada_%'] = (
        df_abc_uf['participacao_relativa_%'].cumsum())

    """
    .cumsum(): É um método do Pandas que calcula a soma acumulada dos valores da coluna anterior (participacao_relativa_%).
    
    O valor da primeira linha é somado ao valor da segunda linha. O resultado é somado ao valor da terceira linha, e assim por diante.

    Função: Como o DataFrame está ordenado, esta coluna informa qual percentual do custo total é coberto ao somar os estados mais importantes.

    Exemplo: Você pode descobrir que os 3 primeiros estados (os que têm maior custo) juntos representam 80% do seu custo total (a famosa Regra 80/20 da Análise ABC)

    """

    # Classificação ABC (80/15/5)
    condicoes = [
        df_abc_uf['participacao_acumulada_%'] <= 80,
        df_abc_uf['participacao_acumulada_%'] <= 95]
    escolhas = ['A', 'B']
    df_abc_uf['classe_abc'] = np.select(condicoes, escolhas, default='C')

    """
    df_abc_final['classe_abc']: Cria a nova coluna chamada classe_abc.

    np.select(...): A função do NumPy que aplica a lógica:

        Argumento 1 (condicoes): As regras (a lista de condições).

        Argumento 2 (escolhas): Os resultados se as regras forem verdadeiras.

        Argumento 3 (default='C'): O valor que será atribuído se nenhuma das condições for verdadeira.

    """

    # Resumo da Classificação
    resumo_abc_estado = df_abc_uf.groupby('classe_abc').agg(num_estados=('estado', 'count'), total_custo=('total_valor', 'sum'), participacao_custo=(
        'participacao_relativa_%', 'sum')).round(2).sort_values(by='participacao_custo', ascending=False)

    # Cálculo da porcentagem de Estados
    total_estados = resumo_abc_estado['num_estados'].sum()
    resumo_abc_estado['(%) S/Total Estados'] = (
        resumo_abc_estado['num_estados'] / total_estados * 100
    ).round(2)

    resumo_abc_estado = resumo_abc_estado.rename(columns={
        'num_estados': 'Qtd. Estados',
        'participacao_custo': '(%) Custo Total Estado'})

    # ---------------------------------------------------------------------------------
    # CURVA ABC: CENTRO CUSTO vs CUSTO FINAL
    # ---------------------------------------------------------------------------------
    # Agregação do custo_final por centro_custo
    df_abc_cc = dfBrindes.groupby('centro_custo').agg(total_valor=('custo_final', 'sum')).sort_values(
        by='total_valor', ascending=False).reset_index()

    # Cálculo da Participação Relativa e Acumulada
    total_geral_cc = df_abc_cc['total_valor'].sum()
    df_abc_cc['participacao_relativa_%'] = (
        df_abc_cc['total_valor'] / total_geral_cc
    ) * 100
    df_abc_cc['participacao_acumulada_%'] = (
        df_abc_cc['participacao_relativa_%'].cumsum()
    )

    # Classificação ABC (80/15/5)
    condicoes_cc = [
        df_abc_cc['participacao_acumulada_%'] <= 80,
        df_abc_cc['participacao_acumulada_%'] <= 95
    ]
    escolhas = ['A', 'B']
    df_abc_cc['classe_abc'] = np.select(condicoes_cc, escolhas, default='C')

    # Resumo da Classificação
    resumo_abc_cc = df_abc_cc.groupby('classe_abc').agg(
        num_ccs=('centro_custo', 'count'),
        total_custo=('total_valor', 'sum'),
        participacao_custo=('participacao_relativa_%', 'sum')
    ).round(2).sort_values(by='participacao_custo', ascending=False)

    # Cálculo da porcentagem de Centros de Custo
    total_ccs = resumo_abc_cc['num_ccs'].sum()
    resumo_abc_cc['(%) S/Total CCs'] = (
        resumo_abc_cc['num_ccs'] / total_ccs * 100
    ).round(2)

    resumo_abc_cc = resumo_abc_cc.rename(columns={
        'num_ccs': 'Qtd. Centros Custo',
        'participacao_custo': '(%) Custo Total CC'
    })

    # ---------------------------------------------------------------------------------
    #  PLOTAGEM ESTADO (APENAS CLASSE A)
    # ---------------------------------------------------------------------------------

    # Cores
    COR_AZUL_ESCURO = '#4E56C0'
    COR_ROXO_CLARO = '#9B5DE0'
    COR_ROSA_MEDIO = '#D78FEE'
    COR_ROSA_CLARO = '#FDCFFA'
    COR_ROXA = '#9112BC'

    # Filtrar apenas a Classe A e o DataFrame original.
    estados_classe_a = df_abc_uf[df_abc_uf['classe_abc']
                                 == 'A']['estado'].tolist()
    # .tolist(): converte a Series em uma lista.

    # Filtrar o DataFrame original para incluir apenas os estados da Classe A.
    df_classe_a_detalhe = dfBrindes[dfBrindes['estado'].isin(estados_classe_a)]
    # .isin(): Verifica, se o estado daquela linha (ex: 'SP') está presente na lista estados_classe_a.

    # Agrupar os componentes do custo por estado (apenas Classe A)
    df_composicao = df_classe_a_detalhe.groupby('estado').agg({
        'custo_unitario_total': 'sum',
        'valor_icms': 'sum',
        'valor_icms_st': 'sum',
        'icms_interestadual_uf_destino': 'sum',
        'valor_icms_fcp_uf_destino': 'sum'
    }).sort_values(by='custo_unitario_total', ascending=False)

    # Calcular o valor total de cada barra (Custo Final do Estado)
    total_custo = df_composicao.sum(axis=1)

    # Calcular o Custo Final Total de TODOS os dados (para o percentual do Eixo Y)
    custo_final_total_geral = dfBrindes['custo_final'].sum()

    # Criação das Bases Percentuais (Para PLOTAGEM)
    # Altura da Barra (Eixo Y): Percentual do Estado sobre o Total Geral
    df_percentual_estado = (total_custo / custo_final_total_geral) * 100

    # Componentes Percentuais (Para cálculo das fatias no Eixo Y e rótulos)
    df_percentual_base = (
        df_composicao['custo_unitario_total'] / total_custo) * 100
    df_percentual_icms = (df_composicao['valor_icms'] / total_custo) * 100
    df_percentual_icms_st = (
        df_composicao['valor_icms_st'] / total_custo) * 100
    df_percentual_icms_interestadual = (
        df_composicao['icms_interestadual_uf_destino'] / total_custo) * 100
    df_percentual_fcp = (
        df_composicao['valor_icms_fcp_uf_destino'] / total_custo) * 100

    # Componentes de PLOTAGEM (A altura de cada fatia no gráfico, proporcional ao total geral)
    plot_custo_base = df_percentual_estado * (df_percentual_base / 100)
    plot_icms = df_percentual_estado * (df_percentual_icms / 100)
    plot_icms_st = df_percentual_estado * (df_percentual_icms_st / 100)
    plot_icms_interestadual = df_percentual_estado * \
        (df_percentual_icms_interestadual / 100)
    plot_fcp = df_percentual_estado * (df_percentual_fcp / 100)

    # Preparar os dados para o plot
    estados = df_composicao.index

    # Acumuladores de altura para o bottom do plot (5 fatias)
    bottom_icms = plot_custo_base
    bottom_icms_st = bottom_icms + plot_icms
    bottom_icms_interestadual = bottom_icms_st + plot_icms_st
    bottom_fcp = bottom_icms_interestadual + plot_icms_interestadual

    # Criar a figura e os eixos
    plt.figure(figsize=(12, 7))

    # Plotar o gráfico de barras empilhadas (5 fatias)
    p1 = plt.bar(estados, plot_custo_base, color=COR_AZUL_ESCURO,
                 label='Custo')
    p2 = plt.bar(estados, plot_icms, bottom=bottom_icms,
                 color=COR_ROXO_CLARO, label='ICMS')
    p3 = plt.bar(estados, plot_icms_st, bottom=bottom_icms_st,
                 color=COR_ROSA_MEDIO, label='ICMS ST')
    p4 = plt.bar(estados, plot_icms_interestadual, bottom=bottom_icms_interestadual,
                 color=COR_ROSA_CLARO, label='ICMS Interestadual')
    p5 = plt.bar(estados, plot_fcp, bottom=bottom_fcp,
                 color=COR_ROXA, label='ICMS FCP')

    # Adicionar Títulos e Rótulos
    plt.title(
        'Composição (%) do Custo Final nos Estados da Classe A', fontsize=16)
    plt.xlabel('Estado', fontsize=12)
    plt.ylabel('(%) S/ Custo Final', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 100)

    # Rótulos no TOPO DA BARRA (Percentual do Estado sobre o Total Geral)
    for i, total_percentual in enumerate(df_percentual_estado):
        plt.text(i, total_percentual + (total_percentual * 0.01),
                 f'{total_percentual:.1f}%',
                 ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Adicionar legenda
    plt.legend(
        loc='upper left',
        bbox_to_anchor=(0, 1),
        frameon=False)

    # ---------------------------------------------------------------------------------
    # INSERÇÃO DO RESUMO ABC COMO TEXTO NO GRÁFICO ------------------------------------

    # Montar o cabeçalho
    cabecalho = "Resumo da Classificação Estado\n"
    # Montar a tabela de dados, focando em Qtd. e (%) Custo Total
    tabela_dados = resumo_abc_estado[['Qtd. Estados', '(%) Custo Total Estado']].to_string(
        header=True, float_format='{:.2f}'.format)

    # Combinar
    texto_box = cabecalho + tabela_dados

    # Inserir o texto no gráfico
    # plt.gca() retorna o eixo atual
    plt.gca().text(
        x=0.98,  # Posição X: 98% da largura do eixo (próximo à direita)
        y=0.95,  # Posição Y: 98% da altura do eixo (próximo ao topo)
        s=texto_box,
        # Garante que as coordenadas sejam relativas ao gráfico (de 0 a 1)
        transform=plt.gca().transAxes,
        fontsize=10,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                  alpha=0.8, edgecolor='gray')
    )

    plt.tight_layout()
    plt.show()

    # ---------------------------------------------------------------------------------
    # PLOTAGEM CENTRO CUSTO (APENAS CLASSE A)
    # ---------------------------------------------------------------------------------

    # Filtrar apenas a Classe A
    ccs_classe_a = df_abc_cc[df_abc_cc['classe_abc']
                             == 'A']['centro_custo'].tolist()

    # Filtrar o DataFrame original para incluir apenas os centros de custo da Classe A
    df_classe_a_detalhe_cc = dfBrindes[dfBrindes['centro_custo'].isin(
        ccs_classe_a)]

    # Agrupar os componentes do custo por centro_custo (apenas Classe A)
    df_composicao_cc = df_classe_a_detalhe_cc.groupby('centro_custo').agg({
        'custo_unitario_total': 'sum',
        'valor_icms': 'sum',
        'valor_icms_st': 'sum',
        'icms_interestadual_uf_destino': 'sum',
        'valor_icms_fcp_uf_destino': 'sum',
        'custo_final': 'sum'})

    df_composicao_cc = df_composicao_cc.sort_values(
        by='custo_final',
        ascending=False)

    df_composicao_cc = df_composicao_cc.drop(columns=['custo_final'])

    # Calcular o valor total de cada barra (Custo Final do Centro de Custo)
    total_custo_cc = df_composicao_cc.sum(axis=1)

    # Calcular o Custo Final Total de TODOS os dados (para o percentual do Eixo Y)
    custo_final_total_geral = dfBrindes['custo_final'].sum()

    # Criação das Bases Percentuais
    # Altura da Barra (Eixo Y): Percentual do CC sobre o Total Geral
    df_percentual_cc = (total_custo_cc / custo_final_total_geral) * 100

    # Componentes Percentuais (Para rótulos internos): Percentual da fatia sobre o TOTAL DA PRÓPRIA BARRA
    df_percentual_base = (
        df_composicao_cc['custo_unitario_total'] / total_custo_cc) * 100
    df_percentual_icms = (
        df_composicao_cc['valor_icms'] / total_custo_cc) * 100
    df_percentual_icms_st = (
        df_composicao_cc['valor_icms_st'] / total_custo_cc) * 100
    df_percentual_icms_interestadual = (
        df_composicao_cc['icms_interestadual_uf_destino'] / total_custo_cc) * 100
    df_percentual_fcp = (
        df_composicao_cc['valor_icms_fcp_uf_destino'] / total_custo_cc) * 100

    # Componentes de PLOTAGEM (A altura de cada fatia deve ser proporcional ao total geral)
    plot_custo_base = df_percentual_cc * (df_percentual_base / 100)
    plot_icms = df_percentual_cc * (df_percentual_icms / 100)
    plot_icms_st = df_percentual_cc * (df_percentual_icms_st / 100)
    plot_icms_interestadual = df_percentual_cc * \
        (df_percentual_icms_interestadual / 100)
    plot_fcp = df_percentual_cc * (df_percentual_fcp / 100)

    # Preparar os dados para o plot
    centros_custo = df_composicao_cc.index

    # Acumuladores de altura para o bottom do plot
    bottom_icms = plot_custo_base
    bottom_icms_st = bottom_icms + plot_icms
    bottom_icms_interestadual = bottom_icms_st + plot_icms_st
    bottom_fcp = bottom_icms_interestadual + plot_icms_interestadual

    # Criar a figura e os eixos
    plt.figure(figsize=(12, 7))

    # Plotar o gráfico de barras empilhadas
    p1 = plt.bar(centros_custo, plot_custo_base,
                 color=COR_AZUL_ESCURO, label='Custo')
    p2 = plt.bar(centros_custo, plot_icms, bottom=bottom_icms,
                 color=COR_ROXO_CLARO, label='ICMS')
    p3 = plt.bar(centros_custo, plot_icms_st, bottom=bottom_icms_st,
                 color=COR_ROSA_MEDIO, label='ICMS ST')
    p4 = plt.bar(centros_custo, plot_icms_interestadual, bottom=bottom_icms_interestadual,
                 color=COR_ROSA_CLARO, label='ICMS Interestadual')
    p5 = plt.bar(centros_custo, plot_fcp, bottom=bottom_fcp,
                 color=COR_ROXA, label='ICMS FCP')

    # Adicionar Títulos e Rótulos
    plt.title(
        'Composição Percentual do Custo Final nos Centros de Custo da Classe A', fontsize=16)
    plt.xlabel('Centro de Custo', fontsize=12)
    plt.ylabel('Representatividade S/ Custo Final (%)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 60)

    # RÓTULOS NO TOPO DA BARRA (Percentual do CC sobre o Total Geral)
    for i, total_percentual in enumerate(df_percentual_cc):
        plt.text(i, total_percentual + (total_percentual * 0.01),
                 f'{total_percentual:.1f}%',
                 ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Adicionar legenda
    plt.legend(
        loc='upper left',
        bbox_to_anchor=(0, 1),
        frameon=False)

    # ---------------------------------------------------------------------------------
    # INSERÇÃO DO RESUMO ABC COMO TEXTO NO GRÁFICO ------------------------------------

    # Montar o cabeçalho
    cabecalho = "Resumo da Classificação CC\n"
    # Montar a tabela de dados, focando em Qtd. e (%) Custo Total
    tabela_dados = resumo_abc_cc[['Qtd. Centros Custo', '(%) Custo Total CC']].to_string(
        header=True, float_format='{:.2f}'.format)

    # Combinar
    texto_box = cabecalho + tabela_dados

    # Inserir o texto no gráfico
    # plt.gca() retorna o eixo atual
    plt.gca().text(
        x=0.98,  # Posição X: 98% da largura do eixo (próximo à direita)
        y=0.95,  # Posição Y: 98% da altura do eixo (próximo ao topo)
        s=texto_box,
        # Garante que as coordenadas sejam relativas ao gráfico (de 0 a 1)
        transform=plt.gca().transAxes,
        fontsize=10,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                  alpha=0.8, edgecolor='gray')
    )

    plt.tight_layout()
    plt.show()

    # ---------------------------------------------------------------------------------
    #  REPRESENTATIVIDADE DO CUSTO POR LINHA DRE
    # ---------------------------------------------------------------------------------
    # Agrupar os dados por 'linha_dre' e somar o 'custo_final'
    df_dre_custo = dfBrindes.groupby('linha_dre').agg(
        total_custo_final=('custo_final', 'sum')
    ).sort_values(by='total_custo_final', ascending=False).reset_index()

    # Calcular o Custo Final Total Geral
    custo_final_total_geral = df_dre_custo['total_custo_final'].sum()

    # Calcular a Participação Relativa (%)
    df_dre_custo['participacao_%'] = (
        df_dre_custo['total_custo_final'] / custo_final_total_geral
    ) * 100

    # Formatação e Exibição da Tabela
    df_dre_custo['participacao_%'] = df_dre_custo['participacao_%'].round(2)
    df_dre_custo['total_custo_final'] = df_dre_custo['total_custo_final'].map(
        '{:,.2f}'.format)

    # PLOTAGEM (Gráfico de Barras)

    # Preparar os dados para plotagem (sem a formatação de string)
    df_plot = df_dre_custo.sort_values(by='participacao_%', ascending=True)
    categorias_dre = df_plot['linha_dre']
    percentuais = df_plot['participacao_%']

    # Destacar a maior categoria
    cores_barras = [COR_ROSA_CLARO] * (len(categorias_dre) - 1) + [COR_ROXA]

    plt.figure(figsize=(10, 6))

    # Plotar o gráfico de barras horizontais
    plt.barh(categorias_dre, percentuais, color=cores_barras)

    # Adicionar rótulos de dados (percentuais)
    for index, value in enumerate(percentuais):
        plt.text(value + 0.5, index,
                 f'{value:.2f}%', va='center', fontweight='bold')

    # Títulos e Rótulos
    plt.title(
        '(%) do Custo Final por Linha DRE', fontsize=16)
    plt.xlabel('Participação no Custo Final (%)', fontsize=12)
    plt.ylabel('Linha DRE', fontsize=12)

    # Formatação do Eixo X (Para adicionar o símbolo de %)
    formatter = mtick.PercentFormatter()
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.xlim(0, 50)

    plt.tight_layout()
    plt.show()
