
# ==========================================================================================================================================
# 1.0 LÓGICA DE PROGRAMAÇÃO E PSEUDOCODIGO
# ==========================================================================================================================================

"""
Para se aprender Python, precisa dominar a geração de pseudocódigos.

Exemplo:

Algoritmo para verificar se um aluno foi aprovado, considerando que a média para aprovação é 7 e que o aluno cursou 2 disciplinas.

Em pseudocódigo, poderíamos escrever:

INÍCIO
	LER a nota1 do aluno 
	LER a nota2 do aluno
	CALCULAR a média = (nota1 + nota2) / 2
	SE média >= 7 ENTÃO
		ESCREVER "Aluno Aprovado!"
	SENÃO
		ESCREVER "Aluno Reprovado."
	FIM SE
FIM

"""

# LER a nota1 do aluno
from datetime import date
nota1 = float(input("Digite a primeira nota do aluno: "))

# LER a nota2 do aluno
nota2 = float(input("Digite a segunda nota do aluno: "))

# CALCULAR a média
media = (nota1 + nota2) / 2

# Exibe a média calculada para o usuário
print(f"A média do aluno é: {media}")

# SE média >= 7 ENTÃO ... SENÃO ...
if media >= 7:
    # ESCREVER "Aluno Aprovado!"
    print("Aluno Aprovado!")
else:
    # ESCREVER "Aluno Reprovado."
    print("Aluno Reprovado.")

# ==========================================================================================================================================
# 2.0 VARIAVEIS: DECLARAÇÃO, REGRAS DE ATRIBUIÇÃO E NOMENCLATURA
# ==========================================================================================================================================

"""
Uma variável é um espaço na memória do computador destinado a armazenar dados. Em Python, a declaração e a atribuição de um valor a uma variável são feitas simultaneamente. 

Regras de Nomenclatura:
Nomes de variáveis devem começar com uma letra ou um underscore (_).
Não podem começar com um número.
Podem conter apenas caracteres alfanuméricos e underscores (A-z, 0-9 e _).
São "case-sensitive" (idade é diferente de Idade).

"""

nome_completo = "Cintya Viana"
idade = 34
altura = 1.61
estudante = True

if estudante == True:
    estudante = "Sim"
else:
    estudante = "Não"

print(f"Nome: {nome_completo}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} metros")
print(f"É estudante? {estudante}")

"""
Retorno:

Nome: Cintya Viana
Idade: 34 anos
Altura: 1.61 metros
É estudante? Sim

"""

"""
Python é uma linguagem dinamicamente "tipada". Você não precisa declarar o tipo das variáveis ao criá-las, pois Python descobre automaticamente pelo valor atribuído:
"""

x = 10
y = 12.0
z = "10"
teste = True

print(type(x))
print(type(y))
print(type(z))
print(type(teste))

"""
Retorno:

<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

"""

# Podemos somar tipos numéricos, mas não podemos somar número com string.
print(x + y)  # 22.0 float

# ==========================================================================================================================================
# 3.0 ESCOPO DE VARIÁVEIS
# ==========================================================================================================================================

"""
O escopo de uma variável define onde ela pode ser acessada no código.

Variáveis Globais: Declaradas fora de qualquer função. Podem ser acessadas de qualquer lugar do código.

Variáveis Locais: Declaradas dentro de uma função. Só podem ser acessadas dentro daquela função.
"""

# Variável Global
saudacao = "Olá, mundo!"
nome = "Aluno DSA"

# Função


def minha_funcao():

    # Variável Local
    nome = "Ana"
    print(f"\nDentro da função: {nome}")
    print(f"\nAcessando a variável global de dentro da função: {saudacao}")


minha_funcao()

print(f"\nFora da função: {saudacao}")
print(f"\nFora da função: {nome}")

"""
Retorno:

Dentro da função: Ana

Acessando a variável global de dentro da função: Olá, mundo!

Fora da função: Olá, mundo!

Fora da função: Aluno DSA
"""

# ==========================================================================================================================================
# 4.0 TIPOS DE DADOS PRIMITIVOS
# =========================================================================================================================================

