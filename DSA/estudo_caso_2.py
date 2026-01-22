# ==========================================================================================================================================
# 1.0 IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================================================================================================


# Instala o pacote watermark
# pip install -q -U watermark

"""
-q (quiet) > faz a instalação de forma silenciosa.
-U (up date)> atualiza caso o pacote estiver instalado.
watermark > cria uma marca d'agua com as versões dos demais pacotes.
"""

# Importação da biblioteca para manipulação de dados em tabelas
from matplotlib.ticker import FuncFormatter
import pandas as pd

# Importação da biblioteca NumPy para operações matemáticas e arrays
import numpy as np

# Importação da biblioteca Matplotlib para geração de gráficos mais simples
import matplotlib.pyplot as plt

# Importação da biblioteca Seaborn para visualização estatística de dados mais customizados
import seaborn as sns

# Importação da biblioteca random para geração de números aleatórios
import random

# Importação das classes datetime e timedelta para manipulação de datas e intervalos de tempo
from datetime import datetime, timedelta

from watermark import watermark

# Informa as versões das bibliotecas importadas.
print(watermark(iversions=True, globals_=globals()))

# Para instalar uma versão específica de um pacote, podemos fazer assim (por exemplo):
# pip install -q pandas==2.3.1

# ==========================================================================================================================================
# 1.0 CRIAÇÃO DO DF COM DADOS ALEATÓRIOS
# ==========================================================================================================================================

# Definição da função para gerar dados fictícios de vendas


def gerar_dados_vendas(num_registros=600):
    """
    Gera um DataFrame do Pandas com dados de vendas fictícios.
    """

    # Mensagem inicial indicando a quantidade de registros a serem gerados
    print(f"\nIniciando a geração de {num_registros} registros de vendas...")

    # Dicionário com produtos, suas categorias e preços
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

    # Cria uma lista apenas com os nomes dos produtos
    lista_produtos = list(produtos.keys())

    # Dicionário com cidades e seus respectivos estados
    cidades_estados = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }

    # Cria uma lista apenas com os nomes das cidades
    lista_cidades = list(cidades_estados.keys())

    # Lista que armazenará os registros de vendas
    dados_vendas = []

    # Define a data inicial dos pedidos
    data_inicial = datetime(2026, 1, 1)

    """ datetime > cria um objeto de data e hora específico = 2026-01-01 00:00:00 """

    # Loop para gerar os registros de vendas
    for i in range(num_registros):
        """ range = faixa """

        # Seleciona aleatoriamente um produto
        produto_nome = random.choice(lista_produtos)

        """ random.choice > escolha, vai escolher a cada loop, um item de produto da lista."""

        # Seleciona aleatoriamente uma cidade
        cidade = random.choice(lista_cidades)

        """ random.choice > escolha, vai escolher a cada loop, uma cidade da lista."""

        # Gera uma quantidade de produtos vendida entre 1 e 7
        quantidade = np.random.randint(1, 8)

        """ np.random.randint > é da biblioteca do numpy, e vai escolher um número aleatório (randint) """

        # Calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + \
            timedelta(days=int(i/5), hours=random.randint(0, 23))

        """ O timedelta é a ferramenta para manipular durações de tempo. Ele permite que você some dias, horas ou minutos a uma data comum.

        timedelta(days=int(i/5) > acrescenta dias (int(i/5) a data inicial). Quando soma dias a uma data, ele gerencia automaticamente a transição de dias para meses e de meses para anos, respeitando inclusive se o mês tem 28, 30 ou 31 dias.

        hours=random.randint(0, 23) > Cada pedido, além do dia calculado, ganhará uma hora aleatória do dia. Isso evita que todos os seus pedidos apareçam como se tivessem sido feitos exatamente à meia-noite. """

        # Se o produto for Mouse ou Teclado, aplica desconto aleatório de até 10%
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * \
                np.random.uniform(0.9, 1.0)
            """ np.random.uniform(0.9, 1.0) > É da bibioteca numpy. Escolhe um número ao acaso entre 0.9 e 1.0. Diferente de um dado (que só dá números inteiros), o uniform pode retornar qualquer valor quebrado, como 0.9234. Isso significa que todos os números dentro desse intervalo têm a mesma chance de serem escolhidos. Não há preferência por números mais próximos de 0.9 ou de 1.0."""
        else:
            preco_unitario = produtos[produto_nome]['preco']

        # Adiciona um registro de venda à lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            # função para arredondar números decimais para o número inteiro mais próximo ou para uma quantidade específica de casas decimais.
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })

    # Mensagem final indicando que a geração terminou
    print("Geração de dados concluída.\n")

    # Retorna os dados no formato de DataFrame
    return pd.DataFrame(dados_vendas)


