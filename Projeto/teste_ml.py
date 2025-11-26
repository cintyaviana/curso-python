# ==================================================================
# 0. IMPORTAÇÕES E CONFIGURAÇÃO INICIAL
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

# Ocultar avisos do sklearn e pandas
warnings.filterwarnings("ignore")

# ==================================================================
# 1. FUNÇÃO PREDITIVA: ICMS (MODELO ML - RANDOM FOREST)
# ==================================================================


def prever_icms_ml(natureza_input, cliente_input, sku_input, valor_nf_input, estado_input, sku_ncm_lookup, modelo_ml):
    # Prevê o valor_icms usando o modelo Random Forest Regressor treinado.

    print("-> Previsão de ICMS usando Random Forest Regressor...")

    # 1. Obter NCM
    ncm_sku = str(sku_ncm_lookup.get(sku_input))

    # 2. Criar o DataFrame de entrada com os mesmos nomes de colunas do treinamento
    data_input = pd.DataFrame({
        'natureza_operacao': [natureza_input],
        'cod_cliente': [cliente_input],
        'cod_sku': [sku_input],
        'valor_total_nf': [valor_nf_input],
        'estado': [estado_input],
        'ncm': [ncm_sku],
    })

    # 3. Fazer a previsão usando o pipeline
    valor_icms_ml_previsto = modelo_ml.predict(data_input)[0]

    """
    modelo_ml: É a variável que contém o Machine Learning ou o modelo treinado em si. O "modelo" é um objeto que encapsula o algoritmo e todos os passos de pré-processamento (como normalização ou codificação de variáveis).

    .predict(): Este é o método padrão usado para fazer a previsão (ou inferência) em um modelo de ML treinado.

    data_input: É a nova entrada de dados que você deseja prever.

    Importante: Esses dados devem ter o mesmo formato (mesmas colunas/variáveis) que os dados usados para treinar o modelo, caso contrário, a previsão falhará.

    [0]: É o índice zero, usado para selecionar o primeiro elemento de uma lista ou array.

        O método .predict() de muitos modelos geralmente retorna um array ou uma lista de previsões, mesmo que você tenha fornecido apenas uma única linha de dados para prever.

        Como você está fazendo uma única previsão (valor_icms_ml_previsto), você usa o [0] para "pegar" o primeiro (e único) resultado desse array.
    
    """
    return valor_icms_ml_previsto

# ==================================================================
# 3. TREINAMENTO DO MODELO RANDOM FOREST REGRESSOR
# ==================================================================


def treinar_modelo_icms(df_treinamento):
    # Treina o modelo Random Forest Regressor para prever o valor_icms.
    print("\n" + "="*70)
    print("🧠 TREINAMENTO DO MODELO DE MACHINE LEARNING (RANDOM FOREST) 🧠")

    # 3.1. Tratamento de dados para o ML
    df_treinamento['valor_icms'] = pd.to_numeric(df_treinamento['valor_icms'])
    df_treinamento['ncm'] = df_treinamento['ncm'].astype(str)

    """
    pd.to_numeric(): Converte todos todos os valores da coluna valor_icms para o tipo numérico (números inteiros ou de ponto flutuante).

    .astype(str): Converte todos os valores da coluna ncm para o tipo string (texto).
    
    """

    # 3.2. Definição de Features (X) e Target (Y)
    features = ['natureza_operacao', 'cod_cliente',
                'cod_sku', 'valor_total_nf', 'base_calculo_icms', 'aliquota_icms', 'estado', 'ncm', 'cfop', 'cnpj_destinatario']
    target = 'valor_icms'

    """
    O objetivo é separar o conjunto de dados (df_treinamento) em duas partes: as variáveis de entrada (Features) que serão usadas para fazer a previsão, e a variável de saída (Target) que o modelo deve aprender a prever.
    
    """

    X = df_treinamento[features]
    Y = df_treinamento[target]

    # 3.3. Pré-processamento (Pipeline)
    categorical_features = ['natureza_operacao', 'cod_cliente',
                            'cod_sku', 'estado', 'ncm', 'cfop', 'cnpj_destinatario']
    numeric_features = ['valor_total_nf',
                        'base_calculo_icms', 'aliquota_icms',]

    """
    categorical_features >> São variáveis que representam categorias ou rótulos e geralmente são compostas por texto ou códigos (mesmo que sejam números, como CNPJ ou SKU).

    numeric_features >> São variáveis que representam quantidades mensuráveis e são intrinsecamente numéricas.
    
    """

    # O ColumnTransformer aplica o OneHotEncoder nas features categóricas
    preprocessor = ColumnTransformer(
        transformers=[('categoria', OneHotEncoder(sparse_output=False), categorical_features)])

    """
    preprocessor = ColumnTransformer() >> é uma ferramenta do scikit-learn que permite aplicar diferentes transformações a diferentes subconjuntos de colunas simultaneamente (e de forma paralela).

        Função: Ele usa a lista de features que você definiu anteriormente (categorical_features e numeric_features) para saber o que fazer com cada coluna.

    'categoria': Nome dado a esta transformação

    OneHotEncoder(...): Este é o transformador de fato. O OneHotEncoder transforma as variáveis categóricas (como 'natureza_operacao', 'estado', 'ncm', etc.) em um formato numérico que o modelo pode usar. Ele cria uma nova coluna binária (0 ou 1) para cada valor único presente na coluna original.

    sparse_output=False: Garante que o resultado do One-Hot Encoding seja uma matriz densa (NumPy array) e não uma matriz esparsa, facilitando o uso subsequente na maioria dos modelos.

    categorical_features: Esta é a lista de colunas que você definiu que receberão o OneHotEncoder.

    """

    # 3.4. Criação do Pipeline e Treinamento
    modelo_ml = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(
            n_estimators=100, random_state=42, n_jobs=-1))
    ])

    # Divisão para validação
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)

    print("-> Iniciando treinamento do Random Forest...")
    modelo_ml.fit(X_train, Y_train)
    print("-> Treinamento concluído.")

    # 3.5. Avaliação
    Y_pred = modelo_ml.predict(X_test)

    mae = mean_absolute_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)

    print(f"--- Métrica do Modelo (Teste Simulado) ---")
    print(f"MAE (Erro Absoluto Médio): R$ {mae:,.2f}")
    print(f"R² (Coef. de Determinação): {r2:.4f}")
    print(f"O modelo de ML treinou com {len(X_train)} registros.")
    print("="*70)

    # Retorna o modelo completo para uso em tempo real
    return modelo_ml

