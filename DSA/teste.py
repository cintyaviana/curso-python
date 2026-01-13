# Define uma variável do tipo string
frase = "  Aprender Python é muito divertido!  "

# Concatenação
nome = "Maria"
saudacao = "Olá, " + nome + "!"
print(saudacao)

# Olá, Maria!

# Tamanho da string
print(f"Tamanho da frase: {len(frase)}")

# Tamanho da frase: 38 - ele considera os espaços também

# Maiúsculas e Minúsculas
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")

# Maiúsculas:   APRENDER PYTHON É MUITO DIVERTIDO!
# Minúsculas:   aprender python é muito divertido!

# Remover espaços em branco do início e do fim
frase_sem_espacos = frase.strip()
print(f"Frase sem espaços: '{frase_sem_espacos}'")

# Frase sem espaços: 'Aprender Python é muito divertido!'

# Substituir texto
print(
    f"Substituindo 'divertido' por 'legal': {frase_sem_espacos.replace('divertido', 'legal')}")

# Substituindo 'divertido' por 'legal': Aprender Python é muito legal!

# Fatiamento (Slicing) - Acessando partes de uma string
# O índice em Python começa em 0
print(frase_sem_espacos)
print(f"O primeiro caractere: {frase_sem_espacos[0]}")
print(f"A palavra 'Python': {frase_sem_espacos[9:15]}")  # Do índice 9 ao 14
