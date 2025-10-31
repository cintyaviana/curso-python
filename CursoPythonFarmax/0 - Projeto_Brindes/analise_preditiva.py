# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS NECESSÁRIAS
# ==========================================================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
from fato_projeto import get_fato_projeto


# ==========================================================
# 1. CARREGAR DADOS E PRÉ-PROCESSAMENTO
# ==========================================================

print("="*50)
print("[ML] 1. INICIANDO O PROJETO DE MACHINE LEARNING")
print("="*50)

# Carrega a base de dados preparada
df = get_fato_projeto()

# Colunas críticas para treinar o novo modelo (custo_final_unitario REMOVIDA)
df.dropna(subset=['estado', 'cod_sku', 'custo_total', 'impostos_total',
                  'custo_final', 'quantidade', 'custo_unitario'], inplace=True)

print("\n[ML] DataFrame base carregado e preparado.")

# ==========================================================
# 2. ENGENHARIA DE CARACTERÍSTICAS E DEFINIÇÃO DO TARGET
# ==========================================================

print("\n[ML] 2. Análise de Premissas (Médias de Imposto e Custo)")

# --- NOVO TARGET: Imposto Unitário por Custo Unitário Base ---
# Esta é a taxa de imposto unitário.

df['imposto_unitario'] = np.divide(
    df['impostos_total'],
    df['quantidade'],
    out=np.zeros_like(df['impostos_total'], dtype=float),
    where=df['quantidade'] != 0
)

# 💡 Novo TARGET: Prever o Imposto Unitário (R$)
TARGET = 'imposto_unitario'

# --- Premissa 1: Imposto Unitário Médio por Estado ---
imposto_unitario_por_estado_medio = df.groupby(
    'estado')[TARGET].mean().reset_index()
imposto_unitario_por_estado_medio.rename(
    columns={TARGET: 'imposto_unitario_medio_estado'}, inplace=True)

# --- Premissa 2: Custo Unitário Base Médio Histórico por SKU (NOVA PREMISSA DE CUSTO BASE) ---
custo_unitario_por_sku_medio = df.groupby(
    'cod_sku')['custo_unitario'].mean().reset_index()
custo_unitario_por_sku_medio.rename(
    columns={'custo_unitario': 'custo_unitario_medio_sku'}, inplace=True)


# --- Merge das Premissas para o Treinamento do Modelo ---
df = df.merge(imposto_unitario_por_estado_medio, on='estado', how='left')
df = df.merge(custo_unitario_por_sku_medio, on='cod_sku', how='left')

# As FEATURES agora são as variáveis categóricas e as médias calculadas
FEATURES = ['estado', 'cod_sku',
            'imposto_unitario_medio_estado', 'custo_unitario_medio_sku']

X = df[FEATURES]
y = df[TARGET]

# Preparação das colunas (Pipeline) - Codifica apenas as variáveis categóricas
preprocessor = ColumnTransformer(
    transformers=[
        # OneHotEncoder para Estado e SKU
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['estado', 'cod_sku'])
    ],
    # As colunas de médias passam sem transformação
    remainder='passthrough'
)

# Cria o pipeline de pré-processamento e o modelo de Regressão Linear
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])

# ==========================================================
# 3. TREINAMENTO DO MODELO
# ==========================================================

# Divide os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n[ML] 3. Treinando o Modelo de Predição de Imposto Unitário...")
model.fit(X_train, y_train)


# ==========================================================
# 4. FUNÇÕES DE CLASSIFICAÇÃO E PREVISÃO INTERATIVA (AJUSTADAS)
# ==========================================================

# Definição dos Limiares para a Classificação (Baixo, Médio, Alto)
# Mantidos baseados no Custo Final Total da base histórica
Q1 = df['custo_final'].quantile(0.33)
Q3 = df['custo_final'].quantile(0.66)

CUSTO_LIMIARES = {
    'BAIXO': Q1,
    'MÉDIO': Q3
}


def classificar_custo(custo_previsto, limiares):
    """Classifica o custo total previsto como Baixo, Médio ou Alto."""
    if custo_previsto <= limiares['BAIXO']:
        return "BAIXO"
    elif custo_previsto <= limiares['MÉDIO']:
        return "MÉDIO"
    else:
        return "ALTO"