# ----------------------------------------------------------------------
# Ponto de Entrada
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # ----------------------------------------------------------------------
    # Gerar, Carregar e Explorar os Dados
    # ----------------------------------------------------------------------

    # Chama a função que você criou e guarda o DataFrame na variável 'df'
    df_vendas = gerar_dados_vendas(1000)

    """
    # Salva o arquivo. O index=False evita que o Pandas crie uma coluna extra de números.
    df_vendas.to_csv('vendas_estudo_caso.csv', index=False,
              sep=';', encoding='utf-8-sig')

    # Salva como arquivo de planilha do Excel
    df_vendas.to_excel('vendas_estudo_caso.xlsx',
                index=False, sheet_name='Vendas_2026')
    """

    # Tipo do df
    print(f"Tipo do df: {type(df_vendas)}")

    # Shape
    print(f"\nShape do df: {df_vendas.shape}")

    # Exibe as 5 primeiras linhas do DataFrame se não for passdo outro argumento
    print(f"\nPrimeiras 10 linhas do df:{df_vendas.head(10)}")

    # Exibe as 5 últimas linhas do DataFrame
    print(f"\nÚltima 10 linhas do df: {df_vendas.tail()}")

    # Exibe informações gerais sobre o DataFrame (tipos de dados, valores não nulos)
    print(f"\nInformações gerais do df: {df_vendas.info()}")

    # Resumo estatístico
    print(f"\nResumo estatístico do fd: {df_vendas.describe()}")

    # Tipos de dados
    print(f"\nTipo de dados do df: {df_vendas.dtypes}")

    # ----------------------------------------------------------------------
    # Limpeza, Pré-Processamento e Engenharia de Atributos
    # ----------------------------------------------------------------------

    # Se a coluna 'Data_Pedido' não estiver como tipo datetime, precisamos fazer a conversão explícita
    # A coluna pode ser usada para análise temporal
    df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

    # Engenharia de atributos
    # Criando a coluna 'Faturamento' (preço x quantidade)
    df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * \
        df_vendas['Quantidade']

    # Engenharia de atributos
    # Usando uma função lambda para criar uma coluna de status de entrega
    df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(
        lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal')

    # Exibe informações gerais sobre o DataFrame (tipos de dados, valores não nulos)
    df_vendas.info()

    # Exibe as 5 primeiras linhas novamente para ver as novas colunas
    df_vendas.head()
    # ----------------------------------------------------------------------
    # Análise 1 - Top 10 Produtos Mais Vendidos
    # ----------------------------------------------------------------------

    #  Quais os top 10 produtos mais vendidos?
    # Agrupa por nome do produto, soma a quantidade e ordena para encontrar os mais vendidos
    top_10_produtos = df_vendas.groupby(
        'Nome_Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)

    print(top_10_produtos)

    # Define um estilo para os gráficos
    sns.set_style("whitegrid")

    # Cria a figura e os eixos
    plt.figure(figsize=(12, 7))

    # Cria o gráfico de barras horizontais
    top_10_produtos.sort_values(ascending=True).plot(
        kind='barh', color='skyblue')

    # Adiciona títulos e labels
    plt.title('Top 10 Produtos Mais Vendidos', fontsize=16)
    plt.xlabel('Quantidade Vendida', fontsize=12)
    plt.ylabel('Produto', fontsize=12)

    # Exibe o gráfico
    plt.tight_layout()
    plt.show()

    # ----------------------------------------------------------------------
    # 7. Análise 2 - Faturamento Mensal
    # ----------------------------------------------------------------------

    # Qual foi o faturamento mensal?

df_vendas.head()

# Cria uma coluna 'Mes' para facilitar o agrupamento mensal
df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')

df_vendas.head()

# Agrupa por mês e soma o faturamento
faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()

# Converte o índice para string para facilitar a plotagem no gráfico
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')

# Formata para duas casas decimais
faturamento_mensal.map('R$ {:,.2f}'.format)

# Cria uma nova figura com tamanho de 12 por 6 polegadas
plt.figure(figsize=(12, 6))

# Plota os dados de faturamento mensal em formato de linha
faturamento_mensal.plot(kind='line', marker='o', linestyle='-', color='green')

# Define o título do gráfico com fonte de tamanho 16
plt.title('Evolução do Faturamento Mensal', fontsize=16)

# Define o rótulo do eixo X
plt.xlabel('Mês', fontsize=12)

# Define o rótulo do eixo Y
plt.ylabel('Faturamento (R$)', fontsize=12)

# Rotaciona os valores do eixo X em 45 graus para melhor visualização
plt.xticks(rotation=45)

# Adiciona uma grade com estilo tracejado e linhas finas
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Ajusta automaticamente os elementos para evitar sobreposição
plt.tight_layout()

# Exibe o gráfico
plt.show()

# 8. Análise 3 - Vendas Por Estado

# Qual o total de vendas por estado?

# Agrupa por estado e soma o faturamento
vendas_estado = df_vendas.groupby(
    'Estado')['Faturamento'].sum().sort_values(ascending=False)

# Formata para duas casas decimais
vendas_estado.map('R$ {:,.2f}'.format)

# Cria uma nova figura com tamanho de 12 por 7 polegadas
plt.figure(figsize=(12, 7))

# Plota os dados de faturamento por estado em formato de gráfico de barras
# Usando a paleta de cores "rocket" do Seaborn
vendas_estado.plot(kind='bar', color=sns.color_palette("husl", 7))

# Define o título do gráfico com fonte de tamanho 16
plt.title('Faturamento Por Estado', fontsize=16)

# Define o rótulo do eixo X
plt.xlabel('Estado', fontsize=12)

# Define o rótulo do eixo Y
plt.ylabel('Faturamento (R$)', fontsize=12)

# Mantém os rótulos do eixo X na horizontal (sem rotação)
plt.xticks(rotation=0)

# Ajusta automaticamente os elementos do gráfico para evitar sobreposição
plt.tight_layout()

# Exibe o gráfico
plt.show()

# 9. Análise 4 - Faturamento Por Categoria

# Qual o faturamento total por categoria?

# Agrupa por categoria, soma o faturamento e formata como moeda para melhor leitura
faturamento_categoria = df_vendas.groupby(
    'Categoria')['Faturamento'].sum().sort_values(ascending=False)

# O .map('{:,.2f}'.format) é opcional, mas deixa a visualização do número mais clara
faturamento_categoria.map('R$ {:,.2f}'.format)

# Importa a função FuncFormatter para formatar os eixos

# Ordena os dados para o gráfico ficar mais fácil de ler
faturamento_ordenado = faturamento_categoria.sort_values(ascending=False)

# Cria a Figura e os Eixos (ax) com plt.subplots()
# Isso nos dá mais controle sobre os elementos do gráfico.
fig, ax = plt.subplots(figsize=(12, 7))

# Cria uma função para formatar os números
# Esta função recebe um valor 'y' e o transforma em uma string no formato 'R$ XX K'


def formatador_milhares(y, pos):
    """Formata o valor em milhares (K) com o cifrão R$."""
    return f'R$ {y/1000:,.0f}K'


# Cria o objeto formatador
formatter = FuncFormatter(formatador_milhares)

# Aplica o formatador ao eixo Y (ax.yaxis)
ax.yaxis.set_major_formatter(formatter)

# Plota os dados usando o objeto 'ax'
faturamento_ordenado.plot(kind='bar', ax=ax, color=sns.color_palette(
    "viridis", len(faturamento_ordenado)))

# Adiciona títulos e labels usando 'ax.set_...'
ax.set_title('Faturamento Por Categoria', fontsize=16)
ax.set_xlabel('Categoria', fontsize=12)
ax.set_ylabel('Faturamento', fontsize=12)

# Ajusta a rotação dos rótulos do eixo X
plt.xticks(rotation=45, ha='right')

# Garante que tudo fique bem ajustado na imagem final
plt.tight_layout()

# Exibe o gráfico
plt.show()

"""
## 10. Conclusão e Entrega do Resultado

Existem várias formas de entregar um projeto de análise de dados e a escolha depende do público, do contexto e dos objetivos. Três formas bastante utilizadas são:

**10.1. Relatório técnico ou executivo (PDF, DOCX, etc.)**

Essa forma é clássica e muito útil quando o público precisa de um documento formal para consulta. O relatório pode conter descrição da metodologia, exploração dos dados, gráficos, tabelas e conclusões. É comum separar a linguagem: uma versão mais técnica (com código, estatísticas detalhadas e testes) e outra mais executiva (com foco em insights, recomendações e storytelling de dados).

**10.2. Dashboard interativo (Power BI, Tableau, Looker, Streamlit, Dash, etc.)**

Um dashboard permite que os usuários explorem os dados por conta própria, filtrando informações, ajustando períodos de tempo ou focando em variáveis específicas. Essa forma de entrega é muito valorizada em ambientes corporativos, pois facilita a tomada de decisão contínua e não exige conhecimentos técnicos avançados dos usuários finais.

**10.3. Apresentação (slides em PowerPoint, Google Slides, etc.)**

Ideal para reuniões de stakeholders, a entrega em formato de apresentação resume os principais pontos do projeto. Ela foca nas descobertas mais relevantes, nas implicações para o negócio e nas recomendações práticas, usando gráficos e visualizações impactantes. A ideia é contar a história dos dados de forma clara e direta, evitando sobrecarregar o público com detalhes técnicos.
"""
