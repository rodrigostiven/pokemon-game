import random

from pokemon import *

NOMES = ["João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego",
         "Patrícia", "Gustavo", "Gerônimo", "Gary", "Ash", "Brock"
         ]

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Charizard"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Gyarados")
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não tem nenhum pokemon".format(self))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("escolha o seu Pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida")
        else:
            print("Esse jogador não possui nenhum pokemon para ser escolhido")

    def batalhar(self, pessoa):
        print("{} iniciou um batalha com {}".format(self, pessoa))

        pessoa.mostrar_pokemons()
        pessoa.escolher_pokemon()

        self.escolher_pokemon()


class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}" .format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Seu inimigo não possui nenhum pokemon para ser escolhido")