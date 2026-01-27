
gen = (x ** 2 for x in range(6))
print(gen)


# Convertendo em tupla
quadrados_tuple = tuple(gen)
print(quadrados_tuple)

type(quadrados_tuple)
