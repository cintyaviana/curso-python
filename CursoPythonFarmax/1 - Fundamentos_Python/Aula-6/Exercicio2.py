
"""
   titulo = ''
    autor = ''
    ano = 0
    disponivel = True  # livro começa disponivel

"""


class Livro:
    # Método construtor
    def __init__(self, titulo: str, autor: str, ano: int):
        # Acessar os atributos da classe e oferecer para eles, como valor os parâmetros do método construtor.
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__disponivel = True

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, p_titulo: str):
        if len(p_titulo.strip()) == 0:
            raise ValueError('O título não pode ser vazio')
        self.__titulo = p_titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, p_autor: str):
        # strip é um método nativo python, que, uma vez aplicado, remove espaço em branco - de uma string
        if len(p_autor.strip()) == 0:
            raise ValueError('O autor não pode ser vazio')
        self.__autor = p_autor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, p_ano: int):
        if p_ano < 1450:
            raise ValueError('Ono inadequado para um livro')
        self.__ano = p_ano
    # ------ Disponível - está propriedade ja possui um valor padrão, True, portanto será uma propriedade somente de leitura.

    @property
    def disponivel(self):
        return self.__disponivel

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def adisponivel(self, p_disponivel: str):
        self.__disponivel = p_disponivel

    def descricao(self) -> str:
        return f'{self.titulo} - Autor: {self.autor} Ano de lançamento: ({self.ano})'

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
        else:
            print('Livros ja emprestado')

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
        else:
            print('Livro ja esta na biblioteca')

    def status(self) -> str:
        return 'Disponivel' if self.__disponivel else 'Emprestado'


print('=================BIBLIOTECA==========================')
livro1 = Livro('Grande Sertão: Veredas', 'Joao Guimaraes Rosa', 1956)
print(livro1.descricao())
print(livro1.status())

# Se o livro estiver com status = disponivel, vamos pedir ese livro emprestado
livro1.emprestar()
print(livro1.status())

# Se quiser empresar o livro, da bibliote, um livro que j´´a foi emprestado?
livro1.devolver()
print(livro1.status())

# Se tentar devolver um livro ja devolvido
livro1.devolver()
