
# 1º passo: criar a classe
class Veiculo:

    # 2º passo: encapsular os atributos
    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, p_placa: str):
        if len(p_placa) == 0:
            raise ValueError('A placa foi inserida de forma incorreta!')
        self.__placa = p_placa

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, p_modelo: str):
        if len(p_modelo) == 0:
            raise ValueError('O modelo foi inserido de forma incorreta!')
        self.__modelo = p_modelo

    # 3 passo: construir o construtor
    def __init__(self, placa: str, modelo: str):
        self.__placa = placa
        self.__modelo = modelo

    # 4º passo: definir o metodo para exibir os valores das propriedades/atributos

    def exibicao(self):
        return f'{self.placa} - {self.modelo} '


# v1 = Veiculo('KMN 6D39', 'Chevrolet Onix Plus')
# print(v1.exibicao())
