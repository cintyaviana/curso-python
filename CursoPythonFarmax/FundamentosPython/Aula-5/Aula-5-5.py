
# definição da classe
class Aluno:
    nome = ''
    notas = []

    # definição do construtor
    def __init__(self, nome: str, notas: list):
        self.nome = nome
        self.notas = notas

    # definição de metodos/funções

    def media(self) -> float:
        if len(self.notas) == 0:
            return 0.0
        else:
            return sum(self.notas)/len(self.notas)

    def aprovado(self) -> bool:
        return self.media() >= 7

    def adicionar_nota(self, nota: float):
        self.notas.append(nota)


aluno1 = Aluno('Gabriel', [8.5, 9.9, 10.0])
print(aluno1.nome, aluno1.notas)
print('Media: ', aluno1.media())
print('Aprovado: ', aluno1.aprovado())
