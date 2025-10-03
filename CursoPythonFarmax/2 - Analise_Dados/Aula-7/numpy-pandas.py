
# importar o recurso numpy para as operações com dados
import pandas as pd  # alias da lib pandas
import numpy as np  # aqui, a lib numpy recebe um apelido convencional

# criar uma lista de de numeros
grupo = [[31, 25, 56], [4, 89, 102], [78, 875, 123]]

# neste passo, vamos criar um matriz usando o recurso numpy - para este porposito, vamos
# definir uma variavel que recebe como valor o método/função matrix() - com origem no numpy
umaMatriz = np.matrix(grupo)
print()
print('-'*50)

# verificar se o data type da variavel umaMatriz é, realmente, uma matriz
print(type(umaMatriz))
print()
print('-'*50)

# verificar o formato /dimensoes da matriz
print(np.shape(umaMatriz))
print()
print('-'*50)
# fazer uso do método/função mean() -> este é o recurso que calcula a media simples -
# considerando todos os valores que compoem a matriz
print(np.mean(umaMatriz))
print()
print('-'*50)

print('================ ALGUMAS OPECAÇÕES COM MATRIZ======================')

# agora, serão criadas duas matrizes -ambas receberão valores distintos
# array(): é uma função/método - com origem no numpy - para criar vetores/arrays de valores
matriz1 = np.array([[2, 4], [5, -6]])
matriz2 = np.array([[9, -4], [3, 5]])

somaMatrizes = matriz1 + matriz2

# exibir o resultado
print('Soma da matrizes', somaMatrizes)
print()
print('-'*50)

# Subtração de matrizes
subMatrizes = matriz1 - matriz2
print('Subtração de matrizes:', subMatrizes)
print()
print('-'*50)

# multiplicação das matrizes - elemento a elemento
multiMatrizes = matriz1 * matriz2
print('Multiplicação das matrizes: ', multiMatrizes)
print()
print('-'*50)

# divisão entre as matrizes
diviMatrizes = matriz1 / matriz2
print('Divisão entre as matrizes: ', diviMatrizes)
print()
print('-'*50)

# produto matricial (multiplicação de matrizes)
produtoMatrizes = np.dot(matriz1, matriz2)
print('Produto matricial: ', produtoMatrizes)
print()
print('-'*50)

# transposição de matrizes
transposta = np.transpose(matriz1)
print('Transposição da matriz1:', transposta)
print()
print('-'*50)


print('================== OPERAÇÕES COM NUMPY/PANDAS ==================')

# importar o pandas

# definir um recurso que passaremos a conhecer como Series: nada mais é do que uma matriz unidimensional, ou seja, de uma única colua
umaSerie = pd.Series([1, 2, 3, np.nan, 6, 8, 'Ola'])

# acima, np.nan é o recurso que oferece a possibilidade de trabalhar com um elemento numerico(not-a-number): origem no numpy
print(umaSerie)
print()
print('-'*50)

# neste passo, será definida uma nova variavel para receber como valor um conjunto de dados
algumasDatas = pd.date_range('20251001', periods=6)
print(algumasDatas)

"""
date_range(): cria um conjunto de dados baseado num intervalo de valores com a
caracteristica de datas; alem disso, temos 2 parametros

20251001: este é o parametro que estabelece o ponto inicial do intervalo de valores
de data. 2023-10-01

periods=6: aqui, está definido a quantidade de valores que compõem o intervalo de
datas que serão geradas pela função

por padrão, a função date_range utiliza-se de frequencia diaria para gerar o
intervalo de valores => freq='D'

o resultado esperado é algo semelhante a isto: '2025-10-01', '2025-10-02', '2025-10-03' ...

"""
