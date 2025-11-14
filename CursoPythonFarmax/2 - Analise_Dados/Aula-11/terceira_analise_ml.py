'''
PREMISSA: detectar padrão, tendencia e possibilidade de predição/previsão de eventos
para este proposito vamos analisar um dataset composto com dados a respeito de candidatos a financiamento imobiliario e dados a respeito, tambem, de perfis de imoveis a serem financiados
'''
# 0. importar todos os recursos necessarios para as operações
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# importar os recursos de metricas estatisticas da lib scipy - biblioteca cientifica do python que contem ferramentas estatisticas avançadas, por exemplo: distribuição de probabilidade, teste estatistico, entre outros
from scipy import stats

# importar os recursos do scikit-learn
# estes recursos auxiliarão na divisão de dados em conjunto de treino e de teste para o modelo ML (Machine Learning)
from sklearn.model_selection import train_test_split, cross_val_score

# regressão logistica: modelo "mais simples" e extremamente util para classificação binaria de dados; usando este recurso, podemos classificar dados em, por exemplo, duas categorias distintas
from sklearn.linear_model import LogisticRegression

# recurso que auxilia na "padronização" dos dados: significa que -> podemos transformar os valores para a média 0(zero) e o desvio padrão 1. Essa transformação ajuda os modelos ML que podem ser sensiveis (sofrer influencia) a partir de escala de conjunto como, por exemplo, SVM, KNN ou regeressão logistica
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import classification_report, confusion_matrix
'''
    este dois recursos atuam com elementos aplicados a avaliação dos modelos ML
    classification_report: retorna algumas métricas relacionadas aos modelos, por exemplo: precisão, f1-score, entre outros

    confusion_matrix: mostraa os errros e acertos - do modelo - a partir de suas classes - usan o formato de matriz; o que são classes do modelo? R.: colunas de dados
'''

# 1.  CARREGAMENTO DOS DADOS E PREPARAÇÃO
# definir uma variavel para receber como valor o arquivo .csv
# usando a função read_csv() da biblioteca Pandas para carregar os dados do arquivo e gerar um dataframe: estrutura de linhas e colunas - semalhante a uma planilha de dados
df = pd.read_csv('Arquivo-Treino.csv')

# exibir o df
print(df)

# criar uma "fatia" dos dados do df para obter a mediana desta "fatia"
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())

# agora, vamos criar uma nova "fatia" que seja referente ao historico de credito de candidatos a emprestimo
df['Credit_History'] = df['Credit_History'].fillna(1.0)

# fazer uso da função dropna(): função que remove linhas d evalores ausentes do df
# lista de colunas que devem ser verificadas para os valroes ausentes - caso eles existam; inplace=True -> este é o recurso que aplica a alteração diretamente no df
df.dropna(subset=['Loan_Status', 'ApplicantIncome', 'Education'], inplace=True)

# aqui, estamos associando os valores Y e N da coluna Loan_Status para true ou false - se tem historico ou não de credito
# df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

# exibição dos valores
print()
print('\n---- Primeiras linhas ----\n')
print(df.head(5))
print('-------------------------------------------')
print()

print('\n---- Resumo estatistico - describe() ----\n')
print(df.describe())
print('-------------------------------------------')
print()

print('\n---- Coluna Loan_Status ----\n')
print(df['Loan_Status'])
print('-------------------------------------------')
print()

print('\n---- Contagem de valores da coluna Loan_Status ----\n')
print(df['Loan_Status'].value_counts())
print('-------------------------------------------')
print()

print('\n---- Soma de valores nulos/ausentes do df ----\n')
print(df.isnull().sum())
print('-------------------------------------------')
print()

# fazer um contagem da quantidade de propriedades por segmento
print(df['Property_Area'].value_counts())

# 2. ANALISE ESTATISTICA "AVANÇADA" (SCIPY) - VAMOS TENTAR ENCONTRAR PADRÕES E TENDENCIA - CASO EXISTAM: A PARTIR DO DATASET

# teste de normalidade  - de shapiro - para a coluna ApplicantIncome (coluna de renda do solicitante do emprestimo): é o teste que verifica se os dados seguem uma "distribuição normal(gaussiana)": é uma distribuição de probabilidade de uso comum em dados reais. ESTAMOS TENTANDO, COM O USO DO MÉTODO SHAPIRO, VERIFICAR SE TODOS OS VALORES DA COLUNA DOS SOLICITANTES AO EMPRESTIMO ESTA DENTRO DA MEDIA OBSERVADA - OBTIDA A PARTIR DA COLUNA DE RENDA
shapiro_stat, shapiro_p = stats.shapiro(df['ApplicantIncome'])

