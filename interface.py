# interface.py
# Main menu screen - launches selection on PLAY button

import pygame
import sys
from draw_choice import main as choose_pokemon  # import selection screen
from draw2 import run_battle  # import battle screen function

pygame.init()

# CONFIG
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon - Menu")
clock = pygame.time.Clock()

# Background
background = pygame.image.load("assets/ground/image (28).jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# COLORS
BLUE = (50, 150, 255)
DARK_BLUE = (30, 100, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# FONTS
title_font = pygame.font.SysFont("arial", 80, bold=True)
button_font = pygame.font.SysFont("arial", 40, bold=True)

# BUTTON CLASS
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()

        # Hover effect
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, DARK_BLUE, self.rect, border_radius=12)
        else:
            pygame.draw.rect(screen, BLUE, self.rect, border_radius=12)

        pygame.draw.rect(screen, BLACK, self.rect, 3, border_radius=12)

        text_surface = button_font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


# CREATE BUTTONS
button_width = 300
button_height = 80

play_button = Button("JOUER", WIDTH//2 - button_width//2, 300, button_width, button_height)
pokedex_button = Button("POKÉDEX", WIDTH//2 - button_width//2, 420, button_width, button_height)
quit_button = Button("QUITTER", WIDTH//2 - button_width//2, 540, button_width, button_height)

pygame.mixer.init()
pygame.mixer.music.load("assets/song_and_sound/Pokemon Red_Blue Opening.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

# MAIN MENU LOOP
running = True
while running:
    clock.tick(60)

    # Background
    screen.blit(background, (0, 0))

    # TITLE
    title_text = title_font.render("", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH//2, 150))
    screen.blit(title_text, title_rect)

    # BUTTONS
    play_button.draw()
    pokedex_button.draw()
    quit_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if play_button.is_clicked(event):
            print("PLAY button pressed → launching selection")
            selected_pokemon = choose_pokemon()  # Launch selection screen
            if selected_pokemon:
                print(f"Selected Pokémon: {selected_pokemon.nom}")
                # Launch battle directly
                run_battle(selected_pokemon)

        if pokedex_button.is_clicked(event):
            print("POKÉDEX button pressed (not implemented yet)")

        if quit_button.is_clicked(event):
            print("Quitting game")
            pygame.quit()
            sys.exit()

    pygame.display.flip()

pygame.quit()
