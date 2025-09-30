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
    mensagemSaida += f" {notas50} Nota(s) de R$ 50,00"
if notas20 > 0:
    mensagemSaida += f", {notas20} Nota(s) de R$ 20,00"
if notas10 > 0:
    mensagemSaida += f", {notas10} Nota(s) de R$ 10,00"
if notas5 > 0:
    mensagemSaida += f", {notas5} Nota(s) de R$ 5,00"

# Construção final da respostas
mensagemSaida += ". Obrigado por usar o caixa do Banco do Brasil!"

# Exibição da resposta ao usuário
print(mensagemSaida)

""" 
    Nota: O while é uma estrutura de repetição em Python, conhecida como laço de repetição condicional. Ele executa um bloco de código repetidamente enquanto uma condição for verdadeira.
"""


# Validação de quais notas foram maiores que 0 para formar a resposta ao usuário usando f-strings.
