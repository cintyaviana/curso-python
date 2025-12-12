# ==================================================================
# 0. IMPORTAÇÕES
# ==================================================================
from py_fBrinde import get_fBrinde
from py_dProduto import get_dProduto

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
import warnings

# Ocultar avisos do sklearn e pandas para manter o código limpo
warnings.filterwarnings("ignore")

# ==================================================================
# 1. FUNÇÃO PREDITIVA: CUSTO UNITÁRIO (MODELO ML - RANDOM FOREST)
# ==================================================================


def prever_custo_unitario_ml(sku_input, quantidade_input, modelo_ml):
    # Prevê APENAS o custo_unitario (custo base)

    print("-> Previsão de Custo Unitário Base usando Random Forest Regressor...")

    # 1. Criar o DataFrame de entrada com as features
    data_input = pd.DataFrame({
        'cod_sku': [sku_input],
        'quantidade': [quantidade_input],
    })

    # GARANTE que o SKU seja STRING
    data_input['cod_sku'] = data_input['cod_sku'].astype(str)

    # 2. Fazer a previsão usando o pipeline
    custo_unitario_previsto = modelo_ml.predict(data_input)[0]

    return custo_unitario_previsto

# ==================================================================
# 3. TREINAMENTO DO MODELO RANDOM FOREST REGRESSOR
# ==================================================================


def treinar_modelo_custo_base(df_treinamento):
    # Treina o modelo Random Forest Regressor para prever o custo_unitario.
    print("\n" + "="*70)
    print("TREINAMENTO DO MODELO DE MACHINE LEARNING (CUSTO UNITÁRIO BASE)")

    # 3.1. Tratamento de dados para o ML
    df_treinamento['custo_unitario'] = pd.to_numeric(
        df_treinamento['custo_unitario'], errors='coerce')
    df_treinamento['quantidade'] = pd.to_numeric(
        df_treinamento['quantidade'], errors='coerce')
    df_treinamento['cod_sku'] = df_treinamento['cod_sku'].astype(str)

    # Remove linhas com valores faltantes
    df_treinamento.dropna(
        subset=['custo_unitario', 'quantidade'], inplace=True)

    # 3.2. Definição de Features (X) e Target (Y)
    features = ['cod_sku', 'quantidade']
    target = 'custo_unitario'

    X = df_treinamento[features]
    Y = df_treinamento[target]

    # 3.3. Pré-processamento (Pipeline)
    categorical_features = ['cod_sku']
    numeric_features = ['quantidade']

    preprocessor = ColumnTransformer(
        transformers=[
            ('categoria', OneHotEncoder(sparse_output=False,
             handle_unknown='ignore'), categorical_features),
            ('numerico', 'passthrough', numeric_features)
        ])

    # 3.4. Criação do Pipeline e Treinamento
    modelo_ml = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(
            n_estimators=100, random_state=42, n_jobs=-1))
    ])

    """
    n_estimators=100 >> Representa o número de árvores de decisão (Decision Trees) que serão construídas na "floresta" (o modelo Random Forest).

    random_state=42 >>  Define a "semente" (seed) para o gerador de números pseudoaleatórios. O processo de Random Forest, por natureza, envolve aleatoriedade (como a amostragem de dados e a seleção de features para cada árvore). 42 é um valor popularmente usado na comunidade de programação e ciência de dados.

    n_jobs=-1 >> Especifica quantos núcleos (ou threads) do seu processador podem ser usados para o treinamento paralelo do modelo. O valor -1 é uma instrução que significa: "Use todos os núcleos de processamento disponíveis no meu computador."

    """

    # Divisão para validação
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)

    """
    O valor 0.2 (ou 20%) significa que 20% de todo o seu conjunto de dados original será usado para o teste (X_test e Y_test), e os restantes 80% serão usados para o treinamento (X_train e Y_train).
    """

    print("-> Iniciando treinamento do Random Forest...")
    if len(X_train) == 0:
        print("ERRO: O conjunto de treinamento está vazio. Verifique os dados de entrada.")
        return None

    # É neste momento que o modelo aprende a fazer previsões usando os dados preparados

    modelo_ml.fit(X_train, Y_train)
    print("-> Treinamento concluído.")

    # 3.5. Avaliação
    Y_pred = modelo_ml.predict(X_test)

    mae = mean_absolute_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)

    """
    MAE: Quanta diferença média, em unidades da sua variável alvo, há entre o que foi previsto e o que é real.
        Se o seu MAE for, por exemplo, R$ 5,00, isso significa que, em média, as previsões do seu modelo de custo estão erradas em R$ 5,00. Quanto menor o MAE, melhor.

    R^2: Quão bem o seu modelo explica a variação dos seus dados.

        Valor: O valor varia de $-\infty$ a $1.0$.
        R^2 = 1.0: O modelo explica perfeitamente 100% da variação.
        R^2 = 0: O modelo não explica nada da variação (é tão bom quanto simplesmente usar a média dos dados).
        R^2 < 0: O modelo é pior do que usar a média (o que indica um modelo muito ruim).
    
    """
    print(f"--- Métrica do Modelo (Teste Simulado) ---")
    print(f"MAE (Erro Absoluto Médio): R$ {mae:,.4f}")
    print(f"R² (Coef. de Determinação): {r2:.4f}")
    print(f"O modelo de ML treinou com {len(X_train)} registros.")
    print("="*70)

    # O modelo_ml vai ser chamado no def anterior "prever_custo_unitario_ml" para o calculo do custo unitario
    return modelo_ml

