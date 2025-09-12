print('Um novo exemplo')


def preco_final(preco, **kwargs):
    # o uso do parametro **kwargs é uma boa pratica quando
    # queremos fazer uso de um parametro variavel que recebe
    # como valor, argumentos baseados em pares key:value

    p_taxa = 0
    p_imposto = 0

    v_taxa = kwargs.get('taxa')
    if v_taxa:
        # aqui, estamos definindo a seguinte operação:
        p_taxa = preco * v_taxa/100
        # a verificação da percentagem da v_taxa em relação
        # ao valor dado ao argumento preco

    v_imposto = kwargs.get('imposto')
    if v_imposto:
        p_imposto = preco * v_imposto/100

    return preco - p_taxa - p_imposto


# praticar a chamada da função
valorLiquido1 = preco_final(1000)
valorLiquido2 = preco_final(1000, taxa=10)
valorLiquido3 = preco_final(1000, imposto=18)
valorLiquido4 = preco_final(1000, taxa=10, imposto=18)

print(f'Valor liquido 1: {valorLiquido1}')
print(f'Valor liquido 2: {valorLiquido2}')
print(f'Valor liquido 3: {valorLiquido3}')
print(f'Valor liquido 4: {valorLiquido4}')
