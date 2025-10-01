
""" 
    Laboratório 4
    Neste laboratório, o usuário fornece as informações: dia, mês e ano.

    Com base nestas informações, determinar quantos dias restam para terminar o ano informado.

    Realizar as validações:

    O mês informado deve estar na faixa entre 1 e 12;

    O dia informado deve ser compatível com o mês informado;

    Usar o ano para determinar o número de dias do mês de fevereiro.
"""

import calendar  # Importar a biblioteca 'calendar' para usar a função de ano bissexto

# 2. Criar uma lista com os dias de cada mês
# Por padrão, fevereiro tem 28 dias
dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# --- Coleta de dados ---
print("--- Calculadora de Dias Restantes no Ano ---")
dia_digitado = int(input("Digite o dia: "))
mes_digitado = int(input("Digite o mês: "))
ano_digitado = int(input("Digite o ano: "))

# 3. Adicionar a lógica do ano bissexto
# Se o ano for bissexto, o número de dias de fevereiro (índice 2) se torna 29
if calendar.isleap(ano_digitado):
    dias_por_mes[2] = 29
    total_dias_no_ano = 366  # Um ano bissexto tem 366 dias
else:
    total_dias_no_ano = 365  # Um ano normal tem 365 dias

# --- Cálculo de dias passados ---
dias_ja_passados = 0

# Usar um loop 'for' para somar os dias dos meses que já terminaram
for mes_passado in range(1, mes_digitado):
    dias_ja_passados = dias_ja_passados + dias_por_mes[mes_passado]

# Adicionar os dias do mês atual que já se passaram
dias_ja_passados = dias_ja_passados + dia_digitado

# --- Fazer a conta final ---
dias_restantes = total_dias_no_ano - dias_ja_passados

# --- Exibir o resultado ---
print("-" * 40)
print(f"Informações: {dia_digitado}/{mes_digitado}/{ano_digitado}")
print(f"Este ano tem {total_dias_no_ano} dias.")
print(f"Dias que já se passaram: {dias_ja_passados}")
print(f"Dias que faltam para o ano terminar: {dias_restantes}")
