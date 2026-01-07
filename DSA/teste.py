# Variável Global
saudacao = "Olá, mundo!"
nome = "Aluno DSA"

# Função


def minha_funcao_dsa():

    # Variável Local
    nome = "Ana"
    print(f"\nDentro da função: {nome}")
    print(f"\nAcessando a variável global de dentro da função: {saudacao}")


minha_funcao_dsa()

print(f"\nFora da função: {saudacao}")
print(f"\nFora da função: {nome}")
