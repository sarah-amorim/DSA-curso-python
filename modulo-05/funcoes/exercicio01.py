# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro),
# e depois faça uma chamada à função para listar os números 

def numeros_pares():
  for numero in range(1, 21):
    if numero % 2 == 0:
      print(numero)

print(numeros_pares())

"""
def listaPar():
    for i in range(2, 21, 2): 
        print(i)
        
listaPar() 
"""