# FUNÇÃO DE PREVISÃO AGORA PREVÊ O IMPOSTO UNITÁRIO (TARGET)
def prever_custo_interativo(cod_sku, estado, quantidade, modelo, imposto_unitario_premissa, custo_premissa, limiares):
    """
    Realiza a simulação de custo final total, baseando o Custo do Produto na 
    MÉDIA HISTÓRICA DO CUSTO UNITÁRIO BASE POR SKU e prevendo o Imposto Unitário.
    """

    # 1. OBTER PREMISSAS CRÍTICAS

    # Premissa de Custo Unitário Base Histórico (Média do SKU)
    custo_unitario_medio_sku = custo_premissa[custo_premissa['cod_sku']
                                              == cod_sku]['custo_unitario_medio_sku']
    if custo_unitario_medio_sku.empty:
        custo_unitario_base_real = custo_premissa['custo_unitario_medio_sku'].mean(
        )
        print(
            f"[AVISO] SKU '{cod_sku}' não encontrado. Usando Custo Unitário Base Médio Histórico Geral de R$ {custo_unitario_base_real:,.2f}."
        )
    else:
        custo_unitario_base_real = custo_unitario_medio_sku.iloc[0]

    # Premissa de Imposto Unitário Médio por Estado
    imposto_medio_val = imposto_unitario_premissa[imposto_unitario_premissa['estado']
                                                  == estado]['imposto_unitario_medio_estado']
    if imposto_medio_val.empty:
        imposto_medio_val = imposto_unitario_premissa['imposto_unitario_medio_estado'].mean(
        )
        print(
            f"[AVISO] Estado '{estado}' não encontrado. Usando Imposto Unitário Médio Geral de R$ {imposto_medio_val:,.2f}")
    else:
        imposto_medio_val = imposto_medio_val.iloc[0]

    # 2. MONTAR INPUT PARA O MODELO
    input_data = pd.DataFrame({
        'estado': [estado],
        'cod_sku': [cod_sku],
        'imposto_unitario_medio_estado': [imposto_medio_val],
        'custo_unitario_medio_sku': [custo_unitario_base_real]
    })

    # 3. FAZER A PREDIÇÃO DE IMPOSTO UNITÁRIO (ML)
    imposto_unitario_previsto = modelo.predict(input_data)[0]

    # Garante que o imposto não seja negativo (embora o modelo seja treinado para prever > 0)
    imposto_unitario_previsto = max(0, imposto_unitario_previsto)

    # 4. CÁLCULOS FINAIS COM A REGRA DE NEGÓCIO

    # CUSTO DO PRODUTO TOTAL (Regra: Custo Base Médio Histórico * Quantidade)
    custo_produto_total = custo_unitario_base_real * quantidade

    # Imposto Total Previsto (Imposto Unitário Previsto * Quantidade)
    imposto_total_previsto = imposto_unitario_previsto * quantidade

    # Custo Total Final (Custo Produto Total + Imposto Total)
    custo_total_final = custo_produto_total + imposto_total_previsto

    # 5. CLASSIFICAÇÃO
    classificacao = classificar_custo(custo_total_final, limiares)

    # 6. RESPOSTA FORMATADA
    print("\n" + "="*80)
    print("RESPOSTA DA SIMULAÇÃO PREDITIVA:")
    print("-" * 80)
    print(f"SKU: {cod_sku} | Estado: {estado} | Quantidade: {quantidade}")
    print(
        f"Custo Unitário Base Histórico (Média do SKU): R$ {custo_unitario_base_real:,.2f}"
    )
    print("-" * 80)

    print(
        f"Custo de Produto Total (Média SKU * Quantidade): R$ {custo_produto_total:,.2f}")
    print(
        f"Imposto Unitário Previsto (ML):                  R$ {imposto_unitario_previsto:,.2f}")
    print(
        f"Custo de Imposto Total (Previsto):               R$ {imposto_total_previsto:,.2f}")
    print(
        f"Custo Total Final Previsto (Global):             **R$ {custo_total_final:,.2f}**")

    print("-" * 80)
    print(f"Classificação do Custo Total Final: **{classificacao}**")
    print("="*80)


def interagir_com_usuario(imposto_unitario_premissa, custo_premissa, modelo, limiares):
    """Lida com a interação de entrada de dados do usuário."""

    print("\n" + "#"*70)
    print("## Ferramenta de Simulação Preditiva de Custo de Brindes ##")
    print(f"## Premissa de Custo Base: Média Histórica do SKU ##")
    print("#"*70)

    # 1. Entrada de SKU
    cod_sku = input("Digite o Código do SKU (Ex: 001002003): ").strip().upper()

    # 2. Entrada de Estado
    estado = input("Digite a UF de Destino (Ex: SP, RJ, MG): ").strip().upper()

    # 3. Entrada de Quantidade (Tratamento de erro simples)
    while True:
        try:
            quantidade = int(input("Digite a Quantidade de Brindes (SKUs): "))
            if quantidade <= 0:
                raise ValueError
            break
        except ValueError:
            print(
                "Entrada inválida. Digite um número inteiro positivo para a quantidade.")

    # Chama a função de previsão
    prever_custo_interativo(
        cod_sku=cod_sku,
        estado=estado,
        quantidade=quantidade,
        modelo=modelo,
        imposto_unitario_premissa=imposto_unitario_premissa,
        custo_premissa=custo_premissa,
        limiares=limiares
    )


# ==========================================================
# 5. EXECUÇÃO DO MÓDULO (INTERAÇÃO COM O USUÁRIO)
# ==========================================================

if __name__ == '__main__':

    # Imprime os limiares de classificação
    print(f"\nLimiares de Classificação (Base Histórica):")
    print(f"  - BAIXO: Até R$ {CUSTO_LIMIARES['BAIXO']:,.2f}")
    print(
        f"  - MÉDIO: R$ {CUSTO_LIMIARES['BAIXO']:,.2f} a R$ {CUSTO_LIMIARES['MÉDIO']:,.2f}")
    print(f"  - ALTO: Acima de R$ {CUSTO_LIMIARES['MÉDIO']:,.2f}")

    # Inicia o loop de interação com o usuário
    # NOTE: imposto_unitario_por_estado_medio substituiu imposto_por_estado_medio
    interagir_com_usuario(imposto_unitario_por_estado_medio,
                          custo_unitario_por_sku_medio, model, CUSTO_LIMIARES)
