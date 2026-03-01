# draw_choice.py
# draw_choice.py
"""
Interface de sélection de Pokémon - retourne une instance avec vraies stats + sprite dos correct
"""
# draw_choice.py
"""
Pokemon selection screen - returns instance with real stats + correct back sprite path
"""

import pygame
import json
import sys
from pokemon import Pokemon

WIDTH, HEIGHT = 1000, 700
FPS = 60

BG_COLOR       = (20, 25, 40)
PANEL_COLOR    = (40, 50, 70)
WHITE          = (245, 245, 255)
LIGHT_BLUE     = (120, 190, 255)
SELECTED_GREEN = (90, 220, 130)
HOVER_GRAY     = (70, 80, 100)
TEXT_COLOR     = (230, 230, 240)
BORDER_COLOR   = (100, 130, 190)

POKEDEX_JSON_PATH = "pokedex.json"

# Fixed mapping: name -> ID (to build correct sprite filename)
POKEDEX_ID = {
    "Pikachu": "25",
    "Salameche": "4",
    "Carapuce": "7",
    "Bulbizarre": "1",
    "Rondoudou": "39",
    "Onix": "95",
}

def load_pokedex_data():
    try:
        with open(POKEDEX_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading pokedex.json: {e}")
        sys.exit(1)

pokedex_data = load_pokedex_data()
pokemon_keys = list(pokedex_data.keys())

def draw_text(surface, text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(text_surface, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sélection Pokémon")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("arial", 38, bold=True)
    normal_font = pygame.font.SysFont("consolas", 26)
    small_font  = pygame.font.SysFont("consolas", 20)

    selected_index = -1
    hovered_index = -1
    selected_pokemon = None

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True

        hovered_index = -1
        for i in range(len(pokemon_keys)):
            rect = pygame.Rect(30, 140 + i*85, 900, 80)
            if rect.collidepoint(mouse_pos):
                hovered_index = i
                if clicked:
                    selected_index = i
                    key = pokemon_keys[i]  # ex: "Salameche"
                    data = pokedex_data[key]

                    # Get ID from fixed map (fallback to 1)
                    id_part = POKEDEX_ID.get(key, "1")

                    # Create instance with real stats from JSON
                    selected_pokemon = Pokemon(
                        nom=data[0],
                        attack_name="Attaque basique",
                        life=data[4],
                        type_=data[1],
                        defense=data[3],
                        power2=data[2],
                        image="",
                        xp=100,
                        imgback=""
                    )

                    # Build correct back sprite path
                    selected_pokemon.sprite_dos = f"assets/spritePokemonDos_PokeAPI/{id_part}_{key.lower()}_dos.png"

                    running = False
                break

        screen.fill(BG_COLOR)
        draw_text(screen, "Choisis ton Pokémon", title_font, WHITE, WIDTH//2, 70, center=True)

        for i, name in enumerate(pokemon_keys):
            y = 140 + i * 85
            rect = pygame.Rect(30, y, 900, 80)

            color = SELECTED_GREEN if i == selected_index else HOVER_GRAY if i == hovered_index else PANEL_COLOR
            pygame.draw.rect(screen, color, rect, border_radius=12)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 3, border_radius=12)

            data = pokedex_data[name]
            draw_text(screen, data[0], normal_font, WHITE, rect.left + 40, y + 12)
            draw_text(screen, f"Type : {data[1]}", small_font, LIGHT_BLUE, rect.left + 40, y + 38)
            draw_text(screen, f"Atk:{data[2]}  Def:{data[3]}  PV:{data[4]}", small_font, TEXT_COLOR, rect.left + 40, y + 58)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.display.quit()  # Fermer seulement le display, pas pygame entier

    if selected_pokemon:
        print("\nSelected Pokemon:")
        selected_pokemon.show_info()
        return selected_pokemon
    else:
        print("No selection made.")
        return None


if __name__ == "__main__":
    pokemon = main()
    if pokemon:
        print(f"Instance created: {pokemon.nom} ({pokemon.type}) - HP: {pokemon.life}")