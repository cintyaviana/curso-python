
# HERANÇA MULTIPLA ==============================

from automovel import Automovel
from caminhao_multiplo import CaminhaoMultiplo


class MotoMultipla(Automovel, CaminhaoMultiplo):
    def __init__(self, modelo, marca, ano, carga, cilindrada):
        # super().__init__(self, marca, modelo, ano)  # referencia a superclasse Automovel
        # super().__init__(self, carga)  # referencia a superclasse CaminhaoMultiplo

        # referencia a superclasse Automovel
        Automovel.__init__(self, marca, modelo, ano)
        # referencia a superclasse CaminhaoMultiplo
        CaminhaoMultiplo.__init__(self, carga)
        self.cilindrada = cilindrada

    # sobrescrita do metodo exibicao
    def exibicao(self):
        # combinar/juntar as informações das duas superclasses
        return f'{self.marca}{self.modelo}{self.ano} | carga {self.carga} | {self.cilindrada}'


# ====================TESTAR HERANÇA MULTIPLA ==================
minhaMoto = MotoMultipla('Honda', 'CG 125', 1983, 0.3, 125)
print(minhaMoto.exibicao())  # método herdado da classe automóvel
print(minhaMoto.capacidade())  # método herdado da classe CaminhãoMultiplo
