# ==========================================================
# IMPORTAÇÃO DOS RECURSOS (MANTIDAS FORA DA DEF)
# ==========================================================

# Módulos de dados (get_fato_brindes, etc., devem estar em arquivos separados)
from fato_brindes import get_fato_brindes
from dimensao_produto import get_dimensao_produto
from fato_impostos import get_fato_impostos
import pandas as pd
import numpy as np
import calendar as cl

# Importação para Gráficos
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Importação para Locale (para meses em português)
import locale

# Configurações de Locale e Matplotlib (MANTIDAS FORA DA DEF)
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
except locale.Error:
    print("Aviso: Locale 'pt_BR.utf8' não disponível. Tentando 'Portuguese_Brazil.1252'.")
    try:
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    except locale.Error:
        print("Aviso: Locale para português do Brasil não configurado. Formatação de moeda e meses pode não estar em PT-BR.")

plt.style.use('default')

# ==========================================================
# 🧱 DEF PRINCIPAL: GERAÇÃO DO DATAFRAME FATO DO PROJETO 🧱
# (O que era o corpo do script foi movido para cá)
# ==========================================================


def get_fato_projeto():
    """
    Carrega os DataFrames brutos (Fato/Dimensões), executa os merges, 
    trata NaNs e calcula as colunas de custo final e impostos.
    Retorna o DataFrame final ('df_analise_final') pronto para consumo pelo ML ou Análise.
    """

    print("\n[PREPARAÇÃO DE DADOS] Iniciando Carregamento Fato/Dimensões...")
    dfBrindes = get_fato_brindes()
    dfCadprod = get_dimensao_produto()
    dfImpostos = get_fato_impostos()
    print("[PREPARAÇÃO DE DADOS] Bases de dados carregadas.")

    # ==========================================================
    # PRIMEIRO MERGE (Fato Brindes + Dimensão Produto)
    # ==========================================================

    COLUNAS_DIMENSAO = ['cod_produto', 'nivel_1', 'nivel_2']
    dfCadprod = dfCadprod[COLUNAS_DIMENSAO].copy()

    print("Executando 1º LEFT MERGE (Brindes + Produto).")

    df1 = pd.merge(
        left=dfBrindes,
        right=dfCadprod,
        left_on='cod_sku',
        right_on='cod_produto',
        how='left'
    )
    df1.drop(columns=['cod_produto'], inplace=True)

    # ==========================================================
    # SEGUNDO MERGE (df1 + Fato Impostos)
    # ==========================================================

    dfImpostos.rename(columns={'codigo_sku': 'cod_sku'}, inplace=True)

    # Selecionar todas as colunas de impostos
    COLUNAS_IMPOSTOS = [
        'nota_fiscal',
        'estado',
        'cod_sku',
        'valor_icms',
        'valor_icms_st',
        'valor_fcp_st',
        'icms_interestadual_uf_destino',
        'valor_icms_fcp_uf_destino',
        'valor_cofins',
        'valor_pis',
        'impostos_total'
    ]
    dfImpostos = dfImpostos[COLUNAS_IMPOSTOS].drop_duplicates(
        subset=['nota_fiscal', 'cod_sku'])

    print("Executando 2º LEFT MERGE (df1 + Impostos) nas chaves: 'nota_fiscal' e 'cod_sku'.")

    df_analise_final = pd.merge(
        left=df1,
        right=dfImpostos,
        on=['nota_fiscal', 'cod_sku'],
        how='left'
    )

    # Lista de colunas de impostos para preencher NaNs com 0
    COLUNAS_IMPOSTOS_VALOR = [
        'valor_icms', 'valor_icms_st', 'valor_fcp_st',
        'icms_interestadual_uf_destino', 'valor_icms_fcp_uf_destino',
        'valor_cofins', 'valor_pis', 'impostos_total'
    ]

    # Trata NaNs nas colunas de custo e imposto
    df_analise_final['custo_total'] = df_analise_final['custo_total'].fillna(0)
    df_analise_final[COLUNAS_IMPOSTOS_VALOR] = df_analise_final[COLUNAS_IMPOSTOS_VALOR].fillna(
        0)

    # Novo cálculo de custo_final somando explicitamente todos os componentes
    impostos_somados = (
        df_analise_final['valor_icms'] +
        df_analise_final['valor_icms_st'] +
        df_analise_final['valor_fcp_st'] +
        df_analise_final['icms_interestadual_uf_destino'] +
        df_analise_final['valor_icms_fcp_uf_destino'] +
        df_analise_final['valor_pis'] +
        df_analise_final['valor_cofins']
    )

    # Atualiza custo_final
    df_analise_final['custo_final'] = df_analise_final['custo_total'] + \
        impostos_somados

    # 💡 Coluna custo unitário para o projeto ML
    df_analise_final['custo_unitario'] = np.where(
        df_analise_final['quantidade'] > 0,
        df_analise_final['custo_total'] / df_analise_final['quantidade'],
        0
    )

    # 💡 Coluna para agrupar ICMS/ST/Difal (Para Gráfico de Composição)
    df_analise_final['ICMS_ST_e_Difal_Soma'] = (
        df_analise_final['valor_icms_st'] +
        df_analise_final['valor_fcp_st'] +
        df_analise_final['icms_interestadual_uf_destino'] +
        df_analise_final['valor_icms_fcp_uf_destino']
    )

    print("[PREPARAÇÃO DE DADOS] Colunas de custo e impostos calculadas. DataFrame FATO DO PROJETO pronto.")
    return df_analise_final

