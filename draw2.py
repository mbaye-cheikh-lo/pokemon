# import pygame
# import gif_pygame
# from Kombat import *
# from pokemon import *
# import time
# import json


# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1000, 700))
# clock = pygame.time.Clock()
# image = pygame.image.load("assets/image (23).jpg").convert()
# image = pygame.transform.scale(image,(1000,700))
# image3 = pygame.image.load("pikachu.png").convert_alpha()
# image3 = pygame.transform.scale(image3,(200,200))
# # gif= gif_pygame.load("assets/spritePokemon/22_rapasdepic.png")
# image2 = pygame.image.load("assets/image__26_-removebg-preview.png").convert_alpha()
# image2 = pygame.transform.scale(image2,(300,450))
# # x,y=780,2

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (50, 220, 50)
# GRAY  = (70, 70, 70)
# RED   = (220, 40, 40)
# BLACK = (0, 0, 0)
# DARK_GRAY = (40, 40, 40)
# LIGHT_GRAY = (80, 80, 80)
# GREEN = (0, 255, 0)
# BLUE = (100, 150, 255)
# # Player variables
# max_health = 100
# current_health = max_health
# max_health2 = 100
# current_health2 = max_health2


# # Health bar position and size
# bar_x = 650
# bar_y = 40
# bar_width = 300
# bar_height = 30

# bar_x2 = 50
# bar_y2 = 400
# bar_width2= 300
# bar_height2 = 30

# # Couleurs de base (juste pour que le menu soit visible)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# DARK_GRAY = (40, 40, 40)

# # Rectangle du menu (en bas à gauche)
# menu_x = 600
# menu_y = 700- 220
# menu_w = 350
# menu_h = 180

# # Hauteur d'une ligne
# option_h = 45

# # Les 3 options avec leur zone cliquable + valeur associée
# options = [
#     {"text": "-Attaquer",       "rect": pygame.Rect(menu_x + 10, menu_y + 15,  menu_w - 20, option_h), "value": 1},
#     {"text": "Changer pokémon", "rect": pygame.Rect(menu_x + 10, menu_y + 65,  menu_w - 20, option_h), "value": 2},
#     {"text": "Fuir",           "rect": pygame.Rect(menu_x + 10, menu_y + 115, menu_w - 20, option_h), "value": 3}
# ]

# font = pygame.font.SysFont("arial", 32, bold=True) 
# import pygame

# pygame.init()
# pygame.mixer.init()


# pygame.mixer.music.load("assets/song_and_sound/Gym Leader Battle - Pokémon Red_Blue_Yellow Soundtrack.mp3")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.2)  # entre 0.0 et 1.0
# sound_attaque=pygame.mixer.Sound("assets/song_and_sound/MegaDrain.wav")

# sound_attaque.set_volume(0.2)


# running=True
# while running:
#     mouse_pos = pygame.mouse.get_pos()
#     # pygame.mixer.music.load("assets/song_and_sound/Gym Leader Battle - Pokémon Red_Blue_Yellow Soundtrack.mp3")
#     # pygame.mixer.music.play(1)
#     # pygame.mixer.music.set_volume(0.2)  # entre 0.0 et 1.0
                    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # if event.type == pygame.KEYDOWN:
#         #     if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
#         #             current_health -=  test.type_puissance("Eau", "Vol")
#         #     if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
#         #             current_health += 45
#         elif event.type == pygame.MOUSEBUTTONDOWN:
            
            
#             for opt in options:
#                 if opt["rect"].collidepoint(mouse_pos) and test.turn %2 != 0 and current_health and current_health2 >0:
                   
#                     current_health -= test.type_puissance("Eau", "Sol")
#                     sound_attaque.play(1)
#                     test.theturn()
#                 else:
#                     if current_health2 <=0:
#                         image2.apend("pokedex.json")
                    
                  
                    
#                     break
#     if test.turn %2 == 0:
         
#         current_health2 -= test.type_puissance("Sol", "Eau")
#         test.theturn()  
#     current_health = max(0, min(max_health, current_health))
#     current_health2 = max(0, min(max_health2, current_health2))
#     screen.fill((255, 255, 255))
#     screen.blit(image,(0,0))
#     screen.blit(image3,(700,80))
#     screen.blit(image2,(40,350))
#     health_ratio = current_health / max_health
#     current_width = int(bar_width * health_ratio)

