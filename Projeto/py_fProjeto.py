# ==================================================================
# 0. IMPORTAÇÕES
# ==================================================================
from py_fBrinde import get_fBrinde
from py_dProduto import get_dProduto

import pandas as pd

# ==================================================================
# 1. FUNÇÃO PREDITIVA: CUSTO UNITÁRIO MÉDIO E CUSTO TOTAL PREVISTO
# ==================================================================
# Prevê o custo total de um SKU baseado no custo médio histórico.


def prever_custo_total(sku_input, quantidade_input, modelo_custo_unitario):
    custo_unitario_medio = modelo_custo_unitario[sku_input]
    custo_total_previsto = custo_unitario_medio * quantidade_input

    return custo_total_previsto, custo_unitario_medio

    """
     "modelo_custo_unitario" >> é um dicionário (chave: SKU, valor: custo unitário médio) criado a partir do cálculo na média dos custos do SKU

    """

# ==================================================================
# 2. FUNÇÃO PREDITIVA: ICMS
# ==================================================================
# Prevê o valor_icms baseado em Natureza, Estado e Alíquota histórico.


def prever_icms(natureza_input, cliente_input, sku_input, valor_nf_input, estado_input,
                sku_ncm_lookup, cliente_cnpj_lookup, estado_aliqicms_lookup):

    # 2.1 APURAÇÃO SE INCIDE OU NÃO ICMS ---------------------------

    # 2.1.1 REGRA ICMS: EXPORTAÇÃO E AMOSTRA GRÁTIS
    if natureza_input in ['Exportação', 'Amostra grátis']:
        return 0.0, f"Natureza '{natureza_input}' não incide ICMS.", 0.0
        """
        0.0 = valor_icms_previsto 
        0.0 = aliquota  
        """

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

            return 0.0, 0.0

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

    return valor_icms_previsto, aliquota

# ==================================================================
# 3. FUNÇÃO PREDITIVA: ICMS-ST
# ==================================================================
# Prevê o valor_icms_st baseado em Natureza, Estado e Alíquota.


def prever_icms_st(natureza_input, cliente_input, sku_input, valor_nf_input, estado_input,
                   sku_ncm_lookup, cliente_cnpj_lookup, valor_icms_previsto):

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
# 5. TREINAMENTO DO MODELO CUSTO UNITÁRIO
# ==================================================================
# Cria o dicionário de busca para o custo unitário em relação ao SKU.

print("[MODELO] Criando modelo de custo médio por SKU...")

dfProjeto['cod_sku'] = pd.to_numeric(
    dfProjeto['cod_sku'])

modelo_custo_unitario = dfProjeto.groupby(
    'cod_sku')['custo_unitario'].mean().to_dict()

"""
pd.to_numeric() >> garante que a coluna de código do produto (cod_sku) seja tratada como um tipo de dado numérico.

errors='coerce': Este é um argumento de segurança. Se o Pandas encontrar qualquer valor na coluna que não possa ser convertido para um número (como, por exemplo, um texto "N/A"), ele irá substituí-lo por NaN (Not a Number).

.groupby() >> Agrupa todas as linhas do DataFrame (dfProjeto) que possuem o mesmo código de SKU.

.mean() >> Pega todos os valores na coluna custo_unitario e calcula a média aritmética em relação ao SKU.

.to_dict() >> O resultado do cálculo da média (que é uma Série do Pandas) é transformado em um dicionário.

    >> O cod_sku se torna a chave (key).

    >> O Custo Unitário Médio calculado se torna o valor.

"""

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

# 6.3: ESTADO -> ALÍQUOTA
df_aliquota_icms = dfProjeto[
    pd.to_numeric(dfProjeto['aliquota_icms']) > 0.0]

"""
errors='coerce' >> converte valores "N/A" pelo valor especial NaN (Not a Number).
"""

estado_aliqicms_lookup = (
    df_aliquota_icms.set_index('estado')['aliquota_icms'] / 100.0
).to_dict()


# ==================================================================
# 7. FUNÇÃO PRINCIPAL DE TESTE
# ==================================================================
# Chama as funções prever_custo_total, prever_icms e prever_icms_st

def simulador(natureza_input, cliente_input, sku_input, quantidade_input, valor_nf_input, estado_input, modelo_custo_unitario, sku_ncm_lookup, cliente_cnpj_lookup, estado_aliqicms_lookup):

    # 7.1 Previsão de Custo Total
    custo_total_previsto, custo_unitario_previsto = prever_custo_total(
        sku_input, quantidade_input, modelo_custo_unitario)

    # 7.2 Previsão de ICMS
    valor_icms_previsto, aliquota_utilizada = prever_icms(
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

    # 7.4. CÁLCULO FINAL E EXIBIÇÃO
    soma_total_prevista = custo_total_previsto + \
        valor_icms_previsto + valor_icms_st_previsto
    percentual_custo_nf = (soma_total_prevista / valor_nf_input) * 100

    # Output Final
    print("\n" + "="*50)
    print("💰 CUSTO TOTAL PREVISTO 💰")
    print(f"SKU: {sku_input} | Cliente: {cliente_input} | Natureza: {natureza_input} | Estado: {estado_input}")
    print("-" * 50)

    print(f"Custo Unitário Médio: R$ {custo_unitario_previsto:,.2f}")
    print(f"Custo Total (Produto): R$ {custo_total_previsto:,.2f}")
    print(f"ICMS ({aliquota_utilizada*100:.2f}%): R$ {valor_icms_previsto:,.2f}")
    print(f"ICMS-ST: R$ {valor_icms_st_previsto:,.2f}")
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
    cliente_teste = 20072
    sku_teste = 11362
    quantidade_teste = 1
    valor_nf_teste = 58.81
    estado_teste = 'RJ'

    resultado_final = simulador(
        natureza_teste,
        cliente_teste,
        sku_teste,
        quantidade_teste,
        valor_nf_teste,
        estado_teste,
        modelo_custo_unitario,
        sku_ncm_lookup,
        cliente_cnpj_lookup,
        estado_aliqicms_lookup
    )
    print(
        f"✅ Processo finalizado. Custo Total Previsto Retornado: R$ {resultado_final:,.2f}")
