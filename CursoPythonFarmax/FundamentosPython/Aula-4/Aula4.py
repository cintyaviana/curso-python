
# Listas - conjunto de valores, definidos entre colchetes

import random as rn
import random  # aqui, estamos "importando/usando" o módulo random para dispor de seus recuros
from random import random, randint
from random import *
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
# Uso do operador Slice - Fatiamento de dados

""" 
A aplicação do operador slice consiste na utilização dos limites numéricos separados por : (dois pontos).

[posição_inicial: limite]

numeros = [5.5, 9, 14, 16, 1, 8]
Posição =  0,   1,  2,  3, 4, 5
"""
numeros = [5.5, 9, 14, 16, 1, 8]

print(type(numeros))
print(numeros)
# Retorna todos as posições da lista
print(numeros[2:])
# Retorna os elementos da posição 2 até o final
print(numeros[2:4])
# Retorna os elementos da posição 2 até a posição 3, pois o 4 é excludente
print(numeros[2:8])
# Retorna os elementos da posição 2 até o final, pois tem menos que 8 posições na lista
print(numeros[:5])
# Retorna os elementos da posição inicial até a 4

# ------------------------------------------------------------------------------------------------------------------
# Troca de elementos de uma lista

numeros = [5.5, 9, 14, 16, 1, 8]

print(numeros)
temp = numeros[1]
print(temp)
numeros[1] = numeros[3]   # numeros = [1] = 9, troca por numeros = [3] = 16
print(numeros)
numeros[3] = temp
print(numeros)

# ------------------------------------------------------------------------------------------------------------------
# Algumas operações sobre listas


numeros = [5.5, 9, 14, 16, 1, 8]

# numeros.append(200)  # Adicionar um novo item ao final da lista
# numeros.clear()  # Limpa os elementos da lista
# num = numeros.copy()  # Retorna uma cópia da lista
# num = numeros.count()  # Retorna o número de elementos da lista
# numeros.sort()  # Ordena a lista em ordem crescente
# numeros.pop(1)  # Remove um item da lista - indicado pela posição
# numeros.remove(5.5)  # Remove um item da lista - indicado pelo valor

print(numeros.append(1222.8))

print(numeros)
print("-")

print(numeros.clear())
print("-")

print(numeros.count(9))
print("-")

NovoNumeros = numeros.copy()
print(NovoNumeros)
print("-")

numeros.sort()
print(numeros)
print("-")

numeros.pop(1)
print(numeros)
print("-")

numeros.remove(5.5)
print(numeros)
print("-")

numeros.reverse()
print(numeros)

# ------------------------------------------------------------------------------------------------------------------
# Tuplas

"""As tuplas são exatamente como as listas, exceto pelo fato de que seus elementos, uma vez inseridos, permanecem naquela posição, ou seja, não podem ser alterados ou substituídos.

A definição de tuplas usa o caractere "parênteses" para reunir seus elementos.

O exemplo a seguir ilustra a definição de uma tupla:
"""

dias = ('dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab')


"""
Os métodos aplicados a uma tupla são bastante limitados, já que não podemos:

Inserir elementos em posição intermediária;

Remover elementos;

Alterar elementos.
"""

x = dias.count('ter')  # retorna o número de ocorrências do elemento informado

y = dias.index('seg')  # retorna a posição do elemento informado

# A obtenção do número de elementos é realizada pela função len():
quantidade = len(dias)

print(x)
print(y)
print(quantidade)

print(dias[2])  # aqui, é o slice da tupla
umaLista = list(dias)  # temos uma tupla transformada numa lista
print('Uma tupla transformada numa lista?', umaLista)

# agora vamos transformar uma lista numa tupla
mix = ['Minas Gerais', 45.6, 89, False]
umaTupla = tuple(mix)
print()
print('Uma lista transformada em uma tupla?', umaTupla)

# ------------------------------------------------------------------------------------------------------------------
# Dicionários

"""
Apesar de pertencer à categoria de coleções, um dicionário não é exatamente como elas. Trata-se de um conjunto de propriedades, e não de elementos. Dicionários possuem propriedades que, juntas, compõem um objeto.

Definição de dicionários
Cada elemento de um dicionário é formado por uma chave e um valor (o que, de fato, caracteriza a definição de dicionário).

O exemplo a seguir mostra a estrutura do dicionário:
# dicionario representando as propriedades de uma pessoa
# """

"""
Um dicionário, em Python, é constituído por pares key:value/chave:valor, significa que o conceito de índice posicional não existe.

Então, temos:

[] -> definem listas

() -> definem tuplas

{} -> definem dicionários
"""

pessoa = {
    'nome': 'Carlos',
    'idade': 30,
    'altura': 1.75,
    1: '3'
}

"""
A variável pessoa possui 4 propriedades (4 elementos). Cada propriedade (elemento) possui uma chave e um valor, conforme apresentado:

chave	valor
---------------
nome	Fulano
idade	30
altura	1.7
1       3
 """

