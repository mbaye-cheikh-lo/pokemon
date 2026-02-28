import pygame
import sys

pygame.init()

# =========================
# CONFIG
# =========================
WIDTH, HEIGHT = 960, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon - Menu")
clock = pygame.time.Clock()

# =========================
# COULEURS ARC-EN-CIEL
# =========================
FOND = (245, 245, 245)  # blanc clair

ARC_EN_CIEL = [
    (255, 0, 0),      # rouge
    (255, 127, 0),    # orange
    (255, 255, 0),    # jaune
    (0, 255, 0),      # vert
    (0, 0, 255),      # bleu
    (75, 0, 130),     # indigo
    (148, 0, 211),    # violet
]

BOUTON_COLORS = [
    (255, 0, 0),   # PLAY
    (0, 255, 0),   # POKEDEX
    (0, 0, 255)    # QUIT
]

TEXTE_BLANC = (255, 255, 255)
BORDURE_NOIR = (0, 0, 0)

# =========================
# POLICES
# =========================
title_font = pygame.font.SysFont("arial", 80, bold=True)
button_font = pygame.font.SysFont("arial", 40, bold=True)

# =========================
# CLASSES
# =========================
class Button:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color  # couleur fixe

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=12)
        pygame.draw.rect(screen, BORDURE_NOIR, self.rect, 3, border_radius=12)
        text_surface = button_font.render(self.text, True, TEXTE_BLANC)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


class Menu:
    def __init__(self):
        self.button_width = 300
        self.button_height = 80
        # boutons avec couleurs fixes arc-en-ciel
        self.play_button = Button("PLAY", WIDTH//2 - self.button_width//2, 300,
                                  self.button_width, self.button_height, BOUTON_COLORS[0])
        self.pokedex_button = Button("POKEDEX", WIDTH//2 - self.button_width//2, 420,
                                     self.button_width, self.button_height, BOUTON_COLORS[1])
        self.quit_button = Button("QUIT", WIDTH//2 - self.button_width//2, 540,
                                  self.button_width, self.button_height, BOUTON_COLORS[2])
        self.buttons = [self.play_button, self.pokedex_button, self.quit_button]

    def draw(self):
        # ===== TITRE ARC-EN-CIEL =====
        title = "POKEMON"
        x_offset = WIDTH//2 - len(title)*40
        for i, letter in enumerate(title):
            color = ARC_EN_CIEL[i % len(ARC_EN_CIEL)]
            text_surf = title_font.render(letter, True, color)
            screen.blit(text_surf, (x_offset + i*80, 100))
        # ===== BOUTONS =====
        for button in self.buttons:
            button.draw()

    def handle_event(self, event):
        if self.play_button.is_clicked(event):
            return "PLAY"
        elif self.pokedex_button.is_clicked(event):
            return "POKEDEX"
        elif self.quit_button.is_clicked(event):
            return "QUIT"
        return None


class Game:
    def __init__(self):
        self.menu = Menu()
        self.state = "MENU"

    def start_game(self):
        print("GAME STARTED")
        self.state = "MENU"

    def show_pokedex(self):
        print("POKEDEX OPEN")
        self.state = "MENU"

    def run(self):
        running = True
        while running:
            clock.tick(60)
            screen.fill(FOND)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.state == "MENU":
                    action = self.menu.handle_event(event)
                    if action == "PLAY":
                        self.state = "GAME"
                        self.start_game()
                    elif action == "POKEDEX":
                        self.state = "POKEDEX"
                        self.show_pokedex()
                    elif action == "QUIT":
                        pygame.quit()
                        sys.exit()

            # Affichage selon état
            if self.state == "MENU":
                self.menu.draw()
            elif self.state == "GAME":
                game_text = title_font.render("GAME SCREEN", True, (0,0,0))
                screen.blit(game_text, game_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
            elif self.state == "POKEDEX":
                pokedex_text = title_font.render("POKEDEX SCREEN", True, (0,0,0))
                screen.blit(pokedex_text, pokedex_text.get_rect(center=(WIDTH//2, HEIGHT//2)))

            pygame.display.flip()


# =========================
# LANCEMENT
# =========================
if __name__ == "__main__":
    game = Game()
    game.run()