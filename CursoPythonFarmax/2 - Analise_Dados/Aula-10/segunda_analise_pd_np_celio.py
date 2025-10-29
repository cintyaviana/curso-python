# IMPORTAR AS BIBLIOTECAS NECESSARIAS
import pandas as pd
import numpy as np

# 1º passo: carregar os dados - para este proposito vamos definir uma variavel
df = pd.read_excel('vendas.xlsx')
print()
print('Primeiras 5 linhas do df')
print(df.head(5))

print()
print('============= RESUMO ESTATISTICO ====================')
print()
print(df.describe())

'''
o processo de trabalho está focado nas operações e analise fazendo uso do método groupby() para que seja possivel fazer "agrupamentos" e entender o contexto do dataset
'''
print()
print('----- Operação 1 - Totalização produtos vendidos por Representante -----')
# vamos definir uma variavel pra receber como valor esta operação de totalização
total_vendas_por_rep = df.groupby(['Rep'])[['Quantity']].sum()
print('\nTotal de vendas de produto por representante:\n')
print(total_vendas_por_rep)
'''
total_vendas_por_rep: esta é variavel que recebe a operação - como valor de atribuição
df.groupby(): aqui o dataframe - df - esta "fazendo uso" do método groupby()

f.groupby(['Rep']): aqui, estamos "agrupando" os representantes
[['Quantity']]: aqui, temos a associação da coluna 'Quantity' junto da coluna 'Rep' - há, então, uma associação entre as duas colunas

.sum(): aqui, o método de soma dos valores é aplicada a coluna 'Quantity' que, por sua vez, esta associada a coluna 'Rep' - de representantes. Dessa forma, poderemos obter o total de quantidade de vendas para cada representante
'''
print()
print('----- Operação 2 - Número de vendas por Representante -----')
numero_vendas_por_rep = df.groupby(['Rep'])[['Rep']].count()
#numero_vendas_por_rep = df.groupby(['Rep'])[['Quantity']].count()
print('\nNumero total de vendas/pedidos feitos por representante:\n')
print(numero_vendas_por_rep)


print()
print('----- Operação 3 - Média de vendas por Representante -----')
media_venda_por_rep = df.groupby(['Rep'])[['Quantity']].mean()
print('\nMedia de vendas de produtos por representante\n')
print(media_venda_por_rep)

'''
aqui, o valor obtido, com o uso do método .mean() - considera o seguinte contexto: para o resultado é feito o calculo é observado quantas vezes o nome do representante é encontrado dividido pelo numero total de produtos que ele vendeu: representante / qtde de produtos vendidos
'''

print()
print('----- Operação 4 - Agregação de dados das variaveis/colunas selecionadas -----')
agregacao = df.groupby(['Rep']).agg({'Quantity': ['count', 'sum', 'mean', 'min', 'max']})
print('\nAnalise de quantidade de produtos e vendas por representante(count, sum, mean, min, max)\n')
print(agregacao)
'''
a instrução acima "agrupa" os dados por representante e, para cada grupo, aplica as funções que foram definidas no dicionario; o resultado da operação de agregação é uma "tabela" resumida com as resultantes de cada operação!
'''


print()
print('----- Operação 5 - Menor preço de produto vendido por representante -----')
menor_preco_rep_prod = df.groupby(['Rep', 'Product'])[['Price']].min()
print('\nMenor preço de produto vendido por representante\n')
print(menor_preco_rep_prod)

print()
print('----- Operação 6 - Maior preço de produto vendido por representante -----')
maior_preco_rep_prod = df.groupby(['Rep', 'Product'])[['Price']].max()
print('\nMaior preço de produto vendido por representante\n')
print(maior_preco_rep_prod)
'''
print()
print('----- Operação 7 - Media preço de produto vendido por representante -----')
media_preco_rep_prod = df.groupby(['Rep', 'Product'])[['Price']].mean()
print('\nMedia preço de produto vendido por representante\n')
print(media_preco_rep_prod)
'''
checando_preco_min = df.groupby(['Rep', 'Product'])[['Price']].min()
checando_preco_max = df.groupby(['Rep', 'Product'])[['Price']].max()

