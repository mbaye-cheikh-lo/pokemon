# pokemon.py
# Pokemon class - used by draw_choice.py and draw.py

class Pokemon:
    def __init__(self, nom, attack_name, life, type_, defense, power2, image="", xp=0, imgback=""):
        self.nom = nom
        self.attack_name = attack_name
        self.life = life
        self.max_life = life  # for health bar max value
        self.type = type_
        self.defense = defense
        self.power2 = power2
        self.image = image
        self.xp = xp
        self.imgback = imgback

        # Optional: back sprite path will be set by draw_choice.py
        self.sprite_dos = None

    def show_info(self):
        print(f"Nom: {self.nom}")
        print(f"Type: {self.type}")
        print(f"Attaque: {self.attack_name}")
        print(f"PV: {self.life}/{self.max_life}")
        print(f"Défense: {self.defense}")
        print(f"Puissance: {self.power2}")
        if self.sprite_dos:
            print(f"Sprite dos: {self.sprite_dos}")
        print("---")


# Optional sample instances (for testing)
fearow = Pokemon(
    nom="Rapasdepic",
    attack_name="Coup d'aile",
    life=85,
    type_="Vol",
    defense=85,
    power2=37,
    image="assets/spritePokemonDos_PokeAPI/22_rapasdepic_dos.png",
    xp=100,
    imgback="imageback"
)

tortank = Pokemon(
    nom="Tortank",
    attack_name="Canon a eau",
    life=95,
    type_="Eau",
    defense=95,
    power2=55,
    image="assets/spritePokemonDos_PokeAPI/9_tortank_dos.png",
    xp=100,
    imgback="assets/pokemon_bw___night.jpg"
)


if __name__ == "__main__":
    tortank.show_info()