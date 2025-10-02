
"""
Exercício 2 - Classe Livro
Crie uma classe chamada Livro que represente um livro em uma biblioteca.

A classe deve conter:

Atributos:
título (string): título do livro.
autor (string): nome do autor.
ano (int): ano de publicação.
disponível (boolean): indica se o livro está disponível (inicia como True).

Construtor: que receba título, autor e ano.

Métodos:

descricao() -> retorna uma string no formato: "Título - Autor (Ano)".
emprestar() -> marca o livro como emprestado (disponível = False). Se já estiver
emprestado, exiba mensagem adequada.

devolver() -> marca o livro como disponível (disponível = True). Se já estiver disponível,
exiba mensagem adequada.

status() -> retorna "Disponível" ou "Emprestado".


"""


class Livro:
    titulo = ''
    autor = ''
    ano = 0
    disponivel = True

    # Método construtor
    def __init__(self, titulo: str, autor: str, ano: int):
        # Acessar os atributos da classe e oferecer para eles, como valor os parâmetros do método construtor.
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def
