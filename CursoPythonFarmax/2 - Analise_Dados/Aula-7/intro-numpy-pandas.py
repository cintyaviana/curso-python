# importar o recurso numpy para as operações com dados
import numpy as np # aqui, a lib numpy recebe um apelido convencional

# criar uma lista de de numeros
grupo = [[31, 25, 56], [4, 89, 102], [78, 875, 123]]

# neste passo, vamos criar um matriz usando o recurso numpy - para este porposito, vamos  definir uma variavel que recebe como valor o método/função matrix() - com origem no numpy
umaMatriz = np.matrix(grupo)

print('-----------------------------------------------------------------------')

# verificar se o data type da variavel umaMatriz é, realmente, uma matriz
print(type(umaMatriz))
print()
print('-----------------------------------------------------------------------')
# verificar o formato /dimensoes da matriz
print(np.shape(umaMatriz))
print()
print('-----------------------------------------------------------------------')
# fazer uso do método/função mean() -> este é o recurso que calcula a media simples - considerando todos os valores que compõem a matriz
print(np.mean(umaMatriz))
print()
print('-----------------------------------------------------------------------')

print('======================= ALGUMAS OPERAÇÕES COM MATRIZ ===================')

# agora, serão criadas duas matrizes  -ambas receberão valores distintos
matriz1 = np.array([[2, 4], [5, -6]]) # array(): é uma função/método - com origem no numpy - para criar vetores/arrays de valores
matriz2 = np.array([[9, -4], [3, 5]])

somaMatrizes = matriz1 + matriz2

# exibir o resultado
print('Soma da matrizes', somaMatrizes)
print('-----------------------------------------------------------------------')

# subtração de matrizes
subMatrizes = matriz1 - matriz2
print('Subtração de matrizes: ', subMatrizes)
print('-----------------------------------------------------------------------')

# multiplicação das matrizes - elemento a elemento
multiMatrizes = matriz1 * matriz2
print('Multiplicação das matrizes: ', multiMatrizes)
print('-----------------------------------------------------------------------')

# divisão entre as matrizes
diviMatrizes  =matriz1 / matriz2
print('Divisão entre as matrizes: ', diviMatrizes)
print('-----------------------------------------------------------------------')

# produto matricial (multiplicação de matrizes)
produtoMatrizes = np.dot(matriz1, matriz2)
print('Produto matricial: ', produtoMatrizes)
print('-----------------------------------------------------------------------')

# transposição de matrizes
transposta = np.transpose(matriz1)
print('Transposição da matriz1: ', transposta)
print()
print('======================= OPERAÇÕES COM NUMPY/PANDAS ===================')

# importar o pandas
import pandas as pd # alias da lib pandas

# definir um recurso que passaremos a conhecer como Series: nada mais é do que uma matriz unidimensional, ou seja, de uma unica coluna

UmaSerie = pd.Series([1, 2, 3, np.nan, 6, 8, 'Ola']) 
umaSerie = pd.Series([1, 2, 3, 6, 8, 'Ola'], index=pd.date_range('20251001', periods=6))

# acima, np.nan é o recurso que oferece a possibilidade de trabalhar com um elemento não numerico(not-a-number): origem no numpy
print(UmaSerie)
print(umaSerie)
print()
print('--------------------------criar alguns dataframes-----------------------------')

# neste passo, será definida uma nova variavel para receber como valor um conjunto de dados
algumasDatas = pd.date_range('20251001', periods=6)
print(algumasDatas)
"""
    date_range(): cria um conjunto de dados baseado num intervalo de valores com a caracteristica de datas; alem disso, temos 2 parametros

    20251001: este é o parametro que estabelece o ponto inicial do intervalo de valores de data. 2023-10-01

    periods=6: aqui, está definido a quantidade de valores que compõem o intervalo de datas que serão geradas pela função

    por padrão, a função date_range utiliza-se de frequencia diaria para gerar o intervalo de valores => freq='D'

    o resultado esperado é algo semelhante a isto: '2025-10-01', '2025-10-02', '2025-10-03'....
"""
# AULA 8 10/10/2025 - CONTINUANDO.....

# vamos definir, neste passo, o 1º dataframe usando como recurso de indice a variavel algumasDatas
df1 = pd.DataFrame(np.random.randn(6, 4), index=algumasDatas, columns=list('ABCD'))

