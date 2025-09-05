
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
print(nomes[0])               # primeiro elemento
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
print(numeros)          # Retorna todos as posiçõe da lista
print(numeros[2:])      # Retorna os elementos da posição 2 até o final
# Retorna os elementos da posição 2 até a posição 3, pois o 4 é excludente
print(numeros[2:4])
# Retorna os elementos da posição 2 até o final, pois tem mmenos que 8 posições na lista
print(numeros[2:8])
print(numeros[:5])      # Retorna os elementos da posição inicial até a 4


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

y = dias.index('seg')  # retorna a primeira posição do elemento informado


"""A obtenção do número de elementos é realizada pela função len():"""

quantidade = len(dias)

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
nome	Fulano
idade	30
altura	1.7

 """

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