# ------------------------------------------------------------------------------------------------------------------
# Buscas em dicionários
"""
Analogamente ao que aconteceu com as listas, para obter o valor de um elemento do dicionário com base na chave basta colocar a chave como item de busca: pessoa['nome']

O exemplo seguinte apresenta um código exibindo algumas informações de um dicionário:
"""

print('Imprimindo operações com o dicionário')
print()
print(pessoa)
# o operador de slice continua o mesmo; mas o fatiamento se dá a partir do elemento 'key/chave' do dicionário
print(pessoa['nome'])
print(pessoa[1])
print(pessoa.keys())  # aqui, serão exibidos as keys do dicionário
print(pessoa.values())  # aqui, serão exibidos as values do dicionário
print(pessoa.items())  # aqui, serãão exibidos as itens do dicionário

"""
E o resultado desta execução é apresentado a seguir:

{ 'nome': 'Carlos', 'idade': 30, 'altura': 1.75, '1': 3}
Carlos
3
dict_keys(['nome', 'idade', 'altura'])
dict_values(['Carlos', 30, 1.75,3])
dict_items([('nome', 'Carlos'), ('idade', 30), ('altura', 1.75),(1: '3')])

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

# Apresentando o valor da chave 'nome' presente no segundo elemento
print(pessoas[1]['nome'])

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
# Funções

"""
"Uma função, nada mais é do que um bloco de instruções lógicas que são agrupadas para cumprir algum tipo de tarefa, a essa, função, indicada. No python, temos funções nativas - como por exemplo print(), random(), entre outras; além dessa característica, python nos dá a possibilidade de construir nossas próprias funções."
"""

"""
Módulos são agrupamentos de componentes. Um conjunto de funções pode fazer parte de um módulo. Via de regra, um arquivo contendo funções no Python é um módulo. Os módulos são definidos para organizar as funções ou quaisquer componentes que possuam propósitos comuns.

Uso de módulos em programas
No Python existem diversas funções, como aquelas que tivemos a oportunidade de usar: print(), input(), etc. Mas nem todas as funções são disponibilizadas imediatamente como estas.

Em muitos casos haverá a necessidade de importar a função ou o módulo, ou mesmo instalar um módulo através de um gerenciamento de dependências.

Os exemplos a seguir utilizam o módulo random e diferentes formas de utilizá-lo. Os demais módulos são consumidos de forma análoga.
"""

# Exemplo 01: importando o módulo random e, a partir dele, chamando a função random(). O exemplo apresentará um número aleatório na tela.
# import random
numero = random.random()
print(numero)

# Exemplo 02: adicionando um alias para o módulo:
# import random as rn
numero = rn.random()
print(numero)

# Nos exemplos 01 e 02 o módulo é importado, significando que todas as funções do módulo estarão disponíveis. O próximo exemplo (Exemplo 03) apresentará uma estrutura onde apenas as funções de interesse são importadas:

# Exemplo 03: importando apenas as funções random() e randint() do módulo random:
# from random import random, randint
numero1 = random()
numero2 = randint(3, 6)
print(numero1)
print(numero2)

"""
No exemplo, o nome do módulo foi referenciado pelo comando from, e a partir dele, o import inclui as funções importadas do módulo. Neste caso, o nome do módulo não é mencionado na instrução de chamada à função.

A função random() retorna um número real aleatório entre 0 e 1. A função randint() retorna um número aleatório inteiro entre os valores informados como parâmetro. Uma execução do exemplo anterior é mostrada a seguir:

0.8965774320986762
5

Analogamente ao exemplo anterior, é possível importar todas as funções de um módulo. Neste caso, a chamada a alguma destas funções também não inclui o nome do módulo. O exemplo a seguir ilustra este procedimento:
"""

# Exemplo 04: importando todas as funções do módulo com o uso do caractere "*".
# from random import *
numero1 = random()
numero2 = randint(3, 6)
print(numero1)
print(numero2)


# ------------------------------------------------------------------------------------------------------------------
# Criação de funções

"""
# Criar funções - para criar uma função precisamos de 4 características importantes: 
# uso da palavra reservada def nomeDaFuncao(parametros):
#                                a tarefa que a função vai cumprir
#                                return - da função
"""

"""
Nesta lição serão apresentados os procedimentos para elaborar funções levando em conta os possíveis parâmetros e tipos de retorno.

Definição de uma função
A forma geral para definição de uma função é mostrada a seguir:

def nome_função([lista_parametros]):
    bloco_da_função