# exibir a normalidade
print(f'\nShapiro-Wilk (normalidade de renda): p = {shapiro_p: .4f}')
# shapiro_p: valor_p(p_value): o valor mais importante para a analise que estamos fazendo: porque é o valor usado para, então, decidir se os dados são normais ou não

''' 
 shapiro_stat: valor estatistico do teste -> esta variavel é um nuemro calculado para medir quão proximo os dados estão de uma distribuição normal
 quanto mais proximo de 1, mais normal é a distribuição
 quanto mais distante de 1, menos normal
'''
# condicional para que seja possivel fazer as observações e analise da distribuição de renda

if shapiro_p < 0.05:  # a expressão do if representa 5% de probabilidade maxima de occorer algum erro na analise
    print('-> A renda ***NÃO SEGUE DISTRIBUIÇÃO NORMAL')

else:
    print('-> A renda SEGUE DISTRIBUIÇÃO NORMAL')

# observar a renda de forma visual: hist(bins=...) desenha o grafico o histograma; plt.show() mostar o grafico -> este histograma nos jauda a observar a distribuição de renda; por exemplo: mostra se os dados estão dispersos, se ha valores muito altos/baixos (outliers)
print(df['ApplicantIncome'].hist(bins=400))
plt.show()

# observar a distribuição de renda via boxplot
print(df.boxplot(column='ApplicantIncome'))
plt.show()

# fazer uma comparação de renda entre graduados e não graduados "olhando" para o nivel educacional dos aplicantes
print(df.boxplot(column='ApplicantIncome', by='Education'))
plt.show()

# histograma e boxplot para o motante de emprestimo solicitado
print(df['LoanAmount'].hist(bins=100))
plt.show()

print(df.boxplot(column='LoanAmount'))
plt.show()

# observar a coluna de historico de credito
obs_1 = df['Credit_History'].value_counts()

obs_2 = df.pivot_table(values='Loan_Status', index=['Credit_History'],
                       aggfunc=lambda x: x.map({'Y': 1, 'N': 0}).mean())
print()
print('Table de frenquencia por historico de crédito')
print(obs_1)

print('\nProbabilidade de obtenção de emprestimo considerando o historico de credito')
print(obs_2)

# observar via grafico
fig = plt.figure(figsize=(10, 6))
# significa: 1 linha, 2 colunas, 1º grafico de grade/grid
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Historico de Credito')
ax1.set_ylabel('Contagem de candidadtos')
ax1.set_title('Candidatos/Aplicants por historico de credito')
obs_1.plot(kind='bar', ax=ax1)

ax2 = fig.add_subplot(122)
ax2.set_xlabel('Historico de credito')
ax2.set_ylabel('Probabilidade de obter emprestimo')
ax2.set_title('Probabilidade de obter emprestimo pelo historico de credito')
obs_2.plot(kind='bar', ax=ax2)
plt.show()

# observar a relação entre historico de credito e status de emprestimo
obs_3 = pd.crosstab(df['Credit_History'], df['Loan_Status'])

# observar a relação entre historico de credito e genero
obs_4 = pd.crosstab(df['Credit_History'], df['Gender'])

# criar a figura para os dois graficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# plotar o 1º grafico
obs_3.plot(kind='bar', stacked=True, ax=ax1, color=['red', 'blue'])
ax1.set_title('Relação hist. credito x status emprestimo ')
ax1.set_xlabel('Historico de credito')
ax1.set_ylabel('Quantidade')
ax1.legend(title='Loan_Status')

# plotar o 2º grafico
obs_4.plot(kind='bar', stacked=True, ax=ax2, color=['red', 'blue'])
ax2.set_title('Relação hist. credito x genero')
ax2.set_xlabel('Historico de credito')
ax2.set_ylabel('Quantidade')
# aqui, exibimos o valores referentes ao genero manifestado na coluna Gender
ax2.legend(title='Gender')

# exibir o grafico
plt.tight_layout()
plt.show()


# calcular o coeficiente da relação
corr = df['ApplicantIncome'].corr(df['LoanAmount'])
print(f'Correlação: {corr: .2f}')
# medir e observar a correlação entre o candidados ao emprestimo e suas rendas com o montante de emprestimo solicitado
plt.figure(figsize=(10, 6))
plt.scatter(df['ApplicantIncome'], df['LoanAmount'])
plt.title('Correlação: renda do candidato x montante solicitado')
plt.xlabel('Renda')
plt.ylabel('Valor do emrpestimo')
plt.tight_layout()
plt.show()