#     health_ratio2 = current_health2 / max_health2
#     current_width2 = int(bar_width2 * health_ratio2)

#     pygame.draw.rect(screen, DARK_GRAY, (menu_x, menu_y, menu_w, menu_h))
#     pygame.draw.rect(screen, WHITE, (menu_x, menu_y, menu_w, menu_h), 3)

   
    

#     if health_ratio > 0.5:
#         color = GREEN
#     elif health_ratio > 0.25:
#         color = (255, 200, 0)
#     else:
#         color = RED
    
#     if health_ratio2 > 0.5:
#         color2 = GREEN
#     elif health_ratio2 > 0.25:
#         color2 = (255, 200, 0)
#     else:
#         color2 = RED


#     pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_width, bar_height))
#     health_ratio = current_health / max_health
#     current_width = int(bar_width * health_ratio)

#     pygame.draw.rect(screen, GRAY, (bar_x2, bar_y2, bar_width2, bar_height2))
#     health_ratio2 = current_health2 / max_health2
#     current_width2 = int(bar_width2 * health_ratio2)

    
    

#     for opt in options:
#         text_surf = font.render(opt["text"], True, WHITE)
#         text_rect = text_surf.get_rect(center=opt["rect"].center)
#         screen.blit(text_surf, text_rect)

#     pygame.draw.rect(screen, color, (bar_x, bar_y, current_width, bar_height))
#     pygame.draw.rect(screen, BLACK, (bar_x, bar_y, bar_width, bar_height), 3)
#     font = pygame.font.SysFont("consolas", 24)
#     text = font.render(f"Pikachu: {current_health}/{max_health}", True, DARK_GRAY)
#     screen.blit(text, (bar_x, bar_y - 35))

#     pygame.draw.rect(screen, color2, (bar_x2, bar_y2, current_width2, bar_height2))
#     pygame.draw.rect(screen, BLACK, (bar_x2, bar_y2, bar_width2, bar_height2), 3)
#     font = pygame.font.SysFont("consolas", 24)
#     text2 = font.render(f"Tortank: {current_health2}/{max_health2}", True, DARK_GRAY)
#     screen.blit(text2, (bar_x2, bar_y2 - 35))

#     # gif.render(screen, (x, y))


   

   
#     pygame.display.flip()

#     clock.tick(60)  

# pygame.quit()






# draw.py
# draw.py
"""
Main Pokémon battle screen - JOUEUR en bas gauche (dos) / ADVERSAIRE en haut droite (face)
"""# draw.py
"""
Main Pokémon battle screen - PLAYER bottom-left (back sprite) / OPPONENT top-right (front sprite)
"""

# import pygame
# import sys
# import random
# import os
# from Kombat import Combat
# from draw_choice import main as choose_pokemon
# from pokemon import Pokemon

# # ────────────────────────────────────────────────
# # PLAYER POKÉMON SELECTION
# # ────────────────────────────────────────────────
# print("Sélection du Pokémon du joueur...")
# player_pokemon = choose_pokemon()

# if player_pokemon is None:
#     print("Aucun Pokémon choisi → fin du programme")
#     sys.exit(0)

# # Back sprite path is already stored in player_pokemon.sprite_dos

# # ────────────────────────────────────────────────
# # RANDOM OPPONENT + front sprite
# # ────────────────────────────────────────────────
# face_dir = "assets/spritePokemonFace_PokeAPI"
# face_files = [f for f in os.listdir(face_dir) if f.endswith("_face.png")]

# if not face_files:
#     print("Erreur : aucun sprite face trouvé dans", face_dir)
#     sys.exit(1)

# random_face_file = random.choice(face_files)
# opponent_filename = random_face_file.replace("_face.png", "")
# opponent_name = opponent_filename.split("_", 1)[1].capitalize() if "_" in opponent_filename else opponent_filename.capitalize()

# opponent_pokemon = Pokemon(
#     nom=opponent_name,
#     attack_name="Attaque basique",
#     life=100,
#     type_="Normal",
#     defense=80,
#     power2=50,
#     image="",
#     xp=100,
#     imgback=""
# )
# opponent_pokemon.sprite_face = os.path.join(face_dir, random_face_file).replace("\\", "/")