# Estes são os tipos mais básicos de dados em python:

# Integer (Inteiro)
numero_inteiro = 100
print(f"Valor: {numero_inteiro}, Tipo: {type(numero_inteiro)}")

# Retorno: Valor: 100, Tipo: <class 'int'>

# Float (Ponto Flutuante)
numero_decimal = 19.99
print(f"Valor: {numero_decimal}, Tipo: {type(numero_decimal)}")

# Retorno: Valor: 19.99, Tipo: <class 'float'>

# String (Texto)
texto = "Python é incrível!"
print(f"Valor: '{texto}', Tipo: {type(texto)}")

# Retorno: Valor: Python é incrível!, Tipo: <class 'str'>

# Boolean (Booleano)
verdadeiro = True
falso = False
print(f"Valor: {verdadeiro}, Tipo: {type(verdadeiro)}")
print(f"Valor: {falso}, Tipo: {type(falso)}")

# Retorno: Valor: True, Tipo: <class 'bool'>
# Retorno: Valor: False, Tipo: <class 'bool'>

# ==========================================================================================================================================
# 5.0 OPERADORES ARITMÉTICOS, DE COMPARAÇÃO E LÓGICOS.
# ==========================================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------------------
# 5.1 OPERADORES ARITMÉTICOS
# -------------------------------------------------------------------------------------------------------------------------------------------
# Usados para realizar operações matemáticas

# Definição de variáveis
a = 10
b = 3

# Usando operadores aritméticos
soma = a + b              # Adição
subtracao = a - b         # Subtração
multiplicacao = a * b     # Multiplicação
divisao = a / b           # Divisão (resultado é sempre float)
divisao_inteira = a // b  # Divisão inteira (descarta a parte decimal)
modulo = a % b            # Módulo (resto da divisão)
potencia = a ** b         # Potenciação

print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao:.2f}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {modulo}")
print(f"{a} ** {b} = {potencia}")

"""
Retorno:

10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
10 // 3 = 3
10 % 3 = 1
10 ** 3 = 1000

"""

# As regras da matemática se aplicam aqui normalmente

# Variáveis
a = 10
b = 0

# Tentativa de divisão por zero
# a/b

# Cuidado. Isso não pode!
# 8 + 's'

# Mas isso pode! (não é soma, é concatenação)
'8' + 's'

# Retorno '8s'

# -------------------------------------------------------------------------------------------------------------------------------------------
# 5.2 OPERADORES DE COMPARAÇÃO
# -------------------------------------------------------------------------------------------------------------------------------------------
# Usados para comparar valores. O resultado é sempre um Boolean (True or False)

# Definição de variáveis
x = 5
y = 10

# Operador "maior que"
x > y

# Operador "menor que"
x < y

# Operador "igual a"
x == y

# Operador "diferente de"
x != y

# Operador "maior ou igual a"
x >= 5

# Operador "menor ou igual a"
x <= y

print(f"{x} > {y} ? {x > y}")      # Maior que
print(f"{x} < {y} ? {x < y}")      # Menor que
print(f"{x} == {y} ? {x == y}")    # Igual a
print(f"{x} != {y} ? {x != y}")    # Diferente de
print(f"{x} >= 5 ? {x >= 5}")      # Maior ou igual a
print(f"{x} <= {y} ? {x <= y}")    # Menor ou igual a

"""
Retorno:
5 > 10 ? False
5 < 10 ? True
5 == 10 ? False
5 != 10 ? True
5 >= 5 ? True
5 <= 10 ? True

"""

# -------------------------------------------------------------------------------------------------------------------------------------------
# 5.3 OPERADORES LÓGICOS
# -------------------------------------------------------------------------------------------------------------------------------------------
# Usados para combinar expressões booleanas

# Definição de variáveis
tem_dinheiro = True
tem_tempo = False

# Operador AND (e): Ambos precisam ser verdadeiros
print(f"O cliente pode viajar? {tem_dinheiro and tem_tempo}")

# Operador OR (ou): Pelo menos um precisa ser verdadeiro
print(f"O cliente pode viajar? {tem_dinheiro or tem_tempo}")