print((menor_preco_rep_prod['Price'] == checando_preco_min['Price']).all())
print((maior_preco_rep_prod['Price'] == checando_preco_max['Price']).all())

print()
print('----- Operação 8 - Menor preço de produto -----')
menor_preco_prod = df.groupby(['Product'])[['Price']].min()
print('\nMenor preço por produto\n')
print(menor_preco_prod)

print()
print('----- Operação 8.b - Contagem, Soma, Media, Maior, Menor preço por produto -----')
agregacaoProduto = df.groupby(['Product']).agg({'Price': ['count', 'sum', 'mean', 'min', 'max']})
print('\nValores em relação ao produtos - utilizando as funções principais\n')
print(agregacaoProduto)

print()
print('----- Operação 9 - Menor valor/preço de produto vendido por representante -----')
# aqui, buscamos o produto "mais barato/com menor valor" que um representante negociou
operacao_9 = df[df['Price'] == df['Price'].min()][['Product', 'Rep', 'Price']]

# agora, vamos fazer uso do groupby() para totalizar
df.groupby(['Rep'])[['Quantity']].sum()
print('\nProduto com o menor preço/valor vendido por representante')
print(operacao_9)

print()
print('----- Operação 9.b - Menor valor/preço de produto vendido por representante - com todos os representantes -----')
operacao_9b = df.groupby('Rep')['Price'].idxmin()
resultado = df.loc[operacao_9b]

print('\nProduto com o menor valor/preço vendio por um representante - com todos os representantes')
print(resultado[['Rep', 'Product', 'Price']])

'''
operacao_9b = df.groupby('Rep')['Price'].idxmin(): esta operação seleciona o produtos com o valor "mais baixo/barato" que foram negociados pro todos os representantes; para que pudessemos trazer este subconjunto foi necessario fazer uso da função idxmin(): é uma função que, ao ser executada, retorna o indice (linhas do df) de menor 'Price' de tro de cada agrupamento/representante e produto
'''

print()
print('----- Operação 10 - Agrupamento com uma função lambda -----')
# calcular o intervalor interquartil (IQR) dos preços por produto
operacao_10 = df.groupby('Product')['Price'].apply(lambda x: x.quantile(0.75) - x.quantile(0.25))

print('Intervalo interquartil (IQR) dos preços - por produto:')
print(operacao_10)
'''
    IQR: é o contexto lógico que mede a dispersão dos dados, ou seja, o quanto os preços variam entre os valores intermediarios (1º  e o 3º quartis)

    .apply(lambda x:
     
    x.quantile(0.75): o 3º quartil Q#, ou seja, o valor abaixo do qual estão 75% dos preços
        
    x.quantile(0.25)): o 1º quartil Q1, ou seja, o valor abaixo do qual estão 25% dos preços 

    Então, a diferença entre Q3 e Q1 é o IQR
'''

print('----- Operação 11 - Uso do pivot_table -----')
tabela_dinamica = pd.pivot_table(df, index=['Rep'], values=['Price'], columns=['Product'], aggfunc = [np.min], fill_value = 0)

print('\nTabela dinamica com o menor preço por representante e produto\n')
print(tabela_dinamica)

print()
print('----- Operação 12 - Função custom com pivot_table -----')

def func_intervalo(x):
    return x.max() - x.min()

# fazer uso do pivot_table
operacao_12 = pd.pivot_table(df, index=['Manager', 'Rep'], values=['Price'], aggfunc = func_intervalo)

print('\nPrivot table com "faixa de preços" min() e max()')
print(operacao_12)

print()
print('----- Operação 13 - Criar uma nova - "populada" com o resultado de uma operação -----')

df['Total_Sales'] = df['Quantity'] * df['Price']
print('\nDataframe com a coluna Total_Sales adicionada')
print(df.head(5))

# continuando - pivot_table com o total de vendas por representante e produto
table_total_vendas  =pd.pivot_table(
    df, 
    index=['Rep'],
    values=['Total_Sales'],
    columns=['Product'],
    aggfunc = np.sum,
    fill_value = 0
)

print('\nTabela dinamica com TOTAL DE DE VENDAS por representante e produto')
print(table_total_vendas)