# # Create battle instance
# combat = Combat(player_pokemon, opponent_pokemon)

# # ────────────────────────────────────────────────
# # PYGAME SETUP
# # ────────────────────────────────────────────────
# pygame.init()
# screen = pygame.display.set_mode((1000, 700))
# clock = pygame.time.Clock()

# # ────────────────────────────────────────────────
# # LOAD DYNAMIC SPRITES
# # ────────────────────────────────────────────────
# try:
#     player_back_sprite = pygame.image.load(player_pokemon.sprite_dos).convert_alpha()
#     player_back_sprite = pygame.transform.scale(player_back_sprite, (280, 280))
# except Exception as e:
#     print(f"Player back sprite not found ({player_pokemon.sprite_dos}) → fallback")
#     player_back_sprite = pygame.image.load("assets/image__26_-removebg-preview.png").convert_alpha()
#     player_back_sprite = pygame.transform.scale(player_back_sprite, (300, 450))

# try:
#     opponent_front_sprite = pygame.image.load(opponent_pokemon.sprite_face).convert_alpha()
#     opponent_front_sprite = pygame.transform.scale(opponent_front_sprite, (200, 200))
# except Exception as e:
#     print(f"Opponent front sprite not found ({opponent_pokemon.sprite_face}) → fallback")
#     opponent_front_sprite = pygame.image.load("pikachu.png").convert_alpha()
#     opponent_front_sprite = pygame.transform.scale(opponent_front_sprite, (200, 200))

# # ────────────────────────────────────────────────
# # BACKGROUND
# # ────────────────────────────────────────────────
# background = pygame.image.load("assets/image (23).jpg").convert()
# background = pygame.transform.scale(background, (1000, 700))

# # ────────────────────────────────────────────────
# # COLORS
# # ────────────────────────────────────────────────
# WHITE       = (255, 255, 255)
# BLACK       = (0, 0, 0)
# GREEN       = (50, 220, 50)
# GRAY        = (70, 70, 70)
# RED         = (220, 40, 40)
# DARK_GRAY   = (40, 40, 40)
# LIGHT_GRAY  = (80, 80, 80)
# BLUE        = (100, 150, 255)

# # ────────────────────────────────────────────────
# # HEALTH BARS
# # ────────────────────────────────────────────────
# player_bar_x, player_bar_y, player_bar_w, player_bar_h = 50, 400, 300, 30   # PLAYER bottom-left
# opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h = 650, 40, 300, 30               # OPPONENT top-right

# # ────────────────────────────────────────────────
# # ACTION MENU
# # ────────────────────────────────────────────────
# menu_x, menu_y = 600, 480
# menu_w, menu_h = 350, 180
# option_h = 45

# options = [
#     {"text": "- Attaquer",       "rect": pygame.Rect(menu_x + 10, menu_y + 15,  menu_w - 20, option_h), "value": 1},
#     {"text": "Changer Pokémon", "rect": pygame.Rect(menu_x + 10, menu_y + 65,  menu_w - 20, option_h), "value": 2},
#     {"text": "Fuir",            "rect": pygame.Rect(menu_x + 10, menu_y + 115, menu_w - 20, option_h), "value": 3}
# ]

# font_menu   = pygame.font.SysFont("arial", 32, bold=True)
# font_health = pygame.font.SysFont("consolas", 24)

# # ────────────────────────────────────────────────
# # AUDIO
# # ────────────────────────────────────────────────
# pygame.mixer.init()
# pygame.mixer.music.load("assets/song_and_sound/Gym Leader Battle - Pokémon Red_Blue_Yellow Soundtrack.mp3")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.0)

# sound_attack = pygame.mixer.Sound("assets/song_and_sound/MegaDrain.wav")
# sound_attack_ops= pygame.mixer.Sound("assets/song_and_sound/Ember.wav")
# sound_attack_ops.set_volume(0.1)
# sound_attack.set_volume(0.2)

# # ────────────────────────────────────────────────
# # MAIN GAME LOOP
# # ────────────────────────────────────────────────
# running = True
# while running:
#     mouse_pos = pygame.mouse.get_pos()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             for opt in options:
#                 if opt["rect"].collidepoint(mouse_pos):
#                     if opt["value"] == 1 and combat.turn % 2 != 0:
#                         damage = combat.player_attack()
#                         if damage > 0:
#                             sound_attack.play()
#                             print(f"{player_pokemon.nom} inflige {damage} dégâts à {opponent_pokemon.nom}")

