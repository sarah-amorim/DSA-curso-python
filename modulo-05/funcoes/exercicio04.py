# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def recebe_argumentos(arg, *vartuple):
  print(f"Apenas um argumento: {arg}")
  for item in vartuple:
    print(item)

recebe_argumentos("Argumento 1")
recebe_argumentos("Argumento 1", "Argumento 2", "Argumento 3", "Argumento 4")

"""
def printNum( arg1, *lista ):
    print (arg1)
    for i in lista:
        print (i)
    return;

# Chamada à função
printNum( 100 )
printNum( 'A', 'B', 'C' )
"""
