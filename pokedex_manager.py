# pokedex_manager.py
"""
Gestionnaire du Pokédex - sauvegarde et gestion des Pokémon capturés
"""

import json
import os
from datetime import datetime

CAPTURED_POKEDEX_PATH = "captured_pokedex.json"

class PokedexManager:
    def __init__(self):
        self.captured = self.load_captured()
    
    def load_captured(self):
        """Charge la liste des Pokémon capturés depuis le fichier JSON"""
        if os.path.exists(CAPTURED_POKEDEX_PATH):
            try:
                with open(CAPTURED_POKEDEX_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Erreur lors du chargement du Pokédex: {e}")
                return {}
        return {}
    
    def save_captured(self):
        """Sauvegarde la liste des Pokémon capturés"""
        try:
            with open(CAPTURED_POKEDEX_PATH, "w", encoding="utf-8") as f:
                json.dump(self.captured, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du Pokédex: {e}")
    
    def add_pokemon(self, pokemon):
        """
        Ajoute un Pokémon au Pokédex après une victoire
        Retourne True si c'est une nouvelle capture, False sinon
        """
        name = pokemon.nom
        is_new = name not in self.captured
        
        if is_new:
            # Première capture
            self.captured[name] = {
                "nom": pokemon.nom,
                "type": pokemon.type,
                "power": pokemon.power2,
                "defense": pokemon.defense,
                "max_life": pokemon.max_life,
                "first_captured": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "times_defeated": 1,
                "total_xp_gained": 100
            }
        else:
            # Déjà capturé, on incrémente les stats
            self.captured[name]["times_defeated"] += 1
            self.captured[name]["total_xp_gained"] += 100
        
        self.save_captured()
        return is_new
    
    def is_captured(self, pokemon_name):
        """Vérifie si un Pokémon est déjà dans le Pokédex"""
        return pokemon_name in self.captured
    
    def get_capture_count(self):
        """Retourne le nombre de Pokémon différents capturés"""
        return len(self.captured)
    
    def get_all_captured(self):
        """Retourne la liste de tous les Pokémon capturés"""
        return self.captured


# Instance globale pour faciliter l'utilisation
pokedex_manager = PokedexManager()
