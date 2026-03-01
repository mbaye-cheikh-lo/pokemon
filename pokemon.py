# pokemon.py
# Pokemon class - used by draw_choice.py and draw.py

class Pokemon:
    def __init__(self, nom, attack_name, life, type_, defense, power2, image="", xp=0, imgback="", level=1):
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
        self.level = level  # Niveau du Pokémon pour le système d'évolution

        # Optional: back sprite path will be set by draw_choice.py
        self.sprite_dos = None

    def show_info(self):
        print(f"Nom: {self.nom}")
        print(f"Type: {self.type}")
        print(f"Attaque: {self.attack_name}")
        print(f"PV: {self.life}/{self.max_life}")
        print(f"Défense: {self.defense}")
        print(f"Puissance: {self.power2}")
        print(f"Niveau: {self.level}")
        print(f"XP: {self.xp}")
        if self.sprite_dos:
            print(f"Sprite dos: {self.sprite_dos}")
        print("---")
    
    def gain_xp(self, amount):
        """Ajoute de l'XP et monte de niveau si nécessaire"""
        self.xp += amount
        xp_needed = self.level * 100  # 100 XP par niveau
        
        if self.xp >= xp_needed:
            self.level += 1
            self.xp = 0  # Reset XP
            # Améliorer les stats à chaque niveau
            self.max_life += 10
            self.life = self.max_life  # Restaurer la vie à fond
            self.power2 += 5
            self.defense += 3
            print(f"*** {self.nom} monte au niveau {self.level} !")
            return True  # A monté de niveau
        return False  # Pas de montée de niveau


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
    imgback="assets/ground/pokemon_bw___night.jpg"
)


if __name__ == "__main__":
    tortank.show_info()