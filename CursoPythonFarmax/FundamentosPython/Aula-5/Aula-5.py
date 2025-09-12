

# ------------------------------------------------------------------------------------------------------------------
# Inferência sobre os parâmetros

"""
Visão geral da lição
Nesta lição será apresentado um procedimento envolvendo a declaração de um parâmetro com base em um tipo do Python, como meio de otimizar o acesso aos atributos desejados.

Declaração do tipo do parâmetro e inferência do tipo
Considerando que uma função deva receber como parâmetro uma string, e que dentro da função seja necessário executar algum método da string, é possível realizar uma inferência sobre o tipo. O exemplo a seguir ilustra melhor esta situação:
"""


def calcular_tamanho(texto: str):

    # Nesta imagem está sendo apresentada uma função contendo o parâmetro declarado como sendo do tipo string:


def calcular_tamanho(texto: str):

    # Isso não significa que o parâmetro seja, de fato, do tipo string, e sim que foi incluído este tipo para permitir o acesso às propriedades e métodos da string.

"""
Mesmo que o parâmetro esteja declarado como string, ainda assim é possível usá-lo como número no corpo da função.

Neste caso, o que foi feito foi uma inferência sobre o tipo do parâmetro, como forma de permitir acesso aos dados do objeto string.
"""
