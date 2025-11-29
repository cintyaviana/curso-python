
# =======================================================
# ROBÔ AUTOMAÇÃO ATENDIMENTO - BASEADO EM IA BASED RULES (IA COM BASE DE CONHECIMENTO PREVIO)
# =======================================================

# fazendo as importações necessárias
from flask_cors import CORS
from flask import Flask, request, jsonify
import numpy as np
import unidecode

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ===========================================================
# FUNÇÕES UTILITÁRIAS - SÃO AS FUNÇÕES QUE ESTABELECEM O MODELO ML
# ===========================================================


# aqui, estamos definindo a função que recebe o parametro 'texto'; a anotação de tipo é opcional
def normalizar(texto: str) -> str:
    return unidecode.unidecode(texto.lower().strip())
# unicode.unicode(): remove acentos e quaisquer outras "particularidades" das palavras que o usuário informar (ex: 'ação' -> 'acao')
# .lower(): converte todos os caracteres para minúsculos
# .strip(): remove espaços em branco no início e no fim de uma string


# função que recebe o arquivo de base de conhecimento
def carregar_perguntas(arquivo: str):
    # atribuição múltipla de variáveis onde cada uma recebe um lista vazia
    perguntas, respostas = [], []

    # esta função - nativa do python - "abre" o arquivo de dados no mod leitura ("r") e considerado todos os caracteres especiais - UTF-8
    with open(arquivo, "r", encoding="utf-8") as f:
        # para ler o arquivo e seu conteúdo precisamos iterar sobre cada linha que ele contém
        for linha in f:
            if ";" in linha:  # somente linhas com este caractere - ; - serão lidas
                # acima, o loop lê todas as linhas e observa se as linhas contem o caracter ; ---- essa abordagem já consegue evitar, por exemplo, erros potenciais caso existam linhas em branco ou mal formatadas

                pergunta, resposta = linha.strip().split(";", 1)

                """Z
                    .split(";", 1): divide a string no primeiro ";" encontrado - este comportamento é determinado pelo valor 1 -> este é o valor maximo de numero de divisões maxsplit=1

                    fazendo a divisão será atribuido, à lista 'perguntas' todos os valores da base de conhecimento e a mesma acontecerá com a lista resposta
                """
                perguntas.append(normalizar(
                    pergunta))  # aqui, "populamos" a lista  'perguntas' com cada pergunta lida na base de conhecimento
                # aqui, "populamos" a lista 'respostas' com cada resposta lida na base de conhecimento
                respostas.append(resposta)

            return perguntas, respostas  # aqui, retornamos as duas listas criadas


"""
======================================================
CARREGAMENTO DA BASE DE CONHECIMENTO
======================================================
"""

# fazer o carregamento das perguntas e respostas definido no arquivo externo para este proposito vamos definir a chamada da função carregar_perguntas

# aqui, atribuímos as duas listas criadas na função - para cada uma das vars aqui, estabelecidas
pf_perguntas, pf_respostas = carregar_perguntas("base_conhecimento.txt")

# definir a vetorização dos textos da base de conhecimento: vetorização é o processo de "transformar" os textos em vetores/conjuntos numericos. Cada palavra se trasnforma num número; é dessa forma que se cria a possibilidade de observar a similaridade

# ao instanciar a classe TfidfTransformer temos o objeto que pode transformar nossos textos em numeros
vetorizador = TfidfTransformer()

# agora, vamos definir o modelo ML para usar o vetorizar e aprender com os dados
# aqui, estamos fazendo duas coisas: 1º o modelo esta aprendendo o "vocabulario" das perguntas e convertendo cada pergunta num vetor TF-IDF (em numero); 2º o resultado - pf_vetorizacao - é uma matriz matematica "esparsa" contendo 1 linha por pergunta
pf_vetorizacao = vetorizador.fit_transform(pf_perguntas)

