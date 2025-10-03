
from veiculo import Veiculo


class VeiculoMotorizado(Veiculo):
    def __init__(self, placa: str, modelo: str, capacidade_tanque: int):
        super().__init__(placa, modelo)
        self.__capacidade_tanque = capacidade_tanque

    def exibicao(self) -> str:
        return super().exibicao() + f' | Tanque: {self.__capacidade_tanque} L'


v1 = VeiculoMotorizado('Chevrolet Onix Plus', 'KMN 6D39', 44)

# exibir estes valores
print(v1.exibicao())
