conjunto1 = [1, 3, 10, 18, 63]

indice = 0

for x in conjunto1:
    print('O valor na indice', indice, '=', x)

    indice += 1

# ------------------------------------------------------------------------------------------------------------------

print('Função range () - atribuida como valor de uma var')
intervalo = range(10)
print(intervalo)
print()
for x in intervalo:
    print(x)


print('Função range () - atribuida como valor de uma var')
for x in range(12):
    print(x)


print('Função range () - atribuida como valor de uma var')
for x in range(-2, 12):
    print(x)

""" aqui, estamos indicando para a função range () onde ela deve iniciar seu intervalo, mas a contagem de 12 começa a partir do valor 0 """

print('Função range () - atribuida como valor de uma var')
for x in range(14, -5, -1):
    print(x)

""" O último valor é excluído do for"""

""" 
    Estrutura de repetição For
    x : variável auxiliar
"""
