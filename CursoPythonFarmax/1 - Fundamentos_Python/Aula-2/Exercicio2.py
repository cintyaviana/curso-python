
# Laboratório 2

"""
    Suponha que em um caixa eletrônico existam cédulas disponíveis de 5, 10, 20 e 50 reais. Usando operações de divisão inteira e resto da divisão, escrever um programa que solicite ao usuário um valor para saque e, a partir deste valor, armazenar em variáveis e apresentar na tela a quantidade de cada cédula para compor o valor do saque.

    Obs.: Considerar neste exercício que os valores sejam sempre múltiplos de 5. Considerar também a menor quantidade possível de cédulas.
    
"""

# Boas Vindas
print("Bem-vindo(a) ao Banco do Brasil")

while True:

    valorSaque = int(
        input("Digite o valor do saque desejado (múltiplo de 5): "))

    if valorSaque > 0 and valorSaque % 5 == 0:
        break  # Sai do loop se o valor for válido
    else:
        print("O valor informado é inválido:")

# Validação da quantidade de notas
notas50 = valorSaque // 50
resto = valorSaque % 50

notas20 = resto // 20
resto = resto % 20

notas10 = resto // 10
resto = resto % 10

notas5 = resto // 5

# 6. Exibir o resultado.
mensagemSaida = "Você receberá as seguintes notas:"

# Validação de quais notas foram maiores que 0 para formar a resposta ao usuário.
if notas50 > 0:
    mensagemSaida += " %d Nota(s) de R$ 50,00" % notas50
if notas20 > 0:
    mensagemSaida += ", %d  Nota(s) de R$ 20,00" % notas20
if notas10 > 0:
    mensagemSaida += ", %d Nota(s) de R$ 10,00" % notas10
if notas5 > 0:
    mensagemSaida += ", %d  Nota(s) de R$ 5,00" % notas5

# Construção final da respostas
mensagemSaida += ". Obrigado por usar o caixa do Banco do Brasil!"

# Exibição da resposta ao usuário
print(mensagemSaida)

""" 
    Nota: 
    
    O while é uma estrutura de repetição em Python, conhecida como laço de repetição condicional. Ele executa um bloco de código repetidamente enquanto uma condição for verdadeira.
"""

# Validação de quais notas foram maiores que 0 para formar a resposta ao usuário usando f-strings.
if notas50 > 0:
    mensagemSaida += f" {notas50} nota(s) de R$ 50,00"
if notas20 > 0:
    mensagemSaida += f", {notas20} nota(s) de R$ 20,00"
if notas10 > 0:
    mensagemSaida += f", {notas10} nota(s) de R$ 10,00"
if notas5 > 0:
    mensagemSaida += f", {notas5} nota(s) de R$ 5,00"
