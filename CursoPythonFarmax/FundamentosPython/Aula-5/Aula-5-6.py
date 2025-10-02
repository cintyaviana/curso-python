
# Classe e Objetos

"""
    DEFINIÇÃO DE CLASSE: classe - de acordo com o paradigma(forma) de programação orientada a objetos "diz" que: classe é um elemento lógico descritivo - onde descrevemos tudo aquilo que, em algum momento, faremos uso para algum proposito

    DEFINIÇÃO DE OBJETO: objeto - de acordo com o paradigma(forma) de programação orientada a objetos diz que: objeto é derivado - a partir de uma classe - determinando que tudo aquilo que, nela, classe, está descrito, agora, pode ser usado para seus respectivos propositos
"""


class Automovel:  # aqui, temos a definição da classe - uso da palavra reservada class junto do nome dado a classe - Automovel

    # marca = '' # neste contexto, a variavel funciona e esta declarada de forma simples. ESTA DECLARAÇÃO, APESAR DE FUNCIONAR, PODE TRAZER VULNERABILIDADE PARA O PROGRAMA. TAMBÉM É CONSIDERADO, PARA O CONTEXTO DE CLASSES, UMA PRATICA DUVIDOSA - NÃO É BOM! POR ISSO, EVITAMOS, NESTE CONTEXTO, SEU USO.

    # --- DEFINIÇÃO DA PROPRIEDADE marca; ABAIXO, A "PROPRIEDADE" marca ESTA SENDO DEFINIDA COMO UM MÉTODO/FUNÇÃO; PORTANTO, precisamos "trasformar" este método/função numa propriedade.

    """ 
        Aqui, estamos fazendo o uso da estrutura de acesso get - que diz o seguinte: "vou acessar a propriedade- dentro do método e retornar este acesso para que ela receba algum valor.
    """
    @property  # este é um decorator/decorador ; este é o decorator que transforma o método marca() na propriedade/varaivel marca
    def marca(self) -> str:
        return self._marca

    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

        """toda e qualquer função declarada dentro de uma classe ganha uma nova
        nomenclatura, passa a ser chamada de: MÉTODO
        
        __init__(): MÉTODO/FUNÇÃO declarada como o CONSTRUTOR DA CLASSE; seu proposito é:
        quando precisarmos gerar, a partir desta classe, um objeto, é esta função/método
        que devemos chamar a sua execução para que o objeto, derivado desta classe, passe
        a existir

        self: palavra reservada/comando que determina o "contexto de uso" de um elemento lógico que está sendo usado dentro de um método mas não faz parte dele

        marca, modelo, ano: são parâmetros do método/função

        self.marca = marca: 
            self.marca -> esta é uma variavel DE CLASSE que foi declarada dentro da função/método; 
            marca -> este é o parametro do método/função construtor da classe.
        
        Quando o método/função construtor for chamado a sua execução, este parametro DEVE receber algum ARGUMENTO/VALOR; este valor recebido será atribuido a variavel de mesmo nome! 
        
        O mesmo de nome da variavel e do parametro do método/função é definido de forma proposital - para que não ocorra equívoco no momento da atribuição de valores entre variaveis e parametros

        """
