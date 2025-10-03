# Laboratório 1

"""
    Escrever um programa em Python que solicite informações de três pessoas, como nome, idade, peso e altura. Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. Usar a formatação de interpolação.
"""

# Exibição dos dados alinhados usando interpolação (%)

# Pessoa 1
print("Informe o seu nome:")
nome1 = input("Nome: ")
idade1 = int(input("Idade: "))
peso1 = float(input("Peso (kg): "))
altura1 = float(input("Altura (m): "))

print()
print("*" * 60)

# # Pessoa 2
print("Informe o seu nome:")
nome2 = input("Nome: ")
idade2 = int(input("Idade: "))
peso2 = float(input("Peso (kg): "))
altura2 = float(input("Altura (m): "))

print()
print("*" * 60)

# # Pessoa 3
print("Informe o seu nome:")
nome3 = input("Nome: ")
idade3 = int(input("Idade: "))
peso3 = float(input("Peso (kg): "))
altura3 = float(input("Altura (m): "))

print()
print("*" * 60)

# Exibindo as informações - forma 1
print("\n--- Segue informações coletadas ---")

print()
print("*" * 60)

print("Pessoa 1 se chama:  %-15s, Idade: %5d anos, Peso: %8.1f kg, Altura: %8.2f m" %
      (nome1, idade1, peso1, altura1))
print("Pessoa 2 se chama:  %-15s, Idade: %5d anos, Peso: %8.1f kg, Altura: %8.2f m" %
      (nome2, idade2, peso2, altura2))
print("Pessoa 3 se chama:  %-15s, Idade: %5d anos, Peso: %8.1f kg, Altura: %8.2f m" %
      (nome3, idade3, peso3, altura3))

# Exibindo as informações - forma 2
print("\n=== Dados Cadastrados ===")
print("%-15s %5s %8s %8s" % ("Nome", "Idade", "Peso", "Altura"))
print("-" * 40)
print("%-15s %55d %8.1f %8.2f" % (nome1, idade1, peso1, altura1))
print("%-15s %55d %8.1f %8.2f" % (nome2, idade2, peso2, altura2))
print("%-15s %55d %8.1f %8.2f" % (nome3, idade3, peso3, altura3))

# Notas:

""" 
    O que é interpolação?

    A interpolação é uma forma de inserir valores em uma string. Ela permite que você crie textos dinâmicos, substituindo "marcadores" por valores de variáveis. É uma técnica muito útil para formatar saídas, como relatórios, mensagens ou, no caso do seu exemplo, tabelas.

    Como funciona a interpolação com %?

    A ideia principal é usar um "código de formatação" dentro da string para indicar onde e como cada valor deve ser inserido.

    Códigos de formatação: São os "marcadores". Eles dizem qual tipo de dado será inserido  e como ele deve ser formatado (alinhamento, número de casas decimais, etc.).

    %s para string; 
    %d para número inteiro; 
    %f para número decimal
    
    Operador %: Ele conecta a string de formatação com os valores que serão inseridos.

    Valores: São as variáveis ou valores literais que substituirão os marcadores na ordem em que aparecem. Eles precisam estar dentro de parênteses.

    \n Este é um caractere de nova linha. Quando o Python encontra o \n, ele faz com que o texto que o segue comece em uma nova linha. Na prática, ele pula uma linha antes de imprimir o texto.

    %-15s: O número 15 define que a string ocupará um espaço de 15 caracteres. O sinal de menos (-) alinha o texto à esquerda. Isso garante que a palavra "Nome" sempre comece no mesmo lugar.

    %5s: Ocupa 5 caracteres, alinhado à direita (o padrão).

    %8s: Ocupa 8 caracteres, alinhado à direita.

    %8.1f: Ocupa 8 caracteres no total para um número decimal (f de float). O .1 define que o número terá uma casa decimal após a vírgula.

    %8.2f: Ocupa 8 caracteres no total. O .2 define que o número terá duas casas decimais.
"""

# ----------------------------------------------------------------------------------------------------------------------

"""
    O uso de f-strings (f'Meu nome é {nome}') é a forma mais moderna e recomendada de fazer interpolação em Python. Elas são mais simples de ler, mais rápidas de executar e muito mais fáceis de usar do que o operador % que vimos antes.

    A sintaxe é bem direta:

    Comece a string com a letra f (minúscula ou maiúscula, mas a minúscula é o padrão).

    Dentro da string, use chaves {} para "envelopar" a variável ou a expressão que você quer inserir.

    Veja a forma geral: f'seu texto {variavel} e mais texto'

print(f"%-15s %5s %8s %8s" % ("Nome", "Idade", "Peso", "Altura")) Usando % para o cabeçalho
print(f"{nome:<15} {idade:>5} {peso:>8.1f} {altura:>8.2f}")

Saída:

Nome           Idade    Peso   Altura
Maria             28   65.4f   1.68f

    {nome:<15}: O sinal < alinha o texto à esquerda em um espaço de 15 caracteres.

    {idade:>5}: O sinal > alinha o texto à direita em um espaço de 5 caracteres.

    {peso:>8.1f}: Alinha à direita em um espaço de 8 caracteres e mostra o valor com uma casa decimal (.1f).

    {altura:>8.2f}: Alinha à direita em um espaço de 8 caracteres e mostra o valor com duas casas decimais (.2f).

    Você também pode colocar operações matemáticas ou chamadas de funções diretamente dentro das chaves.

print(f"A idade de {nome} em 10 anos será de {idade + 10} anos.")

Saída: A idade de Maria em 10 anos será de 38 anos.

"""

# Exibindo as informações usando o f-strings
print("\n--- Segue informações coletadas ---")
print("*" * 60)
print(
    f"Nome: {nome1:<15} Idade: {idade1:>5} Peso: {peso1:>8.1f} Altura: {altura1:>8.1f}")
print(
    f"Nome: {nome2:<15} Idade: {idade2:>5} Peso: {peso2:>8.1f} Altura: {altura2:>8.1f}")
print(
    f"Nome: {nome3:<15} Idade: {idade3:>5} Peso: {peso3:>8.1f} Altura: {altura3:>8.1f}")
