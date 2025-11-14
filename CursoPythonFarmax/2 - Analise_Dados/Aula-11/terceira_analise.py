
"""
PREMISSA: detectar padrão, tendencia e possibilidade de predição/previsão de eventos
para este proposito vamos analisar um dataset composto com dados a respeito de candidatos
a financiamento imobiliario e dados a respeito, tambem, de perfis de imoveis a serem
financiados
"""

#######################################################################
# PASSO 0 - importar todos os recusros necessários para as operações
#######################################################################

from sklearn.neural_network import MLPClassifier
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# importar os recursos de metricas estatisticas da lib scipy - biblioteca cientifica do python que contem ferramentas estatísticas avançadas, por exemplo: distribuição de probabilidade, teste estatítico, entre outros.
from scipy import stats

# importar os recursos do scikit-learn
# estes recursos auxiliarão na divisão de dados em conjunto de treino e de teste para o modelo ML (Machine Learning)
from sklearn.model_selection import train_test_split, cross_val_score

# regressão logistica: modelo "mais simples" e extremamente util para classificação binaria de dados; usando este recurso, podemos classificar dados em, por exemplo, duas categorias distintas
from sklearn.linear_model import LogisticRegression

# recurso que auxilia na "padronização" dos dados: significa que -> podemos transformar os valores para a média 0(zero) e o desvio padrão 1. Essa transformação ajuda os modelos ML que podem ser sensiveis (sofrer influencia) a partir de escala de conjunto como, por exemplo, SVM, KNN ou regeressão logistica
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import classification_report, confusion_matrix

# auxilia na verificação do nivel de precisão do modelo - indice de acerto
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier


'''
este dois recursos atuam com elementos aplicados a avaliação dos modelos ML classification_report: retorna algumas métricas relacionadas aos modelos, por exemplo: precisão, f1-score, entre outros

confusion_matrix: mostraa os errros e acertos - do modelo - a partir de suas classes - usan o formato de matriz; o que são classes do modelo? R.: colunas de dados
'''
#######################################################################
# PASSO 1: CARREGAMENTO DOS DADOS E PREPARAÇÃO
#######################################################################

# Retorna o caminho de onde estão os arquivos do projeto
dataPath = Path(__file__).resolve().parent

# Carregar os dados - para este propósito vamos definir uma variavel para receber como valor o arquivo de dados
df = pd.read_csv(dataPath / 'Arquivo-Treino.csv')

# Exibir o df
print('\n---- Exibição do df ----\n')
print(df)
print('-'*100 + "\n")

# criar uma "fatia" dos dados do df para obter a mediana desta "fatia"
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
"""
O método fillna() é usado para preencher valores nulos/ausentes em um DataFrame ou Series do Pandas.

No Pandas, os valores ausentes são representados por NaN (Not a Number).

A principal tarefa do fillna() é substituir todos os NaN de uma coluna (ou de todo o DataFrame) por um valor que você especificar, que nesse caso foi a mediana: fillna(df['LoanAmount'].median())
"""

# Agora, vamos criar uma nova "fatia" que seja referente ao historico de credito de candidatos a emprestimo
# Nesse contexto o 1.0 seria um bom pagador (positivo) e 0.0 um mal pagador (negativo)
df['Credit_History'] = df['Credit_History'].fillna(1.0)

# fazer uso da função dropna():remove os registros de dados vazios do df
df.dropna(subset=['Loan_Status', 'ApplicantIncome',
          'Education'], inplace=True)

"""
# subset=['LoanStatus', 'ApplicationIncome', 'Education']: lista de colunas que devem ser verificadas quanto aos valores ausêntes caso eles existam.

inplace=True -> este é o recurso que aplica a alteração diretamente no df
"""

# preparando os dados com formato numéricos para ser analizado: aqui, estamos associando os valores Y e N da coluna loan_Status para true ou false - se tem historico ou não de credito
# df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

