"""
    Laboratório 3
    Escrever um programa que produza uma senha com 4 dígitos numéricos onde cada dígito é um valor aleatório entre 0 e 9.

    A senha resultante deve ser uma string.

    Observação: cada dígito gerado deve ser concatenado com o próximo.
"""

import random  # Importar a biblioteca 'random'

Senha = ""  # Variável que vai receber a informação da senha

for i in range(4):  # Loop para gerar os números
    # Gerar um número aleatório entre 0 e 9 através da função random.randint(0,9)
    DigitoAleatorio = random.randint(0, 9)

    # Converter o número gerado para texto (string)
    DigitoTexto = str(DigitoAleatorio)

    Senha = Senha + DigitoTexto  # Adicionar o dígito em texto na nossa string 'senha'

print(f"A senha gerada é: {Senha}")
