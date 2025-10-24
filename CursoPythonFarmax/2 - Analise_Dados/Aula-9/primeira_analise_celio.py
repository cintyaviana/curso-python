'''
Para implementar uma analise exploratoria/estatistica de dados sugere-se o seguinte contexto de trabalho:

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
import matplotlib as plt
# 3 - seaborn: biblioteca, tambem, para a plotagem de graficos
import seaborn as sb

# passo 1: carregar os dados - para este proposito vamos definir uma variavel para receber como valor o arquivo de dados - dataset .csv
dados = np.genfromtxt('iris_com_colunas.csv', delimiter=',',
                      dtype=None, encoding='utf-8', names=True, invalid_raise=False)
'''
np.genformtxt(...): é uma função numpy usada para ler arquivos de texto como, por exemplo, .csv

'iris_com_colunas.csv': nome do arquivo de dados que estamos carregando

delimiter=',': indicando que os dados estão separados por virgula (este é o padrão dos arquivos .csv)

dtype=None: permite que o Numpy "deduza" automaticamente o tipo de dados de cada coluna(float, string, etc.)

enconding='utf-8': estamos tentando garantir que caracteres especiais possam ser lidos sem erro

names=True: significa que a primeira linha do arquivo contem os nomes das colunas e deve ser usada como cabeçalho

invalid_raise=False: faz com que as linhas que possam apresentar eventuais problemas ou dados ausentes sejam ignoradas ao inves de causar um erro de carregamento/leitura de dados
'''

# passo 2 - exibir os nomes das colunas
print('Colunas: ', dados.dtype.names)
print()
# passo 3 - vamos exibir um determinado intervalo a partir do dataset
print('intervalo gerado:')
print(dados[:5])

# ---------------------------------------------------------------------------------

# passo 4 - implementar operações estatisticas; para este proposito vamos criar algumas variaveis
print()

sepal_length = dados['sepal_length']
sepal_width = dados['sepal_width']
petal_length = dados['petal_length']
petal_width = dados['petal_width']

# acima, as quatro colunas numericas pertencem a quatro variaveis distintas

# passo 5 - selecionar a coluna categorica (strings) e atribui-la como valor para outra variavel
species = dados['species']

# passo 6 - aqui, vamos implementar as operações estatisicas
print('--------- Operações Estatisticas ---------------------')
print()
media_sepal_length = np.mean(sepal_length)
media_sepal_width = np.mean(sepal_width)
media_petal_length = np.mean(petal_length)
media_petal_width = np.mean(petal_width)
print()
# passo 7: exibir dos valores das vars
print(f'Media do comprimento da sépala da planta: {media_sepal_length:.2f}')
print(f'Media da largura da sépala: {media_sepal_width:.2f}')
print(f'Media do comprimento da pétala da planta: {media_petal_length:.2f}')
print(f'Media da largura da pétala da planta: {media_petal_width:.2f}')

# -------------------------------------------------------------------------------

# passo 8 - filtrar os dados pro especie - acessando a respectiva coluna
# na sequencia, aplicar um tratamento para "limpar os dados"
species = np.char.strip(dados['species'].astype(str), ' " " ')
print()
print('esta é a coluna species')
print(species)

# passo 9 - definir uma nova variavel para acessar a coluna e selecionar uma unica especie
setosa = dados[species == 'Setosa']
print()
print('\nDados de especie Iris-setosa:\n', setosa)

# passo 10 - definir uma nova var para atribuir como valor o calculo da media somente da especie setosa
print()
media_setosa_sepal_length = np.mean(setosa['sepal_length'])
media_setosa_sepal_width = np.mean(setosa['sepal_width'])
print(
    f'Media do comprimento da sepala da Setosa: {media_setosa_sepal_length:.2f}')
print(f'Media da largura da sepala da Setosa: {media_setosa_sepal_width:.2f}')

# ----------------------------------------------------------------------------
print()
# passo 11  -observação de valores unicos de uma coluna - fazendo uso do método/função np.unique()
print('valores unicos da coluna species')
especies_unicas = np.unique(species)

# passo 12 - vamos definir um loop para iterar/percorrer os valores atribuidos a var especies_unicas
for observadora in especies_unicas:
    # comparando os valores encontrados por observadora em relação ao valores que compõem a coluna spiceis
    especies_dados = dados[species == observadora]
    media_petal_length = np.mean(especies_dados['petal_length'])
    print(
        f'Media do comprimento da petala para {observadora}: {media_petal_length: .2f}')

'''
 este trecho de codigo está calculando a média do comprimento da pétala(petal_length) para cada espécie no conjunto de dados

 especies_unicas = np.unique(especies): retornando uma lista com os nome unicos das especies presentes no array especies

 for observadora in especies_unicas: inicia um loop/laço que irá percorrer cada especie unica do conjunto

  especies_dados = dados[especies == observadora]: criando um filtro para o array/conjundo de dados selecionado onde a coluna especies corresponde ao valor da var observadora

  media_petal_length = np.mean(especies_dados['petal_length']): estamos acessando a couna petal_length do subconjunto de dados de especies e calcuando sua média

'''

# passo 13 - fazer uma contagem das especies
contagem_especies = np.unique(species, return_counts=True)
print()
print('Contagem')
print(contagem_especies)
print()

print('------------------- OUTRAS OPERAÇÕES -------------------------')
print()
print('------ Resumo Estatistico do dataset -------------')
# Passo 14 - fazer um resumo estatistico do dataset - fazendo uso do numpy
mediana_sepal_length = np.median(sepal_length)
desvio_padrao_sepal_length = np.std(sepal_length)
variancia_sepal_length = np.var(sepal_length)
min_sepal_length = np.min(sepal_length)
max_sepal_length = np.max(sepal_length)

# Exibindo os valores do resumo estatistico
print(f'Mediana do comprimento da sépala: {mediana_sepal_length}')
print(
    f'Desvio-padrão do comprimento da sépala: {desvio_padrao_sepal_length: .2f}')
print(f'Variancia do comprimento da sépala: {variancia_sepal_length: .2f}')
print(f'Comprimento minimo da sépala: {min_sepal_length}')
print(f'Comprimento maximo da sépala:{max_sepal_length}')

print()
print('================================== CORRELAÇÃO ================================')

# Passo 15: definir uma variavel para receber como valor a função que vai auxiliar na observação da correlação entre variaveis
correlacao = np.corrcoef(petal_length, petal_width)[0, 1]
print(
    f'Correlação entre o comprimento e a largura da pétala: {correlacao: .2f}')

"""
Correlação nada mais é do que uma matriz numérica entre duas variaveis; no nosso caso de analise a correlação será estabelecida entre petal_length e petal_width; a partir dos dados atribuídos, `estas duas variaveis teremos uma matriz de correlação resultante do cálculo aplicado pela função np.corrcoef() - dada por esta expressão: np.corrcoef(petal_length, petal_width).

Agora temos os parâmetros [0,1]: estes dois parâmetros correspondem ao tamanho da matriz este é o tamanho da matriz 2x2

  0 1 - estes são os indices de colunas da matriz
0     - estes são os indices de linha da matriz
1   

"""
