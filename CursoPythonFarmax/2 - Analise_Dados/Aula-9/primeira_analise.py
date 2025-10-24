'''
Para implementar uma analise exploratoria/estatistica de dados sugere-se o seguinte
contexto de trabalho:

1 - Carregamento e compreensão dos dados: Leitura de planilhas - ou qualquer outro
dataset - com nomes de colunas. Identificação e exibição das colunas.

2 - Analise estatistica descritiva: Cálculo de média, mediana, desvio padrão, variância,
mínimos e máximos. Análise por espécie (ex.: média do comprimento da pétala para Setosa,
VersicoloR, Virginica).

3 - Exploração de distribuição dos dados: Contagem de cada espécie. Cálculo de quartis (Q1, Q2, Q3).

4 - Normalização de padronização dos dados: Aplicação de normalização min-max e padronização

5 - Filtragem condicional: Seleção de registros com comprimento da sépala maior que 5.0.

6 - Relações entre variaveis: Correlação entre comprimento e largura da pétala. Matriz de correlação entre todas as variáveis numéricas.

'''

# importar os recursos necessarios
# 0 - Biblioteca OS para manipulação de caminhos (CORREÇÃO DE CAMINHO)
import os
# 1 - numpy
import numpy as np
# 2 - matplotlib (Usando a convenção padrão pyplot para gráficos)
import matplotlib.pyplot as plt
# 3 - seaborn: biblioteca, tambem, para a plotagem de graficos
import seaborn as sns

# ==============================================================================
# 1 - CARREGAMENTO E COMPREENSÃO DOS DADOS
# ==============================================================================

# Defina o nome do arquivo
NOME_DO_ARQUIVO = 'iris_com_colunas.csv'

# Tenta obter o diretório do script atual (SOLUÇÃO ROBUSTA PARA O FILE NOT FOUND)
try:
    # __file__ é uma variável que armazena o caminho do script.
    DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
    CAMINHO_COMPLETO = os.path.join(DIRETORIO_ATUAL, NOME_DO_ARQUIVO)

    # passo 1: carregar os dados
    dados = np.genfromtxt(CAMINHO_COMPLETO, delimiter=',',
                          dtype=None, encoding='utf-8', names=True, invalid_raise=False)

except FileNotFoundError:
    print(f"\nERRO CRÍTICO: O arquivo '{NOME_DO_ARQUIVO}' NÃO FOI ENCONTRADO.")
    print(f"Por favor, verifique se o arquivo está em: {DIRETORIO_ATUAL}")
    # Encerra o script se o arquivo não for encontrado
    exit()

# passo 2 - exibir os nomes das colunas
print('Colunas: ', dados.dtype.names)
print()
# passo 3 - vamos exibir um determinado intervalo a partir do dataset
print('intervalo gerado (5 primeiras linhas):')
print(dados[:5])

# ---------------------------------------------------------------------------------

# passo 4 - implementar operações estatisticas; para este proposito vamos criar algumas variaveis
print('\n--- Extração das Colunas Numéricas ---')

sepal_length = dados['sepal_length']
sepal_width = dados['sepal_width']
petal_length = dados['petal_length']
petal_width = dados['petal_width']

# passo 5 - selecionar a coluna categorica (strings)
species_original = dados['species']

# ==============================================================================
# 2 - ANÁLISE ESTATÍSTICA DESCRITIVA GERAL
# ==============================================================================

# passo 6 - aqui, vamos implementar as operações estatisicas
print('\n--------- Operações Estatisticas Gerais ---------------------')

media_sepal_length = np.mean(sepal_length)
media_sepal_width = np.mean(sepal_width)
media_petal_length = np.mean(petal_length)
media_petal_width = np.mean(petal_width)

# passo 7: exibir dos valores das vars
print(f'Média do comprimento da sépala da planta: {media_sepal_length:.2f}')
print(f'Média da largura da sépala: {media_sepal_width:.2f}')
print(f'Média do comprimento da pétala da planta: {media_petal_length:.2f}')
print(f'Média da largura da pétala da planta: {media_petal_width:.2f}')


# ==============================================================================
# 4 - FILTRAGEM CONDICIONAL E ESTATÍSTICAS POR GRUPO
# ==============================================================================

# passo 8 - filtrar os dados por especie e limpar (remover espaços/aspas)
species = np.char.strip(dados['species'].astype(str), ' " " ')
print('\nColuna species após limpeza:')
print(np.unique(species))

# passo 9 - definir uma nova variavel para selecionar uma unica especie
setosa = dados[species == 'Setosa']

# passo 10 - calcular a média somente da especie setosa
media_setosa_sepal_length = np.mean(setosa['sepal_length'])
media_setosa_sepal_width = np.mean(setosa['sepal_width'])
print(
    f'\nMédia do comprimento da sépala da Setosa: {media_setosa_sepal_length:.2f}')
print(f'Média da largura da sépala da Setosa: {media_setosa_sepal_width:.2f}')

# ----------------------------------------------------------------------------

# passo 11 - observação de valores unicos de uma coluna
print('\n--- Média do Comprimento da Pétala por Espécie ---')
especies_unicas = np.unique(species)