#                             # Redraw to show damage immediately
#                             screen.blit(background, (0, 0))
#                             screen.blit(player_back_sprite, (40, 350))          # PLAYER bottom-left (back)
#                             screen.blit(opponent_front_sprite, (700, 80))      # OPPONENT top-right (front)

#                             # Player health bar
#                             ratio = player_pokemon.life / player_pokemon.max_life if player_pokemon.max_life > 0 else 0
#                             width = int(player_bar_w * ratio)
#                             color = GREEN if ratio > 0.5 else (255, 200, 0) if ratio > 0.25 else RED
#                             pygame.draw.rect(screen, GRAY, (player_bar_x, player_bar_y, player_bar_w, player_bar_h))
#                             pygame.draw.rect(screen, color, (player_bar_x, player_bar_y, width, player_bar_h))
#                             pygame.draw.rect(screen, BLACK, (player_bar_x, player_bar_y, player_bar_w, player_bar_h), 3)
#                             text = font_health.render(f"{player_pokemon.nom}: {player_pokemon.life}/{player_pokemon.max_life}", True, DARK_GRAY)
#                             screen.blit(text, (player_bar_x, player_bar_y - 35))

#                             # Opponent health bar
#                             ratio2 = opponent_pokemon.life / opponent_pokemon.max_life if opponent_pokemon.max_life > 0 else 0
#                             width2 = int(opp_bar_w * ratio2)
#                             color2 = GREEN if ratio2 > 0.5 else (255, 200, 0) if ratio2 > 0.25 else RED
#                             pygame.draw.rect(screen, GRAY, (opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h))
#                             pygame.draw.rect(screen, color2, (opp_bar_x, opp_bar_y, width2, opp_bar_h))
#                             pygame.draw.rect(screen, BLACK, (opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h), 3)
#                             text2 = font_health.render(f"{opponent_pokemon.nom}: {opponent_pokemon.life}/{opponent_pokemon.max_life}", True, DARK_GRAY)
#                             screen.blit(text2, (opp_bar_x, opp_bar_y - 35))

#                             # Redraw menu
#                             pygame.draw.rect(screen, DARK_GRAY, (menu_x, menu_y, menu_w, menu_h))
#                             pygame.draw.rect(screen, WHITE, (menu_x, menu_y, menu_w, menu_h), 3)
#                             for o in options:
#                                 ts = font_menu.render(o["text"], True, WHITE)
#                                 tr = ts.get_rect(center=o["rect"].center)
#                                 screen.blit(ts, tr)

#                             pygame.display.flip()

#                             # Delay after player attack
#                             pygame.time.wait(2000)

#     # Opponent's turn
#     if combat.turn % 2 == 0:
#         damage = combat.opponent_attack()
#         if damage > 0:
#             sound_attack_ops.play()
#             print(f"{opponent_pokemon.nom} inflige {damage} dégâts à {player_pokemon.nom}")
#             pygame.time.wait(1000)

#     # Check for winner
#     winner = combat.check_winner()
#     if winner:
#         print(f"Gagnant : {winner.nom}")
#         running = False

#     # ─── FULL RENDER ───
#     screen.blit(background, (0, 0))
#     screen.blit(player_back_sprite, (40, 350))          # PLAYER bottom-left (back)
#     screen.blit(opponent_front_sprite, (700, 80))      # OPPONENT top-right (front)

#     # Player health bar (bottom-left)
#     ratio = player_pokemon.life / player_pokemon.max_life if player_pokemon.max_life > 0 else 0
#     width = int(player_bar_w * ratio)
#     color = GREEN if ratio > 0.5 else (255, 200, 0) if ratio > 0.25 else RED
#     pygame.draw.rect(screen, GRAY, (player_bar_x, player_bar_y, player_bar_w, player_bar_h))
#     pygame.draw.rect(screen, color, (player_bar_x, player_bar_y, width, player_bar_h))
#     pygame.draw.rect(screen, BLACK, (player_bar_x, player_bar_y, player_bar_w, player_bar_h), 3)
#     text = font_health.render(f"{player_pokemon.nom}: {player_pokemon.life}/{player_pokemon.max_life}", True, DARK_GRAY)
#     screen.blit(text, (player_bar_x, player_bar_y - 35))

