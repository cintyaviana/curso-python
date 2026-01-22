

# =====================================================================================================================================
# 1.0 TOMADA DE DECISÃO COM ESTRUTURAS CONDICIONAIS
# ====================================================================================================================================
# As estruturas condicionais (if, elif, else) permitem que o programa execute diferentes blocos de código com base em certas condições.

# Define a variável
import dsaprincipal
from modulodsa import dsa_saudacao, PI
import modulodsa
import random
import math
nota = 8.5

# Agora checamos o valor da variável e tomamos decisões
if nota >= 7.0:
    print("Aprovado!")
else:
    print("Reprovado.")

# Retorno: Aprovado!

# -------------------------------------------------------------------------------------------------------------------------------------

# Define a variável
idade = 100

# Agora checamos o valor da variável e tomamos decisões
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

# Retorno: Você é um idoso.

# =====================================================================================================================================
# 2.0 ESTRUTURAS DE REPETIÇÃO
# ====================================================================================================================================
# As estruturas de repetição (for e while) são usadas para executar um bloco de código várias vezes.

# -------------------------------------------------------------------------------------------------------------------------------------
# Loop for
# -------------------------------------------------------------------------------------------------------------------------------------
# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string).

# -------------------------------------------------------------------------------------------------------------------------------------
# Define uma lista
frutas = ["maçã", "banana", "cereja"]

# Imprime a mensagem
print("Frutas disponíveis:")

# Loop pela lista
for fruta in frutas:
    print(f"- {fruta}")

"""
Frutas disponíveis:
- maçã
- banana
- cereja

"""

# -------------------------------------------------------------------------------------------------------------------------------------
# Criando uma tupla
cores = ("vermelho", "verde", "azul")

# Loop for percorrendo a tupla
for cor in cores:
    print(cor)

"""
vermelho
verde
azul
"""

# -------------------------------------------------------------------------------------------------------------------------------------
# Criando um dicionário com o número de cursos em Formações da DSA
formacoes_dsa = {"Formação Cientista de Dados": 6,
                 "Formação Analista de Dados": 4, "Formação Engenheiro de Dados": 5}

# Loop for percorrendo chaves e valores
for chave, valor in formacoes_dsa.items():
    print(chave, ":", valor)

"""
Formação Cientista de Dados : 6
Formação Analista de Dados : 4
Formação Engenheiro de Dados : 5
"""

# -------------------------------------------------------------------------------------------------------------------------------------
# Exemplo com a função range()
print("\nContagem até 5:")
for numero in range(6):  # Gera números de 0 a 5
    print(numero)

"""
Contagem até 5:
0
1
2
3
4
5
"""

# -------------------------------------------------------------------------------------------------------------------------------------
# Loop while
# ------------------------------------------------------------------------------------------------------------------------------------
# O loop while executa um bloco de código enquanto uma condição for verdadeira.

# -------------------------------------------------------------------------------------------------------------------------------------
# Define a variável
contador = 5

# Imprime a mensagem
print("Contagem regressiva:")

# Loop
while contador > 0:
    print(contador)
    contador -= 1

"""
Contagem regressiva:
5
4
3
2
1
"""

"""
O for em Python é usado quando você já sabe sobre o que quer iterar (como uma lista, tupla, dicionário, string, range, etc.). Ele percorre cada elemento de uma sequência ou iterável de forma automática, sem que você precise gerenciar manualmente a condição de parada.

Já o while é usado quando você não sabe previamente quantas vezes o loop vai rodar e a repetição depende de uma condição booleana que deve continuar verdadeira para que o loop prossiga. Você precisa cuidar manualmente de alterar o estado dessa condição para evitar loops infinitos.

Em resumo:

- for → ideal quando você já tem uma coleção ou um número definido de repetições.

- while → ideal quando a repetição depende de uma condição que pode mudar dinamicamente ao longo da execução.

"""

# =====================================================================================================================================
# 3.0 ITERAÇÃO SOBRE ESTRUTURA DE DADOS COM LOOPS E CONDICIONAIS
# ====================================================================================================================================
# Iterar significa percorrer os elementos de uma coleção de dados.

# -------------------------------------------------------------------------------------------------------------------------------------
# Tupla de números
numeros = (3, 7, 10, 15, 20)

# Itera pela tupla e mostra apenas os números pares
for n in numeros:
    if n % 2 == 0:
        print(f"{n} é par")

"""
10 é par
20 é par
"""

