# ==========================================================
# Importações e Setup Inicial
# ==========================================================

from py_fBrinde import get_fBrinde
from py_dProduto import get_dProduto

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Definições
ICMS_UNITARIO_MODELO_PLACEHOLDER = 5.50
NATUREZAS_MENU = ['Exportação', 'Bonificação', 'Degustação', 'Amostra grátis']
NATUREZAS_ICMS_ZERO = ['Exportação', 'Amostra grátis']
dfBrindeComDimensao = None  # Inicializa o DataFrame completo


# ==========================================================
# 1. FUNÇÃO PREDITIVA (Modelo de Custo)
# ==========================================================
def prever_custo_total(sku_input, quantidade_input, modelo_custo):
    """
    Calcula o custo total previsto de um SKU baseado em sua média histórica.
    """
    custo_unitario_medio = modelo_custo.get(sku_input)

    if custo_unitario_medio is not None:
        custo_total_previsto = custo_unitario_medio * quantidade_input

        print(f"\n--- PREVISÃO DE CUSTO PARA {sku_input} ---")
        print(f"Quantidade: {quantidade_input}")
        print(
            f"Custo Unitário Médio Histórico: R$ {custo_unitario_medio:,.2f}")
        print(f"Custo Total Previsto: R$ {custo_total_previsto:,.2f}")
        print("--------------------------------\n")

        return custo_total_previsto, custo_unitario_medio
    else:
        print(
            f"⚠️ Erro: SKU '{sku_input}' não encontrado no histórico de custos.")
        return None, None


# ==========================================================
# 2. FUNÇÃO PREDITIVA (Modelo de ICMS - Regra de Negócio FINAL)
# ==========================================================
def prever_icms_final(natureza_input, cliente_input, sku_input, quantidade_input,
                      valor_nf_input, estado_input, sku_ncm_lookup, cliente_cnpj_lookup,
                      aliquota_estado_lookup, DEFAULT_ALIQUOTA):
    """
    Prevê o valor_icms baseado em 6 inputs, Premissas 1 a 5, e lookups de alíquota.
    Retorna (valor_icms_previsto, justificativa, aliquota).
    """
    natureza_input = natureza_input.strip().capitalize()
    estado_input = estado_input.strip().upper()

    print(
        f"\n--- VALIDAÇÃO ICMS PARA {sku_input} / NATUREZA: {natureza_input} ---")
    print(f"Estado: {estado_input} | Valor NF: R$ {valor_nf_input:,.2f}")

    aliquota = 0.0
    valor_icms_previsto = 0.0
    justificativa = ""

    # --- REGRA P3: ICMS ZERO ---
    if natureza_input in NATUREZAS_ICMS_ZERO:
        valor_icms_previsto = 0.0
        aliquota = 0.0
        justificativa = f"Natureza '{natureza_input}' não incide ICMS (P3)."
        print(f"Valor ICMS Previsto: R$ {valor_icms_previsto:,.2f}")
        print(f"Justificativa: {justificativa}")
        print("--------------------------------\n")
        return valor_icms_previsto, justificativa, aliquota

    # --- REGRA P4: EXCEÇÃO DE BONIFICAÇÃO ---
    elif natureza_input == 'Bonificação':
        ncm_sku = sku_ncm_lookup.get(sku_input)

        if ncm_sku is None:
            valor_icms_previsto = None
            aliquota = None
            justificativa = f"SKU '{sku_input}' não encontrado na base histórica (NCM). Não é possível validar a exceção."
            print(f"⚠️ {justificativa}")
            print("--------------------------------\n")
            return None, justificativa, None

        ncm_excecao = str(ncm_sku) in ['96170010', '48236900']
        sku_excecao = sku_input != 10915

        if ncm_excecao and sku_excecao:
            valor_icms_previsto = 0.0
            aliquota = 0.0
            justificativa = f"Bonificação em exceção: NCM ({ncm_sku}) e SKU ({sku_input} != 10915). ICMS ZERO (P4)."
            print(f"Valor ICMS Previsto: R$ {valor_icms_previsto:,.2f}")
            print(f"Justificativa: {justificativa}")
            print("--------------------------------\n")
            return valor_icms_previsto, justificativa, aliquota

        justificativa_base = "Bonificação com incidência de ICMS (Regra Geral) => "

    # --- CASOS QUE APURAM ICMS (Brinde, Degustação) ---
    elif natureza_input in ['Brinde', 'Degustação']:
        justificativa_base = f"Natureza '{natureza_input}' incide ICMS => "

    else:
        print(
            f"⚠️ Erro: Natureza '{natureza_input}' inválida ou não suportada.")
        return None, None, None

    # --- REGRA P5: APURAÇÃO DA ALÍQUOTA E CÁLCULO DO ICMS ---

    # 5.1 - Verifica se o Cliente é Revendedor
    is_revendedor = False
    try:
        cnpj_value = cliente_cnpj_lookup.get(sku_input)
        if cnpj_value is not None and int(cnpj_value) > 0:
            is_revendedor = True
    except ValueError:
        pass

    # --- Regra P5.1: Exceção de Alíquota SP/Revendedor (12%) ---
    if estado_input == 'SP' and is_revendedor:
        aliquota = 0.12  # 12%
        justificativa = justificativa_base + \
            "Alíquota de 12% (Exceção SP/Revendedor)."

    else:
        # Regra P5.2: Busca a alíquota no histórico (Lookup de Estado)
        aliquota_lookup = aliquota_estado_lookup.get(estado_input)

        if aliquota_lookup is not None:
            aliquota = aliquota_lookup
            justificativa = justificativa_base + \
                f"Alíquota de {aliquota*100:,.2f}% (Moda/Mais Frequente das alíquotas > 0 do Estado)."
        else:
            # Fallback: Usa a alíquota default (0.0)
            aliquota = DEFAULT_ALIQUOTA
            justificativa = justificativa_base + \
                f"Alíquota de {aliquota*100:,.2f}% (Padrão/Fallback, Estado não mapeado ou dados ausentes - ICMS Zero)."

    # Cálculo final do ICMS: Valor Total da NF * Alíquota
    valor_icms_previsto = valor_nf_input * aliquota

    # Impressão do resultado
    print(f"Alíquota Utilizada: {aliquota*100:.2f}%")
    print(f"Valor ICMS Previsto: R$ {valor_icms_previsto:,.2f}")
    print(f"Justificativa: {justificativa}")
    print("--------------------------------\n")

    return valor_icms_previsto, justificativa, aliquota


