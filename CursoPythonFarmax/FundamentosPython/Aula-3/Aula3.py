
# Comando IF

numero = int(input('Forneça um valor inteiro'))
if numero > 0:
    print('O número informado é positivo')
    print("Segunda instrução do bloco")

""" Os dois prints está dentro dessa condição If"""

print()
print("------------------------------------------------------")
print()

numero = int(input('Forneça um valor inteiro: '))
if numero > 0:
    print('O número informado é positivo')
print("Segunda instrução do bloco")

""" Nesse caso, o primeiro print está dentro do If o outro fora, ou seja, o segundo print será executado dentro do contexto mesmo se no If retornar False"""

print()
print("------------------------------------------------------")
print()

# -----------------------------------------------------------------------------------------------------------------------
# Comando If ... Else

numero = int(input('Forneça um valor inteiro: '))

if numero % 2 == 0:
    print('Voce informou um número par.')
    print('Numero informado:', numero)
else:
    print('Voce informou um número ímpar.')
    if numero > 10:
        print('O número é maior que 10.')
    else:
        print('O número não é maior que 10.')

print()
print("------------------------------------------------------")
print()

# ------------------------------------------------------------------------------------------------------------------
# Comando if...elif...else

nome = input('Nome do associado: ')
idade = int(input('Idade do Associado: '))


if idade < 18:
    ingresso = 50
elif idade >= 60:
    ingresso = 20
else:
    ingresso = 60

print("Associoado:", nome)
print("Valor a ser pago:", ingresso)

print()
print("------------------------------------------------------")
print()

# ------------------------------------------------------------------------------------------------------------------
# Listas - conjunto de valores, definidos entre colchetes

lista = []
nomes = ['Carlos', 'Sergio', 'Ana Maria', 'Jose', 'Claudia']
numeros = [5.5, 9, 14, 16, 1, 8]
mistos = ['São Paulo', 322, True, 75.2]

# ------------------------------------------------------------------------------------------------------------------
# Buscas em índices

""" 
    Para buscar elementos em uma lista são utilizados os índices dos elementos. No python, o primeiro elemento possui índice 0.

    Para buscar um elemento em uma lista pode-se usar índices com valores positivos ou negtivos. Se o índice for positivo, a localização é realizado a partir do zero para a direira, e se for negativo, para a esquerda.
"""

print(nomes)
print(type(nomes))
print(nomes[0])              # primeiro elemento
print(nomes[-1])             # último elemento
print(nomes[-2])             # penúltimo elemento
print(nomes[len(nomes)-1])   # último elemento

""" 
    (len(nomes): A função len() retorna o número total de elementos na lista nomes. Por exemplo, se a lista tem 5 elementos, len(nomes) retornará 5, nesse caso, 5-1 = 4, ou seja posição 4 é o último elemento dessa lista
"""

# ------------------------------------------------------------------------------------------------------------------
# Uso do operador Slice

""" 
A aplicação do operador slice consiste na utilização dos limites numéricos separados por : (dois pontos).

[posição_inicial: limite]

numeros = [5.5, 9, 14, 16, 1, 8]
Posição =  0,   1,  2,  3, 4, 5
"""

print(type(numeros))
print(numeros)
# Retorna todos as posições da lista
print(numeros[2:])
# Retorna os elementos da posição 2 até o final
print(numeros[2:4])
# Retorna os elementos da posição 2 até a posição 3, pois o 4 é excludente
print(numeros[2:8])
# Retorna os elementos da posição 2 até o final, pois tem mmenos que 8 posições na lista
print(numeros[:5])
# Retorna os elementos da posição inicial até a 4

# ------------------------------------------------------------------------------------------------------------------
# Troca de elementos de uma lista

print(numeros)
temp = numeros[1]
print(temp)
numeros[1] = numeros[3]   # numeros = [1] = 9, troca por numeros = [3] = 16
print(numeros)
numeros[3] = temp
print(numeros)

# # Algumas operações sobre listas