# ==================================================================
# 1. FUNÇÃO PREDITIVA: CUSTO UNITÁRIO E CUSTO TOTAL PREVISTO
# ==================================================================
# Prevê o custo total de um SKU usando o def "prever_custo_unitario_ml"


def prever_custo_total(sku_input, quantidade_input, modelo_ml):
    custo_unitario_previsto = prever_custo_unitario_ml(
        sku_input, quantidade_input, modelo_ml
    )
    custo_total_previsto = custo_unitario_previsto * quantidade_input

    return custo_total_previsto, custo_unitario_previsto

# ==================================================================
# 2. FUNÇÃO PREDITIVA: ICMS
# ==================================================================
# Prevê o valor_icms baseado em Natureza, Estado e Alíquota histórico.


def prever_icms(
    natureza_input,
    cliente_input,
    sku_input,
    valor_nf_input,
    estado_input,
    sku_ncm_lookup,
    cliente_cnpj_lookup,
    estado_aliqicms_lookup
):

    # 2.1 APURAÇÃO SE INCIDE OU NÃO ICMS ---------------------------

    # 2.1.1 REGRA ICMS: EXPORTAÇÃO E AMOSTRA GRÁTIS
    if natureza_input in ['Exportação', 'Amostra grátis']:
        return 0.0

    # 2.1.2 REGRA ICMS: EXCEÇÃO DE BONIFICAÇÃO
    if natureza_input == 'Bonificação':
        ncm_sku = sku_ncm_lookup[sku_input]

        # Regra da exceção: NCM 96170010 OU NCM 48236900 AND SKU != 10915
        ncm_excecao = str(ncm_sku) in ['96170010', '48236900']
        sku_excecao = sku_input != 10915

        """
        sku_ncm_lookup >> é um dicionário (chave: SKU, valor: ncm) 

        ncm_excecao e sku_excecao >> retorna true ou False se atender ou não a condição

        """

        if ncm_excecao and sku_excecao:
            # Se ncm_excecao e sku_excecao = true então segue o retur, caso contrário entra na condição do elif.

            # Se passar do Elif, iniciar o proceddo de apuração da alíquota icms.

            return 0.0

    # 2.1.3 REGRA ICMS DEGUSTAÇÃO
    elif natureza_input == 'Degustação':
        pass

    # 2.2 APURAÇÃO DA ALÍQUOTA  ---------------------------------

    # Verifica se o Cliente é Revendedor
    cnpj_value = cliente_cnpj_lookup[cliente_input]
    is_revendedor = int(str(cnpj_value)) != 0
    aliquota = 0.0

    """
    is_revendedor >> retorna True ou False

    """

    # Regra exceção de alíquota sp/revendedor (12%)
    if estado_input == 'SP' and is_revendedor:
        aliquota = 0.12

    # Busca a alíquota no lookup (dicionário criado)
    else:
        aliquota_lookup = estado_aliqicms_lookup[estado_input]

        if aliquota_lookup is not None:
            # None significa "nada", "ausente" ou "valor não encontrado".
            aliquota = aliquota_lookup

        else:
            aliquota = 0.0

    # 2.3 CÁLCULO DO ICMS ---------------------------------
    valor_icms_previsto = valor_nf_input * aliquota

    return valor_icms_previsto

# ==================================================================
# 3. FUNÇÃO PREDITIVA: ICMS-ST
# ==================================================================
# Prevê o valor_icms_st baseado em Natureza, Estado e Alíquota.