# -------------------------------------------------------------------------------------------------------------------------------------
# Lista de nomes
nomes = ["Ana", "Bruno", "Carlos", "Amanda", "Beatriz"]

# Itera pela lista e mostra apenas os nomes que começam com 'A'
for nome in nomes:
    if nome.startswith("A"):
        print(f"Nome encontrado com A: {nome}")

"""
Nome encontrado com A: Ana
Nome encontrado com A: Amanda
"""

# -------------------------------------------------------------------------------------------------------------------------------------
# Dicionário com produtos e preços
produtos = {"arroz": 25, "feijão": 12, "carne": 45, "macarrão": 8}

# Itera pelo dicionário e mostra apenas produtos acima de 20 reais
for item, preco in produtos.items():
    if preco > 20:
        print(f"{item} custa {preco} reais (acima de 20)")

"""
arroz custa 25 reais (acima de 20)
carne custa 45 reais (acima de 20)
"""

# =====================================================================================================================================
# 4.0 CONTROLE DE FLUXO EM LOOPS
# ====================================================================================================================================
# As instruções break e continue alteram o fluxo de execução de um loop.

# -------------------------------------------------------------------------------------------------------------------------------------
# break
# -------------------------------------------------------------------------------------------------------------------------------------
# A instrução break para a execução do loop imediatamente.

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mensagem
print("\nBuscando pelo número 5...")

# Loop com break
for numero in numeros:
    if numero == 5:
        print("Número 5 encontrado!")
        break  # Sai do loop
    print(f"Verificando {numero}...")  # Faz parte do for

"""
Buscando pelo número 5...
Verificando 1...
Verificando 2...
Verificando 3...
Verificando 4...
Número 5 encontrado!
"""

# -------------------------------------------------------------------------------------------------------------------------------------
# continue
# -------------------------------------------------------------------------------------------------------------------------------------
# A instrução continue pula a iteração atual e continua com a próxima.

# Mensagem
print("\nImprimindo apenas os números ímpares:")

# Loop com instrução continue
for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # Pula para a próxima iteração se o número for par
    print(numero)

"""
Imprimindo apenas os números ímpares:
1
3
5
7
9
"""

# =====================================================================================================================================
# 5.0 COMPREHENSIONS (LIST, SET, DICT E GENERATOR) EM PYTHON
# ====================================================================================================================================

"""
Estas estruturas são consideradas construtores sintáticos (syntactic constructs) ou, mais formalmente, expressões de compreensão (comprehension expressions).

Na documentação oficial Python, os nomes são:

- List comprehension → expressão que gera listas.

- Set comprehension → expressão que gera conjuntos.

- Dict comprehension → expressão que gera dicionários.

- Generator expression → expressão que gera iteradores (e pode ser convertido em tupla, lista, etc.).

Ou seja, o termo técnico mais amplo é comprehension: uma forma mais curta e expressiva de construir coleções (ou geradores) a partir de iteráveis com filtros e transformações aplicadas inline.
"""

# Criando uma lista de quadrados dos números de 0 a 9
quadrados = [x ** 2 for x in range(10)]

# Print
print(f"\nQuadrados de 0 a 9: {quadrados}")

# Quadrados de 0 a 9: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

type(quadrados)  # list

# -------------------------------------------------------------------------------------------------------------------------------------

# Criando uma lista de números pares de 0 a 20
pares = [x for x in range(21) if x % 2 == 0]

# Print
print(f"Números pares de 0 a 20: {pares}")

# Números pares de 0 a 20: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

type(pares)  # list

# -------------------------------------------------------------------------------------------------------------------------------------

# Cria um dicionário com números e seus quadrados
quadrados_dict = {x: x ** 2 for x in range(6)}
print(quadrados_dict)

# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

type(quadrados_dict)  # dict

# -------------------------------------------------------------------------------------------------------------------------------------

# Conjunto de quadrados (sem valores repetidos)
quadrados_set = {x ** 2 for x in [1, 2, 2, 3, 3, 4]}
print(quadrados_set)

# {16, 1, 4, 9}

type(quadrados_set)  # set

# -------------------------------------------------------------------------------------------------------------------------------------
# Generator expression (não é tupla ainda)
gen = (x ** 2 for x in range(6))
print(gen)

# Convertendo em tupla
quadrados_tuple = tuple(x ** 2 for x in range(6))
print(quadrados_tuple)

