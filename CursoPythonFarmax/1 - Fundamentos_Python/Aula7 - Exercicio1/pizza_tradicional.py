
from pizza import Pizza


class PizzaTradicional(Pizza):
    pass


pedido1 = PizzaTradicional('Pequena', 'Quatro Queijos', 35.99)

# exibir estes valores
print(pedido1.exibicao())