"""
O map() aplica uma correspondência (um mapeamento) a cada elemento de uma coluna (df['Loan_Status']), substituindo o valor original pelo valor correspondente que você fornece.

No seu caso, a correspondência é feita através de um dicionário Python ({'Y': 1, 'N': 0}).
"""

# exibição dos valores

print('\n---- Primeiras linhas ----\n')
print(df.head(5))
print('-'*100 + "\n")

print('\n---- Resumo estatistico - describe() ----\n')
print(df.describe())
print('-'*100 + "\n")

print('\n---- Coluna Loan_Status ----\n')
print(df['Loan_Status'])
print('-'*100 + "\n")

print('\n---- Contagem de valores da coluna Loan_Status ----\n')
print(df['Loan_Status'].value_counts())
print('-'*100 + "\n")

print('\n---- Soma de valores nulos/ausentes do df ----\n')
print(df.isnull().sum())
print('-'*100 + "\n")

# fazer um contagem da quantidade de propriedades por segmento
print(df['Property_Area'].value_counts())
print('-'*100 + "\n")

#################################################################################################################################
# PASSO 2: NALISE ESTATISTICA "AVANÇADA" (SCIPY) - VAMOS TENTAR ENCONTRAR PADRÕES E TENDENCIA - CASO EXISTAM: A PARTIR DO DATASET
#################################################################################################################################

# teste de normalidade - de shapiro - para a coluna ApplicantIncome (coluna de renda do solicitante do emprestimo): é o teste que verifica se os dados seguem uma "distribuição normal (gaussiana)": é uma distribuição de probabilidade de uso comum em dados reais.

# ESTAMOS TENTANDO, COM O USO DO MÉTIDO SHAPIRO, VERIFICAR SE TODOS OS VALORES DA COLUNA DOS COLICITANTES AO EMPRESTIMO ESTÁ DENTRO DA MÉDIA OBSERVADA - OBTIDA A PARTIR DA COLUNA DE RENDA.

shapiro_stat, shapiro_p = stats.shapiro(df['ApplicantIncome'])

"""
O objetivo deste comando é determinar se a distribuição da coluna 'ApplicantIncome' (Renda do Solicitante) segue uma distribuição normal (curva em forma de sino).

------------------------------------------------------------------------------------------------------------------------------------------------
Componente	            Função	                        Explicação:
------------------------------------------------------------------------------------------------------------------------------------------------
stats.shapiro()	        Função principal.	            É a função do módulo stats da biblioteca SciPy que executa o Teste de Shapiro-Wilk.

df['ApplicantIncome']	Argumento de entrada.	        É a coluna do seu DataFrame (df) cujos dados serão testados para verificar a normalidade.

shapiro_stat	        Primeira variável de retorno.	É a Estatística do Teste de Shapiro-Wilk. Este valor é o quão perto a amostra se                                                      se aproxima de uma distribuição normal.

shapiro_p	            Segunda variável de retorno.	É o Valor-P (p-value). Este é o resultado mais importante para a sua análise.
------------------------------------------------------------------------------------------------------------------------------------------------

O Valor-P é usado para decidir se você rejeita ou não a hipótese de que os dados são normalmente distribuídos:

------------------------------------------------------------------------------------------------------------------------------------------------
Regra de Ouro (Geralmente alpha = 0.05):
------------------------------------------------------------------------------------------------------------------------------------------------
Se p > 0.05: Você não rejeita a hipótese nula. A distribuição é considerada Normal.

Se p menor/igual 0.05: Você rejeita a hipótese nula. A distribuição não é considerada Normal.

Se o seu shapiro_p for muito baixo (por exemplo, 0.0001), indica que a coluna de renda tem uma distribuição muito diferente da normal, o que pode influenciar modelos como a Regressão Logística.
------------------------------------------------------------------------------------------------------------------------------------------------
"""

