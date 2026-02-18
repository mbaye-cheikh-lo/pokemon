import pygame
import sys

pygame.init()

# =========================
# CONFIG
# =========================
WIDTH = 960
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon - Menu")

clock = pygame.time.Clock()

# =========================
# COULEURS
# =========================
BLUE = (50, 150, 255)
DARK_BLUE = (30, 100, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# =========================
# POLICE
# =========================
title_font = pygame.font.SysFont("arial", 80, bold=True)
button_font = pygame.font.SysFont("arial", 40, bold=True)

# =========================
# BOUTON CLASS
# =========================
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()

        # effet hover
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, DARK_BLUE, self.rect, border_radius=12)
        else:
            pygame.draw.rect(screen, BLUE, self.rect, border_radius=12)

        pygame.draw.rect(screen, BLACK, self.rect, 3, border_radius=12)

        text_surface = button_font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False


# =========================
# CREATION BOUTONS
# =========================
button_width = 300
button_height = 80

play_button = Button("PLAY", WIDTH//2 - button_width//2, 300, button_width, button_height)
pokedex_button = Button("POKEDEX", WIDTH//2 - button_width//2, 420, button_width, button_height)
quit_button = Button("QUIT", WIDTH//2 - button_width//2, 540, button_width, button_height)

# =========================
# BOUCLE PRINCIPALE
# =========================
running = True
while running:
    clock.tick(60)
    screen.fill(GRAY)

    # ===== TITRE =====
    title_text = title_font.render("POKEMON", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH//2, 150))
    screen.blit(title_text, title_rect)

    # ===== BOUTONS =====
    play_button.draw()
    pokedex_button.draw()
    quit_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if play_button.is_clicked(event):
            print("PLAY pressed")

        if pokedex_button.is_clicked(event):
            print("POKEDEX pressed")

        if quit_button.is_clicked(event):
            pygame.quit()
            sys.exit()

    pygame.display.flip()

pygame.quit()
