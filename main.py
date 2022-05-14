from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print("Olá {}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possui 3 escolhas: ")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)

    while True:
        escolha = input("escolha o seu Pokemon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida")

if __name__ == "__main__":
    print("===========================================")
    print("Bem-vindo ao game Pokemon")
    print("===========================================")

    nome = input("Olá, qual é o seu nome? ")
    player = Player(nome)
    print("Olá {}, esse é mundo habitado por pokemons," 
          "a partir de agora a sua missão é se tornar um mentre de pokemons".format(player))
    print("Capture o máximo de pokemons que conseguir e lute com seus inimigos")
    player.mostrar_dinheiro()

    if player.pokemons:
        print("Já vi que você tem alguns pokemons")
        player.mostrar_pokemons()
    else:
        print("Você não tem nenhum pokemon, portanto escolher um")
        escolher_pokemon_inicial(player)

    print("Pronto, agora que você já tem o seu pokemon, enfrente o seu arqui-rival Gary")
    gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
    player.batalhar(gary)

    while True:
        print("================================")
        print("O que deseja fazer?")
        print("1 - Explorar pelo mundo a fora")
        print("2 - Lutar com um inimigo")
        print("0 - Sair do jogo")
        escolha = input("Sua escolha: ")

        if escolha == "0":
            print("Fechando o jogo...")
            break
        elif escolha == "1":
            player.explorar()
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
        else:
            print("Escolha Inválida")