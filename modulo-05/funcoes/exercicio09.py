# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome

lista = ["morango","kiwi","uva", "ameixa", "coco", "limão"]
palavras_a = [palavra for palavra in lista if "a" in palavra]
print(palavras_a)

"""
palavras = ["maça", "coiote", "banana", "terreno", "Python"]
resultado = [x for x in palavras if "a" in x]
print(resultado)
"""
