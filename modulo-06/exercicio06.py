# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar 
# apenas os valores negativos.
# range(-5, 5)

negativos = filter(lambda x: x < 0, range(-5, 5))
print(list(negativos))

"""
range(-5, 5)
list(filter((lambda x: x < 0), range(-5,5)))
"""