def prever_icms_st(
    natureza_input,
    cliente_input,
    sku_input,
    valor_nf_input,
    estado_input,
    sku_ncm_lookup,
    cliente_cnpj_lookup,
    valor_icms_previsto
):

    # Premissas
    estados_validos = ['SP', 'RJ', 'AL', 'DF']
    ncm_sku = sku_ncm_lookup[sku_input]
    cnpj_val = cliente_cnpj_lookup[cliente_input]

    # Premissas de Incidência de ICMS-ST
    cond_natureza = (natureza_input == 'Bonificação')
    cond_estado = (estado_input in estados_validos)
    cond_ncm = (str(ncm_sku) == '21069090')
    cond_revendedor = int(str(cnpj_val)) != 0

    """
    cond_natureza,cond_estado, cond_ncm e cond_revendedor >> retorna True ou False

    """

    if not (cond_natureza and cond_estado and cond_ncm and cond_revendedor):
        # Se cond_natureza e cond_estado e cond_ncm e cond_revendedor = not True (False) vai para o retunr, caso contrário continua o próximo código.
        return 0.0

    # Parâmetros de Cálculo:
    # MVA
    percentuais_base = {'SP': 0.7783, 'RJ': 0.6368, 'AL': 0.4926, 'DF': 0.7511}
    pct = percentuais_base[estado_input]

    # Alíquotas ST
    aliquotas_icms_st = {'SP': 0.18, 'RJ': 0.22, 'AL': 0.19, 'DF': 0.20}
    aliq_st = aliquotas_icms_st[estado_input]

    base_st = valor_nf_input * (1 + pct)

    icms_st_cheio = base_st * aliq_st

    valor_icms_st_previsto = icms_st_cheio - valor_icms_previsto

    return valor_icms_st_previsto

# ==================================================================
# 4. FUNÇÃO PREDITIVA: ICMS INTERESTADUAL UF DESTINO
# ==================================================================
# Prevê o valor_icms_interestadual_uf_destino (DIFAL)


def prever_icms_interestadual_uf_destino(
    natureza_venda_input,
    estado_input,
    valor_nf_input,
    valor_icms_previsto,
    estado_aliqdifal_lookup
):
    # 4.1. VERIFICAÇÃO DE INCIDÊNCIA ---------------------------------
    estados_excluidos = ['SP', 'EX']

    # Regra de Incidência
    if (natureza_venda_input != 'Consumidor final' or estado_input in estados_excluidos):
        return 0.0

    # 4.2. BUSCA DA ALÍQUOTA INTERNA (POR ESTADO) --------
    aliquota_interna_destino = estado_aliqdifal_lookup[estado_input]

    # 4.3. CÁLCULO ---------------------------------

    # 1º passo: calcular a base_calculo_icms_uf_destino:
    base_icms = valor_nf_input - valor_icms_previsto
    fator_divisao = 1 - (aliquota_interna_destino / 100.0)

    if fator_divisao == 0:
        return 0.0

    base_calculo_icms_uf_destino = base_icms / fator_divisao

    # 2º passo: calcular o icms_interestadual_uf_destino:
    icms_cheio_destino = base_calculo_icms_uf_destino * \
        (aliquota_interna_destino / 100.0)
    valor_icms_interestadual_uf_destino = icms_cheio_destino - valor_icms_previsto

    return valor_icms_interestadual_uf_destino

# ==================================================================
# 4. CARREGAMENTO E CRIAÇÃO DA BASE - MERGE
# ==================================================================


print("[PREPARAÇÃO] Carregando bases e criando DataFrame de trabalho...")

dfBrindes = get_fBrinde()
dfCadprod = get_dProduto()

dfCadprod_subset = dfCadprod[['cod_produto', 'nivel_1', 'nivel_2']]

# Realiza o MERGE
dfProjeto = pd.merge(
    left=dfBrindes,
    right=dfCadprod_subset,
    left_on='cod_sku',
    right_on='cod_produto',
    how='left'
).drop(columns=['cod_produto'])

# ==================================================================
# 5. TREINAMENTO DO MODELO_ML DE CUSTO UNITÁRIO
# ==================================================================
# Agora treina o modelo ML para prever o Custo Unitário (Target: custo_unitario).

print("[MODELO] Treinando modelo de Machine Learning (Custo Unitário Base)...")

# Chamada da função de treinamento ML
modelo_ml = treinar_modelo_custo_base(dfProjeto)

# Renomeia a variável para manter a compatibilidade com a função simulador
modelo_custo_unitario = modelo_ml

# ==================================================================
# 6. CRIAÇÃO DOS LOOKUPS PARA REGRAS DE ICMS
# ==================================================================

print("[LOOKUPS] Criando lookups de NCM, CNPJ e Alíquota ICMS")

# 6.1: SKU -> NCM
sku_ncm_lookup = dfProjeto.set_index(
    'cod_sku')['ncm'].astype(str).to_dict()

"""
set_index('cod_sku') >> transforma a coluna 'cod_sku' em seu índice. Os valores de SKU agora funcionam como as chaves que serão usadas para acessar o dicionário.
    Se houver SKUs repetidos na base de dados (dfProjeto), o Pandas, por padrão, mantém a última ocorrência do valor duplicado para o índice resultante.

astype(str) >> converte todos os valores da coluna ncm para tipo str.

.to_dict >> transforma em um dicionário contendo o cod_sku e o ncm.

"""

