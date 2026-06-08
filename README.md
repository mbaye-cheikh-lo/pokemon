# Pokemon Battle Game

Un jeu de combat Pokémon en tour par tour développé avec Python et Pygame.

## Fonctionnalités

- Combat tour par tour avec système de types et multiplicateurs de dégâts
- 18 types avec matrice d'efficacité complète (Feu, Eau, Plante, Électrik...)
- Sélection de Pokémon parmi 5 disponibles
- Adversaire aléatoire parmi 151 sprites PokeAPI
- Gain d'XP et montée de niveau après chaque victoire
- Système d'évolution (Salamèche → Reptincel → Dracaufeu, etc.)
- Pokédex persistant avec sauvegarde des Pokémon capturés
- Écran de victoire/défaite animé
- Musiques et effets sonores

## Prérequis

- Python 3.x
- pygame >= 2.6.0

```bash
pip install pygame
```

## Lancement

```bash
# Double-clic sur launch.bat (Windows)

# Ou via terminal
python interface/interface.py
```

## Contrôles

### Menu principal
| Action | Contrôle |
|--------|----------|
| Jouer | Clic sur **JOUER** |
| Pokédex | Clic sur **POKÉDEX** |
| Quitter | Clic sur **QUITTER** |

### Sélection
- Clic sur un Pokémon pour le choisir

### Combat
| Action | Effet |
|--------|-------|
| **Attaquer** | Inflige des dégâts selon le type |
| **Changer Pokémon** | Ouvre la sélection — l'adversaire attaque en premier |
| **Fuir** | Quitte le combat sans XP ni défaite |

### Après combat
- **Entrée** ou **Clic** → Retour au menu

## Pokémon jouables

| Nom | Type | Atk | Def | PV |
|-----|------|-----|-----|----|
| Pikachu | Électrik | 55 | 40 | 100 |
| Salamèche | Feu | 52 | 43 | 100 |
| Carapuce | Eau | 48 | 65 | 110 |
| Bulbizarre | Plante | 49 | 49 | 105 |
| Rondoudou | Fée | 45 | 20 | 120 |

## Stack

- **Langage :** Python 3
- **Framework :** Pygame
- **Données :** JSON
- **Sprites :** PokeAPI (151 Pokémon)
