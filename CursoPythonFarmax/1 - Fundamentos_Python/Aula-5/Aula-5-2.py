
# passo 1: definição da classe
class Veiculo:

    # 2 passo: declarar as propriedades da classe
    marca = ''
    modelo = ''
    ano = 0

# passo 3: defini o método-construtor da classe -> método é uma função; recebe este novo nome por ser declarada/descrita dentro de uma classe. O método construtor da classe é definido com o uso da expressão __init__()

# ainda, dentro da definição do método/função construtor da classe, vamos descrever 3 parametros para ele - junto do comando, palavra reservada self

    def __init__(self, marca: str, modelo: str, ano: int):
        # as declarações marca, modelo, ano PERTECEM AO MÉTODO/FUNÇÃO CONSTRUTOR DA CLASSE - MESMO TENDO A NOMENCLATURA IDENTICA AS PROPRIEDADES DA CLASSE.

        # passo 4: acessar as propriedades pertencentes a classe e, aqui, dentro do método/função construtor da classe, inicializa-las com os valores dos parametros

        # aqui, abaixo, a variavel/... marca PERTENCE a classe; esta propriedade esta sendo acessando dentro do metodo construtor, por isso é necessario fazer uso do comando self - ajuda a "contextualziar" o uso de uma propriedade - descrita fora do método - dentro dele, método

        # neste passo, atribuimos como valor para a propriedade marca qualquer valor/argumento que for dado ao parametro marca - que pertence ao método
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


# passo 5: gerando o objeto -para este proposito, vamos criar uma variavel para receber como valor a instancia da classe Veiculo
# aqui, estamos praticando a instancia da classe Veiculo; esta instancia é criada a partir da "chamada" do método-contrutor da classe; portanto, quando escrevemos : "Veiculo()", na verdade, estamos chamando o método construtor à sua execução
vel1 = Veiculo('VW', 'Gol', 1992)
vel2 = Veiculo('Fiat', '147', 1978)
vel3 = Veiculo('Chevrolet', 'Opala', 1975)
vel4 = Veiculo('Toyota', 'Corolla', 2025)

# passo 6: exibir os carros
print('===== CARROS DA GARAGEM DO LUIS =====')
print('Veiculo 1:', vel1.marca, vel1.modelo, vel1.ano)
print('Veiculo 2:', vel2.marca, vel2.modelo, vel2.ano)
print('Veiculo 3:', vel3.marca, vel3.modelo, vel3.ano)
print('Veiculo 4:', vel4.marca, vel4.modelo, vel4.ano)
