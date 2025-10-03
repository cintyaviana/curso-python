
class Automovel:

    @property
    def marca(self):  # esta instrução, neste momento, é um método! mas, aqui, não podemos tratar esta instrução como método, deve ser tratado como o método acessor get que retorna a propriedade private que é acessada - dessa forma, temos o uso do conceito do método acessor get. Para este propósito, temos de usar o elemento lógico decorator @property - acima da declaração do método.
        return self.__marca  # aqui, é a propriedade private __marca

    @marca.setter  # declaração do setter da propriedade __marca; quando gerarmos o objeto desta classe poderemos oferecer a propriedade/atributo privado um valor: auto.marca = 'Fiat'
    def marca(self, p_marca: str):  # p_marca: é o parametro da "cápsula" - recebe o valor atribuido - a partir do uso do objeto gerado da classe
        if len(p_marca) == 0:  # aqui, temos uma validação - se o valor oferecido para o parametro não esta vazio (p_marca == 0) temos o lançamento da exceção
            # esta é a exceção lançada caso o parametro esteja vazio; para lançar esta exceção usamos o comando raise
            raise ValueError('A marca foi inserida de forma incorreta!')
        # atribui/armazena o valor do parametro p_marca (que foi validado) para a propriedade private (privada) __marca
        self.__marca = p_marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, p_modelo: str):
        if len(p_modelo) == 0:
            raise ValueError('O modelo foi inserido de forma incorreta!')
        self.__modelo = p_modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, p_ano: int):
        if p_ano < 1970:
            raise ValueError('Este automovel e vintage')
        self.__ano = p_ano

    # 2 passo: construir o construtor
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # 3º passo: definir o metodo para exibir os valores das propriedades/atributos

    def exibicao(self):
        texto = '%20s %20s %5d' % (self.marca, self.modelo, self.ano)
        return texto


# ============= gerar o objeto e exibir os valores
auto = Automovel('Chevrolet', 'Opala', 1975)
print(auto.exibicao())