# ==========================================================
# 2.b NOVA FUNÇÃO PREDITIVA (ICMS-ST) - Segue suas 4 premissas
# ==========================================================
def prever_icms_st(natureza_input, sku_input, valor_nf_input, estado_input,
                   sku_ncm_lookup, cliente_cnpj_lookup, valor_icms_previsto_modelo):
    """
    1) Verifica as premissas: Natureza=Bonificação, Estado em {SP,RJ,AL,DF},
       NCM == 21069090 (pelo lookup sku_ncm_lookup), e cnpj_destinatario != 0 (pelo lookup cliente_cnpj_lookup).
    2) Calcula base_calculo_icms_st = valor_nf + valor_nf * percentual_estado (percentuais especificados).
    3) Calcula icms_cheio = base_calculo_icms_st * aliquota_estado.
    4) valor_icms_st_final = icms_cheio - valor_icms_previsto_modelo
    Retorna: (valor_icms_st_final, justificativa)
    """

    # normaliza inputs
    nat = str(natureza_input).strip().capitalize()
    est = str(estado_input).strip().upper()
    sku = sku_input

    # Premissas: Natureza, Estado, NCM, Revendedor
    estados_validos = ['SP', 'RJ', 'AL', 'DF']

    ncm_sku = sku_ncm_lookup.get(sku)
    cnpj_val = cliente_cnpj_lookup.get(sku, 0)

    cond_natureza = (nat == 'Bonificação')
    cond_estado = (est in estados_validos)
    cond_ncm = (str(ncm_sku) == '21069090')
    try:
        cond_revendedor = int(str(cnpj_val)) != 0
    except:
        cond_revendedor = False

    if not (cond_natureza and cond_estado and cond_ncm and cond_revendedor):
        justificativa = f"ICMS-ST não aplicável (Bonificação={cond_natureza}, Estado={cond_estado}, NCM_OK={cond_ncm}, Revendedor={cond_revendedor})."
        return 0.0, justificativa

    # Percentuais para base (MVA equivalente) conforme estado
    percentuais_base = {
        'SP': 0.7783,
        'RJ': 0.6368,
        'AL': 0.4926,
        'DF': 0.7511
    }

    aliquotas_st = {
        'SP': 0.18,
        'RJ': 0.22,
        'AL': 0.19,
        'DF': 0.20
    }

    pct = percentuais_base.get(est)
    aliq_st = aliquotas_st.get(est)

    # base_calculo_icms_st = valor_nf + (valor_nf * pct)
    base_st = valor_nf_input * (1 + pct)

    # icms_cheio = base_st * aliq_st
    icms_cheio = base_st * aliq_st

    # subtrai o icms próprio previsto pelo modelo
    if valor_icms_previsto_modelo is None:
        valor_icms_previsto_modelo = 0.0

    valor_icms_st_final = icms_cheio - valor_icms_previsto_modelo

    justificativa = f"ICMS-ST calculado por regra. Base ST: R$ {base_st:,.2f}; ICMS cheios: R$ {icms_cheio:,.2f}; ICMS próprio subtraído: R$ {valor_icms_previsto_modelo:,.2f}."

    return valor_icms_st_final, justificativa


