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

    dfImpostos = get_fato_projeto()

    # Exibir os nomes das colunas e o tipo dos dados
    print('='*120)
    print('🔗 Nome das colunas do dfImpostos')
    print('='*120 + "\n")
    print('Colunas: ', dfImpostos.dtypes)
    print("\n")
