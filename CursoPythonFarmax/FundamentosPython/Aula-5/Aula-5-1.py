
# passo 1 - vamos definir a classe

class Carro:  # todo o nome de classe começa com a letra maiuscula!

    # definir 3 propriedades/variaveis/atributos/fields... estas propriedades são, naturalmente, publicas - ou seja, podem ser "vistas" tanto, daqui, desta classe, quanto de qualquer outro "pedaço" do nosso projeto

    marca = ''
    modelo = ''
    ano = 0

# passo 2 - agora, queremos acessar as variaveis/... que foram declaradas dentro da classe Carro! E, na sequencia, atribuir valores a elas. Depois exibir os valores que elas receberam

# para conseguir fazer este acesso e MANIPULAR as propriedades/... é necessario gerar um OBJETO - a partir da classe Carro. Pois uma classe é somento um elemento declarativo - para que possamos fazer uso das propriedades lá, descritas, precisamos do objeto.

# aqui, estamos praticando a instancia da classe Carro; uma instancia de classe nada mais do que a INICIALIZAÇÃO desta classe dizendo o seguinte: "aquilo que , aqui, na classe, esta descrito, agora, pode ser usado". Portanto, agora, no ato da instancia/inicialização da classe, o objeto carroA acaba de ser criado!


carroA = Carro()
carroA.marca = 'Vw'
carroA.modelo = 'Gol'
carroA.ano = 1992

carroB = Carro()
carroB.marca = 'Fiat'
carroB.modelo = '147'
carroB.ano = 1978

carroC = Carro()
carroC.marca = 'Chevrolet'
carroC.modelo = 'Opala'
carroC.ano = 1975

carroD = Carro()
carroD.marca = 'Toyota'
carroD.modelo = 'Corolla'
carroD.ano = 2025

# passo 3 - exibir os carros na garagem
print('===== CARROS DA GARAGEM DO LUIS =====')
print('Carro A:', carroA.marca, carroA.modelo, carroA.ano)
print('Carro B:', carroB.marca, carroB.modelo, carroB.ano)
print('Carro C:', carroC.marca, carroC.modelo, carroC.ano)
print('Carro D:', carroD.marca, carroD.modelo, carroD.ano)