# 6.2: CLIENTE -> CNPJ DESTINATARIO
cliente_cnpj_lookup = dfProjeto.set_index(
    'cod_cliente')['cnpj_destinatario'].to_dict()

# 6.3: ESTADO -> ALÍQUOTA ICMS
df_aliquota_icms = dfProjeto[
    pd.to_numeric(dfProjeto['aliquota_icms']) > 0.0]

estado_aliqicms_lookup = (
    df_aliquota_icms.set_index('estado')['aliquota_icms'] / 100.0
).to_dict()

# 6.3: ESTADO -> ALÍQUOTA DIFAL
df_aliquota_difal = dfProjeto[
    pd.to_numeric(dfProjeto['aliquota_interna_uf_destino']) > 0.0]

estado_aliqdifal_lookup = (
    df_aliquota_difal.set_index(
        'estado')['aliquota_interna_uf_destino']
).to_dict()

# ==================================================================
# 7. FUNÇÃO PRINCIPAL DE TESTE
# ==================================================================
# Chama as funções prever_custo_total, prever_icms e prever_icms_st


def simulador(natureza_input, natureza_venda_input, cliente_input, sku_input, quantidade_input, valor_nf_input, estado_input, modelo_custo_unitario, sku_ncm_lookup, cliente_cnpj_lookup, estado_aliqicms_lookup, estado_aliqdifal_lookup):

    # 7.1 Previsão de Custo Total
    custo_total_previsto, custo_unitario_previsto = prever_custo_total(
        sku_input, quantidade_input, modelo_custo_unitario)

    # 7.2 Previsão de ICMS
    valor_icms_previsto = prever_icms(
        natureza_input,
        cliente_input,
        sku_input,
        valor_nf_input,
        estado_input,
        sku_ncm_lookup,
        cliente_cnpj_lookup,
        estado_aliqicms_lookup
    )

    # 7.3 Previsão de ICMS-ST
    valor_icms_st_previsto = prever_icms_st(
        natureza_input,
        cliente_input,
        sku_input,
        valor_nf_input,
        estado_input,
        sku_ncm_lookup,
        cliente_cnpj_lookup,
        valor_icms_previsto
    )
    # 8.4 Previsão de DIFAL
    valor_icms_interestadual_uf_destino = prever_icms_interestadual_uf_destino(
        natureza_venda_input,
        estado_input,
        valor_nf_input,
        valor_icms_previsto,
        estado_aliqdifal_lookup
    )

    # 7.4. CÁLCULO FINAL E EXIBIÇÃO
    soma_total_prevista = custo_total_previsto + valor_icms_previsto + \
        valor_icms_st_previsto + valor_icms_interestadual_uf_destino
    percentual_custo_nf = (soma_total_prevista / valor_nf_input) * 100

    # Output Final
    print("\n" + "="*50)
    print("💰 CUSTO TOTAL PREVISTO 💰")
    print(f"Natureza: {natureza_input} |Natureza: {natureza_venda_input} | SKU: {sku_input} | Cliente: {cliente_input} |  Estado: {estado_input}")
    print("-" * 50)

    print(f"Custo Unitário Médio: R$ {custo_unitario_previsto:,.2f}")
    print(f"Custo Total (Produto): R$ {custo_total_previsto:,.2f}")
    print(f"ICMS: R$ {valor_icms_previsto:,.2f}")
    print(f"ICMS-ST: R$ {valor_icms_st_previsto:,.2f}")
    print(f"ICMS-Difal: R$ {valor_icms_interestadual_uf_destino:,.2f}")
    print("-" * 50)

    print(f"Custo Total Final: R$ {soma_total_prevista:,.2f}")
    print(
        f"Representação s/ NF (R$ {valor_nf_input:,.2f}): {percentual_custo_nf:,.2f}%")
    print("="*50)

    return soma_total_prevista


# ==========================================================
# 8. EXECUÇÃO PARA TESTE (Bloco de Chamada)
# ==========================================================
if __name__ == "__main__":

    natureza_teste = 'Bonificação'
    natureza_venda_teste = 'Consumidor final'
    cliente_teste = 20001
    sku_teste = str(10343)
    quantidade_teste = 230
    valor_nf_teste = 18837
    estado_teste = 'PE'

    resultado_final = simulador(
        natureza_teste,
        natureza_venda_teste,
        cliente_teste,
        sku_teste,
        quantidade_teste,
        valor_nf_teste,
        estado_teste,
        modelo_custo_unitario,
        sku_ncm_lookup,
        cliente_cnpj_lookup,
        estado_aliqicms_lookup,
        estado_aliqdifal_lookup
    )
    print(
        f"✅ Processo finalizado. Custo Total Previsto Retornado: R$ {resultado_final:,.2f}")
