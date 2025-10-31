
# IMPORTAR AS BIBLIOTECAS NECESSÁRIAS
import seaborn as sns
import matplotlib.pyplot as plt
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

print()
print('----- Operação 12 - Função custom com pivot_table -----')


def func_intervalo(x):
    return x.max() - x.min()


# fazer uso do pivot_table
operacao_12 = pd.pivot_table(df, index=['Manager', 'Rep'], values=[
                             'Price'], aggfunc=func_intervalo)

print('\nPrivot table com "faixa de preços" min() e max()')
print(operacao_12)

print()
print('----- Operação 13 - Criar uma nova - "populada" com o resultado de uma operação -----')

df['Total_Sales'] = df['Quantity'] * df['Price']
print('\nDataframe com a coluna Total_Sales adicionada')
print(df.head(5))

# continuando - pivot_table com o total de vendas por representante e produto
table_total_vendas = pd.pivot_table(
    df,
    index=['Rep'],
    values=['Total_Sales'],
    columns=['Product'],
    aggfunc=np.sum,
    fill_value=0
)

print('\nTabela dinamica com TOTAL DE DE VENDAS por representante e produto')
print(table_total_vendas)

print()
print('----- Operação 14 - observar a correlação entre algumas variaveis -----')
# método que estabelece a correlação entre variaveis
correlacao = df[['Price', 'Quantity', 'Total_Sales']].corr()
print('Correlação entre Preço, Qunaitdade e Vendas totais')
print(correlacao)
print()

# graficos
print('========================= GRÁFICOS =========================')
print()


print('------------- 1. total de vendas por representante -------------')
print()

plt.figure(figsize=(10, 6))
df.groupby('Rep')['Quantity'].sum().plot(kind='bar', color='skyblue')
plt.title('total de vendas por representante')
plt.xlabel('Representante')
plt.ylabel('Qtde vendida')
# método/função que "rotaciona" - em 45 graus - os elementos exibidos no grafico para que não fiquem sobrepostos
plt.xticks(rotation=45)
# método/função que adiciona uma "grade" horizontal - a partir do eixo y do grafico para "facilitar" a leitura
plt.grid(axis='y')
# método/função que ajusta o layout do gráfico para que nada fique cortado na exibição
plt.tight_layout()
plt.show()  # exibir o gráfico


print()
print('------------- 2. vendas por produto -------------')
print()

plt.figure(figsize=(10, 6))
df.groupby('Product')['Quantity'].sum().plot(kind='bar', color='orange')
plt.title('Quantidade de vendas por produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# nova operação, inserção de um elemento de data
print('----- operação 15 - observar colunas disponiveis e inserir uma nova ---------')
print()
print('Colunas disponiveis no df')
print(df.columns)
print()
# caso não exista uma coluna de, por exemplo: data, podemos adiciona-la
if 'Date' not in df.columns and 'Data' not in df.columns:
    # podemos criar uma nova
    df['Date'] = pd.to_datetime('2024-01-01')
    print('\nAdicionando coluna Date com data fixa')

# "converter" a coluna 'Date' para o formato adequado - datetime
df['Date'] = pd.to_datetime(df['Date'])

# agrupar as vendas por trimestre
vendas_por_trimestre = df.resample('QE', on='Date')['Total_Sales'].sum()

# criar intervalo trimestral completo - a indicação é: '2023-01-01' a 2025
intervalo_trimestre = pd.date_range('2023-01-01', '2025-12-31', freq='Q')

# reindexar para incluir o intervalo trimestral ja criado, acima
vendas_por_trimestre = vendas_por_trimestre.reindex(
    intervalo_trimestre, fill_value=0)

print('\nTotal de vendas por trimestre')
print(vendas_por_trimestre)

# QE = Quarter End, ou seja, trimestres encerrando no final do quarter(1/4 de 12 == 3: trimestre)

print('\nTotal de vendas por trimestre (2024-2025)')
print(vendas_por_trimestre)

"""
QE = Quarter End, ou seja, trimestres encerrando no final do quarter (1/4 de 12 == 3: trimestre)
"""

print(df)

print()
print('------------- 3. evolução trimestral de vendas -------------')
print()

plt.figure(figsize=(10, 6))
vendas_por_trimestre.plot(marker='o', linestyle='-', color='purple')
plt.title('Total de vendas por trimestre')
plt.xlabel('Trimestre')
plt.ylabel('Total de vendas (R$)')
# plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

print()
print('------------- 4. Boxplot dos preços por produto -------------')
print()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Product', y='Price', palette='Set2')
plt.title('Boxplot de preços por produto')
plt.xlabel('Produto')
plt.ylabel('Preço (R$)')
plt.xticks(rotation=45)
# plt.grid(True)
plt.tight_layout()
plt.show()

print('----- operação 16 - definição de uma classificação simples para as vendas')
print()
print('função para classificar as vendas')


def classificar_vendas(preco):
    if preco > 500:
        return 'Alto'
    elif preco > 200:
        return 'Medio'
    else:
        return 'Baixo'


# fora da função
df['ClassifiClassification_Salescação_Vendas'] = df['Price'].apply(
    classificar_vendas)

print()
print('--- 5. Heatmap - auxiliam na observação da correlação ---')
print()
plt.figure(figsize=(10, 6))
sns.heatmap(df[['Price', 'Quantity', 'Total_Sales']].corr(), annot=True, cmap='Blues',
            fmt='.2f')
plt.title('Mapa de correlação entre Preço, quantidade e total de vendas')
# plt.xlabel('Produto')
# plt.ylabel('Preço (R$)')
# plt.xticks(rotation=45)
# plt.grid(True)
plt.tight_layout()
plt.show()


print('------------------ 6.Classificação de vendas (Alto, Médio e Baixo) -----------------')
print()
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Classification_Sales',
              order=['Baixo', 'Média', 'Alto'])
sns.color_palette('pastel')
plt.title('Classificação de vendas por faixa de preço')
plt.xlabel('Classificação')
plt.ylabel('Quantidade de ocorrencias de vendas')
# plt.xticks(rotation=45)
# plt.grid(True)
