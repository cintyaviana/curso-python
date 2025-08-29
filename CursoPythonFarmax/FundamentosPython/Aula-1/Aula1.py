# O uso desse caracter "#" indica um comentário. 

# Variável = instrução lógica com o propósito de guardar e/ou armazenar algum valor para ser usado mais tarde em alguma instrução no código.

"""O sinal "=" indica atribuição de valor e não o famoso sinal de = (igual)"""
x = 10

#-----------------------------------------------------------------------------------------------------------------------
# Tipos de variáveis:
x = 10                    # Variável numérica (int)
nome = "Cintya"           # Variável alfanuméricas (str)
curso = 'Python'          # Variável alfanuméricas (str)
altura = 1.61             # Variável real (float)
compra = x > 10           # Variável booleana (bool) - True or False

#-----------------------------------------------------------------------------------------------------------------------
# Usamos a função print para mostrar a variável:
print("x = ",x," - Tipo:",type(x))
print("nome = ",nome,"- Tipo: ",type(nome))
print("curso = ",curso," - Tipo: ",type(curso))
print("altura =",altura," - Tipo",type(altura))
print("compra", compra," - Tipo: ",type(compra))

print()
print("------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------------------------
# Múltiplas Atribuições:
v1 = v2 = v3 = 10

print(v1,",",v2,",",v3)
print("A variável V1 = ",v1)
print("A variável V2 = ",v2)
print("A variável V3 = ",v3)
v2 = 50     #Reatribuindo o valor para a variável
print(v1,",",v2,",",v3)

print()
print("------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------------------------
# Atribuições Sequenciais:
"""A atribuição das variáveis precisa seguir a ordem"""
aluna, idade = "Cintya", 34

print("A Aluna",aluna,"está fazendo", idade, "anos de idade hoje.")

print()
print("------------------------------------------------------")
print()

""" Texto dentro de aspas triplas funciona como comentário dentro do código mas se for atribuído a uma variável ela vai ser interpretada como uma string"""

frase = """ Esta frase vai ser uma string"""

print(frase)

print()
print("------------------------------------------------------")
print()

a = 23
b = 24
c = 12
x = 8
 
"""Utiliza a bara "\" quando a função for muito grande e queira continuar na linha de baixo."""
"""Potencia é referenciado por dois asteriscos (**)"""

y = a*x**2+ \
    b*x+c

"""Forma errada de fazer"""
w = a*x^2+ \
    b*x+c

print("O valor da variável y é", y,".")
print("O valor da variável y é", w,".")

print()
print("------------------------------------------------------")
print()