# --- FIM DAS DEFINIÇÕES DE FUNÇÕES ---
# -------------------------------------


# ==========================================================
# 3. CARREGAMENTO E MERGE DAS BASES (EXECUTADO PRIMEIRO)
# ==========================================================
print("\n[PREPARAÇÃO DE DADOS] Iniciando Carregamento Fato/Dimensões...")

try:
    dfBrindes = get_fBrinde()
    dfCadprod = get_dProduto()

    print("[PREPARAÇÃO DE DADOS] Bases carregadas.")

    # Colunas necessárias do dfCadprod (Dimensão)
    COLUNAS_DIMENSAO_NECESSARIAS = ['cod_produto', 'nivel_1', 'nivel_2']

    # Filtra apenas colunas que realmente existem no dfCadprod
    COLUNAS_DIMENSAO = [
        col for col in COLUNAS_DIMENSAO_NECESSARIAS if col in dfCadprod.columns]
    dfCadprod_subset = dfCadprod[COLUNAS_DIMENSAO].copy()

    # Realiza o MERGE para criar a única base de trabalho
    dfBrindeComDimensao = pd.merge(
        left=dfBrindes,
        right=dfCadprod_subset,
        left_on='cod_sku',
        right_on='cod_produto',
        how='left'
    )

    if 'cod_produto' in dfBrindeComDimensao.columns:
        dfBrindeComDimensao.drop(columns=['cod_produto'], inplace=True)

    print('='*80)
    print('✅ DataFrame Completo (dfBrindeComDimensao) criado.')
    print('Primeiras 5 linhas:')
    print(dfBrindeComDimensao.head(5))
    print("\n")

except Exception as e:
    print(
        f"❌ Erro na fase de Carregamento e Merge. O modelo não pode ser inicializado. Erro: {e}")
    dfBrindeComDimensao = pd.DataFrame()  # Define DataFrame vazio em caso de falha


# ==========================================================
# 4. TREINAMENTO DO MODELO DE CUSTO
# ==========================================================
modelo_custo_medio = {}
if not dfBrindeComDimensao.empty:
    print("[MODELO CUSTO] Calculando custo médio histórico por SKU...")

    dfBrindeComDimensao['cod_sku'] = pd.to_numeric(
        dfBrindeComDimensao['cod_sku'], errors='coerce')

    if 'custo_unitario' in dfBrindeComDimensao.columns:
        custo_medio_sku = dfBrindeComDimensao.groupby(
            'cod_sku')['custo_unitario'].mean()
        modelo_custo_medio = custo_medio_sku.to_dict()
        print("✅ Modelo de custo médio criado!")
    else:
        print("⚠️ Coluna 'custo_unitario' não encontrada - modelo de custo ficou vazio.")
else:
    print("❌ DataFrame vazio. Modelo de custo não pode ser criado.")


# ==========================================================
# 5. CRIAÇÃO DOS LOOKUPS PARA REGRAS DE ICMS
# ==========================================================
sku_ncm_lookup = {}
cliente_cnpj_lookup = {}
aliquota_estado_lookup = {}
DEFAULT_ALIQUOTA = 0.0

