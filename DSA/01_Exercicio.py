
# ======================================================================
# EXERCÍCIO 1
# ======================================================================
# Escreva um programa que peça ao usuário para digitar seu nome e, em seguida, imprima uma mensagem de boas-vindas com o nome fornecido

# 1.0 Input dos dados pelo usuário
nome = str(input("Qual o seu nome?"))

# 2.0 Print dos dados no terminal
print(f"Seja bem vindo(a) {nome}!")

"""
Qual o seu nome? Cintya
Seja bem vindo(a) Cintya!
"""

# ======================================================================
# EXERCÍCIO 2
# ======================================================================
# Crie duas variáveis, numero1 e numero2, e atribua a elas valores inteiros. Calcule a soma, subtração, multiplicação e divisão dessas variáveis e imprima os resultados.

# 1.0 Input dos dados pelo usuário
numero1 = int(input("Informe o 1º número!"))
numero2 = int(input("Informe o 2º número!"))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# 2.0 Print dos dados no terminal
print(f"Soma de {numero1} + {numero2} = {soma}.")
print(f"Subtração de {numero1} + {numero2} = {subtracao}.")
print(f"Multiplicação de {numero1} + {numero2} = {multiplicacao}.")
print(f"Divisão de {numero1} + {numero2} = {divisao}.")

# ======================================================================
# EXERCÍCIO 3
# ======================================================================
# "Qual é a principal diferença entre uma variável de escopo local e uma de escopo global?"

# Resposta: Uma variável de escopo global pode ser retomanda tando dentro de uma função quando fora, já a variável local só pode ser retomanda dentro da função em que ela foi gerada.

# ======================================================================
# EXERCÍCIO 4
# ======================================================================
# Crie uma variável chamada saldo com o valor 500.50 (float). Em seguida, crie uma variável saque com o valor 200.25 (float). Subtraia o saque do saldo e imprima o saldo final formatado para duas casas decimais.

# 1.0 Input dos dados pelo usuário
valor = 500.00
saque = 200.25

# 2.0 Calculo do saldo final
saldo_final = valor - saque

# 3.0 Print dos dados no terminal
print(f"Seu saldo é de R$ {saldo_final:.2f}.")


# ======================================================================
# EXERCÍCIO 5
# ======================================================================
# Declare uma variável booleana chamada **tem_carteira_de_motorista** e atribua a ela o valor True. Imprima uma mensagem que diga "Pode dirigir" se a variável for verdadeira e "Não pode dirigir" caso contrário.

# 01 Declaração de variáveis
tem_carteira_de_motorista = True

# 02 Teste de hipótese
if tem_carteira_de_motorista == True:
    print(f"Pode dirigir")

else:
    print(f"Não pode dirigir")

# ======================================================================
# EXERCÍCIO 6
# ======================================================================
"""
Crie duas variáveis: 

- idade_ana = 25
- idade_beto = 30

Use operadores de comparação para verificar se a idade de Ana é menor que a de Beto e imprima o resultado booleano.
"""
# 01 Declaração de variáveis
idade_ana = 25
idade_beto = 30

# 02 Comparativo de idade
comparativo = idade_ana < idade_beto

# 3.0 Print da comparação no terminal
print(f"Ana é mais nova que Beto? {comparativo}")


# ======================================================================
# EXERCÍCIO 7
# ======================================================================
# Receba um número inteiro do usuário e use o operador de módulo (%) para verificar se o número é par ou ímpar. Imprima o resultado.

# 01 Input de variáveis
numero = int(input("Digite um número inteiro!"))

# 02 Teste de hipótese

if numero % 2 == 0:
    print(f"Este número é par")

else:
    print(f"Este número é impar")


# ======================================================================
# EXERCÍCIO 8
# ======================================================================
"""
Crie duas variáveis booleanas: 

- chovendo = True
- guarda_chuva = False

Use operadores lógicos para verificar se uma pessoa vai se molhar (se está chovendo E ela não tem guarda-chuva).
"""

# 01 Declaração de variáveis
chovendo = True
guarda_chuva = False

# 02 Teste de hipótese
vai_se_molhar = chovendo and not guarda_chuva

# 3.0 Print da comparação no terminal
print(f"Você vai se molhar? {vai_se_molhar}")


# ======================================================================
# EXERCÍCIO 9
# ======================================================================
# Calcule a potência de 2 elevado a 10 e imprima o resultado.

# 01 Declaração de variáveis
numero = 2
potencia = 10

# 02 Cálculo da potência
resultado = numero ** potencia

# 3.0 Print da comparação no terminal
print(f"O resultado de {numero} elevado a {potencia} é igual a {resultado}.")


# ======================================================================
# EXERCÍCIO 10
# ======================================================================
# Converta a string "2026" para um tipo inteiro e armazene-a em uma variável chamada ano. Em seguida, some 1 a essa variável e imprima o novo ano.

ano = int("2026")

print(f"{ano + 1}")

# ======================================================================
# EXERCÍCIO 11
# ======================================================================

# ======================================================================
# EXERCÍCIO 12
# ======================================================================

# ======================================================================
# EXERCÍCIO 13
# ======================================================================

# ======================================================================
# EXERCÍCIO 14
# ======================================================================

# ======================================================================
# EXERCÍCIO 15
# ======================================================================

# ======================================================================
# EXERCÍCIO 16
# ======================================================================

# ======================================================================
# EXERCÍCIO 17
# ======================================================================

# ======================================================================
# EXERCÍCIO 18
# ======================================================================

# ======================================================================
# EXERCÍCIO 15
# ======================================================================

# ======================================================================
# EXERCÍCIO 19
# ======================================================================

# ======================================================================
# EXERCÍCIO 20
# ======================================================================

# ======================================================================
# EXERCÍCIO 21
# ======================================================================

# ======================================================================
# EXERCÍCIO 22
# ======================================================================

# ======================================================================
# EXERCÍCIO 23
# ======================================================================

# ======================================================================
# EXERCÍCIO 24
# ======================================================================

# ======================================================================
# EXERCÍCIO 25
# ======================================================================

# ======================================================================
# EXERCÍCIO 26
# ======================================================================

# ======================================================================
# EXERCÍCIO 27
# ======================================================================

# ======================================================================
# EXERCÍCIO 28
# ======================================================================

# ======================================================================
# EXERCÍCIO 29
# ======================================================================

# ======================================================================
# EXERCÍCIO 30
# ======================================================================
