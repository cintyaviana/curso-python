
from veiculo_motorizado import VeiculoMotorizado


class VeiculoAbastecimento(VeiculoMotorizado):
    def __init__(self, placa: str, modelo: str, capacidade_tanque: int, tipo_combustivel: str, litros_abastecidos: int):
        super().__init__(placa, modelo, capacidade_tanque)
        self.__tipo_combustivel = tipo_combustivel
        self.__litros_abastecidos = litros_abastecidos
