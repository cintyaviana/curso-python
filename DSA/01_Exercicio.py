
# ======================================================================
# EXERCÍCIO 1
# ======================================================================
# Escreva um programa que peça ao usuário para digitar seu nome e, em seguida, imprima uma mensagem de boas-vindas com o nome fornecido
"""
Qual o seu nome? Cintya
Seja bem vindo(a) Cintya!
"""

# 1.0 Input dos dados pelo usuário
nome = str(input("Digite seu nome: "))

# 2.0 Print dos dados no terminal
print(f"Olá, {nome}! Seja bem-vindo(a)!")

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

# Pode ser feito dessa forma também:

print(f"Soma: {numero1 + numero2}")
print(f"Subtração: {numero1 - numero2}")
print(f"Multiplicação: {numero1 * numero2}")
print(f"Divisão: {numero1 / numero2}")

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

# Pode ser feito dessa forma também:

print(idade_ana < idade_beto)


# ======================================================================
# EXERCÍCIO 7
# ======================================================================
# Receba um número inteiro do usuário e use o operador de módulo (%) para verificar se o número é par ou ímpar. Imprima o resultado.

# 01 Input de variáveis
numero = int(input("Digite um número inteiro!"))

# 02 Teste de hipótese

if numero % 2 == 0:
    print(f"Este número {numero} é par")

else:
    print(f"Este número {numero} é impar")


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

# 01 Declaração de variáveis
ano = int("2026")

# 02 Print da csoma do ano
print(f"{ano + 1}")

# ======================================================================
# EXERCÍCIO 11
# ======================================================================
"""
Crie a string:

frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   ". 

Remova os espaços em branco do início e do fim da string e imprima a nova string.
"""

# 01 Declaração de variáveis
frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   "

# 02 Print da variável tratada
print(f"{frase.strip()}")

# ======================================================================
# EXERCÍCIO 12
# ======================================================================
# Na string do exercício anterior (já sem os espaços), converta toda a frase para letras maiúsculas.

# 01 Declaração de variáveis
frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   "

# 02 Print da variável tratada
print(f"{frase.strip().upper()}")


# ======================================================================
# EXERCÍCIO 13
# ======================================================================
# Ainda usando a mesma string, substitua a palavra "poderosa" por "incrível".

# 01 Declaração de variáveis
frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   "

# 02 Print da variável tratada
print(f"{frase.replace('poderosa', 'incrível').strip().upper()}")

# ======================================================================
# EXERCÍCIO 14
# ======================================================================
# Verifique e imprima o número total de caracteres na string frase (após as modificações dos exercícios anteriores).

# 01 Declaração de variáveis
frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   "

# 02 Print da variável tratada
print(
    f"O número total de caracteres na string é {len(frase.replace('poderosa', 'incrível').strip().upper())}.")

# ======================================================================
# EXERCÍCIO 15
# ======================================================================
# Use fatiamento (slicing) para extrair e imprimir apenas a palavra "Python" da string frase.

# 01 Declaração de variáveis
frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   "

# 02 Print da variável
print(f"{frase[3:8]}")

# ======================================================================
# EXERCÍCIO 16
# ======================================================================
# Crie uma lista chamada compras com os seguintes itens: "arroz", "feijão", "macarrão", "carne". Imprima a lista.

# 01 Declaração de variáveis
compras = ["arroz", "feijão", "macarrão", "carne"]

# 02 Print da variável
print(f"{compras}")

# ======================================================================
# EXERCÍCIO 17
# ======================================================================
# Adicione o item "leite" ao final da lista compras e imprima a lista atualizada.

# 01 Declaração de variáveis
compras = ["arroz", "feijão", "macarrão", "carne"]
compras.append("leite")

# 02 Print da variável
print(f"{compras}")

# ======================================================================
# EXERCÍCIO 18
# ======================================================================
# Acesse e imprima o segundo item da lista compras.

# 01 Declaração de variáveis
compras = ["arroz", "feijão", "macarrão", "carne"]

# 02 Print da variável
print(f"{compras[1]}")

# ======================================================================
# EXERCÍCIO 19
# ======================================================================
# Remova o item "macarrão" da lista compras e imprima a lista final.

# 01 Declaração de variáveis
compras = ["arroz", "feijão", "macarrão", "carne"]

compras.remove("macarrão")

# 02 Print da variável
print(f"{compras}")

