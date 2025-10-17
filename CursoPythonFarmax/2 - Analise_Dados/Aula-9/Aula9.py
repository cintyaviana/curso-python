
import matplotlib.pyplot as plt
from functools import reduce
print('-------------------- AULA 9 - CONTINUANDO NUMPY E PANDAS --------------------')
print()

# observar o df1
print('este é o df1')
print(df1)
print()

# PREMISSA: criar um novo df - com 10 linhas e 4 colunas - 10 x 4
df4 = pd.DataFrame(np.random.randn(10, 4))
print('este é o df4')
print(df4)

# PREMISSA: "quebrar" o novo df4 em "pedaços"/subconjuntos - a partir dos indices de linhas
pedacos = [df4[:3], df4[3:7], df4[7:]]
print('estes são os pedaços do df4 que quebramos')
print(pedacos)
print()

# PREMISSA: queremos "juntar/concatenar" todos os pedaços que geramos - a partir do df4;
# para este proposito, vamos fazer uso do método concat()
print('Juntando "pedaços"')
print(pd.concat(pedacos))  # consigo "juntar/concatenar" pedaços distintos de dados - fazendo uso da função concat() - desde que estes "pedaços" estejam atribuidos como valor de uma mesma variavel

# PREMISSA: agora, vamos fazer uso da função/método merge(); seu proposito é - teoricamente - "juntar" DFs; o merge possui um comportamento semelhante as instruções SQL; por exemplo, o merge oferece alguns tipos de junção : inner, outer, left, right; também faz uso do operador ON - para indicar qual a coluna-chave por onde a "junção" deve acontecer
print('df1')
print(df1)
print()
print('df2')
print(df2)
print()
print('usando merge()')
"""
juncao = pd.merge(df1, df2, how='inner', on='A')
# inner: juntar apenas os valores comuns nas colunas-chave
print(juncao)
"""

"""
print()
juncao = pd.merge(df1, df2, how='outer', on='A')
# outer: juntar TODOS OS VALORES preenchendo os elementos não-comuns, entre os DFs, com
# NaN
print(juncao)
"""

"""
print()
juncao = pd.merge(df1, df2, how='left', on='A')
# traz todos os dados dados do df1 e somente os dados de df2 compativeis - em commun - do
# elemente a esquerda da junção
print(juncao)
"""

"""
print()
juncao = pd.merge(df1, df2, how='rightt', on='A')
# right: traz todos os elementos de df2 e somente os dados compativeis - em comum - do elemento a direita da junção - df1
print(juncao)
"""

"""
print('juntando mais de uma DFs')
juncao = pd.merge(df1, df2, how='right', on='C')
juncao = pd.merge(juncao, df4, how='right', on='C')
print(juncao)
print()
"""
"""
print('juntando mais de uma DFs')
juncao = df1.merge(df2, how='right', on='C').merge(df4, how='right', on='C')
print(juncao)
print()
"""

# importar uma biblioteca python que auxilia no uso de funções de calculo e "redução" de
# elementos variaveis para a operação de junção
dfs = [df1, df2, df4]
juncao = reduce(lambda dfLeft, dfRight: pd.merge(
    dfLeft, dfRight, how='right', on='C'), dfs)

# reduce: função da biblioteca python functools (padrão) que aplica uma operação
# acumulativasobre um sequencia de elementos logicos; ou seja, a função faz uso de
# elementos de uma lista e os "combina" dois a dois usando a função que nós quisermos
# descrever par ao reduce

# lambda left, right: pd.merge(left, right, how='right', on='C'): esse lambda é uma
# função anônima que recebe dis dfs dfLeft e dfRight e retorna o seguinte resultado: o merge
# () entre eles, unidos pela coluna 'C'
print(juncao)
print()


print('============ AGRUPAMENTO - GROUPBY ============')
print()

# definir um novo df
df5 = pd.DataFrame({
    'A': ['ola', 'dia', 'ola', 'dia',
          'ola', 'dia', 'ola', 'dia'],
    'B': ['um', 'um', 'dois', 'dois',
          'um', 'um', 'dois', 'dois'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
})

print('este é o df5')
print(df5)

# PREMISSA: vamos fazer uso do agrupamento(gruopby) de valores: para este proposito será
# referenciado o método/função groupby(); para funcionar corretamente, o método precisa
# ter, associado a ele, uma operação pela qual o agrupamento ocorre

print()
print('groupby() usando a operação de soma')
# aqui, estamos fazendo a seleção da coluna 'A' do df5 e a
print(df5.groupby('A').sum())
# soma - sum() - de seus valores

"""
a saida demonstra o seguinte: o df5 sendo agrupado pelos valores unicos da coluna 'A' -
ola e dia; cada grupo será uma 'subtabela' onde todas as linhas tem o mesmo valor em 'A'
"""

print()
print(df5.groupby(['A', 'B', 'C']).sum())
print()


print('================== GRÁFICOS/MATPLOTLIB ==================')
print()
'''
Matplotlib é uma biblioteca do Python que cria graficos 2D para visualização de
dados. A visualização sempre ajuda na pratica de qualquer analise de dados e,
consequentemente, aumento da capacidade de obtenção de informações
'''

# importar o recurso necessario para a exibição do grafico

'''
PREMISSA: fazer uso do metodo/função plot() para exibir um grafico - simples - e tentar
entender o comportamento da saida exibida; para este proposito vamos definir um novo df -
df6 - onde estabeleceremos um contexto de série temporal
'''

# para fazer dos gráficos, vamos definir o df6
df6 = pd.Series(np.random.randn(1000),
                index=pd.date_range('20180101', periods=1000))
# o df6 nada mais é do que uma Time Series - series temporais -, significa que: foi
# criada uma Series com indice posicional de suas linhas de dados baseado em datas
print('este é o df6')
print(df6)

# agora, vamos tentar gerar o grafico a partir deste df6
grafico = df6.cumsum()

grafico.plot()
plt.show()

# PREMISSA: fazer uso do metodo plot() para exibir um grafico - a partir de um nova Time
# Series
df7 = pd.DataFrame(np.random.randn(1000, 4), index=df6.index, columns=['A', 'B', 'C',
                                                                       'D'])
print(df7)
print()

# "plotar" um novo grafico a partir do df7
graficoNovo = df7.cumsum()
graficoNovo.plot()
plt.show()