#     # Opponent health bar (top-right)
#     ratio = opponent_pokemon.life / opponent_pokemon.max_life if opponent_pokemon.max_life > 0 else 0
#     width = int(opp_bar_w * ratio)
#     color = GREEN if ratio > 0.5 else (255, 200, 0) if ratio > 0.25 else RED
#     pygame.draw.rect(screen, GRAY, (opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h))
#     pygame.draw.rect(screen, color, (opp_bar_x, opp_bar_y, width, opp_bar_h))
#     pygame.draw.rect(screen, BLACK, (opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h), 3)
#     text = font_health.render(f"{opponent_pokemon.nom}: {opponent_pokemon.life}/{opponent_pokemon.max_life}", True, DARK_GRAY)
#     screen.blit(text, (opp_bar_x, opp_bar_y - 35))

#     # Menu
#     pygame.draw.rect(screen, DARK_GRAY, (menu_x, menu_y, menu_w, menu_h))
#     pygame.draw.rect(screen, WHITE, (menu_x, menu_y, menu_w, menu_h), 3)

#     for opt in options:
#         text_surf = font_menu.render(opt["text"], True, WHITE)
#         text_rect = text_surf.get_rect(center=opt["rect"].center)
#         screen.blit(text_surf, text_rect)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.mixer.music.stop()
# pygame.quit() 

# draw.py
"""
Main Pokémon battle screen - PLAYER bottom-left (back sprite) / OPPONENT top-right (front sprite)
"""

import pygame
import sys
import random
import os
from Kombat import Combat
from pokemon import Pokemon
from pokedex_manager import pokedex_manager
from victory_screen import show_victory_screen
from evolution_system import evolution_system

