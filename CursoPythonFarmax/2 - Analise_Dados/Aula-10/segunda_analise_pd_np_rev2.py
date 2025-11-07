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

print()
print('----- Operação 14 - observar a correlação entre algumas variaveis -----')
correlacao = df[['Price', 'Quantity', 'Total_Sales']].corr() # método que estabelece a correlação entre variaveis
print('Correlação entre Preço, Quantidade e Vendas totais')
print(correlacao)

print()

# graficos
print('================== GRÁFICOS ========================')
print()
import matplotlib.pyplot as plt
import seaborn as sns
print('------------ 1. total de vendas por representante ------')
print()
plt.figure(figsize=(10, 6))
df.groupby('Rep')['Quantity'].sum().plot(kind='bar', color='skyblue')
plt.title('total de vendas por representante')
plt.xlabel('Representante')
plt.ylabel('Qtde vendida')
plt.xticks(rotation=45) # metodo/função que "rotaciona" - em 45 graus - os elementos exibidos no grafico para que não fiquem sobrepostos 
plt.grid(axis='y') # método/função que adiciona uma "grade" horizontal - a partir o eixo y do grafico par a"facilitar" a leitura 
plt.tight_layout() # método/função que ajusta o layout do grafico para nada fique "cortado" de exibição
plt.show() # exibe o grafico


print()
print('------------ 2. vendas por produto ------')
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

print()
# nova operação, inserção de um elemento de data
print('----- operação 15 - observar colunas disponives e inserir uma nova -----------')
print()
print('Colunas disponiveis no df')
print(df.columns)
print()

# caso não exista uma coluna de, por exemplo: data, podemos adiciona-la
if 'Date' not in df.columns and 'Data' not in df.columns:
    # podemos criar uma nova
   # df['Date'] = pd.to_datetime('2024-01-01')
    df['Date'] = pd.date_range(start='2024-01-01', periods=len(df), freq='M')
    #print('\nAdicionando coluna Date com data fixa')
    print('\nColuna Date criada com novas datas, agora, distribuidas entre 2023/2025')

# "converter"  a coluna 'Date' para o formato adequado - datetime
df['Date'] = pd.to_datetime(df['Date'])
# agrupar as vendas por trimestre
vendas_por_timestre = df.resample('Q', on='Date')['Total_Sales'].sum()

# criar intervalo trimestral completo - a indicação é: '2023-01-01' a 2025
intervalo_trimestre = pd.date_range('2024-01-01', '2025-12-31', freq='Q')


# reindexar para incluir o intervalo trimestral ja criado, acima
vendas_por_timestre = vendas_por_timestre.reindex(intervalo_trimestre, fill_value=0)


print('\nTotal de vendas por trimestre(2024-2025)')
print(vendas_por_timestre)
'''
QE = Quarter End, ou seja, trimestres encerrando no final do quarter(1/4 de 12 == 3: trimestre)
'''
print(df)

print()
print('------------ 3. evolução trimestral de vendas ------')
print()
plt.figure(figsize=(10, 6))
vendas_por_timestre.plot(marker='o', linestyle='-', color='purple')
plt.title('Total de vendas por trimestre')
plt.xlabel('Timestre')
plt.ylabel('Total de vendas (R$)')
#plt.xticks(rotation=45) 
plt.grid(True) 
plt.tight_layout() 
plt.show() 

print()
print('------------ 4. Boxplot dos preços por produto ------')
print()
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Product', y='Price')
plt.title('Boxplot de preços por produto')
plt.xlabel('Produto')
plt.ylabel('Preço (R$)')
plt.xticks(rotation=45) 
#plt.grid(True) 
plt.tight_layout() 
plt.show() 


print()
print('------------ 5. Heatmap - auxiliam na observação da correlação ------')
print()
plt.figure(figsize=(10, 6))
sns.heatmap(df[['Price', 'Quantity', 'Total_Sales']].corr(), annot=True, cmap='Blues', fmt='.2f')
plt.title('Mapa de correlação entre Preço, quantidade e total de vendas')
#plt.xlabel('Produto')
#plt.ylabel('Preço (R$)')
#plt.xticks(rotation=45) 
#plt.grid(True) 
plt.tight_layout() 
plt.show() 

print('----- operação 16 - definição de uma classificação simples para as vendas -----------')
print()
print('função para classificar as vendas')
def classificar_vendas(preco):
    try:
        preco = float(preco)
    except (TypeError, ValueError):
        return 'Indefinido'
    
    # caso o contraro ocorra...
    if preco <= 0:
        return 'Indefinido'
    elif preco >= 60000:
        return 'Alto'
    elif preco >= 20000 and preco <= 50000:
        return 'Medio'
    else:
        return 'Baixo'

# fora da função
df['Classification_Sales'] = df['Price'].apply(classificar_vendas)
print('\nDataframe com coluna de Classificação de vendas')
print(df[['Price', 'Classification_Sales']].head(5))


print()
print('------------ 6. Classificação de vendas (Alto, médio, baixo) ------')
print()
# ajuste
sns.set_style('whitegrid')
sns.set_palette('pastel')

plt.figure(figsize=(10, 6))

ax = sns.countplot(
    data=df, 
    x='Classification_Sales', 
    order=['Baixo, Medio, Alto'])

plt.title('Classificação das vendas por faixa de preço')
plt.xlabel('Classificação')
plt.ylabel('Qtde de ocorrencias de vendas')
#plt.xticks(rotation=45) 
#plt.grid(True) 

# adição de valores acima da barra
for p in ax.patches:
    ax.annotate(
        f'{(int(p.get.height()))}',
        (p.get_x() + p.get_width()/2., p.get_height()),
        ha='center', va='bottom', fontsize=10
    )
plt.tight_layout() 
plt.show() 