"""


# Exibir a normalidade
print(f'\nShapiro-Wilk (normalidade de renda): p = {shapiro_p:.4f}')
print('-'*100 + "\n")
"""
# Shapiro_p: valor_p(p_value): o valor mais importante para a analise que estamos fazendo: porque é o valor usado para, então, decidir se os dados são normais ou não.

# Shapiro_stat: valor estatistico do teste -> esta variavel é um nuemro calculado para medir quão proximo os dados estão de uma distribuição normal quanto mais proximo de 1, mais normal é a distribuição quanto mais distante de 1, menos normal
"""
if shapiro_p < 0.05:  # a expressão do if representa 5% de probabilidade maxima de occorrer
    # algum erro na analise
    print('-> A renda NÃO SEGUE DISTRIBUIÇÃO NORMAL')

else:
    print('-> A renda SEGUE DISTRIBUIÇÃO NORMAL')

# observar a renda de forma visual: # observar a renda de forma visual: hist(bins=...) desenha o grafico o histograma; plt. show() mostrar o grafico -> este histograma nos jauda a observar a distribuição de renda; por exemplo: mostra se os dados estão dispersos, se ha valores muito altos/baixos (outliers)

print(df['ApplicantIncome'].hist(bins=200))
plt.show()
print('-'*100 + "\n")

# observar a distribuição de renda via boxplot
print(df.boxplot(column='ApplicantIncome'))
plt.show()
print('-'*100 + "\n")

# fazer uma comparação de renda entre graduados e não graduados "olhando" para o nível
# educacional dos aplicantes
print(df.boxplot(column='ApplicantIncome', by='Education'))
plt.show()
print('-'*100 + "\n")

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




"""


"""

# MODELAGEM ML

para qualquer dataset que está em análise é importante que seja observado 4 pontos fundamentais:
1 - observação da normalidade
2 - distribuição
3 - correlação
4 - graficos
"""

# ----------------------------------------------------------------------------------------------------------------------

# MODELAGEM ML (Machine Learning)

"""
Modelagem - Nível 1: a partir do momento que nós, analista, observamos - a partir do dataset - padrão e tendencia, nosso modelo ML também precisa detectar os mesmos. Se o modelo for capaz de detectar, é provavel que conseguiremos implementa-lo para fazer previsões. A 1º previsão será implementado a partir da coluna Lon_Status(Y/N)

    Características:
    Melhor modelo: Regressão Logística
    Tipo de classificação: binária
    Justificativa da escolha: a premissa é estabelecer a previsão de aprovação de
    empréstimos. Portanto, a regressão Logística é rápida, simples e facilmente
    "interpretável".
    O modelo ML vai aprender a partir de relações entre as variaveis, tais como: renda,
    historico de credito, tipo de imovel e prever se o emprestimo será aprovado ou não

"""

# convertendo Loan_Status par ao contexto numerico necessario
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

# selecionar as vars numéricas necessarias

df_ml = df[['ApplicantIncome', 'CoapplicantIncome',
            # lista de dados que será analizado
            'LoanAmount', 'Credit_History', 'Loan_Status']].copy()

# vamos "limpar" os dados atribuidos a var df_ml
df_ml = df_ml.dropna()

# agora, vamos crias duas vars; a 1º receberá como valor o 'Loan_Status' no eixo da coluna - axis = 1
# a 2º receberá como valor a 1º
# não queremos o nome da coluna mas somente os dados numericos que, a ela, pertencem
X = df_ml.drop('Loan_Status', axis=1)
Y = df_ml['Loan_Status']

# neste passo, dividir os dados em blocos de treino do modelo e teste deste modelo treinado
X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.25,
                                                    random_state=42)