"""
<generator object <genexpr> at 0x111d6c1e0>
(0, 1, 4, 9, 16, 25)
"""

type(quadrados_tuple)  # tuple

"""
Um generator em Python é um iterador especial que não armazena todos os valores na memória de uma vez, mas sim gera cada valor sob demanda. No caso, gen não é uma lista de quadrados de 0 a 5, mas um objeto que sabe como calcular esses valores quando você pedir. A grande vantagem é que o generator economiza memória.
"""

# =====================================================================================================================================
# 6.0 TRABALHANDO COM FUNÇÕES
# ====================================================================================================================================
# Funções são blocos de código reutilizáveis que realizam uma tarefa específica.

# -------------------------------------------------------------------------------------------------------------------------------------
# Definindo uma função simples


def dsa_saudacao():
    print("\nOlá! Bem-vindo ao Python.")


# Chamando a função
dsa_saudacao()

# Olá! Bem-vindo ao Python.

# -------------------------------------------------------------------------------------------------------------------------------------
# Definindo uma função que retorna um valor


def dsa_soma_numeros(a, b):
    """Esta função retorna a soma de dois números."""
    return a + b


# Chamando a função e armazenando o resultado em uma variável
resultado = dsa_soma_numeros(5, 3)

# Print
print(f"O resultado da soma é: {resultado}")

# O resultado da soma é: 8

# =====================================================================================================================================
# 7.0 PARÂMETROS E ARGUMENTOS DE FUNÇÕES
# ====================================================================================================================================
# Diferentes formas de passar informações para as funções.

# -------------------------------------------------------------------------------------------------------------------------------------
# Argumentos posicionais


