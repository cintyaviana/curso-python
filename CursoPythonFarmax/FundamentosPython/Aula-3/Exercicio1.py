
"""
    Laboratório 1
    Criar um programa que utilize uma estrutura de repetição for. Nesta estrutura, o usuário deverá fornecer 5 nomes a serem adicionados em uma lista. No final, apresentar os nomes em ordem crescente.
"""

nomes = []  # Lista para armazenar os nomes

for i in range(5):  # Coletar os nomes
    nome = input(f"Digite o nome {i+1}: ")

    nomes.append(nome)  # Adicionar o nome na lista

''' O comando .append adicionar um novo item ao final da lista '''

nomes.sort()  # Organizar a lista em ordem alfabética

"""O método .sort() ordena a lista em ordem crescente"""

# Exibir a lista
print("Os nomes digitados, em ordem alfabética, são:")
print(nomes)