"""
Aqui está a transcrição do texto na imagem:

X: dados de entrada do modelo (features)
y: rotulagem(classe/variavel/coluna que queremos prever )
test_size=0.25: aqui, estamos separando 25% dos dados para teste e 75% - os dados restantes - para o treino do modelo random_state: aqui, garantimos que a divisão sempre será igual, ou seja, teremos a possibilidade de reproduzir o treino e o teste sempre que for necessario.

X_train e y_train: vars usadas para treinar o modelo
X_test e y_test: vars usadas para avaliar o modelo ML(o modleo nunca ve os dados de teste antes do treino)

"""
# criar a padronização necessaria para os valores que o modelo vai usar para treino e test (normalização)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
# fit -> calcula a media dos dados aplicado, á ele, como argumento; tambem observa o desvio padrão - caso exista
# transform -> usa os valores resultantes do calculo do fit e aplica este resultado aos dados transformando-os no conjunto ideal para ser testado, posteriorment
# aqui, o metodo transform tem o mesmo proposito da aplicação acima, somente aplicando a transformação nos dados de teste
X_test_scaled = scaler.transform(X_test)

"""
StandardScaler(): # recurso que auxilia na "padronização" dos dados: significa que -> podemos transformar os valores para a média 0(zero) e o desvio padrão 1. Modelos baseados em Regressão Logística trabalham muito melhor com dados padronizados

fit_transform(): é usado somente no treino transform(): é usado somente no teste; usando os mesmos parametros do treino - porque, dessa forma, mantemos a consistencia dos dados usados para o modelo prever aquilo que queremos;

"""

# criação do modelo ML
# estabelecemos a instancia/criação do modelo ML de regeressão logistica
model_lr = LogisticRegression()
# fazendo do uso do método fit() para treinar o modelo
model_lr.fit(X_train_scaled, y_train)

# as instruções acima estabelecem o "aprendizado" da relação entre as variaveis X_train_scaled e as classes atribuidas como valor a variavel y_train

# implementar a previsão/predição que modelo pode fazer a partir dos dados dos quais ele - modelo ML - se "alimentou"

# aqui, o modelo faz as previsões a partir dos dados de teste que ele NUNCA viu antes; porque a var pred_lr vai conter as classes previstas para cada linha do valor dado à var X_test_scaled
pred_lr = model_lr.predict(X_test_scaled)

# exibir o resultado
print('\nModelo Nivel 1 - Regeressão Logística')
print()
print('------------------ Matriz de confusão ------------------')
print(confusion_matrix(y_test, pred_lr))
print()
print('------------------ relatorio de classificação do modelo ------------------')
print(classification_report(y_test, pred_lr))
print()
print('------------------ Precisão do Modelo ------------------')
print(accuracy_score(y_test, pred_lr))
print()
print('------------------ Coeficiente da vars/colunas aplicadas pelo RL ------------------')
print(model_lr.coef_)
print(X.columns)
print()

"""
Modelagem - Nível 2: a partir do momento que nós, analista, observamos - a partir do dataset - padrão e tendencia, nosso modelo ML também precisa detectar os mesmos. Se o modelo for capaz de detectar, é provavel que conseguiremos implementa-lo para fazer previsões. A 2º previsão será implementado a partir da coluna Lon_Status(Y/N)

    Características:
    Melhor modelo: Random Forest
    Tipo de classificação: variada

    Justificativa da escolha: o modelo consegue capturar relações não-lineares; oferece boa resistência a outliers (dados fora do padrão); geralmente, lidam melhor do que modelos baseados em regressão linear.

    O modelo ML vai aprender a partir de relações entre as variaveis, tais como: renda, historico de credito, tipo de imovel e prever se o emprestimo será aprovado ou não

"""

# definição do modelo RandomForest
model_rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=8,
    random_state=42
)

# definição do modelo RandomForest
model_rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=8,
    random_state=42
)

# implementar o treino do modelo
model_rf.fit(X_train, y_train)
# implementar a predição/previsão
pred_rf = model_rf.predict(X_test)