def dsa_apresentacao(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

# Pode usar os argemento em ordem, ou fora de ordem, mas sendo nomeados:


# Argumentos em ordem
dsa_apresentacao("Ana", 25)

# Argumentos nomeados
dsa_apresentacao(idade=30, nome="Bob")

# -------------------------------------------------------------------------------------------------------------------------------------
# Parâmetros com valores padrão (default: valor padrão)


def dsa_saudacao_completa(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}!")


# Chamando a função
dsa_saudacao_completa("Maria")  # pode ser passado em o 2º argumento.

# Chamando a função
dsa_saudacao_completa("Bob", "Bom dia")


# =====================================================================================================================================
# 7.1 TRABALHANDO COM NÚMERO VARIADO DE ARGUMENTOS EM FUNÇÃO PYTHON
# ====================================================================================================================================

"""
Em Python, *args e **kwargs são formas de tornar funções mais flexíveis, permitindo receber um número variável de argumentos sem precisar definí-los todos na assinatura da função.

*args – argumentos posicionais variáveis

O asterisco (*) antes do nome indica que a função pode receber qualquer quantidade de argumentos posicionais. Esses valores chegam dentro da função como uma tupla.

**kwargs – argumentos nomeados variáveis

Os dois asteriscos (**) indicam que a função pode receber qualquer quantidade de argumentos nomeados (chave e valor). Esses valores chegam dentro da função como um dicionário.
"""

# -------------------------------------------------------------------------------------------------------------------------------------
# Argumentos de tamanho variável (*args)


def dsa_soma_numeros(*args):
    """Soma um número variável de argumentos."""

    total = 0

    for numero in args:
        total += numero

    return total


# Soma dos Números: 15
print(f"Soma dos Números: {dsa_soma_numeros(1, 2, 3, 4, 5)}")

print(f"Soma dos Números: {dsa_soma_numeros(1, 2, 3)}")  # Soma dos Números: 6

# Soma dos Números: 530.3
print(f"Soma dos Números: {dsa_soma_numeros(10, 400, 0.3, 120)}")

# -------------------------------------------------------------------------------------------------------------------------------------
# Argumentos de tamanho variável (**kwargs)


def dsa_exibe_info_pessoa(**kwargs):
    """Exibe informações passadas como pares chave-valor."""

    print("\nInformações da Pessoa:\n")

    for chave, valor in kwargs.items():
        print(f"- {chave}: {valor}")


# Chamando a função
dsa_exibe_info_pessoa(nome="Carla",
                      profissao="Engenheira de Dados",
                      hobby="Leitura")

"""
Informações da Pessoa:

- nome: Carla
- profissao: Engenheira de Dados
- hobby: Leitura
"""
# Chamando a função
dsa_exibe_info_pessoa(nome="Bob", profissao="Cientista de Dados")

"""
Informações da Pessoa:

- Bob: Cientista de Dados
"""

# =====================================================================================================================================
# 8.0 FUNÇÕES ANÔNIMAS (EXPRESSÃO LAMBDA)
# ====================================================================================================================================
# São pequenas funções anônimas definidas com a palavra-chave lambda, que ocorre no tempo de execução do código.

"""
dobro = lambda x : x *2

print(f"O dobro de 7 é: {dobro(7)}") 

"""

"""
A grande vantagem de usar expressões lambda em Python é a simplicidade e concisão para criar funções pequenas, temporárias e sem nome (anônimas).

Normalmente, quando você precisa de uma função, define com def. Mas às vezes a função é muito simples e usada apenas uma vez, dentro de outra operação (como um map, filter ou sorted). Nesses casos, a lambda evita código extra e deixa o fluxo mais direto.

Você pode combinar uma expressão lambda com a função map() para aplicar uma operação a cada elemento da lista, por exemplo.
"""

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lambda que retorna o quadrado de cada elemento
quadrados = list(map(lambda x: x ** 2, numeros))

print(quadrados)  # [1, 4, 9, 16, 25]


"""
Aqui:

- lambda x: x**2 define uma função anônima que calcula o quadrado.

- map() aplica essa função a cada elemento da lista.

- list() converte o resultado do map (um iterador) de volta para lista.

👉 Também daria para fazer com list comprehension, mas aí não seria lambda.
"""

# Lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Primeiro calculamos os quadrados com map + lambda
quadrados = list(map(lambda x: x ** 2, numeros))

# Agora filtramos apenas os pares com filter + lambda
quadrados_pares = list(filter(lambda x: x % 2 == 0, quadrados))

print("Quadrados:", quadrados)              # [1, 4, 9, 16, 25, 36]
print("Quadrados pares:", quadrados_pares)  # [4, 16, 36]

# =====================================================================================================================================
# 9.0 MÓDULOS DA BIBLIOTECA PADRÃO PYTHON
# ====================================================================================================================================
#  Python vem com uma vasta biblioteca de módulos para todo tipo de tarefa. E se precisar de mais, visite o repositório oficial de pacotes da linguagem:

# -------------------------------------------------------------------------------------------------------------------------------------
# Usando o módulo 'math' para funções matemáticas

# Calcula a raiz quadrada
raiz_quadrada = math.sqrt(25)

print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

# A raiz quadrada de 25 é: 5.0

# -------------------------------------------------------------------------------------------------------------------------------------
# Usando o módulo 'random' para gerar números aleatórios

# Gera um inteiro entre 1 e 100
numero_aleatorio = random.randint(1, 100)

print(f"Um número aleatório entre 1 e 100: {numero_aleatorio}")

# Um número aleatório entre 1 e 100: 95

# -------------------------------------------------------------------------------------------------------------------------------------
# Seleciona aleatoriamente uma cidade da lista
cidade_aleatoria = random.choice(["Rio de Janeiro", "Salvador", "Curitiba"])

# choice = escolha

print(f"Cidade escolhida aleatoriamente: {cidade_aleatoria}")

# Cidade escolhida aleatoriamente: Curitiba

# =====================================================================================================================================
# 10.0 CRIANDO E IMPORTANDO SEUS PRÓPRIOS MÓDULOS
# ====================================================================================================================================
# Você pode organizar seu código em arquivos (módulos) e importá-los em outros scripts.

# Passo 1: Crie o arquivo do módulo modulodsa.py


def dsa_saudacao(nome):
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}! Tudo bem?"


PI = 3.14159


# Passo 2: Crie o script principal para importar o módulo dsaprincipal.py

"""import modulodsa"""

# Usa a função e a variável do módulo
mensagem = modulodsa.dsa_saudacao("Mundo")
print(mensagem)
print(f"O valor de PI do nosso módulo é: {modulodsa.PI}")

# Outra forma: importando itens específicos

"""from modulodsa import dsa_saudacao, PI"""

mensagem_direta = dsa_saudacao("Aluno DSA")
print(mensagem_direta)
print(f"Valor de PI importado diretamente: {PI}")

# Para executar, você rodaria o arquivo principal.py. O Python automaticamente encontraria e usaria o conteúdo de meu_modulo.py.

"""
Olá, Mundo! Tudo bem?
O valor de PI do nosso módulo é: 3.14159
Olá, Aluno DSA! Tudo bem?
Valor de PI importado diretamente: 3.14159
"""