numeros.append(200)  # Adicionar um novo item ao final da lista
numeros.clear()  # Limpa os elementos da lista
num = numeros.copy()  # Retorna umja cópia da lista
num = numeros.count()  # Retorna o número de elementos da lista
numeros.sort()  # Ordena a lista em ordem crescente
numeros.pop(1)  # Remove e retorna o elemento na posição indicada
numeros.remove(5.5)  # Remove a primeira ocorrência do valor indicado

# ------------------------------------------------------------------------------------------------------------------
# Tuplas

"""As tuplas são exatamente como as listas, exceto pelo fato de que seus elementos, uma vez inseridos, permanecem naquela posição, ou seja, não podem ser alterados ou substituídos.

A definição de tuplas usa o caractere "parênteses" para reunir seus elementos.

O exemplo a seguir ilustra a definição de uma tupla:
"""

dias = ('dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab')


"""
s métodos aplicados a uma tupla são bastante limitados, já que não podemos:

Inserir elementos em posição intermediária;

Remover elementos;

Alterar elementos.
"""

x = dias.count('ter')  # retorna o número de ocorrências do elemento informado

y = dias.index('seg')  # retorna a posição do elemento informado


"""A obtenção do número de elementos é realizada pela função len():"""

quantidade = len(dias)

print(x)
print(y)
print(quantidade)


# ------------------------------------------------------------------------------------------------------------------
# Dicionários

"""
Apesar de pertencer à categoria de coleções, um dicionário não é exatamente como elas. Trata-se de um conjunto de propriedades, e não de elementos. Dicionários possuem propriedades que, juntas, compõem um objeto.

Definição de dicionários
Cada elemento de um dicionário é formado por uma chave e um valor (o que, de fato, caracteriza a definição de dicionário).

O exemplo a seguir mostra a estrutura do dicionário:
# dicionario representando as propriedades de uma pessoa
# """
pessoa = {
    'nome': 'Fulano',
    'idade': 30,
    'altura': 1.75
}

"""
A variável pessoa possui três propriedades (três elementos). Cada propriedade (elemento) possui uma chave e um valor, conforme apresentado:

chave	valor
---------------
nome	Fulano
idade	30
altura	1.7

 """

# ------------------------------------------------------------------------------------------------------------------
# Buscas em dicionários
"""
Analogamente ao que aconteceu com as listas, para obter o valor de um elemento do dicionário com base na chave basta colocar a chave como item de busca: pessoa['nome']

O exemplo seguinte apresenta um código exibindo algumas informações de um dicionário:
"""

print(pessoa)
print(pessoa['nome'])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

"""
E o resultado desta execução é apresentado a seguir:

{ 'nome': 'Carlos', 'idade': 30, 'altura': 1.75}
Carlos
dict_keys(['nome', 'idade', 'altura'])
dict_values(['Carlos', 30, 1.75])
dict_items([('nome', 'Carlos'), ('idade', 30), ('altura', 1.75)])

Pode-se observar que a definição de um dicionário é feita com o uso de chaves, e cada elemento é um par chave / valor separados por ':' (dois pontos).
"""

# ------------------------------------------------------------------------------------------------------------------
# Combinando Dicionários e Listas

"""
Dicionários podem ser elementos de listas, o que é útil para representar uma coleção de objetos com atributos, como a lista de pessoas no exemplo a seguir.
"""

# dicionários como elementos de listas
pessoas = [
    {'nome': 'Carlos', 'idade': 30},
    {'nome': 'Sergio', 'idade': 23},
    {'nome': 'Ana Maria', 'idade': 25}
]

# Apresentado o primeiro elemento
print(pessoas[0])

# Apresentando o valor da chave 'nome' presente no primeiro elemento
print(pessoas[0]['nome'])


"""No próximo exemplo é apresentado um dicionário onde o valor de uma propriedade é uma lista:"""

curso = {
    'descricao': 'Análise de Sistemas',
    'disciplinas': [
        'Lógica de programação',
        'Banco de Dados',
        'Scrum',
        'Programação Avançada'
    ]
}

print(curso)
print(curso['disciplinas'][2])


