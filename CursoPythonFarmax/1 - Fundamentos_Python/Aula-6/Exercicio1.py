
class Produto:

    def __init__(self, nome: str, preco: float, quantidade: int):
        # Acessar os atributos da classe e oferecer para eles, como valor os parâmetros do método construtor.
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, p_nome: str):
        self.__nome = p_nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, p_preco: float):
        self.__preco = p_preco

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, p_quantidade: int):
        self.__quantidade = p_quantidade

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
