# importar o recurso numpy para as operações com dados
import pandas as pd  # aqui, a lib pandas recebe um apelido convencional
import numpy as np  # aqui, a lib numpy recebe um apelido convencional


# Definir um recurso que passaremos a conhecer como Series: nada mais é do que uma matriz unidimensional, ou seja, de uma única colua
umaSerie = pd.Series([1, 2, 3, 6, 8, 'Ola'],
                     index=pd.date_range('20251001', periods=6))
print(umaSerie)


# Neste passo, será definida uma nova variavel para receber como valor um conjunto de dados
algumasDatas = pd.date_range('20251001', periods=6)
print(algumasDatas)

"""
date_range(): cria um conjunto de dados baseado num intervalo de valores com a caracteristica de datas; alem disso, temos 2 parametros

20251001: este é o parametro que estabelece o ponto inicial do intervalo de valores de data. 2023-10-01 (ano, mês, dia)

periods=6: aqui, está definido a quantidade de valores que compõem o intervalo de datas que serão geradas pela função

Por padrão, a função date_range utiliza-se de frequencia diaria para gerar o intervalo de valores => freq='D'

O resultado esperado é algo semelhante a isto: '2025-10-01', '2025-10-02', '2025-10-03' ...

"""

# Vamos definir, neste passo, o 1º dataframe usando como recurso de indice a variavel algumasDatas
"""
O DataFrame é uma estrutura de dados tabular, rotulada e bidimensional que possui as seguintes características:

1. Formato de Tabela
É composto por linhas e colunas.

É ideal para trabalhar com dados do "mundo real" (tabelas, CSVs, bancos de dados, etc.).

2. Eixos Rotulados (Labeled Axes)
Colunas: Cada coluna tem um rótulo (nome), o que permite acessar os dados por nome (ex: df['Nome']).

Index (Linhas): Cada linha tem um rótulo (o "índice"), que pode ser um número, uma string ou uma data.

3. Tipos de Dados Mistos (Heterogêneo)
Diferente do NumPy, o DataFrame é feito para lidar com colunas de tipos diferentes.

Exemplo: A Coluna A pode ser de strings (nomes), a Coluna B de inteiros (idade) e a Coluna C de floats (salário).

Internamente, cada coluna é uma Series do Pandas, que, por sua vez, é construída sobre um array do NumPy.

"""
print('======================== DATAFRAME 1 ===========================')

df1 = pd.DataFrame(np.random.randn(
    6, 4), index=algumasDatas, columns=list('ABCD'))

"""
    1º ARGUMENTO: é a definição do numero de linhas e colunas que irão compor o dataframe; alem disso, tambem, indicamos os valores aleatorios que farão aprte do df
    2º ARGUMENTO: index=algumasDatas -> define qual será o recurso de indice "principal do df
    3º ARGUMENTO: columns=list('ABCD') -> define os nomes das colunas que irão compor o df

    A função np.random.randn() do NumPy é uma ferramenta fundamental para gerar dados aleatórios que seguem uma distribuição estatística muito específica.
"""
print()
print('Este é o Dataframe 1 (df1)')
print(df1)
print()

print('======================== DATAFRAME 2 ===========================')

# Gerar um novo dataframe que será gerado a partir de um dicionário

df2 = pd.DataFrame({
    # Valor constante repetido para todas as linhas do df
    'A': 1.,
    # Mesmo valor de data para todas as linhas do df
    'B': pd.Timestamp('20251006'),
    # 1.0: Series com 4 elementos do tipo float
    'C': pd.Series(1, index=list(range(4)), dtype='float64'),
    # 3: array com 4 valores inteiros [3,3,3,3]
    'D': np.array([3.0] * 4, dtype='int32'),
    # Coluna com dados de diferentes tipos; conhecidos como dados categoricos
    'E': pd.Categorical(['teste', 853, 'novo teste', 59.9]),
    # Mesma string para todas as linhas
    'F': 'esta é uma string'
})
print()
print('este é o DataFrame 2')
print(df2)

# ----------------------------------------------------------------------------------------------------------

print('================================ COPIAR UM DF E REALIZAR NOS OPS ========================================')
print()

# PREMISSA: copiar um df - para este proposito vamos definir uma nova var para receber como valor a cópia do df1
print('este é o df3')
df3 = df1.copy()  # método/função que faz a cópia do df1 e atrivui como valor para o df3
print(df3)
print()
print('-'*50)

# PREMISSA: inserir uma nova coluna no df3
print('df3 com mais uma coluna - E')
df3['E'] = ['tret', 'ola', 'numero', 'srfd', '43256', 'j']
print(df3)
print()
print('-'*50)

# PREMISSA: fazer uso do operador .isin -> o proposito deste operador é verificar se os valores de qualquer elemento do df - devidamente selecionado (aqui, selecionaremos a coluna 'E' ) - estão dentro de algum conjunto de dados(aqui, teremos uma lista com dois valores quaisquer); portanto a repsota que será recebida só pode ser booleana - TRUE ou FALSE

# esta operação "atua" como um "filtro" de valores a partir de uma coluna
print('uso do operador .isin')
print(df3['E'].isin(['ola', 'j']))
print()
print('-'*50)

# PREMISSA: definir uma nova coluna para o df3 - a partir de valores criados com uma Series
# Atenção a data, tem que estar coerente com o Df
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20251001', periods=6))
print('esta é a Series s1')
print(s1)
print()
print('-'*50)

# agora, vamos inseri-la no df3
df3['F'] = s1
print('df3 com sua nova coluna - F')
print(df3)
print()
print('-'*50)

# agora, vamos inserir uma nova no df3
df3['G'] = umaSerie
print('df3 com uma nova coluna - com a variavel umaSerie')
print(df3)
print()

# PREMISSA: estabelecer uma operação para a substituição de valores de uma coluna no df; para este proposito precisamos selecionar a coluna que terá seus valores substituidos

# df3.loc[:, 'D']: aqui, estamos selecionando todas as linhas do df3 - considerando, somente, a coluna 'D'

# np.array([5] * len(df3)): aqui, estamos criando uma lista/array com o numero 5 repetido para cada linha do df3
df3.loc[:, 'D'] = np.array([5] * len(df3))
print(df3)
print()
print('-'*50)
