
# 1º passo: criar a classe
class Pizza:

    # 2º passo: encapsular os atributos
    @property
    def sabor(self):
        return self.__sabor

    @sabor.setter
    def sabor(self, p_sabor: str):
        if len(p_sabor) == 0:
            raise ValueError('O sabor foi inserido de forma incorreta!')
        self.__sabor = p_sabor

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, p_tamanho: str):
        if len(p_tamanho) == 0:
            raise ValueError('O tamanho foi inserido de forma incorreta!')
        self.__tamanho = p_tamanho

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, p_preco: float):
        if p_preco <= 0:
            raise ValueError('O valor foi inserido de forma incorreta!')
        self.__preco = p_preco

    # 3 passo: construir o construtor
    def __init__(self, tamanho: str, sabor: str, preco: float):
        self.__tamanho = tamanho
        self.__sabor = sabor
        self.__preco = preco

    # 4º passo: definir o metodo para exibir os valores das propriedades/atributos
    def exibicao(self):
        return f'{self.tamanho} - {self.sabor} | R$: {self.preco}'


pedido1 = Pizza('Grande', 'Portuguesa', 59.99)
print(pedido1.exibicao())
