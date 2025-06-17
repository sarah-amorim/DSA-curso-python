# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():
  def __init__(self, nome, cidade, telefone, email):
    self.nome = nome
    self.cidade = cidade
    self.telefone = telefone 
    self.email = email
    
  def informacoes(self):
    print(f"Nome: {self.nome}\nCidade: {self.cidade}\nTelefone: {self.telefone}\nE-mail: {self.email}")

  def cumprimentar(self):
    print(f"Olá, {self.nome}!")

pessoa1 = Pessoa("Sarah", "Maceió", "82990000000", "email@email.com")
pessoa1.informacoes()
pessoa1.cumprimentar()

"""
class Pessoa():
    
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        print("Objeto criado")
        
    def __str__(self):
        return "O usuário " + self.nome + " mora na cidade " + self.cidade

P1 = Pessoa("Pele", "Três Corações", 99887766, "pele@gmail.com")
str(P1)
"""