"""
    1º ARGUMENTO: é a definição do numero de linhas e colunas que irão compor o dataframe; alem disso, tambem, indicamos os valores aleatorios que farão aprte do df
    2º ARGUMENTO: index=algumasDatas -> define qual será o recurso de indice "principal do df
    3º ARGUMENTO: columns=list('ABCD') -> define os nomes das colunas que irão compor o df
"""
print()
print('este é o Dataframe 1 == df1')
print(df1)
print()

print('======================== DATAFRAME 2 ===========================')
# gerar um novo dataframe; será gerado a partir de um dicionario

df2 = pd.DataFrame({
    'A': 1., # valor constante repetido para todas as linhas do df
    'B': pd.Timestamp('20251006'), # mesmo valor de data para todas as linhas do df
    'C': pd.Series(1, index=list(range(4)), dtype='float64'), # 1.0: Series com 4 elementos do tipo float
    'D': np.array([3.0] * 4, dtype='int32'), # 3: array com 4 valores inteiros [3,3,3,3]
    'E': pd.Categorical(['teste', 853, 'novo teste', 59.9]), # coluna com dados de diferentes tipos; conhecidos como dados categoricos
    'F': 'esta é uma string' # mesma string para todas as linhas
})
print()
print('este é o DataFrame 2')
print(df2)

# -------------------------------------------------------------------------

print()
print('======================== OBSERVAR OS CONTEXTO DOS DFs==========================')
print()

# palavra reservada dtypes(data types) demonstra os tipos de dados que compõem os DFs
print('composição dos data types do df1')
print(df1.dtypes)
print('composição dos data types do df2')
print(df2.dtypes)


print()

# neste passo, vamos fazer uma "leitura" resumida dos DFs; para este proposito vamo fazer uso do método/função head(): por padrão, o método head() lê as primerias 5 linhas do df; também é possivel customizar a quantidade de linhas que deve ser lida pelo head()
print('primeiras linhas do df1')
print(df1.head(3))
print('primeiras linhas do df2')
print(df2.head(3))

print()

# neste paso, vamos fazer uma nova leitura; só que, agora, será uma leitura das ultimas linhas do df
# para este proposito usaremos o método/função tail(): por padrão, tail(), lê as utlimas 3 linhas do df
print('ultimas linhas do df1')
print(df1.tail(2))
print('ultimas linhas do df2')
print(df2.tail(2))

print()

# vamos, neste passo, observar os elementos de indice de cada DF
print('indices do df1')
print(df1.index)
print('indices do df2')
print(df2.index)

print()

# agora, neste passo, vamos observar a colunas de cada DF
print('colunas do df1')
print(df1.columns)
print('colunas do df2')
print(df2.columns)

print()
# uso do método/função describe()
print('resumo estatistico do df1')
print(df1.describe())
print('resumo estatistico do df2')
print(df2.describe())

'''
count: contagem da qtde numero de valores NÃO NULOS do df (df1 = 6, df2 = 4)
mean: média aritmética dos valores que compõem o df
std: desvio padrão(medida da dispersão dos dados)
min: é o menor valor - valor minimo - de cada coluna do df
25%: 1º quartil(25% dos dados estão abaixo destes valores indicados em cada coluna)
50%  2º quartil(50% dos valores gera, a partir do df, a mediana)
75%  3º quartil(75% dos dados estão abaixo destes valores indicados em cada coluna)
max: é o maior valor - valor maximo - de cada coluna do df

'''

# vamos "converter" os DFs em arrays numpy
print()
print('convertendo o df1 num array numpy')
print(df1.to_numpy())
print()
print('convertendo o df2 num array numpy')
print(df2.to_numpy())

print()

# observar a organização dos DFs a partir de valores de uma coluna especifica
print('Ordenando o df1 por uma coluna especifica')
print(df1.sort_values(by='C', ascending=False))
print()
print('Ordenando o df2 por uma coluna especifica')
print(df2.sort_values(by='E', ascending=False))

print()