if not dfBrindeComDimensao.empty:

    # Lookup 5.1: SKU -> NCM
    if 'ncm' in dfBrindeComDimensao.columns:
        sku_ncm_lookup = dfBrindeComDimensao.dropna(
            subset=['cod_sku', 'ncm']).set_index('cod_sku')['ncm'].astype(str).to_dict()
        print("✅ Lookup SKU-NCM criado.")
    else:
        print("⚠️ Coluna 'ncm' não encontrada. Exceção de Bonificação não será validada.")

    # Lookup 5.2: SKU -> CNPJ DESTINATARIO
    if 'cnpj_destinatario' in dfBrindeComDimensao.columns:
        temp_df = dfBrindeComDimensao[['cod_sku', 'cnpj_destinatario']].dropna(
        ).drop_duplicates(subset=['cod_sku'])
        cliente_cnpj_lookup = temp_df.set_index(
            'cod_sku')['cnpj_destinatario'].to_dict()
        print("✅ Lookup SKU-CNPJ_Destinatario criado.")
    else:
        print("⚠️ Coluna 'cnpj_destinatario' não encontrada. A regra de SP/Revendedor será limitada.")

    # Lookup 5.3: Estado -> Alíquota Mais Frequente (Moda) > 0
    if 'aliquota_icms' in dfBrindeComDimensao.columns and 'estado' in dfBrindeComDimensao.columns:

        df_aliquota = dfBrindeComDimensao.dropna(
            subset=['estado', 'aliquota_icms']).copy()
        df_aliquota['aliquota_icms'] = pd.to_numeric(
            df_aliquota['aliquota_icms'], errors='coerce')

        # FILTRA APENAS ALÍQUOTAS MAIORES QUE ZERO (resolve o problema do 7%)
        df_aliquota_tributada = df_aliquota[df_aliquota['aliquota_icms'] > 0.0].copy(
        )

        if not df_aliquota_tributada.empty:

            # Cálculo MODA: Encontra o valor mais frequente da alíquota para cada estado
            aliquota_moda_estado = df_aliquota_tributada.groupby('estado')['aliquota_icms'].apply(
                lambda x: (x.mode().iloc[0] /
                           100.0) if not x.mode().empty else np.nan
            ).dropna()
            aliquota_estado_lookup = aliquota_moda_estado.to_dict()
            print("✅ Lookup Estado-Alíquota (Moda/Mais Frequente > 0) criado.")
            if 'MT' in aliquota_estado_lookup:
                print(
                    f"   Teste MT: Alíquota Moda > 0 mapeada: {aliquota_estado_lookup['MT']*100:,.2f}%")
        else:
            print(
                "⚠️ Colunas encontradas, mas NENHUMA alíquota > 0. Usando 0% como fallback.")
    else:
        print("⚠️ Colunas 'aliquota_icms' ou 'estado' não encontradas. Usando 0% como fallback (ICMS Zero).")
else:
    print("❌ DataFrame vazio. Lookups de ICMS não criados.")