# Operador NOT (não): Inverte o valor booleano
print(f"O cliente pode viajar? {tem_dinheiro and not tem_tempo}")

"""
Retorno:
O cliente pode viajar? False
O cliente pode viajar? True
O cliente pode viajar? True

"""

# ==========================================================================================================================================
# 6.0 MANIPULAÇÃO DE STRING
# ==========================================================================================================================================
# Strings são sequências de caracteres e possuem muitos métodos úteis

# Define uma variável do tipo string
frase = "  Aprender Python é muito divertido!  "

# Concatenação
nome = "Maria"
saudacao = "Olá, " + nome + "!"
print(saudacao)

# Olá, Maria!

# Tamanho da string
print(f"Tamanho da frase: {len(frase)}")

# Tamanho da frase: 38 - ele considera os espaços também

# len > length : comprimento

# Maiúsculas
print(f"Maiúsculas: {frase.upper()}")

# Maiúsculas:   APRENDER PYTHON É MUITO DIVERTIDO!
# upper : mais alto

# Minúsculas
print(f"Minúsculas: {frase.lower()}")

# Minúsculas:   aprender python é muito divertido!
# lower: mais baixo

# Remover espaços em branco do início e do fim
frase_sem_espacos = frase.strip()
print(f"Frase sem espaços: '{frase_sem_espacos}'")

# Frase sem espaços: 'Aprender Python é muito divertido!'
# strip: aparar

# Substituir texto
print(
    f"Substituindo 'divertido' por 'legal': {frase_sem_espacos.replace('divertido', 'legal')}")

# Substituindo 'divertido' por 'legal': Aprender Python é muito legal!
# replase: substituir

# Fatiamento (Slicing) - Acessando partes de uma string
# O índice em Python começa em 0
print(frase_sem_espacos)
print(f"O primeiro caractere: {frase_sem_espacos[0]}")
print(f"A palavra 'Python': {frase_sem_espacos[9:15]}")  # Do índice 9 ao 14

"""
Retorno:

Aprender Python é muito divertido!
O primeiro caractere: A
A palavra 'Python': Python
"""


# ==========================================================================================================================================
# 7.0 ESTRUTURA DE DADOS - LISTAS
# ==========================================================================================================================================
# Listas são coleções ordenadas e mutáveis de itens. Podem conter diferentes tipos de dados.

# Criando uma lista
frutas = ["maçã", "banana", "laranja", "abacaxi"]
# Lista de frutas: ['maçã', 'banana', 'laranja', 'abacaxi']
print(f"Lista de frutas: {frutas}")

type(frutas)  # list

# Acessando um item pelo índice
print(f"A primeira fruta é: {frutas[0]}")  # A primeira fruta é: maçã
print(f"A última fruta é: {frutas[-1]}")  # A última fruta é: abacaxi

# Adicionando um item ao final da lista
frutas.append("uva")
# Lista após adicionar 'uva': ['maçã', 'banana', 'laranja', 'abacaxi', 'uva']
print(f"Lista após adicionar 'uva': {frutas}")

# Removendo um item
frutas.remove("laranja")
# Lista após remover 'laranja': ['maçã', 'banana', 'abacaxi', 'uva']
print(f"Lista após remover 'laranja': {frutas}")

# Modificando um item
frutas[0] = "morango"
# Lista após modificar o primeiro item: ['morango', 'banana', 'abacaxi', 'uva']
print(f"Lista após modificar o primeiro item: {frutas}")

# Podemos imprimir diretamente
print(frutas)  # ['morango', 'banana', 'abacaxi', 'uva']

# Verificando o tamanho da lista
print(f"A lista tem {len(frutas)} frutas.")  # A lista tem 4 frutas.

# Deletando a lista
del frutas

# Lista não pode mais ser acessada
print(frutas)

# ==========================================================================================================================================
# 8.0 ESTRUTURA DE DADOS - TRUPLAS
# ==========================================================================================================================================
# Tuplas são coleções ordenadas e imutáveis de itens. Uma vez criadas, não podem ser alteradas.

