
from veiculo import Veiculo


class VeiculoMotorizado(Veiculo):
    def __init__(self, placa: str, modelo: str, capacidade_tanque: int):
        super().__init__(placa, modelo)
        self.__capacidade_tanque = capacidade_tanque

    def exibicao(self) -> str:
        return super().exibicao() + f' | Tanque {self.__capacidade_tanque} litros'


v1 = VeiculoMotorizado('KMN 6D39', 'Chevrolet Onix Plus', 44)

# exibir estes valores
print(v1.exibicao())