# ==========================================================
# 6. INTERFACE DE INPUT PARA TESTE
# ==========================================================
if modelo_custo_medio:
    print("\n" + "="*50)
    print("🚀 Módulo de Teste de Previsão de Custo e ICMS")
    print(f"Naturezas Permitidas: {', '.join(NATUREZAS_MENU)}")
    print("="*50)

    while True:
        try:
            # 1. Input Natureza com Menu de Seleção
            print("\n➡️ 1. Selecione o Tipo de Natureza (ou 'sair'):")
            for i, natureza in enumerate(NATUREZAS_MENU, 1):
                print(f"   [{i}] {natureza}")

            escolha_raw = input(
                "   Digite o número da opção (ou 'sair'): ").strip().lower()

            if escolha_raw == 'sair':
                print("Sessão de teste encerrada.")
                break

            escolha_indice = int(escolha_raw) - 1

            if 0 <= escolha_indice < len(NATUREZAS_MENU):
                natureza_capitalizada = NATUREZAS_MENU[escolha_indice]
            else:
                print(
                    f"❌ Opção inválida. Digite um número entre 1 e {len(NATUREZAS_MENU)}.")
                continue

            # --- VALIDAÇÃO ICMS ZERO (OTIMIZAÇÃO) ---
            if natureza_capitalizada in NATUREZAS_ICMS_ZERO:
                print(
                    f"\n--- VALIDAÇÃO ICMS PARA NATUREZA: {natureza_capitalizada} ---")
                print("Valor ICMS Previsto: R$ 0.00")
                print(
                    f"Justificativa: Natureza '{natureza_capitalizada}' não incide ICMS (P3).")
                print("--------------------------------\n")
                continue

            # --- CASOS QUE REQUEREM MAIS DADOS ---
            print("--- Requer mais dados ---")
            cliente_input_teste = input(
                "➡️ 2. Digite o Código do Cliente: ").strip()
            sku_input_raw = input("➡️ 3. Digite o Código SKU: ").strip()
            quantidade_input_teste = input(
                "➡️ 4. Digite a Quantidade de itens: ").strip()
            valor_nf_input_raw = input(
                "➡️ 5. Digite o Valor Total da NF (R$): ").strip().replace(',', '.')
            estado_input_teste = input(
                "➡️ 6. Digite o Estado do Destinatário (Ex: SP, MG): ").strip()

            # Conversão de Tipos
            sku_input_teste = int(sku_input_raw)
            quantidade_input_teste = int(quantidade_input_teste)
            valor_nf_input_teste = float(valor_nf_input_raw)

            # 1. Previsão de Custo Total
            custo_total_previsto, custo_unitario_previsto = prever_custo_total(
                sku_input_teste, quantidade_input_teste, modelo_custo_medio)

            if custo_total_previsto is None:
                continue

            # 2. Previsão de ICMS
            valor_icms_previsto, _, aliquota_utilizada = prever_icms_final(
                natureza_capitalizada,
                cliente_input_teste,
                sku_input_teste,
                quantidade_input_teste,
                valor_nf_input_teste,
                estado_input_teste,
                sku_ncm_lookup,
                cliente_cnpj_lookup,
                aliquota_estado_lookup,
                DEFAULT_ALIQUOTA
            )

            # 2.b Previsão / Cálculo de ICMS-ST (Nova Etapa)
            valor_icms_st_previsto = 0.0
            justificativa_icms_st = "ICMS-ST não calculado."
            try:
                valor_icms_st_previsto, justificativa_icms_st = prever_icms_st(
                    natureza_capitalizada,
                    sku_input_teste,
                    valor_nf_input_teste,
                    estado_input_teste,
                    sku_ncm_lookup,
                    cliente_cnpj_lookup,
                    valor_icms_previsto
                )
            except Exception as e:
                # Em caso improvável de erro, mantemos icms_st = 0 e registramos justificativa
                valor_icms_st_previsto = 0.0
                justificativa_icms_st = f"Erro ao calcular ICMS-ST: {e}"

            # 3. CÁLCULO FINAL E EXIBIÇÃO
            if valor_icms_previsto is not None:
                soma_total_prevista = custo_total_previsto + \
                    valor_icms_previsto + valor_icms_st_previsto

                # Cálculo do percentual
                percentual_custo_nf = 0.0
                if valor_nf_input_teste > 0:
                    percentual_custo_nf = (
                        soma_total_prevista / valor_nf_input_teste) * 100

                print("="*40)
                print("💰 SOMATÓRIO DO CUSTO TOTAL PREVISTO 💰")

                print(
                    f"Valor Total da NF (Input): R$ {valor_nf_input_teste:,.2f}")
                print("-" * 40)

                print(
                    f"Custo Unitário (Modelo): R$ {custo_unitario_previsto:,.2f}")
                print(f"Custo Total (Produto): R$ {custo_total_previsto:,.2f}")

                # Alíquota utilizada
                print(
                    f"Alíquota ICMS Aplicada: {aliquota_utilizada*100:,.2f}%")
                print(f"ICMS Previsto: R$ {valor_icms_previsto:,.2f}")

                # --- NOVO: Exibe ICMS-ST ---
                print(f"ICMS-ST Previsto: R$ {valor_icms_st_previsto:,.2f}")
                print(f"Justificativa ICMS-ST: {justificativa_icms_st}")

                print("-" * 40)
                print(
                    f"Custo Total Final Previsto (Produto + ICMS + ICMS-ST): R$ {soma_total_prevista:,.2f}")

                print(f"Representação s/ NF: {percentual_custo_nf:,.2f}%")
                print("="*40)
                print("\n")

        except ValueError as ve:
            print(
                f"\n❌ Entrada inválida. Verifique se a opção de Natureza é um número e se os demais inputs (SKU, Quantidade, Valor NF) são válidos. Erro: {ve}\n")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}\n")
else:
    print("❌ Modelo de custo não disponível. Verifique se o carregamento de dados foi bem sucedido.")