# definição do modelo RandomForest
model_rf = RandomForestClassifier(
    # este é o numero de estimadores da floresta. Quando mais estimadores, maior é a estabilidade (menos variância) do modelo; porem é provável que quanto maior o numero de arvore, maior é o consumo de memoria
    n_estimators=300,
    # este numero é relacionado a profundidade maxima de cada estimadores.
    max_depth=8,
    random_state=42
)

# implementar o treino do modelo
model_rf.fit(X_train, y_train)

# implementar a predição/previsão
pred_rf = model_rf.predict(X_test)

# exibir os resultados
print('\nModelo Nivel 2 - Random Forest')
print()
print('------------------ Matriz de confusão ------------------')
print(confusion_matrix(y_test, pred_rf))
print()
print('------------------ Relatorio de classificação ------------------')
print(classification_report(y_test, pred_rf))
print()
print('------------------ Relevancia/Importancia das variaveis ------------------')
importancias = pd.Series(model_rf.feature_importances_, index=X.columns)
print(importancias.sort_values(ascending=False))


"""
Modelagem - Nível 3: a partir do momento que nós, analista, observamos - a partir do dataset - padrão e tendencia, nosso modelo ML também precisa detectar os mesmos. Se o modelo for capaz de detectar, é provavel que conseguiremos implementa-lo para fazer previsões. A 3º previsão será implementado a partir da coluna Lon_Status(Y/N)

    Características:
    Melhor modelo: rede neural MLPClassifier

    Tipo de classificação: variada

    Justificativa da escolha: o modelo consegue capturar relações não-lineares; oferece boa resistência a outliers (dados fora do padrão); geralmente, lidam melhor do que modelos baseados em regressão linear e baseados em random forest - porque consegue observar e aprender maiores relações e compexidades entre as variaveis/classes.

    O modelo ML vai aprender a partir de relações entre as variaveis, tais como: renda, historico de credito, tipo de imovel e prever se o emprestimo será aprovado ou não e ainda, fazer uma recomendação de credito para um novo usuário.

"""


# implementando o modelo
model_mlp = MLPClassifier(
    hidden_layer_sizes=(50, 25),
    activation='relu',
    solver='adam',
    max_iter=800,
    random_state=42
)

# implementar o treino do modelo
model_mlp.fit(X_train, y_train)
# implementar a predição/previsão
pred_mlp = model_mlp.predict(X_test_scaled)

# função de recomendação de emprestimo para um novo usuario


def recomendar_credito(modelo, dados_candidato):
    """
    o parametro dados_candidato é um lista com valores referentes a:
    [ApplicantIncome, CoapplicantIncome, LoanAmount, Credit_History]
    """

    # definir uma var para receber como valor o lista com os dados do novo usuario
    dados_candidato = np.array([dados_candidato])
    dados_scaled = scaler.transform(dados_candidato)

    # definir uma nova var que vai receber como valor a predição do emprestimo
    pred = modelo.predict(dados_scaled)[0]

    # uma nova var para "calculamos" a probabilidade do aplicante reeber o emprestimo
    prob = modelo.predict_proba(dados_scaled)[0][1]

    # agora, vamos criar um dicionario com o status do emprestimo para o candidato e a
    # probabilidade dele conseguir o emprestimo
    resultado = {
        "status": "APROVADO" if pred == 1 else "NEGADO",
        "probabilidade": round(prob * 100, 2)
    }

    return resultado


# inserir um novo candidato
novo_candidato = [5000, 0, 120, 1]

"""
ApplicantIncome: 5000
CoapplicantIncome: 0
LoanAmount: 120
Credit_History: 1
"""

resposta = recomendar_credito(model_mlp, novo_candidato)
print()

# exibir os resultados
print('\nModelo Nivel 3 - Saídas')
print()
print('================== SISTEMA DE RECOMENDAÇÃO DE CREDITO ==================')
print(f'Status: {resposta["status"]}')
print(f'Probabilidade de aprovação: {resposta["probabilidade"]}%')