"""
{'descricao': 'Análise de Sistemas', 'disciplinas': ['Lógica de programação', 'Banco de Dados', 'Scrum', 'Programação Avançada']}

Scrum
"""

# ------------------------------------------------------------------------------------------------------------------
# Estrutura de repetição for


"""
Dentre as estruturas de repetição, a estrutura for é adequada para situações em que a quantidade de repetições é conhecida previamente. Nesta lição serão mostrados exemplos de utilização desta estrutura.

Percorrendo uma lista

Uma das formas mais comuns de utilização da estrutura for é a realização de buscas em listas. Aqui existe a possibilidade de se realizar algum tratamento diferenciado em cada elemento da estrutura

"""

colecao = [1, 3, 4, 7, 10]
posicao = 0
for x in colecao:
    print('Elemento na posição', posicao, '=', x)
    posicao += 1

"""
No exemplo, a variável x representa, sequencialmente, cada elemento da variável colecao a cada passo da repetição.

O resultado da execução deste código é mostrado a seguir:

Elemento na posição 0 = 1
Elemento na posição 1 = 3
Elemento na posição 2 = 4
Elemento na posição 3 = 7
Elemento na posição 4 = 10

"""

# ------------------------------------------------------------------------------------------------------------------
# A função range()

"""
Em muitas situações a estrutura de repetição é usada para outros propósitos diferentes de manipular coleções – apenas para repetir trechos de código. Para cenários como esse, o Python disponibiliza a função range().

Esta função possui diferentes formas de execução, variando a quantidade de parâmetros. Os exemplos a seguir ilustram o uso desta função:
"""

c1 = range(10)  # produz uma sequencia numérica de 0 a 9, com passo 1


"""
O parâmetro informado na função range() não entra na sequência – ele é apenas o limite superior. O exemplo a seguir mostra a estrutura for usando a função range():
"""

for x in range(10):
    print(x)


"""
Resultado:
0
1
2
3
4
5
6
7
8
9
"""

"""
O exemplo a seguir mostra a função range() com dois parâmetros. O primeiro parâmetro é o primeiro elemento da sequência:
"""

for x in range(-3, 10):
    print(x)

"""
Resultado:
-3
-2
-1
0
1
2
3
4
5
6
7
8
9
"""

"""
Quando a função for for usada com três parâmetros, seus valores são:
range(valor_inicial, limite, passo)

O terceiro parâmetro indica o passo usado na sequência.
"""

for x in range(3, 10, 2):  # o terceiro parâmetro é o passo (step)
    print(x)

"""
Resultado:
3
5
7
9
"""

"""
É possível também executar esta função em uma ordem numérica decrescente:
"""

for x in range(12, 2, -1):  # o terceiro parâmetro é o passo (step)
    print(x)


""""
Resultado:
12
11
10
9
8
7
6
5
4
3
"""

"""
Combinando for com else
É possível combinar a estrutura for com o comando else. Neste caso, o else é executado quando a estrutura de repetição finalizar.
"""

for x in range(5):
    print(x)
else:
    print('Final da estrutura de repetição')

"""
Resultado:
0
1
2
3
4
Final da estrutura de repetição
"""

# ------------------------------------------------------------------------------------------------------------------

# Estrutura for em dicionários
"""
Sabendo que um dicionário é formado por elementos compostos por chave e valor, é possível contemplar esta abordagem na elaboração da estrutura de repetição. Exemplo:
"""

notas = {
    'Potuguês': 7,
    'Matemática': 9,
    'Lógica': 7,
    'Algoritmo': 7
}

for chave, valor in notas.items():
    print(f"{chave}: {valor}")

"""
Resultado da execução:
Potuguês: 7
Matemática: 9
Lógica: 7
Algoritmo: 7
  
"""

"""
Uso do for em cadeias de caracteres
Muitas vezes temos a necessidade de analisar caracteres de uma string — por diversos motivos. O comando for pode perfeitamente ser usado para este fim.

O exemplo a seguir percorre os caracteres de uma string e adiciona o caractere * entre eles:

"""

s = ''
for ch in 'python':
    s += ch + '*'

print(s)
