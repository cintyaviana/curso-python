
'''
Para implementar uma analise exploratoria/estatistica de dados sugere-se o seguinte
contexto de trabalho:

1 - Carregamento e compreensão dos dados:

2 - Analise estatistica descritiva:

3 - Exploração de distribuição dos dados:

4 - Filtragem condicional:

5 - Relações entre variaveis:

6 - Normalização de padronização dos dados:

'''

# importar os recursos necessarios
# 1 - numpy
import numpy as np
# 2 - matplotlib
import matplotlib.pyplot as plt
# 3 - seaborn: biblioteca, tambem, para a plotagem de graficos
import seaborn as sb

# passo 1: carregar os dados - para este proposito vamos definir uma variavel para
# receber como valor o arquivo de dados - dataset .csv
dados = np.genfromtxt('iris_com_colunas.csv', delimiter=',', dtype=None,
                      encoding='utf-8', names=True, invalid_raise=False)

# passo 2 - exibir os nomes das colunas
print('Colunas: ', dados.dtype.names)
print()
# passo 3 - vamos exibir um determinado intervalo a partir do dataset
print('intervalo gerado:')
print(dados[:5])

# passo 4 - implementar operações estatisticas; para este proposito vamos criar algumas
# variaveis
print()

sepal_length = dados['sepal_length']
sepal_width = dados['sepal_width']
petal_length = dados['petal_length']
petal_width = dados['petal_width']

# acima, as quatro colunas numericas pertencem a quatro variaveis distintas

# passo 5 - selecionar a coluna categorica (strings) e atribui-la como valor para outra
# variavel
species = dados['species']

# passo 6 - aqui, vamos implementar as operações estatisticas
print('------------- Operações Estatisticas ------------------')
print()
media_sepal_length = np.mean(sepal_length)
media_sepal_width = np.mean(sepal_width)
media_petal_length = np.mean(petal_length)
media_petal_width = np.mean(petal_width)
print()

# passo 7: exibir dos valores das vars
print(f'Media do comprimento da sépala da planta: {media_sepal_length:.2f}')
print(f'Media da largura da sépala: {media_sepal_width:.2f}')
print(f'Media do comprimento da sépala da planta: {media_petal_length:.2f}')
print(f'Media da largura da sépala da planta: {media_petal_width:.2f}')

# -----------------------------------------------------------------------------------------------------------------------------------------

# passo 8 - filtrar os dados pro especie - acessando a respectiva coluna
# na sequencia, aplicar um tratamento para "limpar os dados"
especies = np.char.strip(dados['species'].astype(str), ' " " ')
print()
print('esta é a coluna especies')
print(especies)

# passo 9 - definir uma nova variavel para acessar a coluna e selecionar uma unica especie
setosa = dados[species == 'Setosa']
print()
print('\nDados de especie Iris-setosa:\n', setosa)

# passo 10 - definir uma nova var para atribuir como valor o calculo da media somente da
# especie setosa
print()
media_setosa_sepal_length = np.mean(setosa['sepal_length'])
media_setosa_sepal_width = np.mean(setosa['sepal_width'])
print(
    f'Media do comprimento da sepala da Setosa: {media_setosa_sepal_length:.2f}')
print(f'Media da largura da sepala da Setosa: {media_setosa_sepal_width:.2f}')

# -----------------------------------------------------------------------------------------------------------------------------------------
print()
# passo 11 -observação de valores unicos de uma coluna - fazendo uso do método/função np.
# unique()
print('valores unicos da coluna species')
especies_unicas = np.unique(species)

# passo 12 - vamos definir um loop para iterar/percorrer os valores atribuidos a var
# especies_unicas
for observadora in especies_unicas:
    # comparando os valores encontrados
    especies_dados = dados[species == observadora]
    # por observadora em relação ao valores que compõem a coluna spiceis
    media_petal_length = np.mean(especies_dados['petal_length'])
    print(
        f'Media do comprimento da petala para {observadora}: {media_petal_length:.2f}')
