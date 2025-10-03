
from pizza import Pizza


class PizzaEspecial(Pizza):

    def __init__(self, sabor: str, tamanho: str, preco: float, ingredientes_extra: str):
        super().__init__(sabor, tamanho, preco)
        self.__ingredientes_extra = ingredientes_extra

    def exibicao(self) -> str:
        return super().exibicao() + f' | Extras: {self.__ingredientes_extra}'


pedido_esp = PizzaEspecial('Pequena', 'Quatro Queijos', 35.99, 'tomate, ovo')

# exibir estes valores
print(pedido_esp.exibicao())