# ======================================================================
# EXERCÍCIO 20
# ======================================================================
# Crie uma lista de números de 1 a 5. Use uma função para calcular e imprimir o tamanho (número de elementos) dessa lista.

# 01 Declaração de variáveis
lista = [1, 2, 3, 4, 5]

# 02 Print da variável
print(f"{len(lista)}")

# ======================================================================
# EXERCÍCIO 21
# ======================================================================
# Crie uma tupla chamada meses com os três primeiros meses do ano: "Janeiro", "Fevereiro", "Março".

# 01 Declaração de variáveis
tupla = ("Janeiro", "Fevereiro", "Março")

# ======================================================================
# EXERCÍCIO 22
# ======================================================================
# Tente adicionar o mês "Abril" à tupla meses. O que acontece? Explique o resultado.

# Resposta: Depois de criada uma tupla não é possível alterar ela, é imutável.

# ======================================================================
# EXERCÍCIO 23
# ======================================================================
# Acesse e imprima o primeiro mês da tupla meses.

# 01 Declaração de variáveis
tupla = ("Janeiro", "Fevereiro", "Março")

# 02 Print da variável
print(f"{tupla[0]}")

# ======================================================================
# EXERCÍCIO 24
# ======================================================================
"""
Crie um dicionário chamado filme com as seguintes chaves e valores: 

- titulo = "O Poderoso Chefão",
- ano = 1972
- diretor = "Francis Ford Coppola"
"""
# 01 Declaração de variáveis
filme = {
    "titulo": "O Poderoso Chefão",
    "ano": 1972,
    "diretor": "Francis Ford Coppola"
}

# ======================================================================
# EXERCÍCIO 25
# ======================================================================
# Acesse e imprima o ano de lançamento do filme a partir do dicionário.

# 01 Declaração de variáveis
filme = {
    "titulo": "O Poderoso Chefão",
    "ano": 1972,
    "diretor": "Francis Ford Coppola"
}

# 02 Print da variável
print(f"Ano do filme: {filme['ano']}.")


# ======================================================================
# EXERCÍCIO 26
# ======================================================================
# Adicione uma nova chave genero com o valor "Drama" ao dicionário filme e imprima o dicionário completo.

# 01 Declaração de variáveis
filme = {
    "titulo": "O Poderoso Chefão",
    "ano": 1972,
    "diretor": "Francis Ford Coppola"
}

filme["genero"] = "Drama"

# 02 Print da variável
print(f"{filme}")

# ======================================================================
# EXERCÍCIO 27
# ======================================================================
# Modifique o valor da chave ano para 1973 e imprima o dicionário atualizado.

# 01 Declaração de variáveis
filme = {
    "titulo": "O Poderoso Chefão",
    "ano": 1972,
    "diretor": "Francis Ford Coppola"
}

filme["ano"] = 1973

# 02 Print da variável
print(f"{filme}")

# ======================================================================
# EXERCÍCIO 28
# ======================================================================
# Crie uma lista com os seguintes números: [1, 2, 2, 3, 4, 4, 5, 1]. Use um conjunto para remover os números duplicados e imprima o resultado.

# 01 Declaração de variáveis
lista = [1, 2, 2, 3, 4, 4, 5, 1]
lista = set(lista)

# 02 Print da variável
print(F"{lista}")

# ======================================================================
# EXERCÍCIO 29
# ======================================================================
"""
Crie dois conjuntos: 

- set_a = {1, 2, 3, 4}
- set_b = {3, 4, 5, 6}

Encontre e imprima a interseção entre os dois conjuntos (os elementos que estão em ambos).
"""
# 01 Declaração de variáveis
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# 02 Print da variável
print(f"{set_a.intersection(set_b)}")

# ======================================================================
# EXERCÍCIO 30
# ======================================================================
# Escreva um programa que peça ao usuário para digitar sua altura em metros (ex: 1.75) e seu peso em quilogramas (ex: 68.5). Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura * altura) e imprima o resultado formatado com duas casas decimais.

"""
altura = Informe sua altura: 1.75
peso = Informe o seu peso: 68.5

IMC = peso / (altura * altura)

"""

# 01 Declaração de variáveis
altura = float(input("Informe a sua altura:"))
peso = float(input("Informe o seu peso:"))

# 02 Print da variável
print(f"Seu IMC é: {(peso/(altura * altura)):.2f}")