# observar as organização dos DFs a partir de seus eixos: axis=0 e axis=1
print('Ordenando o df1 de forma decrescente - pelo eixos das linhas')
print(df1.sort_index(axis = 0, ascending=False))# sort_index(): ordena o df pelo indice
# axis = 0: indica que o ordenamento será realizado pelas LINHAS do df
print('Ordenando o df1 de forma decrescente - pelo eixos das colunas')
print(df1.sort_index(axis = 1, ascending=False))
# axis = 1: indica que o ordenamento será realizado pelas COLUNAS do df
print()

print('Ordenando o df2 de forma decrescente - pelo eixos das linhas')
print(df2.sort_index(axis = 0, ascending=False))# sort_index(): ordena o df pelo indice
# axis = 0: indica que o ordenamento será realizado pelas LINHAS do df
print('Ordenando o df1 de forma decrescente - pelo eixos das colunas')
print(df2.sort_index(axis = 1, ascending=False))
# axis = 1: indica que o ordenamento será realizado pelas COLUNAS do df

print()
print('======== OPERAÇÕES COM DADOS - SELEÇÃO/FATIAMENTO DE DFs ===============')
print()

print('Fatiando o df1')
print(df1['A']) # aqui, estamos fatiando/selecionando a coluna A do df1
print()
print('Fatiandp o df2')
print(df2['D'])

print()

# aplicar a seleção de um intervalor de valores a partir do df
print('Fatiando df1 - via intervalo')
print(df1[1:3]) # aqui, continua valendo o conceito de intervalo semi-aberto [...[ )(-1)
print()
print('Fatiando df2 - via intervalo')
print(df2[2:4])

print()

print('Fatiando df1 - via intervalo de indice')
print(df1['2025-10-02': '2025-10-06']) # aqui, temos o indice de "rotulo": é uma "mascara" que criamos para o indices posicionais de linha do df1
print()
print('Fatiando df2 - via intervalo de indice')
print(df2[1:3])
#--------------------------------------------------------------------------------

print()
print('-------------- .loc, .iloc, .at, .iat -------------')
print()
"""
    os comandos, acima, proorcionam processos de seleção precisa, a partir dos dfs
    .loc: este operador é usado através de elementos nomeados do df - (lables/nomes de colunas ou linhas)

    .iloc: este operador é usado a partir de elementos de indice posicional do df

    agora, os dois operadores abaixo, de acordo com a documentação oficial do pandas, demonstram uma performance melhor do que os outros dois anteriores

     .at: este operador é usado através de elementos nomeados do df - (lables/nomes de colunas ou linhas)

    .iat: este operador é usado a partir de elementos de indice posicional do df

"""

# praticando uma nova seleção - a partir de indices label/nomeados '2025-10-02' e trazendo, a partir desta seleção, os valores das colunas que vamos especificar
print(df1.loc['2025-10-02', ['A', 'B']]) # .loc[] aceita criar/selecionar fatias e subconjuntos, ou seja, devo usar o .loc[] quando preciso criar um subconjunto que será composto por duas ou linhas/colunas
print()

# uma nova seleção: selecionar o elemento de indice de linha algumasDatas[0] e extrair, desta linha, os valores da coluna 'C'
print(df1.loc[algumasDatas[0], 'C'])

print()
# agora, a seleção será via intervalo de indices posicionais -feita de forma precisa - .iloc[]
print(df1.iloc[:4, :3])
print()
# acima, foram selecionados os seguintes dados: todas as ocorrencias até a linha de indice posicional - de linha - até 4;  e todas as ocorrencias até indice posicional 3 - todas as colunas(até 3) do df1;

# ------------ ESTABELECENDO PREMISSAS ----------

# PREMISSA: a seleção será composta pelo segunte intervalo: linhas 1 a 5 (sempre será praticado o intervalo semiaberto); e queremos todas as colunas 
# qual o conjunto d einstruções lógicas pode responder a esta premissa
print(df1.iloc[1:5, :])
print()

# PREMISSA: compor uma seleção com mais de um indice posicional - pedimos, especificamente, os indices de linha 1,2,3 tambem os indices de coluna 0 e 2
print(df1.iloc[[1, 2, 3], [0, 2]])
print()

# PREMISSA: a seleção será composta pelo seguinte intervalo: todas as linhas; queremos, também, as colunas de 1:3
print(df1.iloc[:, 1:3])
print()

