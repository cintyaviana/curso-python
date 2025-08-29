
# Entrada de dados
nome = input("Qual o seu nome?")
idade = int(input("Qual a sua idade?"))
altura = float(input("Qual a sua altura?"))

print("A aluna", nome, "tem", idade,
      "anos de idade e está com", altura, "de altura.")
print('*' * 50)

resultado = 'Nome: {0:20}, idade: {1}, altura: {2:10.2f}'

""" Uma string, em python pode ser considerado o menor conjunto de dados com o qual a linguagem pode Lidar.

    Um conjunto de dados, em python, é definido por 2 características fundamentais:
    1 - o dado do conjunto
    2 - a posição que esse valor ocupa

    Índices posicionais em ordem crescente: 0, 1, 2, 3, 4 ...
               0123456789
    Exemplo = 'jabuticaba'

    1 - o dado do conjunto = jabuticaba

"""

print(resultado.format(nome, idade, altura))

"""
    Posição 0 - Nome: {0:20} : a variável nome poderá ter até 20 caracter. 0123456789...20
                                                               Cintya Viana
    Posição 1 - idade: {1} : a variável idade ocupa o índice posicional de 2ª posição. 012
                                                                           034
    Posição 2 - altura: {2:10.2f} : a variável altura ocupa o índice posicional de 3ª posição e pode ter até 10 caracter. 0123 --10
                                                                                                              1.61
    .2f = 2 float = 2 casas decimais

    OBS: Se inverter o primeiro caracter em ordem diferente essa 0,1,2...etc vai dar erro.

    ex: resultado = 'Nome: {1:20}, idade: {2}, altura: {0:10.2f}'
# """

print()
print("------------------------------------------------------")
print()

# Operadores Aritméticos

n1 = 100
n2 = 30
n3 = 20
n4 = 50
n5 = 39
n6 = 10
n7 = 11

op1 = n1 / n2               # Divisão Real (float)
op2 = n1 // n2              # Divisão inteiro (int)
op3 = n1 % n2               # Resto da divisão inteiro (int)
op4 = n5 // n6              # Divisão inteiro (int)
op5 = n5 / n6               # Divisão Real (float)

print("Op1 =", op1, type(op1))
print("Op2 =", op2, type(op2))
print("Op3 =", op3, type(op3))
print("Op4 =", op4, type(op4))
print("Op5 =", op5, type(op5))

print()
print("------------------------------------------------------")
print()

# Operadores Aritméticos reduzidos

n1 = 100
n2 = 30
n3 = 20
n4 = 50
n5 = 39
n6 = 10

n1 += 2
n2 - + 10
n3 *= 5
n4 /= 5
n5 //= 2
n6 **= 2

print("n1", n1, type(n1))
print("n2", n2, type(n2))
print("n3 =", n3, type(n3))
print("n4 =", n4, type(n4))
print("n5 =", n5, type(n5))
print("n6 =", n6, type(n6))

print()
print("------------------------------------------------------")
print()

# Operadores Relacionais

"""== : verifica se dois operadores são iguais"""
"""!= : verifica se dois operadores são diferentes"""
"""> : verifica se o primeiro operador é maior que o segundo operador"""
""" >= : verifica se o primeiro operador é maior ou igual que o segundo operador"""
""" < : verifica se o primeiro operador é menor que o segundo operador"""
"""<= : verifica se o primeiro operador é menor ou igual que o segundo operador"""

# Operadores Lógicos

""" and : Operador E lógico. Resulta True somense se as duas condições envolvidas forem True, caso contrário, resulta False. """
""" or : Operador OU lógico. Resulta True se pelo menos uma das condições envolvidas for True, resulta em False quando as duas condições forem False"""
""" not : Inverte o resultado lógico"""

n1 = 100
n2 = 30
n3 = 20
n4 = 50

op1 = n1 == 100  # True
op2 = n2 <= n1  # True
op3 = n3 % 2 == 0  # True
op4 = n4 < n2  # False
op5 = n2 != 31 and n3 > 0  # True
op6 = n4 > 50 or n3 == 20  # True
op7 = (n2 >= 3 and n4 % 5 == 0) or n3 != 20  # True

print("op1", op1)
print("op2", op2)
print("op3", op3)
print("op4", op4)
print("op5", op5)
print("op6", op6)
print("op7", op7)

print()
print("------------------------------------------------------")
print()

n1 = 100
n2 = "Curso"
n3 = 12.5

op1 = type(n1) is int
op2 = type(n2) is not str
op3 = type(n3) is not float
op4 = type(n1) is float or n3 > 3

print('op1:', op1)
print('op2:', op2)
print('op3:', op3)
print('op4:', op4)

print()
print("------------------------------------------------------")
print()

# aqui, estamos observando se existe uma instacia de classe que classifica este dado como um tipo específico
n1 = isinstance(n1, int)
n2 = isinstance(n2, str)
n3 = not isinstance(n3, float)
n4 = not isinstance(n1, float) and (n3 > 0)

print('n1:', n1)
print('n2:', n2)
print('n3:', n3)
print('n4:', n4)

print()
print("------------------------------------------------------")
print()
