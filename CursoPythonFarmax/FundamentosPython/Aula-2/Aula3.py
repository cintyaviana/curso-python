
# Comando IF

# numero = int(input('Forneça um valor inteiro'))
# if numero > 0:
#     print('O número informado é positivo')
#     print("Segunda instrução do bloco")

# print()
# print("------------------------------------------------------")
# print()

# numero = int(input('Forneça um valor inteiro: '))
# if numero > 0:
#     print('O número informado é positivo')
# print("Segunda instrução do bloco")

# print()
# print("------------------------------------------------------")
# print()

# Comando If ... Else

# numero = int(input('Forneça um valor inteiro: '))

# if numero % 2 == 0:
#     print('Voce informou um número par.')
#     print('Numero informado:', numero)
# else:
#     print('Voce informou um número ímpar.')
#     if numero > 10:
#         print('O número é maior que 10.')
#     else:
#         print('O número não é maior que 10.')

# print()
# print("------------------------------------------------------")
# print()

# Comando if...elif...else

# nome = input('Nome do associado: ')
# idade = int(input('Idade do Associado: '))


# if idade < 18:
#     ingresso = 50
# elif idade >= 60:
#     ingresso = 20
# else:
#     ingresso = 60

# print("Associoado:", nome)
# print("Valor a ser pago:", ingresso)

# print()
# print("------------------------------------------------------")
# print()

# Listas - conjunto de valores, definidos entre colchetes

nomes = ['Carlos', 'Sergio', 'Ana Maria', 'Jose', 'Claudia']
numeros = [5.5, 9, 14, 16, 1, 8]
mistos = ['São Paulo', 322, True, 75.2]

# Buscas em índices

""" Para buscar elementos em uma lista são utilizados os índices dos elementos. No python, o primeiro elemento possui índice 0 """

""" Para buscar um elemento em uma lista pode-se usar índices com valores positivos ou negtivos. Se o índice for positivo, a localização é realizado a partir do zero para a direira, e se for negativo, para a esquerda"""

# print(nomes)
# print(type(nomes))
# print(nomes[0])               # primeiro elemento
# print(nomes[-1])             # último elemento
# print(nomes[-2])             # penúltimo elemento
# print(nomes[len(nomes)-1])   # último elemento

""" (len(nomes): A função len() retorna o número total de elementos na lista nomes. Por exemplo, se a lista tem 5 elementos, len(nomes) retornará 5, nesse caso, 5-1 = 4, ou seja posição 4 é o último elemento dessa lista"""


# Uso do operador Slice

""" 

A aplicação do operador slice consiste na utilização dos limites numéricos separados por : (dois pontos).

[posição_inicial: limite]

"""

print(numeros)
print(numeros[2:0])
print(numeros[2:4])
print(numeros[2:0])
