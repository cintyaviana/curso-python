
"""
Exercício 1 - Classe Produto

* PREMISSA - PROBLEMA A SER RESOLVIDO
Crie uma classe chamada Produto que represente um item de estoque.

*TENHO QUE OBSERVAR QUAIS SÃO AS REGRAS/ORBRIGATORIEDADES MINIMAS QUE MEU PROJETO DEVE OBEDECER
A classe deve conter:

Atributos/variáveis
nome (string): nome do produto.
preço (float): preço unitário.
quantidade (int): quantidade em estoque.

Construtor: que receba todos os atributos na criação do objeto.
___init__

Métodos:
valor_total() -> retorna o valor total em estoque (preço * quantidade).
repor(qtd) -> aumenta a quantidade em estoque.
vender(qtd) -> diminui a quantidade em estoque (não pode ficar negativo; caso a quantidade pedida seja maior que o estoque, exiba uma mensagem adequada).
aplicar_desconto(porcentagem) -> aplica um desconto no preço do produto.

"""

# Criação da classe


class Produto:
    nome = ''
    preco = 0.0
    quantidade = 0
    # Método construtor

    def __init__(self, nome: str, preco: float, quantidade: int):
        # Acessar os atributos da classe e oferecer para eles, como valor os parâmetros do método construtor.
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self) -> float:
        return self.preco * self.quantidade

    def repor(self, qtd: int):
        self.quantidade += qtd
        print(f'Quantidade em estoque: ', self.quantidade)

    def vender(self, qtd: int):
        if qtd <= 0:
            print('Você não pode vender uma quantidade negativa de produtos')
        elif qtd > self.quantidade:
            print('Estoqur induficiente')
        else:
            self.quantidade -= qtd
            print('Quantidade em estoque: ', self.quantidade)

    def aplicar_desconto(self, porcentagem: float):
        if 0 < porcentagem < 100:
            self.preco -= self.preco*(porcentagem/100)
        else:
            print('Este desconto não é permitido')


# Gerando o objeto
p1 = Produto('Acetona', 50.99, 50)

# Exibir os produtos
print('======= Produtos========')
print(
    f'Produto1: {p1.nome}, Preço unitário: {p1.preco}, Qtde em estoque{p1.quantidade}')
print('Valor total em estoque: ', p1.valor_total())

# Chamada do 2º método (repor)
p1.repor(50)

# Chamada do 3º método (vender)
p1.vender(80)

# Chamada do 4º método (vender)
p1.aplicar_desconto(10)
print(f'Preço com desconto {p1.preco:.2f}')
