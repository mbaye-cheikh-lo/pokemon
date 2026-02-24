class Pokemon:
    def __init__(self, name, type, attack, defense, life):
        self.name = name
        self.type = type
        self.attack = attack
        self.defense = defense
        self.life = life

    def show_info(self):
        print("Nom :", self.name)
        print("Type :", self.type)
        print("Attaque :", self.attack)
        print("Défense :", self.defense)
        print("Vie :", self.life)
        print("----------------------")


# Base de données Pokémon
pokedex = {

    "Pikachu": Pokemon("Pikachu", "Électrik", 55, 40, 100),

    "Salameche": Pokemon("Salameche", "Feu", 52, 43, 100),

    "Carapuce": Pokemon("Carapuce", "Eau", 48, 65, 110),

    "Bulbizarre": Pokemon("Bulbizarre", "Plante", 49, 49, 105),

    "Rondoudou": Pokemon("Rondoudou", "Fée", 45, 20, 120),

    "Onix": Pokemon("Onix", "Roche", 45, 160, 120)

}


def show_pokedex():
    print("===== POKEDEX =====")
    for pokemon in pokedex.values():
        pokemon.show_info()


def get_pokemon(name):
    return pokedex.get(name)