# Criando uma tupla
coordenadas = (10.0, 20.5)
# Tupla de coordenadas: (10.0, 20.5)
print(f"Tupla de coordenadas: {coordenadas}")

type(coordenadas)  # tuple

# Acessando um item pelo índice
print(f"Coordenada X: {coordenadas[0]}")  # Coordenada X: 10.0
print(f"Coordenada Y: {coordenadas[1]}")  # Coordenada Y: 20.5

# Tentativa de modificar uma tupla resultará em erro (descomente para ver)
# coordenadas[0] = 15.0

# Tuplas são úteis para dados que não devem ser alterados, como meses do ano, coordenadas, etc.
dias_da_semana = ("Segunda", "Terça", "Quarta",
                  "Quinta", "Sexta", "Sábado", "Domingo")
# O primeiro dia da semana é: Segunda
print(f"O primeiro dia da semana é: {dias_da_semana[0]}")

# ==========================================================================================================================================
# 9.0 ESTRUTURA DE DADOS - DICIONÁRIOS
# ==========================================================================================================================================
# Dicionários são coleções de pares chave: valor. São mutáveis.

# Criando um dicionário de informações de um aluno
aluno = {
    "nome": "Bob",
    "idade": 22,
    "curso": "Data Science Para Análise Multivariada",
    "aluno_ativo": True
}

print(f"Dicionário do aluno: {aluno}")

# Dicionário do aluno: {'nome': 'Bob', 'idade': 22, 'curso': 'Data Science Para Análise Multivariada', 'aluno_ativo': True

type(aluno)  # dict

# Acessando um valor pela sua chave
print(f"Nome do aluno: {aluno['nome']}")

# .get() é uma forma segura de acessar chaves
print(f"Curso: {aluno.get('curso')}")

"""
Nome do aluno: Bob
Curso: Data Science Para Análise Multivariada
"""

# Adicionando um novo par chave-valor
aluno["cidade"] = "São Paulo"
print(f"Dicionário atualizado:\n {aluno}")

"""
Dicionário atualizado:
 {'nome': 'Bob', 'idade': 22, 'curso': 'Data Science Para Análise Multivariada', 'aluno_ativo': True, 'cidade': 'São Paulo'}
"""

# Modificando um valor existente
aluno["idade"] = 23
print(f"Idade atualizada: {aluno['idade']}")  # Idade atualizada: 23

# Removendo um par chave-valor
del aluno["aluno_ativo"]
print(f"Dicionário após remover a chave 'ativo':\n {aluno}")

"""
Dicionário após remover a chave 'ativo':
 {'nome': 'Bob', 'idade': 23, 'curso': 'Data Science Para Análise Multivariada', 'cidade': 'São Paulo'}
"""

# ==========================================================================================================================================
# 10.0 ESTRUTURA DE DADOS - CONJUNTOS (SETS)
# ==========================================================================================================================================
# Conjuntos são coleções não ordenadas de itens únicos e mutáveis. Eles são úteis para remover duplicatas e realizar operações matemáticas de conjuntos (união, interseção)

# Criando um conjunto (note que os itens duplicados são removidos)
numeros = {1, 2, 3, 4, 2, 3, 5}
# Conjunto de números (sem duplicatas): {1, 2, 3, 4, 5}
print(f"Conjunto de números (sem duplicatas): {numeros}")

type(numeros)  # set

# Adicionando um item
numeros.add(6)
# Após adicionar o valor 6: {1, 2, 3, 4, 5, 6}
print(f"Após adicionar o valor 6: {numeros}")

# Removendo um item
numeros.remove(2)
print(f"Após remover o 2: {numeros}")  # Após remover o 2: {1, 3, 4, 5, 6}

# Operações de conjunto
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# União (todos os elementos de ambos os conjuntos)
uniao = conjunto_a.union(conjunto_b)
print(f"União de A e B: {uniao}")  # União de A e B: {1, 2, 3, 4, 5, 6}

# Interseção (elementos que estão em ambos os conjuntos)
intersecao = conjunto_a.intersection(conjunto_b)
print(f"Interseção de A e B: {intersecao}")  # Interseção de A e B: {3, 4}