# ================================================================================================================================
# INÍCIO DAS ANÁLISES (Lógica de Plotagem e Execução da Análise)
# ================================================================================================================================


if __name__ == '__main__':

    print("\n" + "="*80)
    print("Iniciando o Projeto Brindes: Análise e Geração de Gráficos...")
    print("="*80)

    # ⚠️ AQUI a DEF é chamada para obter o DataFrame final
    df_analise_final = get_fato_projeto()

    # A variável 'meses' é inicializada aqui, no escopo da análise
    meses = sorted(df_analise_final['mes'].dropna().unique())

    # --- Funções Auxiliares (mantidas dentro do __main__ para escopo de análise) ---
    def mil_formatter(x, pos):
        valor_mil = int(round(x * 1e-3, 0))
        valor_formatado = locale.format_string('%d', valor_mil, grouping=True)
        return f'R$ {valor_formatado} mil'

    def classificar_abc(percentual_acumulado):
        if percentual_acumulado <= 80:
            return 'A'
        elif percentual_acumulado <= 95:
            return 'B'
        else:
            return 'C'

    def calcular_curva_abc(df, coluna_agrupamento, coluna_valor, nome_curva_abc):
        df_abc = df.groupby(coluna_agrupamento)[
            coluna_valor].sum().reset_index()
        df_abc = df_abc.sort_values(
            by=coluna_valor, ascending=False).reset_index(drop=True)
        total_geral = df_abc[coluna_valor].sum()
        df_abc['participacao_perc'] = (
            df_abc[coluna_valor] / total_geral) * 100
        df_abc['acumulado_perc'] = df_abc['participacao_perc'].cumsum()
        df_abc[nome_curva_abc] = df_abc['acumulado_perc'].apply(
            classificar_abc)
        resumo_abc = df_abc.groupby(nome_curva_abc).agg(
            total_custo=(coluna_valor, 'sum'),
            num_itens=(coluna_agrupamento, 'count')
        ).reset_index()
        num_total_itens = len(df_abc)
        resumo_abc['perc_custo_total'] = (
            resumo_abc['total_custo'] / total_geral) * 100
        resumo_abc['perc_item_total'] = (
            resumo_abc['num_itens'] / num_total_itens) * 100
        return df_abc, resumo_abc.sort_values(by=nome_curva_abc).round(2)

    # --- Funções de Plotagem (Manter as definições completas aqui) ---
    def plotar_pareto(df_abc, titulo, coluna_item, coluna_valor, coluna_abc):
        # ... (Código completo da plotagem de Pareto) ...
        df_plot = df_abc.head(20).copy()
        fig, ax1 = plt.subplots(figsize=(14, 7))
        fig.patch.set_facecolor('white')
        ax1.set_facecolor('white')
        ax1.bar(df_plot[coluna_item], df_plot[coluna_valor], color='cadetblue')
        ax1.set_xlabel(titulo, color='black')
        ax1.set_ylabel(f'Custo Final (R$)', color='black')
        ax1.tick_params(axis='y', labelcolor='black')
        ax1.tick_params(axis='x', labelcolor='black')
        ax1.grid(False, axis='y')
        ax1.grid(False, axis='x')
        formatter = FuncFormatter(mil_formatter)
        ax1.yaxis.set_major_formatter(formatter)
        plt.xticks(rotation=45, ha='right')
        ax2 = ax1.twinx()
        ax2.plot(df_plot[coluna_item], df_plot['acumulado_perc'],
                 color='navy', marker='o', linestyle='--')
        ax2.set_ylabel('Acumulado (%)', color='black')
        ax2.tick_params(axis='y', labelcolor='black')
        ax2.grid(False, axis='y')
        ax2.axhline(80, color='gray', linestyle=':',
                    linewidth=0.8, label='Curva A (80%)')
        ax2.axhline(95, color='gray', linestyle=':',
                    linewidth=0.8, label='Curva B (95%)')
        plt.title(
            f'Gráfico de Pareto da Curva ABC por {titulo}', fontsize=16, color='black')
        fig.tight_layout()
        plt.show()

    def plotar_evolucao_mensal(df, coluna_data, coluna_valor, titulo):
        # ... (Código completo da evolução mensal) ...
        df_mensal = df.groupby(coluna_data)[coluna_valor].sum().reset_index()
        df_mensal['nome_mes'] = df_mensal[coluna_data].astype(
            int).apply(lambda x: cl.month_name[x].capitalize())
        media_custo = df_mensal[coluna_valor].mean()
        fig = plt.figure(figsize=(12, 6))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(111)
        ax.set_facecolor('white')
        plt.plot(df_mensal['nome_mes'], df_mensal[coluna_valor],
                 marker='o', linestyle='-', color='darkblue')
        media_formatada = locale.format_string(
            '%d', int(round(media_custo, 0)), grouping=True)
        plt.axhline(media_custo, color='navy', linestyle='--',
                    linewidth=1, label=f'Média: R$ {media_formatada}')
        formatter = FuncFormatter(mil_formatter)
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.title(titulo, fontsize=16, color='black')
        plt.xlabel('Mês', color='black')
        plt.ylabel(f'Custo Final Total', color='black')
        ax.tick_params(axis='y', labelcolor='black')
        ax.tick_params(axis='x', labelcolor='black')
        plt.grid(False)
        plt.xticks(rotation=45, ha='right')
        plt.legend(loc='upper left', frameon=False, labelcolor='black')
        plt.tight_layout()
        plt.show()

    def plotar_custo_vs_imposto(df_analise_final, df_abc_estado, titulo):
        # ... (Código completo do custo vs imposto) ...
        estados_ab = df_abc_estado[df_abc_estado['curva_abc_estado'].isin(
            ['A', 'B'])]['estado'].unique()
        df_filtrado = df_analise_final[df_analise_final['estado'].isin(
            estados_ab)]
        df_comparativo = df_filtrado.groupby('estado').agg(
            Custo_Base=('custo_total', 'sum'),
            Imposto=('impostos_total', 'sum')
        ).reset_index()
        df_comparativo['Custo_Total'] = df_comparativo['Custo_Base'] + \
            df_comparativo['Imposto']
        df_comparativo = df_comparativo.sort_values(
            by='Custo_Total', ascending=False)
        fig = plt.figure(figsize=(14, 7))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(111)
        ax.set_facecolor('white')
        plt.bar(df_comparativo['estado'], df_comparativo['Custo_Base'],
                label='Custo Base (Sem Imposto)', color='steelblue')
        plt.bar(df_comparativo['estado'], df_comparativo['Imposto'],
                bottom=df_comparativo['Custo_Base'], label='Imposto (Carga Tributária)', color='navy')
        formatter = FuncFormatter(mil_formatter)
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.grid(False)
        plt.title(titulo, fontsize=16, color='black')
        plt.xlabel('Estado (Curva A e B)', color='black')
        plt.ylabel('Custo Total', color='black')
        ax.tick_params(axis='y', labelcolor='black')
        ax.tick_params(axis='x', labelcolor='black')
        plt.xticks(rotation=45, ha='right')
        plt.legend(frameon=False, labelcolor='black')
        plt.tight_layout()
        plt.show()

    def plotar_composicao_custo_mensal(df, titulo):
        # ... (Código completo da composição mensal) ...
        df_composicao_mensal = df.groupby('mes').agg(
            Custo_Base=('custo_total', 'sum'),
            ICMS_Geral=('valor_icms', 'sum'),
            ICMS_ST_e_Difal=('ICMS_ST_e_Difal_Soma', 'sum'),
            PIS=('valor_pis', 'sum'),
            COFINS=('valor_cofins', 'sum')
        ).reset_index()
        df_composicao_mensal['nome_mes'] = df_composicao_mensal['mes'].astype(
            int).apply(lambda x: cl.month_name[x].capitalize())
        fig = plt.figure(figsize=(14, 7))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(111)
        ax.set_facecolor('white')
        colors = ['steelblue', 'skyblue', 'lightblue',
                  'lightsteelblue', 'powderblue']
        plt.bar(df_composicao_mensal['nome_mes'], df_composicao_mensal['Custo_Base'],
                color=colors[0], label='Custo Base (Produtos)')
        bottom_val = df_composicao_mensal['Custo_Base']
        plt.bar(df_composicao_mensal['nome_mes'], df_composicao_mensal['ICMS_Geral'],
                bottom=bottom_val, color=colors[1], label='ICMS (Geral)')
        bottom_val = bottom_val + df_composicao_mensal['ICMS_Geral']
        plt.bar(df_composicao_mensal['nome_mes'], df_composicao_mensal['ICMS_ST_e_Difal'],
                bottom=bottom_val, color=colors[2], label='ICMS ST/Difal/FCP')
        bottom_val = bottom_val + df_composicao_mensal['ICMS_ST_e_Difal']
        plt.bar(df_composicao_mensal['nome_mes'], df_composicao_mensal['PIS'],
                bottom=bottom_val, color=colors[3], label='PIS')
        bottom_val = bottom_val + df_composicao_mensal['PIS']
        plt.bar(df_composicao_mensal['nome_mes'], df_composicao_mensal['COFINS'],
                bottom=bottom_val, color=colors[4], label='COFINS')
        formatter = FuncFormatter(mil_formatter)
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.grid(False)
        plt.title(titulo, fontsize=16, color='black')
        plt.xlabel('Mês', color='black')
        plt.ylabel('Custo Final Composição (R$)', color='black')
        ax.tick_params(axis='y', labelcolor='black')
        ax.tick_params(axis='x', labelcolor='black')
        plt.xticks(rotation=45, ha='right')
        plt.legend(frameon=False, labelcolor='black', loc='upper left')
        plt.tight_layout()
        plt.show()

    # --- Lógica de Análise (A partir daqui, tudo é análise e print) ---
    df_curva_a = {}
    df_para_plotagem = {}

    # 1. ESTADO
    print("\nIniciando a Análise da Curva ABC por ESTADO...")
    df_estado_completo, resumo_estado = calcular_curva_abc(
        df_analise_final, coluna_agrupamento='estado', coluna_valor='custo_final', nome_curva_abc='curva_abc_estado'
    )
    df_curva_a['estado'] = df_estado_completo
    df_para_plotagem['Estado'] = df_estado_completo
    print("\n--- Resumo da Análise da Curva ABC por ESTADO ---")
    print(resumo_estado)
    print("-" * 50)

    # 2. NÍVEL 1
    print("\nIniciando a Análise da Curva ABC por NIVEL_1...")
    df_nivel1_completo, resumo_nivel1 = calcular_curva_abc(
        df_analise_final, coluna_agrupamento='nivel_1', coluna_valor='custo_final', nome_curva_abc='curva_abc_nivel1'
    )
    df_curva_a['nivel_1'] = df_nivel1_completo
    df_para_plotagem['Nível 1'] = df_nivel1_completo
    print("\n--- Resumo da Análise da Curva ABC por NIVEL_1 ---")
    print(resumo_nivel1)
    print("-" * 50)

    # 3. CENTRO DE CUSTO AJUSTADO
    print("\nIniciando a Análise da Curva ABC por CENTRO DE CUSTO AJUSTADO...")
    if 'centro_custo_ajustado' in df_analise_final.columns:
        df_cc_completo, resumo_cc = calcular_curva_abc(
            df_analise_final, coluna_agrupamento='centro_custo_ajustado', coluna_valor='custo_final', nome_curva_abc='curva_abc_cc'
        )
        df_curva_a['centro_custo_ajustado'] = df_cc_completo
        df_para_plotagem['Centro de Custo Ajustado'] = df_cc_completo
        print("\n--- Resumo da Análise da Curva ABC por CENTRO DE CUSTO AJUSTADO ---")
        print(resumo_cc)
        print("-" * 50)
    else:
        print("AVISO: A coluna 'centro_custo_ajustado' não foi encontrada. Curva ABC e gráficos ignorados para esta coluna.")

    # --- GERAÇÃO DOS GRÁFICOS ---
    print("\n\n" + "="*100)
    print("📈 INICIANDO GERAÇÃO DOS GRÁFICOS PARA APRESENTAÇÃO 📈")
    print("="*100)

    for titulo, df_abc in df_para_plotagem.items():
        coluna_item = df_abc.columns[0]
        coluna_valor = df_abc.columns[1]
        coluna_abc = df_abc.columns[-1]
        plotar_pareto(df_abc, titulo, coluna_item, coluna_valor, coluna_abc)
        print(f"\n[Gráfico de Pareto da Análise: {titulo} exibido.]\n")

    plotar_evolucao_mensal(df_analise_final, coluna_data='mes',
                           coluna_valor='custo_final', titulo='Evolução Mensal do Custo Final Total')
    print("\n[Gráfico de Linha da Evolução Mensal exibido.]\n")

    plotar_custo_vs_imposto(df_analise_final, df_estado_completo,
                            titulo='Custo Base vs. Impostos por Estados A e B')
    print("\n[Gráfico de Barras Empilhadas (Custo vs. Imposto) exibido.]\n")

    plotar_composicao_custo_mensal(
        df_analise_final, titulo='Composição Mensal Detalhada do Custo Final')
    print("\n[Gráfico de Barras Empilhadas da Composição Mensal do Custo Final exibido.]\n")

    # --- PRINTS FINAIS ---
    print("\n\n" + "="*100)
    print("⭐ ITENS CLASSIFICADOS COMO CURVA A (80% DO Custo Final) ⭐")
    print("="*100)

    for analise, df_abc in df_curva_a.items():
        coluna_curva_abc = df_abc.columns[-1]
        df_filtrado_a = df_abc[df_abc[coluna_curva_abc] == 'A']
        print(f"\n--- Curva A por {analise.upper()} ---")
        print(df_filtrado_a.iloc[:, [0, 1, -3, -2, -1]].round(2))
        print("-" * 50)

    print("\nAnálises e Geração de Gráficos concluídas com sucesso.")
