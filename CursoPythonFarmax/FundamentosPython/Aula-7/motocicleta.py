

# ===================== POLIMOSFISMO ===========================

"""
Polimorfismo: significa "muitas formas"
Em POO, polimorfismo nada mais é do que: a capacidade de um mesmo método ter comportamentos diferentes - dependendo da classe que o implementa.
Polimorfismo só pode existir se ocorrer o mecanismo de herança
"""

# Definir a classe Motocicleta - praticando o mecanismo de herança com a classe Automovel
# Será necessário estabelecer a "relação" entre as classes Automovel() e Motocicleta
from automovel import Automovel


class Motocicleta(Automovel):  # mecanismo de herança definido entre as classes
    # definir o método construtor da classe Motocicleta
    # aqui, o método construtor da classe Motocicleta recebe os mesmos parametros indicados no construtor da classe Automovel e, além disso, descrevemos um novo parametro que pertence somente a classe Motocicleta - cilindrada
    def __init__(self, marca: str, modelo: str, ano: int, cilindrada: int):

        # aqui, estamos chamando o construtor da classe-pai - Automovel
        super().__init__(marca, modelo, ano)

        """
        essa chamada se dá seguindo estes passos:
        a) o comando super() é usado para chamar o construtor da classe pai.
        b) ewssa chamada garante que os atrbutos - privados - da classe Automovel (encapsulados)sejam, devidamente, configurados - de forma correta - com todas as validações/caracteristica definidas na classe-pai
        c) sem esta referencia, provavelmente, a classe Motocicleta - e seus atributos - não receberiam, adequadamente, seus respectivos valores
        """
        self.cilindrada = cilindrada  # este atributo é exclusivo da classe Motocicleta(); dessa forma, a classe Motocicleta pode usar tudo aquilo que esta na classe Automovel e, também, fazer uso de seu atributo especifico - cilindrada.

        """
        fazer uso do método exibicao() - neste ponto, estamos criando, para esta classe um método chamada exibicao() - mas, aqui, vale indicar que: estamos praticando o POLIMORFISMO; Porque estamos fazer uso de um método que existe na classe - exibicao - mas, aqui, nesta classe, ele vai exibir um outro comportamento - além daquele que ja conhecemos.
        """

    def exibicao(self) -> str:
        return super().exibicao() + f' | Cilindrada: {self.cilindrada}'

    """
    acima, o polimorfismo foi aplicado a partir da sobrescrita do método exibicao (); significa que: acessamos o metodos da classe-pai e "escrevemos" a paritr dele-uma nova tarefa para ser executada
    """


# ========= TESTANDO O POLIMORFISMO ============
moto = Motocicleta('Honda', 'CG 125', 1982, 125)
print(moto.exibicao())
