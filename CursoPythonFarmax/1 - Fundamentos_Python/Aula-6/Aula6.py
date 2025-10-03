

# 1º passo: definir a classe
class Automovel:
    """
    nesta nova classe queremos "proteger" nossas propriedades/atributos... o que isso significa? 

    R.: Isso significa que: as propriedades/atributos que vamos definir podem ser operadas/manipuladas somente por esta classe. 

    Portanto, o acesso a estas propriedades/atributos - teoricamente - só podem ser feitas, aqui, dentro desta classe. 

    Os demais "pedaços" do projeto, poderão acessar somente o "resultado" das operações/manipulações feitas com estas propriedades/ atributos.

    Essa nova modalidade é possível porque, para as propriedades/atributos que, aqui, serão criados, vamos definir uma "cápsula" protetora para envolve-las.

    Essa abordagem é importante porque:
        1 - mantemos a integridade das propriedades
        2 - teremos uma estrutura de classe mais robusta - considerando as boas práticas de programação
        3 - nosso código passa a ser compreendido como um aplicação profissional.
        4 - vamos expor, somente, o resultado das operações realizadas com a propriedades/atributos

        Nas linguagens de programação que trabalham com a programação orientada a objetos, essa técnica é conhecida com : ENCAPSULAMENTO.

        Aqui está a transcrição do terceiro texto:

        objetos, essa técnica é conhecida com : ENCAPSULAMENTO; o encapsulamento se dá a partir do uso de uma propriedade/atributo/método definido como private(privado); na sequência, é implementada - para este elemento private(privado) - uma "cápsula" que, necessariamente, é pública - pois é ela, "cápsula/camada de proteção" que deve ficar "exposta" para todos os outros "pedaços" do projeto! Então, para o funcionamento desta "proteção" as linguagens orientadas a objeto fazem uso do - chamados - métodos acessores: getters e setters

        Os métodos acessores se comportam da seguinte forma: os getters retornam o acesso aos elementos private(privados); dessa forma, os setters podem manipular os elementos private(privados) da forma que for necessária.
    """

    # marca = '' aqui, a propriedade/atributo é publico
    # modelo = '' aqui, a propriedade/atributo é publico
    # ano = 0 aqui, a propriedade/atributo é publico

    # agora, queremos definir nossas propriedades/atributos e protegê-los; para este propósito, vamos defini-los como elementos privados
    # Este ´´e o decorator python que transforma um metodo num atributo de leitura.
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
        """
        usamos a formatação %
        %20s -> string largura mínima de 20, alinhada a direita
        %5d -> um valor inteiro com largura mínima de 5
        """


# ============= gerar o objeto e exibir os valores
auto = Automovel('Chevrolet', 'Opala', 1975)
print(auto.exibicao())
