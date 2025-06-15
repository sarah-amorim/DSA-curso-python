# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e
# imprima a lista

def recebe_lista(arg):
  arg.append(8)
  arg.append(9)

lista = [1, 2, 3, 4]
recebe_lista(lista)
print(lista)

"""
def novaLista(lista):
    print(lista.append(5))
    print(lista.append(6))
   
lista1 = [1, 2, 3, 4]   
novaLista(lista1)
print(lista1)
"""
