# evolution_system.py
"""
Système d'évolution des Pokémon
"""

import pygame

# Base de données des évolutions
# Format: {"Pokemon actuel": {"evolves_to": "Nom évolution", "level": niveau requis, "battles": combats requis}}
EVOLUTION_DATA = {
    "Salameche": {
        "evolves_to": "Reptincel",
        "level": 16,
        "battles": 3,
        "type": "Feu",
        "power": 64,
        "defense": 58,
        "life": 120
    },
    "Reptincel": {
        "evolves_to": "Dracaufeu",
        "level": 36,
        "battles": 8,
        "type": "Feu",
        "power": 84,
        "defense": 78,
        "life": 156
    },
    "Carapuce": {
        "evolves_to": "Carabaffe",
        "level": 16,
        "battles": 3,
        "type": "Eau",
        "power": 63,
        "defense": 80,
        "life": 118
    },
    "Carabaffe": {
        "evolves_to": "Tortank",
        "level": 36,
        "battles": 8,
        "type": "Eau",
        "power": 83,
        "defense": 100,
        "life": 158
    },
    "Bulbizarre": {
        "evolves_to": "Herbizarre",
        "level": 16,
        "battles": 3,
        "type": "Plante",
        "power": 62,
        "defense": 63,
        "life": 120
    },
    "Herbizarre": {
        "evolves_to": "Florizarre",
        "level": 36,
        "battles": 8,
        "type": "Plante",
        "power": 82,
        "defense": 83,
        "life": 160
    },
    "Pikachu": {
        "evolves_to": "Raichu",
        "level": 20,
        "battles": 5,
        "type": "Electrik",
        "power": 90,
        "defense": 55,
        "life": 120
    }
}


class EvolutionSystem:
    def __init__(self):
        self.battle_count = {}  # Compteur de combats par Pokémon
    
    def can_evolve(self, pokemon, current_level=1):
        """
        Vérifie si un Pokémon peut évoluer
        
        Args:
            pokemon: Instance de Pokemon
            current_level: Niveau actuel du Pokémon
        
        Returns:
            dict ou None: Données d'évolution si possible, None sinon
        """
        if pokemon.nom not in EVOLUTION_DATA:
            return None
        
        evolution_info = EVOLUTION_DATA[pokemon.nom]
        
        # Incrémenter compteur de combats
        if pokemon.nom not in self.battle_count:
            self.battle_count[pokemon.nom] = 0
        self.battle_count[pokemon.nom] += 1
        
        # Vérifier conditions
        battles_done = self.battle_count[pokemon.nom]
        required_battles = evolution_info["battles"]
        required_level = evolution_info["level"]
        
        if current_level >= required_level or battles_done >= required_battles:
            return evolution_info
        
        return None
    
    def evolve_pokemon(self, pokemon, evolution_data):
        """
        Fait évoluer un Pokémon
        
        Args:
            pokemon: Instance de Pokemon à faire évoluer
            evolution_data: Données d'évolution depuis EVOLUTION_DATA
        
        Returns:
            Pokemon: Instance du Pokémon évolué
        """
        from pokemon import Pokemon
        
        evolved = Pokemon(
            nom=evolution_data["evolves_to"],
            attack_name="Attaque évoluée",
            life=evolution_data["life"],
            type_=evolution_data["type"],
            defense=evolution_data["defense"],
            power2=evolution_data["power"],
            image=pokemon.image,  # Garder l'image actuelle (ou mettre à jour si disponible)
            xp=pokemon.xp + 200,
            imgback=pokemon.imgback
        )
        
        # Copier sprite_dos si existant
        if hasattr(pokemon, 'sprite_dos'):
            evolved.sprite_dos = pokemon.sprite_dos
        
        return evolved
    
    def show_evolution_screen(self, screen, old_name, new_name):
        """
        Affiche un écran d'évolution (simple animation)
        
        Args:
            screen: Surface Pygame
            old_name: Nom avant évolution
            new_name: Nom après évolution
        """
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        PURPLE = (150, 50, 255)
        
        font_big = pygame.font.SysFont("arial", 60, bold=True)
        font_small = pygame.font.SysFont("arial", 40)
        
        # Animation simple (3 secondes)
        for frame in range(180):  # 3 secondes à 60 FPS
            screen.fill((10, 10, 30))
            
            # Effet de flash
            alpha = abs((frame % 30) - 15) * 10
            overlay = pygame.Surface((1000, 700))
            overlay.set_alpha(alpha)
            overlay.fill(PURPLE)
            screen.blit(overlay, (0, 0))
            
            # Texte d'évolution
            if frame < 90:
                text = font_big.render(f"{old_name}", True, WHITE)
            else:
                text = font_big.render(f"{new_name}", True, PURPLE)
            
            text_rect = text.get_rect(center=(500, 300))
            screen.blit(text, text_rect)
            
            # "Évolution en cours..."
            if frame < 150:
                evolution_text = font_small.render("Évolution en cours...", True, WHITE)
                evo_rect = evolution_text.get_rect(center=(500, 400))
                screen.blit(evolution_text, evo_rect)
            
            pygame.display.flip()
            pygame.time.Clock().tick(60)
    
    def reset_battle_count(self, pokemon_name):
        """Réinitialise le compteur de combats d'un Pokémon"""
        if pokemon_name in self.battle_count:
            self.battle_count[pokemon_name] = 0
    
    def get_battle_count(self, pokemon_name):
        """Retourne le nombre de combats effectués"""
        return self.battle_count.get(pokemon_name, 0)
    
    def get_evolution_progress(self, pokemon_name):
        """
        Retourne la progression vers l'évolution (en %)
        
        Returns:
            int: Pourcentage de progression (0-100), ou None si non évolutif
        """
        if pokemon_name not in EVOLUTION_DATA:
            return None
        
        required = EVOLUTION_DATA[pokemon_name]["battles"]
        current = self.battle_count.get(pokemon_name, 0)
        
        progress = min(100, int((current / required) * 100))
        return progress


# Instance globale
evolution_system = EvolutionSystem()