def run_battle(player_pokemon):
    """
    Run the battle screen with the selected player Pokémon
    """
    print(f"Battle started with {player_pokemon.nom}")

    # Random opponent + front sprite
    face_dir = "assets/spritePokemonFace_PokeAPI"
    face_files = [f for f in os.listdir(face_dir) if f.endswith("_face.png")]

    if not face_files:
        print("Error: no front sprites found")
        return

    random_face_file = random.choice(face_files)
    opponent_filename = random_face_file.replace("_face.png", "")
    opponent_name = opponent_filename.split("_", 1)[1].capitalize() if "_" in opponent_filename else opponent_filename.capitalize()

    opponent_pokemon = Pokemon(
        nom=opponent_name,
        attack_name="Attaque basique",
        life=100,
        type_="Normal",
        defense=80,
        power2=50,
        image="",
        xp=100,
        imgback=""
    )
    opponent_pokemon.sprite_face = os.path.join(face_dir, random_face_file).replace("\\", "/")

    # Create combat instance
    combat = Combat(player_pokemon, opponent_pokemon)

    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    clock = pygame.time.Clock()

    # Load sprites
    try:
        player_back_sprite = pygame.image.load(player_pokemon.sprite_dos).convert_alpha()
        player_back_sprite = pygame.transform.scale(player_back_sprite, (280, 280))
    except Exception as e:
        print(f"Player back sprite not found → fallback")
        player_back_sprite = pygame.image.load("assets/spritePokemonDos_PokeAPI/95_onyx_dos.png").convert_alpha()
        player_back_sprite = pygame.transform.scale(player_back_sprite, (300, 450))

    try:
        opponent_front_sprite = pygame.image.load(opponent_pokemon.sprite_face).convert_alpha()
        opponent_front_sprite = pygame.transform.scale(opponent_front_sprite, (200, 200))
    except Exception as e:
        print(f"Opponent front sprite not found → fallback")
        opponent_front_sprite = pygame.image.load("pikachu.png").convert_alpha()
        opponent_front_sprite = pygame.transform.scale(opponent_front_sprite, (200, 200))

    # Background
    background = pygame.image.load("assets/image (23).jpg").convert()
    background = pygame.transform.scale(background, (1000, 700))

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (50, 220, 50)
    GRAY = (70, 70, 70)
    RED = (220, 40, 40)
    DARK_GRAY = (40, 40, 40)
    LIGHT_GRAY = (80, 80, 80)
    BLUE = (100, 150, 255)

    # Health bars
    player_bar_x, player_bar_y, player_bar_w, player_bar_h = 50, 400, 300, 30
    opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h = 650, 40, 300, 30

    # Action menu
    menu_x, menu_y = 600, 480
    menu_w, menu_h = 350, 180
    option_h = 45

    options = [
        {"text": "- Attaquer", "rect": pygame.Rect(menu_x + 10, menu_y + 15, menu_w - 20, option_h), "value": 1},
        {"text": "Changer Pokémon", "rect": pygame.Rect(menu_x + 10, menu_y + 65, menu_w - 20, option_h), "value": 2},
        {"text": "Fuir", "rect": pygame.Rect(menu_x + 10, menu_y + 115, menu_w - 20, option_h), "value": 3}
    ]

    font_menu = pygame.font.SysFont("arial", 32, bold=True)
    font_health = pygame.font.SysFont("consolas", 24)

    # Audio
    pygame.mixer.init()
    pygame.mixer.music.load("assets/song_and_sound/Gym Leader Battle - Pokémon Red_Blue_Yellow Soundtrack.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)

    sound_attack_ops= pygame.mixer.Sound("assets/song_and_sound/Ember.wav")
    sound_attack_ops.set_volume(0.1)

    sound_attack = pygame.mixer.Sound("assets/song_and_sound/MegaDrain.wav")
    sound_attack.set_volume(0.6)

    # Main battle loop
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for opt in options:
                    if opt["rect"].collidepoint(mouse_pos):
                        if opt["value"] == 1 and combat.turn % 2 != 0:
                            damage = combat.player_attack()
                            if damage > 0:
                                sound_attack.play()
                                print(f"{player_pokemon.nom} inflige {damage} dégâts à {opponent_pokemon.nom}")

                                # Immediate redraw
                                screen.blit(background, (0, 0))
                                screen.blit(player_back_sprite, (40, 350))
                                screen.blit(opponent_front_sprite, (700, 80))

                                # Player health bar
                                ratio = player_pokemon.life / player_pokemon.max_life if player_pokemon.max_life > 0 else 0
                                width = int(player_bar_w * ratio)
                                color = GREEN if ratio > 0.5 else (255, 200, 0) if ratio > 0.25 else RED
                                pygame.draw.rect(screen, GRAY, (player_bar_x, player_bar_y, player_bar_w, player_bar_h))
                                pygame.draw.rect(screen, color, (player_bar_x, player_bar_y, width, player_bar_h))
                                pygame.draw.rect(screen, BLACK, (player_bar_x, player_bar_y, player_bar_w, player_bar_h), 3)
                                text = font_health.render(f"{player_pokemon.nom}: {player_pokemon.life}/{player_pokemon.max_life}", True, DARK_GRAY)
                                screen.blit(text, (player_bar_x, player_bar_y - 35))

                                # Opponent health bar
                                ratio2 = opponent_pokemon.life / opponent_pokemon.max_life if opponent_pokemon.max_life > 0 else 0
                                width2 = int(opp_bar_w * ratio2)
                                color2 = GREEN if ratio2 > 0.5 else (255, 200, 0) if ratio2 > 0.25 else RED
                                pygame.draw.rect(screen, GRAY, (opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h))
                                pygame.draw.rect(screen, color2, (opp_bar_x, opp_bar_y, width2, opp_bar_h))
                                pygame.draw.rect(screen, BLACK, (opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h), 3)
                                text2 = font_health.render(f"{opponent_pokemon.nom}: {opponent_pokemon.life}/{opponent_pokemon.max_life}", True, DARK_GRAY)
                                screen.blit(text2, (opp_bar_x, opp_bar_y - 35))

                                # Menu
                                pygame.draw.rect(screen, DARK_GRAY, (menu_x, menu_y, menu_w, menu_h))
                                pygame.draw.rect(screen, WHITE, (menu_x, menu_y, menu_w, menu_h), 3)
                                for o in options:
                                    ts = font_menu.render(o["text"], True, WHITE)
                                    tr = ts.get_rect(center=o["rect"].center)
                                    screen.blit(ts, tr)

                                pygame.display.flip()

                                pygame.time.wait(1200)

        # Opponent turn
        if combat.turn % 2 == 0:
            damage = combat.opponent_attack()
            if damage > 0:
                sound_attack_ops.play()
                print(f"{opponent_pokemon.nom} inflige {damage} dégâts à {player_pokemon.nom}")
                pygame.time.wait(1000)

        # Check winner
        winner = combat.check_winner()
        if winner:
            print(f"Gagnant : {winner.nom}")
            is_player_winner = (winner == player_pokemon)
            
            # Si victoire du joueur
            if is_player_winner:
                # Gagner XP et monter de niveau
                leveled_up = player_pokemon.gain_xp(100)
                if leveled_up:
                    print(f"🎉 {player_pokemon.nom} est maintenant niveau {player_pokemon.level}!")
                
                # Ajouter l'adversaire au Pokédex
                is_new_capture = pokedex_manager.add_pokemon(opponent_pokemon)
                print(f"✨ Pokémon ajouté au Pokédex ! Nouvelle capture: {is_new_capture}")
                
                # Vérifier évolution
                evolution_data = evolution_system.can_evolve(player_pokemon, player_pokemon.level)
                if evolution_data:
                    print(f"🌟 {player_pokemon.nom} peut évoluer en {evolution_data['evolves_to']} !")
                    evolution_system.show_evolution_screen(screen, player_pokemon.nom, evolution_data["evolves_to"])
                    player_pokemon = evolution_system.evolve_pokemon(player_pokemon, evolution_data)
                    print(f"✅ Évolution réussie ! Bienvenue {player_pokemon.nom}")
                
                # Écran de victoire
                show_victory_screen(screen, winner.nom, True, is_new_capture)
            else:
                # Écran de défaite
                show_victory_screen(screen, winner.nom, False)
            
            running = False

        # Full render
        screen.blit(background, (0, 0))
        screen.blit(player_back_sprite, (40, 350))
        screen.blit(opponent_front_sprite, (700, 80))

        # Player health bar
        ratio = player_pokemon.life / player_pokemon.max_life if player_pokemon.max_life > 0 else 0
        width = int(player_bar_w * ratio)
        color = GREEN if ratio > 0.5 else (255, 200, 0) if ratio > 0.25 else RED
        pygame.draw.rect(screen, GRAY, (player_bar_x, player_bar_y, player_bar_w, player_bar_h))
        pygame.draw.rect(screen, color, (player_bar_x, player_bar_y, width, player_bar_h))
        pygame.draw.rect(screen, BLACK, (player_bar_x, player_bar_y, player_bar_w, player_bar_h), 3)
        text = font_health.render(f"{player_pokemon.nom}: {player_pokemon.life}/{player_pokemon.max_life}", True, DARK_GRAY)
        screen.blit(text, (player_bar_x, player_bar_y - 35))

    # Fermer la musique mais PAS pygame
    pygame.mixer.music.stop()
    print("Combat terminé - retour au menu")
    # Ne pas faire pygame.quit() ici ! On retourne juste au menu
        color = GREEN if ratio > 0.5 else (255, 200, 0) if ratio > 0.25 else RED
        pygame.draw.rect(screen, GRAY, (opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h))
        pygame.draw.rect(screen, color, (opp_bar_x, opp_bar_y, width, opp_bar_h))
        pygame.draw.rect(screen, BLACK, (opp_bar_x, opp_bar_y, opp_bar_w, opp_bar_h), 3)
        text = font_health.render(f"{opponent_pokemon.nom}: {opponent_pokemon.life}/{opponent_pokemon.max_life}", True, DARK_GRAY)
        screen.blit(text, (opp_bar_x, opp_bar_y - 35))

        # Menu
        pygame.draw.rect(screen, DARK_GRAY, (menu_x, menu_y, menu_w, menu_h))
        pygame.draw.rect(screen, WHITE, (menu_x, menu_y, menu_w, menu_h), 3)

        for opt in options:
            text_surf = font_menu.render(opt["text"], True, WHITE)
            text_rect = text_surf.get_rect(center=opt["rect"].center)
            screen.blit(text_surf, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.stop()
    pygame.quit()
    print("Combat terminé - retour au menu")