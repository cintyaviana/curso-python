
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
Python é uma linguagem dinamicamente "tipada". Você não precisa declarar o tipo das variáveis ao criá-las, pois Python descobre automaticamente pelo valor atribuído:
"""

x = 10
y = 12.0
z = "10"
teste = True

print(type(x))  # int
print(type(y))  # float
print(type(z))  # str
print(type(teste))  # Bool

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

# As regras da matemática de aplicam aqui normalmente

# Variáveis
a = 10
b = 0

# Tentativa de divisão por zero
# a/b

# Cuidado. Isso não pode!
# 8 + 's'

# Mas isso pode! (não é soma, é concatenação)
'8' + 's'

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
