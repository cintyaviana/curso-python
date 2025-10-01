
"""
Laboratório 2
Neste laboratório, uma lista de 100 números será criada de forma aleatória, ou seja, os elementos serão números aleatórios.

Escrever o programa de forma a exibir E adicionar em uma lista, apenas os valores gerados que sejam maiores que 10.
"""

import random  # Importar a biblioteca 'random'

ListaCompleta = []  # Lista para armazenar os dados aleatórios
MaioresQue10 = []  # Lista para armazenar os valores > 10

for i in range(100):  # Loop para gerar os números
    # Gerar um número aleatório entre 1 e 100 através da função random.randint(0,100)
    NumeroAleatorio = random.randint(0, 100)

    if NumeroAleatorio > 10:  # Verificar se o número é maior que 10
        # Se for, adicionar esse número à lista
        MaioresQue10.append(NumeroAleatorio)

print("Números gerados que são maiores que 10:")
print(MaioresQue10)
