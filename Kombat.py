
from pokemon import Pokemon
from data import types, matrice

class Combat:
    def __init__(self, player_pokemon: Pokemon, opponent_pokemon: Pokemon):
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon
        
        self.player_max_life = player_pokemon.life
        self.opponent_max_life = opponent_pokemon.life
        
        self.turn = 1  # 1 = joueur, 2 = adversaire
        self.state = "bataille"
        self.winner = None

    def type_puissance(self, type1: str, type2: str) -> float:
        """Retourne le coefficient multiplicateur depuis la matrice de data.py"""
        # Normalisation : enlève accents et met en majuscule
        type1_clean = type1.replace("É", "E").replace("é", "e").capitalize()
        type2_clean = type2.replace("É", "E").replace("é", "e").capitalize()
        
        try:
            i = types.index(type1_clean)
            j = types.index(type2_clean)
            return matrice[i][j]
        except ValueError:
            print(f"Type inconnu : {type1_clean} ou {type2_clean}")
            return 1.0

    def calculate_damage(self, attacker: Pokemon, defender: Pokemon) -> int:
        """Calcule les dégâts avec multiplicateur de type + power2"""
        multiplier = self.type_puissance(attacker.type, defender.type)
        base_damage = attacker.power2
        damage = int(base_damage * multiplier)
        
        # Réduction par défense : beaucoup plus douce (÷5 au lieu de ÷2)
        defense_reduction = defender.defense // 5
        reduced = max(1, damage - defense_reduction)
        
        return reduced

    def apply_damage(self, target: Pokemon, damage: int):
        target.life -= damage
        if target.life <= 0:
            target.life = 0

    def check_winner(self):
        if self.player_pokemon.life <= 0:
            self.winner = self.opponent_pokemon
            self.state = "fini"
            return self.opponent_pokemon
        elif self.opponent_pokemon.life <= 0:
            self.winner = self.player_pokemon
            self.state = "fini"
            return self.player_pokemon
        return None

    def next_turn(self):
        self.turn += 1

    def player_attack(self):
        if self.state != "bataille" or self.check_winner():
            return 0
        damage = self.calculate_damage(self.player_pokemon, self.opponent_pokemon)
        self.apply_damage(self.opponent_pokemon, damage)
        self.next_turn()
        return damage

    def opponent_attack(self):
        if self.state != "bataille" or self.check_winner():
            return 0
        damage = self.calculate_damage(self.opponent_pokemon, self.player_pokemon)
        self.apply_damage(self.player_pokemon, damage)
        self.next_turn()
        return damage

    def __str__(self):
        return (f"Combat : {self.player_pokemon.nom} ({self.player_pokemon.life} PV) "
                f"VS {self.opponent_pokemon.nom} ({self.opponent_pokemon.life} PV) "
                f"- Tour {self.turn}")