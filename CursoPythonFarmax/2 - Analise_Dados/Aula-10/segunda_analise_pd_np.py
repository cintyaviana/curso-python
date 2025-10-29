
# IMPORTAR AS BIBLIOTECAS NECESSÁRIAS
import pandas as pd
import numpy as np
import os  # Necessário para a solução de caminho

# 1 - PASSO: CARREGAR OS DADOS
NOME_DO_ARQUIVO = 'vendas.xlsx'

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo
CAMINHO_COMPLETO = os.path.join(DIRETORIO_ATUAL, NOME_DO_ARQUIVO)

# Carrega o DataFrame usando o caminho absoluto.
df = pd.read_excel(CAMINHO_COMPLETO)

# Exibe o resumo
print('Primeiras 5 linhas do df:')
print(df.head(5))
print('-'*50)

print()
print('=========================RESUMO ESTATISTICO===========================')
print()
print(df.describe())
print('-'*50)
print()

# o processo de trabalho está focado nas operações e análise fazendo uso do método groupby()
# para que seja possível fazer "agrupamentos" e entender o contexto do dataset


# vamos definir uma variavel pra receber como valor esta operação de totalização
print('----- Operação 1 - Totalização de produtos vendidos por Representante -----')
total_vendas_por_rep = df.groupby(['Rep'])[['Quantity']].sum()
print('\nTotal de vendas de produto por representante:\n')
print(total_vendas_por_rep)
print()
print('-'*50)

"""
total_vendas_por_rep: esta é variavel que recebe a operação - como valor de atribuição
# df.groupby(): aqui o dataframe - df - esta "fazendo uso" do método groupby()

# df.groupby(['Rep']): aqui, estamos "agrupando" os representantes
# [['Quantity']]: aqui, temos a associação da coluna 'Quantity' junto da coluna 'Rep' - há,
#                 então, uma associação entre as duas colunas

"""
print('----- Operação 2 - Número de vendas por Representante -----')
numero_venda_por_rep = df.groupby(['Rep'])['Rep'].count()
print('\nNúmero Total de vendas feito por representantes\n')
print(numero_venda_por_rep)
print('-'*50)

print('----- Operação 3 - Média de vendas por Representante -----')
media_venda_por_rep = df.groupby(['Rep'])['Quantity'].mean()
print('\nMédia de vendas de produtos por representante\n')
print(media_venda_por_rep)
print('-'*50)

"""
aqui, o valor obtido, com o uso do método .mean() - considera o seguinte contexto: para o  resultado é feito o calculo é observado quantas vezes o nome do representante é  encontrado dividido pelo numero total de produtos que ele vendeu: representante / qtde de  produtos vendidos
"""

print('----- Operação 4 - Agregação de dados das variáveis/colunas selecionadas -----')
agregacao = df.groupby(['Rep']).agg(
    {'Quantity': ['count', 'sum', 'mean', 'min', 'max']})
print('\nAnálise de quantidade de produtos e vendas pro representante(count, sum, mean, min, mas)\n')
print(agregacao)
print('-'*50)

"""
A instrução acima "agrupa" os dados por representantes e, para cada grupo, aplica as funções que foram definidas no dicionário; o resultado da operação de agregação é uma "tabela" resumida com as resultantes de cada operação!
"""

print('----- Operação 5 - Menor  preço de produto vendido por representante -----')
menor_preco_rep_prod = df.groupby(['Rep', "Product"])[['Price']].min()
print('\nMenor preço de produto vendido por representante\n')
print(menor_preco_rep_prod)
print('-'*50)

print('----- Operação 6 - Menor  preço de produto vendido por representante -----')
maior_preco_rep_prod = df.groupby(['Rep', "Product"])[['Price']].max()
print('\nMaior preço de produto vendido por representante\n')
print(maior_preco_rep_prod)
print('-'*50)

print('----- Operação 7 - Média preço de produto por representante -----')
media_preco_rep_prod = df.groupby(['Rep', "Product"])[['Price']].mean()
print('\nMédia preço de produto vendido por representante\n')
print(media_preco_rep_prod)
print('-'*50)
print()

print('----- CONFERINDO OS VALORES MIN E MAX DOS PRODUTOS -----')
checando_preco_min = df.groupby(['Rep', 'Product'])[['Price']].min()
checando_preco_max = df.groupby(['Rep', 'Product'])[['Price']].max()
print((menor_preco_rep_prod['Price'] == checando_preco_min['Price']).all())
print((maior_preco_rep_prod['Price'] == checando_preco_max['Price']).all())
print('-'*50)
print()

print('----- Operação 8 - Menor preço de produto -----')
menor_preco_pro = df.groupby(['Product'])[['Price']].min()
print('\nMenor preço por produto\n')
print(menor_preco_pro)
print('-'*50)
print()

print('----- Operação 8.b - Contagem, Soma, Media, Maior, Menor preço por produto -----')
agregacaoProduto = df.groupby(['Product']).agg(
    {'Price': ['count', 'sum', 'mean', 'min', 'max']})
print('\nValores em relação ao produtos - utiliziand as funções principais\n')
print(agregacaoProduto)
print('-'*50)
print()

print('----- Operação 9 - Menor valor/preço de produto vendido por representante -----')
# aqui, buscamos o produto "mais barato/com menor valor" que um representante negociou
operacao_9 = df[df['Price'] == df['Price'].min()][['Product', 'Rep', 'Price']]

# agora, vamos fazer uso do groupby() para totalizar
df.groupby(['Rep'])[['Quantity']].sum()
print('\nProduto com o menor preço/valor vendido por representante')
print(operacao_9)
print('-'*50)
print()

print('----- Operação 9.b - Menor valor/preço de produto vendido por representante - com todos os representantes -----')
operacao_9b = df.groupby(['Rep'])['Price'].idxmin()
resultado = df.loc[operacao_9b]

print('\nProduto com o menor valor/preço vendido por um representante - com todos os representantes')
print(resultado[['Rep', 'Product', 'Price']])
print('-'*50)
print()

"""
operacao_9b = df.groupby(['Rep'])['Price'].idxmin(): esta operação seleciona o produtos com 
o valor "mais baixo/barato" que foram negociados pro todos os representantes; para que 
pudessemos trazer este subconjunto foi necessario fazer uso da função idxmin(): é uma 
função que, ao ser executada, retorna o indice (linhas do df) de menor 'Price' de tro de 
cada agrupamento/representante e produto
"""


print('----- Operação 10 - Agrupamento com uma função lambda -----')
# calcular o intervalo interquartil (IQR) dos preços por produto
operacao_10 = df.groupby('Product')['Price'].apply(
    lambda x: x.quantile(0.75) - x.quantile(0.25))

print('Intervalo interquartil (IQR) dos preços - por produto:')
print(operacao_10)
print('-'*50)
print()

"""
IQR: é o contexto lógico que mede a dispersão dos dados, ou seja, o quanto os preços variam entre os valores intermediarios (1º e o 3º quartis)
"""

print('----- Operação 11 - Uso do pivot_table -----')
tabela_dinamica = pd.pivot_table(df, index=['Rep'], values=['Price'], columns=[
                                 'Product'], aggfunc=[np.min], fill_value=0)

print('\nTabela dinamica com o menor preço por representante e produto\n')
print(tabela_dinamica)
print('-'*50)
print()
