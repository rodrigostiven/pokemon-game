from pokemon import *

class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Anônimo"

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)

class Player(Pessoa):
    tipo = "player"


class Inimigo(Pessoa):
    tipo = "inimigo"