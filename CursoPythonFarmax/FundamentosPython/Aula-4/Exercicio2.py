
"""
Laboratório 4

Escrever uma função que receba como parâmetro uma lista variável de preços de produtos (itens de produtos) e uma lista de taxas aplicadas a estes produtos. 

A lista de produtos deve representar um parâmetro *args, enquanto a lista de taxas aplicadas, **kwargs.
"""


def CalcularPrecoFinal(*args, **kwargs):
    """
    *args: Coleta argumentos (p´reço) em uma tupla: (100,50,60)
    **kwargs: Coleta argumentos (Imposto e Desconto) em um dicionário: {'imposto': 10, 'desconto': 5}
    """

    PrecosFinais = []

    # Pega os valores das taxas, se eles existirem, caso contrário retorna o valor indicado (0).
    Imposto = kwargs.get('Imposto', 0)
    Desconto = kwargs.get('Desconto', 0)

    """O get() é um método de dicionários em Python que é usado para buscar um valor por sua chave."""

    # Loop para calcular o imposto e desconto de acordo com os preços informados
    for Preco in args:
        ValorImposto = Preco * (Imposto / 100)
        ValorDesconto = Preco * (Desconto / 100)

        PrecoFinal = Preco + ValorImposto - ValorDesconto

        # Adiciona o preço final na nossa lista.
        PrecosFinais.append(PrecoFinal)

    return PrecosFinais


PrecoProduto1 = CalcularPrecoFinal(2000)
print(f"Preços sem taxas: {PrecoProduto1}")

PrecoProduto2 = CalcularPrecoFinal(2000, Imposto=10)
print(f"Preços com 10% de imposto: {PrecoProduto2}")

PrecoProduto3 = CalcularPrecoFinal(2000, Desconto=5)
print(f"Preços com 5% de desconto: {PrecoProduto3}")

PrecoProduto4 = CalcularPrecoFinal(2000, 6000, 10000, Imposto=10, Desconto=5)
print(f"Preços com imposto de 10% e desconto de 5%: {PrecoProduto4}")
