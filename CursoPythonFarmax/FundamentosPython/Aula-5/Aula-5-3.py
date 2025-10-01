
# passo 1 - definição de classe
class Veiculo:
    marca = ''
    modelo = ''
    ano = 0

    # passo 2 - definição do método construtor da classe, com parametros
    def __init__(self, marca: str, modelo: str, ano: int):

        # passo 3: acessar as propriedades da classe e inicializa-las
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # passo 4: definição de um método/função para cumprir a seguinte tarefa: descrever o carro
    def descricao(self) -> str:
        return f'{self.marca} {self.modelo} ({self.ano})'

    # passo 5: definição de um novo método para executar a seguinte tarefa: verificar se o veiculo pode ser considerado antigo
    def eh_antigo(self) -> bool:
        return self.ano < 2000


# passo 6: gerando os objetos
vel1 = Veiculo('Toyota', 'Corolla', 2025)
vel2 = Veiculo('Chevrolet', 'Opala', 1975)

# passo 7: fazer uso do Objeto
print(vel1.descricao())
print(vel1.eh_antigo())

print(vel2.descricao())
print(vel2.eh_antigo())