Os exemplos seguintes são funções elaboradas com e sem parâmetros, e com e sem valor de retorno.
"""

# Exemplo 01: função definida para apresentar uma mensagem, e sua chamada.
# definição da função


def mostrar_mensagem():
    print('Primeira função')


# chamada da função
# Mesmo que a função não possua parâmetros, os parênteses são necessários, tanto na definição como na chamada.
mostrar_mensagem()


# Exemplo 02: definição de um valor de retorno para a função
# definição da função
def mostrar_mensagem():
    return 'Segunda função'


# chamada da função
msg = mostrar_mensagem()
print(msg)

# função com parametros
print('função com parametros')


def somar_valores(a, b):  # (a, b) -> estas variaveis, aqui, dentro da definição da função, ganham um "papel" especial: passam a ser consideradas PARAMETROS DA FUNÇÃO
    return a + b


def subtrair_valores(a, b):  # quando criamos parametros de função precisamos dar as estes, valores para cada um; estes valores são chamados de ARGUMENTOS DE FUNÇÃO
    resultado = a - b
    print(resultado)

# AGORA, VAMOS CHAMAR AS FUNÇÕES À SUA EXECUÇÃO; quando temos funções parametrizadas, no momento de sua chamada a execução, precisamos dar aos seus parametros, os argumentos necessarios


# chamando a função somar_valores() - com uma expressão de chamada
somando = somar_valores('22', '89')  # aqui temos uma junção de strings
print(somando)

somando = somar_valores(22, 89)
print(somando)

# chamando a função subtrair_valores
subtrair_valores(89, 10)
subtrair_valores(15, 2)

"""
De um modo geral não constitui boa prática interagir com o usuário ao escrever uma função. Isso significa que não é um procedimento correto apresentar informações por meio da função print(), ou solicitar informações por meio da função input() como parte da sua definição, a menos que a função tenha exatamente este propósito.

No Exemplo 01 a função mostrar_mensagem() está "assumindo" a responsabilidade de mostrar a mensagem na tela, não oferecendo nenhum meio de armazená-la.
"""

# definição da função


def calcular_soma(x, y):
    if (type(x) is not int and type(x) is not float) and \
            (type(y) is not int and type(y) is not float):
        return 0
    else:
        return x + y


# chamada da função com parametros numéricos
v1 = calcular_soma(10, 12)
print(v1)

v2 = calcular_soma(10.5, 12)
print(v2)

# chamada da função com parâmetro alfanuméricos
v3 = calcular_soma('10', '12')
print(v3)

# Se os parâmetros não forem numéricos, a função retornará zero. O correto seria produzir um erro, porém, como mencionado, este tema será abordado em lições futuras.


# ------------------------------------------------------------------------------------------------------------------
# Funções com parametros default

# significa que: ao definirmos parametros para uma função, podemos dar à eles, já, em sua definição, alguns valores

def mostrar_profissionais(qtde, cidade='Divinópolis-MG'):
    # f: indica que vamos fazer uma formatação para a saída de dados
    return f'Qtde de profissionais: {qtde}\nCidade: {cidade}'


# vamos praticar a chamada da função à sua execução
mostrar_profissionais(45)  # 1ª chamada da função
# 2ª chama da função, agora com 2 argumentos
mostrar_profissionais(1000, 'Belo Horizonte')
# 3ª chamada da função - inverter a ordem dos argumentos
mostrar_profissionais(cidade='Sorocaba', qtde=1500)

# ------------------------------------------------------------------------------------------------------------------
# Funções com parametros de tamanho variavel


def somatoria(um, *args):  # o uso do asterisco - junto da palavra reservada args determina que o segundo argumento da função pode receber um ou mais valores - como argumento
    acumuladora = um
    # definir um loop
    for item in args:
        acumuladora = acumuladora + item  # acumuladora += item
    return acumuladora


# chamar a função
resultadoDaFuncao = somatoria(12, 15, 41, 53, 78, 89, 65, 32, 4523)
print(resultadoDaFuncao)

# ------------------------------------------------------------------------------------------------------------------
print('Um novo exemplo')


def preco_final(preco, **kwargs):
    # o uso do parametro **kwargs é uma boa pratica quando
    # queremos fazer uso de um parametro variavel que recebe
    # como valor, argumentos baseados em pares key:value

    p_taxa = 0
    p_imposto = 0

    v_taxa = kwargs.get('taxa')
    if v_taxa:
        # aqui, estamos definindo a seguinte operação:
        p_taxa = preco * v_taxa/100
        # a verificação da percentagem da v_taxa em relação
        # ao valor dado ao argumento preco

    v_imposto = kwargs.get('imposto')
    if v_imposto:
        p_imposto = preco * v_imposto/100

    return preco - p_taxa - p_imposto


# praticar a chamada da função
valorLiquido1 = preco_final(1000)
valorLiquido2 = preco_final(1000, taxa=10)
valorLiquido3 = preco_final(1000, imposto=18)
valorLiquido4 = preco_final(1000, taxa=10, imposto=18)

print(f'Valor liquido 1: {valorLiquido1}')
print(f'Valor liquido 2: {valorLiquido2}')
print(f'Valor liquido 3: {valorLiquido3}')
print(f'Valor liquido 4: {valorLiquido4}')