# passo 12 - loop para iterar/percorrer os valores e calcular a média por grupo
for observadora in especies_unicas:
    especies_dados = dados[species == observadora]
    media_petal_length_especie = np.mean(especies_dados['petal_length'])
    print(
        f'Média do comprimento da pétala para {observadora}: {media_petal_length_especie:.2f}')

# passo 13 - fazer uma contagem das especies
contagem_especies = np.unique(species, return_counts=True)
print('\nContagem de Espécies (Nomes, Contagens):')
print(contagem_especies)

# ==============================================================================
# 2 - RESUMO ESTATÍSTICO DETALHADO
# ==============================================================================

print('\n------------------- OUTRAS OPERAÇÕES -------------------------')
print('\n------ Resumo Estatístico do Comprimento da Sépala -------------')
# Passo 14 - fazer um resumo estatistico do dataset
mediana_sepal_length = np.median(sepal_length)
desvio_padrao_sepal_length = np.std(sepal_length)
variancia_sepal_length = np.var(sepal_length)
min_sepal_length = np.min(sepal_length)
max_sepal_length = np.max(sepal_length)

# Exibindo os valores do resumo estatistico
print(f'Mediana do comprimento da sépala: {mediana_sepal_length:.2f}')
print(
    f'Desvio-padrão do comprimento da sépala: {desvio_padrao_sepal_length:.2f}')
print(f'Variância do comprimento da sépala: {variancia_sepal_length:.2f}')
print(f'Comprimento mínimo da sépala: {min_sepal_length:.2f}')
print(f'Comprimento máximo da sépala: {max_sepal_length:.2f}')

# ==============================================================================
# 5 - RELAÇÕES ENTRE VARIÁVEIS (CORRELAÇÃO)
# ==============================================================================

print('\n================================== CORRELAÇÃO ================================')

# Passo 15: definir uma variavel para receber a correlação entre petal_length e petal_width
correlacao = np.corrcoef(petal_length, petal_width)[0, 1]
print(
    f'Correlação entre o comprimento e a largura da pétala: {correlacao:.2f}')

"""
Correlação nada mais é do que uma matriz numérica entre duas variaveis; no nosso caso de analise a correlação será estabelecida entre petal_length e petal_width; a partir dos dados atribuídos, `estas duas variaveis teremos uma matriz de correlação resultante do cálculo aplicado pela função np.corrcoef() - dada por esta expressão: np.corrcoef(petal_length, petal_width).

Agora temos os parâmetros [0,1]: estes dois parâmetros correspondem ao tamanho da matriz este é o tamanho da matriz 2x2

  0 1 - estes são os indices de colunas da matriz
0  [[1.0,096]]   - estes são os indices de linha da matriz
1   [0.96, 1.0]]

Acima, a diagonal, que tem o valor - sempre $1.0$ (este valor/diagonal determina a correlação de uma variável com ela mesma); o valor importante para a nossa análise está na outra diagonal - $0.96$ e $0.96$ - pois é este o valor que define a correlação entre pétala, no comprimento e na largura. Significa que a correlação entre comprimento e largura da pétala é "muito" forte - traduzindo: na medida em que o comprimento da pétala aumenta, aumenta, também, sua largura

"""

print()
print('========= GRÁFICO =============')
# passo 16: indicar o "estilo" visual que este grafico terá
# indica que as linhas do gird do grafico serão claras
sns.set_theme(style='whitegrid')

# definir o tamanho da figura - do grafico - que será exibida
plt.figure(figsize=(8, 5))  # 8" de largura x 5" de altura

# definir os elementos de dispersão exibidos no grafico
sns.scatterplot(x=petal_length, y=petal_width, color='blue', s=60)

"""
neste grafico temos 2 eixos: x e y;
o eixo x mostra o comprimento da pétala (petal-length) já, o eixo y (petal_width) mostra a
largura da pétala

color=blue: define a cor azul para cada ponto que surgirá no grafico - cada um deste
pontos representa uma flor

s=60: aqui, estamos definindo o tamanho dos pontos (quanto mairo o numero, maior será o
tamanho dos pont)
"""
# definir a linha de tendencia (regressão linear)
sns.regplot(x=petal_length, y=petal_width, scatter=False, color='red')

"""
o eixo x mostra o comprimento da pétala(petal-length) já, o eixo y(petal_width) mostra a
largura da pétala
scatter=False: impede que os pontos sejam repetidos, pois já foram exibidos pela função
scatterplot()

color=red: define a cor vermelha para a linha de tendencia (regressão)
"""

# adicionar os titulos/labels/rotulos/nomenclaturas no grafico
plt.title('Correlação entre comprimento e largura da pétala', fontsize=12)

plt.xlabel('Comprimento da pétala', fontsize=12)  # label do eixo x

plt.ylabel('Largura da pétala', fontsize=12)  # label do eixo y

# adicionar a exibição do valor da correlação diretamente no grafico
correlacao = np.corrcoef(petal_length, petal_width)[0, 1]

# adicionar um texto com o valor da correlação
plt.text(min(petal_length), max(petal_width)*0.9, f'Correlação: {correlacao:.2f}',
         fontsize=12, color='darkblue')

# ajusta e exibir o gráfico
plt.tight_layout()
plt.show()

"""
min(petal_length), max(petal_width)*0.9: esta é a posição do texto no grafico; é calculada com base min() e max() das variaveis
"""
