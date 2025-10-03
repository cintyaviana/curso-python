
"""
Laboratório 3
Tomar como base o cálculo do Imposto de Renda Pessoa Física. O acesso para este cálculo pode ser realizado através do link: https://www27.receita.fazenda.gov.br/simulador-irpf/

Escrever uma função que receba como parâmetro o valor da base de cálculo do salário, e retorne o imposto de renda correspondente.

Sugestão: Usar tuplas para armazenar as faixas de valores.
"""

# Lista + Tuplas (valor_maximo, aliquota, parcela_a_deduzir)
"""
    As tuplas são exatamente como as listas, exceto pelo fato de que seus elementos, uma vez inseridos, permanecem naquela posição, ou seja, não podem ser alterados ou substituídos.

    A definição de tuplas usa o caractere "parênteses" para reunir seus elementos.
"""

TabelaIR = [
    (2259.20, 0, 0),
    (2826.65, 7.5, 169.44),
    (3751.05, 15, 381.44),
    (4664.68, 22.5, 662.77),
    (999999999, 27.5, 896.00)
]


def CalcularIR(Salario):
    # Calcula o Imposto de Renda com base no salário.

    ImpostoDevido = 0

    # Validação da faixa de salário
    for Faixa in TabelaIR:
        Limite, Aliquota, Deducao = Faixa
        if Salario <= Limite:
            # O cálculo do imposto é (salário * alíquota) - dedução
            ImpostoDevido = (Salario * Aliquota / 100) - Deducao
            break  # Sai do loop depois de achar a faixa.

    # Validação se o IR for menor que 0
    if ImpostoDevido < 0:
        return 0

    return ImpostoDevido


Salario1 = 1200
IRCalculado1 = CalcularIR(Salario1)
print(
    f"Para um salário de R${Salario1:.2f}, o imposto de renda é R${IRCalculado1:.2f}")

Salario2 = 2100
IRCalculado2 = CalcularIR(Salario2)
print(
    f"Para um salário de R${Salario2:.2f}, o imposto de renda é R${IRCalculado2:.2f}")

Salario3 = 2500
IRCalculado3 = CalcularIR(Salario3)
print(
    f"Para um salário de R${Salario3:.2f}, o imposto de renda é R${IRCalculado3:.2f}")

Salario4 = 4600
IRCalculado4 = CalcularIR(Salario4)
print(
    f"Para um salário de R${Salario4:.2f}, o imposto de renda é R${IRCalculado4:.2f}")

Salario5 = 1000000
IRCalculado5 = CalcularIR(Salario5)
print(
    f"Para um salário de R${Salario5:.2f}, o imposto de renda é R${IRCalculado5:.2f}")
