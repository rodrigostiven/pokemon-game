class Pokemon:
    def __init__(self, especie, level = 1, nome=None):
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({})" .format(self.nome, self.level)

    def atacar(self, pokemon):
        print("{} atacou {}!".format(self.especie, pokemon.especie))

class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))

class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo em {}".format(self, pokemon))

class PokemonAgua(Pokemon):
    tipo = "água"

    def atacar(self, pokemon):
        print("{} lançou o jato de água em {}".format(self, pokemon))