# PREMISSA: a seleção será composta pelo seguinte intervalo: todas as linhas; queremos, também, as colunas de 1:3
# agora, vamos usar o .iat
print(df1.iat[1, 3]) # a premissa NÃO PODE SER ATENDIDA PELO .iat[]; proque eçe serve para acessar um unico valor escalr - usando indices posicionais numericos
print()
# acima, a premissa deveria ser a seguinte: PREMISSA: selecionar o valor da linha de indice posicional 1 da coluna de indice posicional 3

# PREMISSA: praticando uma nova seleção a partir do indice nomeado/label '2025-10-05' e trazendo, a partir dessa "fatia", os valores de duas colunas em especifico; MAS, AGORA, USANDO O .at[]
print(df1.at['2025-10-05', 'A']) # .at[] possui caracteristica especial - ele deve ser usado prara acessar um unico valor escalar (unico valor escalar: é a junção de uma coluna com um indice de linha do df) se quisermos selecionar duas ou mais colunas, devemos usar o .loc[]
print()

# PREMISSA: uma nova seleção - selecionar a partir do indice posicional, com uso da variavel algumasDatas[0] e extrair, desta linha, o valor da coluna 'C'; MAS, AGORA, USANDO O .at[]
print(df1.at[algumasDatas[0], 'C'])
print()

print('================ REINDEXAÇÃO =====================')
# PREMISSA: vamos reindexar o df1 a partir de uma avaliação booleana; selecionaremos a coluna A e reorganizaremos a coluna a partir da relação onde os valores, da coluna, sejam maiores do que 1 (um)
print(df1[df1.A > 1])
print()

# PREMISSA: vamos "recriar/reorganizar" o df1 a partir da seguinte condição: o df1 será "recriado/reorganizado" com valores abaixo de 0(zero); portanto, os valores acima de 0 (zero) serão interpretados como NaN (Not-a-Number)
print('recriando o df1 com valores abaixo de 0')
print(df1[df1 < 0])
print()

# PREMISSA: vamos "recriar/reorganizar" o df1 a partir da seguinte condição: o df1 será "recriado/reorganizado" com valores acima de 0(zero); portanto, os valores abaixo de 0 (zero) serão interpretados como NaN (Not-a-Number)
print('recriando o df1 com valores acima de 0')
print(df1[df1 > 0])
print()

print('================ COPIAR UM DF E REALIZAR NOS OPS=====================')
print()

# PREMISSA: copiar um df - para este proposito vamos definir uma nova var para receber como valor a cópia do df1
print('este é o df3')
df3 = df1.copy() # método/função que faz a cópia do df1 e atrivui como valor para o df3
print(df3)
print()

# PREMISSA: inserir uma nova coluna no df3
print('df3 com mais uma coluna - E')
df3['E'] = ['tret', 'ola', 'numero', 'srfd', '43256', 'j']
print(df3)

print()

# PREMISSA: fazer uso do operador .isin -> o proposito deste operador é verificar se os valores de qualquer elemento do df - devidamente selecionado (aqui, selecionaremos a coluna 'E' ) - estão dentro de algum conjunto de dados(aqui, teremos uma lista com dois valores quaisquer); portanto a repsota que será recebida só pode ser booleana - TRUE ou FALSE
print('uso do operador .isin')
print(df3['E'].isin(['ola', 'j'])) # esta operação "atua" como um "filtro" de valores a partir de uma coluna
print()

# PREMISSA: definir uma nova coluna para o df3 - a partir de valores criados com uma Series
# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20251006', periods=6))
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20251001', periods=6))
print('esta é a Series s1')
print(s1)
print()

# agora, vamos inseri-la no df3
df3['F'] = s1
print('df3 com sua nova coluna - F')
print(df3)
print()

# agora, vamos inserir uma nova no df3
df3['G'] = umaSerie
print('df3 com uma nova coluna - com a variavel umaSerie')
print(df3)

print()

# PREMISSA: estabelecer uma operação para a substituição de valores de uma coluna no df; para este proposito precisamos selecionar a coluna que terá seus valores substituidos
df3.loc[:, 'D'] = np.array([5] * len(df3))
# df3.loc[:, 'D']: aqui, estamos selecionando todas as linhas do df3 - considerando, somente, a coluna 'D'

# np.array([5] * len(df3)): aqui, estamos criando uma lista/array com o numero 5 repetido para cada linha do df3
print(df3)
print()