# neste passo, vamos definir o limite/indice minio para considerar a pergunta do usuario "parecida" com alguma pergunta na base de conhecimento do modelo ML

# ======================================================
# acima temo o ml e abaixo o uso do ml
# ================================================================
INDICE_SIMILARIDADE = 0.3


# definindo a função que recebe uma pergunta do usuario; o parametro pergunta_usuario -> texto digitado pelo usuario
def responder_perguntas(pergunta_usuario: str, top_n=3):
    # top_n=3 -> quantidade de respostas mais parecidas com aquilo que o usuario espera receber como resposta - definimos um parametro para uma especie de "ranking"
    # aqui, o parametro recebe ele mesmo como valor só que "normalizado" com o uso da função normalizar
    pergunta_usuario = normalizar(pergunta_usuario)

    # agora, vamos vetorizar a pergunta do usuario - converte em numeros
    usuario_vetorizacao = vetorizador.transform([pergunta_usuario])

    # precisamos, neste passo, calcular a similaridade para dar ao usuario a resposta mais adequada - de acordo com sua pergunta
    # estamos calculando o quanto a pergunta do usuario se parece com a pergunta que temos na base de conhecimento do modelo ML
    similaridades = cosine_similarity(usuario_vetorizacao, pf_vetorizacao)[0]

    # precisamos ordenar as resposta da mais relevante para a menos relevante - considerando o top_n=3
    indices = np.argsort(similaridades)[:: -1][:top_n]

    """
    acima, estamos ordenando pelas mais parecidas
    np.argsort(similaridades)[: : -1][:top_n]: aqui, é a ordenação dos indices das
    similaridades de menor para maior

    [: : -1]: aaqui, temos a inversão da ordem -> do menor para o maior
    [:top_n]: selecione apenas os N melhores -> N = 3
        
    """

    # vamos verificar as mais parecidas
    # SE ESTA VERIFICAÇÃO FOR AVALIDA COMO TRUE....
    if similaridades[indices[0]] < INDICE_SIMILARIDADE:
        return "😔 Desculpe, não encontrei uma resposta adequada!"

    # caso o contrario ocorra....
    """
    Montagem da resposta final: para este proposito, vamos criar uma lista de respostas;
    cada resposta, teoricamente, terá este formato:

    indice de similarida    resposta em texto
    (0.67)                 Sua fatura vence no dia 14
    (0.56)                 Você pode consultar o saldo no app
    (0.31)                 Ligue para o setor de finanças
    """

    respostas = []
    for i in indices:
        respostas.append(f'({similaridades[i]:.2f}) {pf_respostas}')

    # na expressão de retorno da função precisamos "juntar" todos os valores encontrados num unico texto final! separado, se necessario, por quebra de linhas
    return "\n".join(respostas)

# ================================================================
# API WEB - FLASK
# =================================================================


# transformando o bot IA numa api web
app = Flask(__name__)  # aqui, estamos criando a "api" flask

CORS(app)  # agora, estamos dizendo que é permitido esta aplicação se integrar e compartilhar com conteudo com uma outra aplicação qualquer

# precisamos criar um "endereço/rota" para que esta aplicação seja acessada por outra


@app.route("/perguntar", methods=["POST"])
# FUNÇÃO que será executada quando o endereço(endpoint), acima, for acessado
def perguntar():
    # vamos obter a pergunta que o usuario enviou
    dado = request.get_json()  # serializando os dados - trasnformando-os numa unica linha
    # aqui, estamos lendo a pergunta que o usuario enviou
    pergunta = dado.get("perguntar", "")
    # estamos chamando a função do nosso bot(composta pela vetorização e pelo indice de similaridade). Pedindo as 3 melhores respostas encontrados
    resposta = responder_perguntas(pergunta, top_n=3)
    return jsonify({"resposta": resposta})  # retornando a resposta serializada


@app.route("/")  # rota raiz
def home():
    return jsonify({"status": "API flask para a nossa IA - rodando lindamente"})