# ==========================================================================================================================================
# 11.0 CONVERSÃO ENTRE TIPOS DE DADOS (TYPE CASTING)
# ==========================================================================================================================================
# É a conversão de um tipo de dado para outro.

# Convertendo de string para número integer
numero_em_texto = "123"
numero_inteiro = int(numero_em_texto)
print(
    f"String '{numero_em_texto}' para Inteiro: {numero_inteiro}, Tipo: {type(numero_inteiro)}")

# String '123' para Inteiro: 123, Tipo: <class 'int'>

# Isso aqui não pode ser feito
# teste = "Esta é uma string de teste"
# teste_int = int(teste)
# print(teste_int)

# Convertendo de string para número float
numero_decimal_em_texto = "45.67"
numero_float = float(numero_decimal_em_texto)
print(
    f"String '{numero_decimal_em_texto}' para Float: {numero_float}, Tipo: {type(numero_float)}")

# String '45.67' para Float: 45.67, Tipo: <class 'float'>

# Convertendo de número para string
idade = 25
idade_texto = str(idade)
print(
    f"Inteiro {idade} para String: '{idade_texto}', Tipo: {type(idade_texto)}")

# Inteiro 25 para String: '25', Tipo: <class 'str'>

# Convertendo entre estruturas de dados
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 4, 5]
conjunto_unico = set(lista_com_duplicatas)
lista_sem_duplicatas = list(conjunto_unico)

print(f"\nLista original: {lista_com_duplicatas}")
print(f"\nConvertida para Conjunto (remove duplicatas): {conjunto_unico}")
print(f"\nConvertida de volta para Lista: {lista_sem_duplicatas}\n")

"""
Lista original: [1, 2, 2, 3, 4, 4, 4, 5]

Convertida para Conjunto (remove duplicatas): {1, 2, 3, 4, 5}

Convertida de volta para Lista: [1, 2, 3, 4, 5]
"""

# ==========================================================================================================================================
# 12.0 ENTRADA E SAÍDA PADRÃO
# ==========================================================================================================================================
# A forma mais comum de interagir com o usuário é através da entrada (input) de dados pelo teclado e da saída (output) de informações na tela

# -------------------------------------------------------------------------------------------------------------------------------------------
# 12.1 Saída de dados com print()
# -------------------------------------------------------------------------------------------------------------------------------------------
# Já usamos bastante, mas aqui estão alguns recursos adicionais, como as f-strings."

# Variáveis
nome = "Juliana"
idade = 28
cidade = "Rio de Janeiro"

# Usando f-string (a forma mais moderna e recomendada)
print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro no {cidade}.")

# Formatando números
preco = 49.95678
print(f"O preço do produto é R$ {preco:.2f}")  # Formata para 2 casas decimais

"""
Olá, meu nome é Juliana, tenho 28 anos e moro no Rio de Janeiro.
O preço do produto é R$ 49.96
"""

# -------------------------------------------------------------------------------------------------------------------------------------------
# 12.2 Entrada de Dados com input()
# -------------------------------------------------------------------------------------------------------------------------------------------
# A função input() sempre retorna uma string. Por isso, é comum precisar fazer o type casting."

# Pedindo o nome do usuário (string)
nome_usuario = input("Qual é o seu nome? ")

# Pedindo a idade do usuário (precisa converter para int)
idade_usuario_str = input("Qual é a sua idade? ")
idade_usuario_int = int(idade_usuario_str)

# Pode fazer direto:

idade_usuario_str = int(input("Qual é a sua idade? "))


# Pega o ano corrente na data definida no sistema operacional da sua máquina
ano_atual = date.today().year

# Processando os dados
ano_nascimento = ano_atual - idade_usuario_int

# Exibindo o resultado
print(f"\nOlá, {nome_usuario}! Bem-vindo(a).")
print(
    f"Você tem {idade_usuario_int} anos e nasceu aproximadamente em {ano_nascimento}.")

"""
Qual é o seu nome?  Bob
Qual é a sua idade?  35

Olá, Bob! Bem-vindo(a).
Você tem 35 anos e nasceu aproximadamente em 1990.
"""
