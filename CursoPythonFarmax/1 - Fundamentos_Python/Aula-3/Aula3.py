
# Comando IF

numero = int(input('Forneça um valor inteiro'))
if numero > 0:
    print('O número informado é positivo')
    print("Segunda instrução do bloco")

""" Os dois prints está dentro dessa condição If"""

print()
print("-" * 100)
print()

numero = int(input('Forneça um valor inteiro: '))
if numero > 0:
    print('O número informado é positivo')
print("Segunda instrução do bloco")

""" Nesse caso, o primeiro print está dentro do If e o outro fora, ou seja, o segundo print será executado dentro do contexto mesmo se no If retornar False"""

print()
print("-" * 100)
print()

# -----------------------------------------------------------------------------------------------------------------------
# Comando IF ... ELSE

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
print("-" * 100)
print()

# ------------------------------------------------------------------------------------------------------------------
# Comando IF ... ELIF ... ELSE

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
print("-" * 100)
print()

# ------------------------------------------------------------------------------------------------------------------
# Estrutura de repetição for

"""
Dentre as estruturas de repetição, a estrutura for é adequada para situações em que a quantidade de repetições é conhecida previamente. Nesta lição serão mostrados exemplos de utilização desta estrutura.

# Percorrendo uma lista

Uma das formas mais comuns de utilização da estrutura "for" é a realização de buscas em listas. Aqui existe a possibilidade de se realizar algum tratamento diferenciado em cada elemento da estrutura
"""

colecao = [1, 3, 4, 7, 10]
posicao = 0
for x in colecao:
    print('Elemento na posição', posicao, '=', x)
    posicao += 1

"""
No exemplo, a variável x representa, sequencialmente, cada elemento da variável "colecao" a cada passo da repetição.

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
Em muitas situações a estrutura de repetição é usada para outros propósitos diferentes de manipular coleções, apenas para repetir trechos de código. Para cenários como esse, o Python disponibiliza a função range().

Esta função possui diferentes formas de execução, variando a quantidade de parâmetros. Os exemplos a seguir ilustram o uso desta função:
"""
c1 = range(10)  # produz uma sequencia numérica de 0 a 9, com passo 1

"""
O parâmetro informado na função range() não entra na sequência, ele é apenas o limite superior. O exemplo a seguir mostra a estrutura for usando a função range():
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
Quando a função "for" for usada com três parâmetros, seus valores são: range(valor_inicial, limite, passo)

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

# ------------------------------------------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------------------------------------------
# Uso do for em cadeias de caracteres

"""
Muitas vezes temos a necessidade de analisar caracteres de uma string — por diversos motivos. O comando for pode perfeitamente ser usado para este fim.

O exemplo a seguir percorre os caracteres de uma string e adiciona o caractere * entre eles:
"""

s = ''
for ch in 'python':
    s += ch + '*'

print(s)

# ------------------------------------------------------------------------------------------------------------------
# O comando pass

"""
Existem momentos em que o programa deve ser escrito, mas ainda não foi definido o bloco a ser executado pelo for. Como o comando não pode ser escrito sem um bloco, pode-se usar o comando pass. Este comando não tem nenhuma utilidade prática, mas ajuda no desenvolvimento do código impedindo que apresente erros.
"""

for x in range(5):
    pass

"""
Vale ressaltar que este comando pode ser usado em outras estruturas também, como o comando if, outras estruturas de repetição e até mesmo em classes.
"""

# ------------------------------------------------------------------------------------------------------------------
# Estrutura de repetição while

"""
Ela possui suas vantagens em relação à estrutura for, o que justifica seu uso.

Este modelo de estrutura de repetição é adequado para os cenários onde não se sabe a quantidade de repetições a ser executada, ou seja, sabe-se quando começa, mas não se tem informação de quando irá terminar.

O exemplo a seguir ilustra um uso da estrutura while:
"""

x = 0
while x < 10:
    print(x)
    x += 1
print('Fim do programa.')

"""ou"""

x = 0
while x < 10:
    print(x)
    x += 1
else:
    print('Fim do programa.')

"""
Assim como a estrutura for, a estrutura while também permite o uso do comando else.

Nos dois exemplos o resultado é o mesmo:
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
Fim do programa.

# ------------------------------------------------------------------------------------------------------------------
# Os comandos break e continue

Ao longo da execução de uma estrutura de repetição é possível interrompê-la ou suspendê-la para atender a alguma regra imposta ao programa. Para casos como estes, pode-se usar os comandos break e/ou continue.

break: interrompe a execução da estrutura de repetição. O programa continua sua execução a partir da próxima instrução após a estrutura;

continue: pausa a estrutura de repetição, seguindo para o próximo passo da mesma estrutura.

Neste exemplo, o usuário informa uma certa quantidade de números. O programa termina (a estrutura de repetição é interrompida) quando o usuário digitar o número 0 (zero). Se o número informado for negativo, este será ignorado. O programa apresentará a quantidade de números não negativos informados.
"""

soma = 0
quantidade = 0

while True:
    numero = int(input('Informe um número: '))
    if numero == 0:
        break
    if numero < 0:
        continue
    soma += numero
    quantidade += 1

print(f'Soma dos valores positivos informados: {soma}')
print(f'Quantidade de valores positivos informados: {quantidade}')

"""
Neste exemplo pode-se destacar o uso dos comandos break e continue. break é usado para interromper o processo de solicitação de números para o usuário, e continue é usado para impedir que o valor negativo seja incluído na soma ou na quantidade.
"""