# ==================================================================
# 4. FUNÇÃO DE SIMULAÇÃO PARA USO EXTERNO (APENAS ICMS)
# ==================================================================


def simulador_ml_apenas_icms(natureza_input, cliente_input, sku_input, valor_nf_input, estado_input, sku_ncm_lookup, modelo_ml):

    # --- 4.1 PREVISÃO DE ICMS (ML) ---
    valor_icms_previsto_ml = prever_icms_ml(
        natureza_input, cliente_input, sku_input, valor_nf_input, estado_input,
        sku_ncm_lookup, modelo_ml
    )

    # --- Output de Resumo (Opcional) ---
    print("\n" + "="*70)
    print("💰 RESULTADO DA PREVISÃO DE IMPOSTO (APENAS ICMS - ML) 💰")
    print(
        f"Natureza: {natureza_input} | SKU: {sku_input} | NF: R$ {valor_nf_input:,.2f} | Estado: {estado_input}")
    print("-" * 70)
    print(f"ICMS (ML) Previsto: R$ {valor_icms_previsto_ml:,.2f}")
    print("="*70)

    # Retorna o valor do ICMS previsto
    return valor_icms_previsto_ml


# ==========================================================
# 5. EXECUÇÃO PRINCIPAL E PREPARAÇÃO DOS DADOS
# ==========================================================
if __name__ == "__main__":

    # 5.1. CARREGAMENTO E CRIAÇÃO DA BASE - MERGE
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

    # 5.2. CRIAÇÃO DOS LOOKUPS
    print("[LOOKUPS] Criando lookups de NCM...")
    dfProjeto['cod_sku'] = pd.to_numeric(dfProjeto['cod_sku'], errors='coerce')

    # Apenas o lookup de NCM é necessário para o modelo de ML
    sku_ncm_lookup = dfProjeto.set_index(
        'cod_sku')['ncm'].astype(str).to_dict()

    # 5.3. TREINAMENTO DO MODELO RANDOM FOREST
    modelo_ml = treinar_modelo_icms(dfProjeto)

    # 5.4. EXECUÇÃO PARA TESTE (Bloco de Chamada)
    natureza_teste = 'Bonificação'
    # natureza_venda_teste = 'Consumidor final' # Removido
    cliente_teste = 19965
    sku_teste = 10344
    quantidade_teste = 1650
    valor_nf_teste = 105517.5
    estado_teste = 'SP'

    print("\n" + "="*70)
    print(
        f"EXECUTANDO TESTE APENAS ICMS (ML): {natureza_teste} | SKU: {sku_teste} | NF: R$ {valor_nf_teste:,.2f} | Estado: {estado_teste}")
    print("="*70)

    icms_ml = simulador_ml_apenas_icms(
        natureza_teste,
        cliente_teste,
        sku_teste,
        valor_nf_teste,
        estado_teste,
        sku_ncm_lookup,
        modelo_ml
    )

    print(f"\n✅ Processo finalizado. ICMS (ML) Retornado: R$ {icms_ml:,.2f}")
