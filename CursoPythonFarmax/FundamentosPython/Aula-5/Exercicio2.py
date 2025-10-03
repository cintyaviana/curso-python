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
emprestar() -> marca o livro como emprestado (disponível = False). Se já estiver emprestado, exiba mensagem adequada.
devolver() -> marca o livro como disponível (disponível = True). Se já estiver disponível, exiba mensagem adequada.
status() -> retorna "Disponível" ou "Emprestado".


"""


class Livro:
    titulo = ''
    autor = ''
    ano = 0
    disponivel = True  # livro começa disponivel

    # Método construtor
    def __init__(self, titulo: str, autor: str, ano: int):
        # Acessar os atributos da classe e oferecer para eles, como valor os parâmetros do método construtor.
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descricao(self) -> str:
        return f'{self.titulo} - Autor: {self.autor} Ano de lançamento: ({self.ano})'

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
        else:
            print('Livros ja emprestado')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
        else:
            print('Livro ja esta na biblioteca')

    def status(self) -> str:
        return 'Disponivel' if self.disponivel else 'Emprestado'


print('=================BIBLIOTECA==========================')
livro1 = Livro('Grande Sert~~ao: Veredas', 'Joao Guimaraes Rosa', 1956)
print(livro1.descricao())
print(livro1.status())

# Se o livro estiver com status = disponivel, vamos pedir ese livro emprestado
livro1.emprestar()
print(livro1.status())

# Se quiser empresar o livro, da bibliote, um livro que j´´a foi emprestado?
livro1.devolver()
print(livro1.sta())

# Se tentar devolver um livro ja devolvido
livro1.devolver()
