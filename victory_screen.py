# victory_screen.py
"""
Écran de victoire/défaite avec feedback visuel
"""

import pygame
import sys

def show_victory_screen(screen, winner_name, is_player_winner, is_new_capture=False):
    """
    Affiche un écran de victoire ou de défaite
    
    Args:
        screen: Surface Pygame
        winner_name: Nom du Pokémon gagnant
        is_player_winner: True si le joueur a gagné
        is_new_capture: True si c'est une nouvelle capture pour le Pokédex
    """
    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (50, 220, 50)
    RED = (220, 40, 40)
    GOLD = (255, 215, 0)
    BLUE = (100, 150, 255)
    
    # Fonts
    title_font = pygame.font.SysFont("arial", 80, bold=True)
    subtitle_font = pygame.font.SysFont("arial", 40, bold=True)
    button_font = pygame.font.SysFont("arial", 35, bold=True)
    info_font = pygame.font.SysFont("arial", 30)
    
    # Couleur de fond selon victoire/défaite
    if is_player_winner:
        bg_color = (20, 80, 20)  # Vert foncé
        main_color = GREEN
        title_text = "VICTOIRE !"
    else:
        bg_color = (80, 20, 20)  # Rouge foncé
        main_color = RED
        title_text = "DÉFAITE !"
    
    # Bouton retour au menu
    button_rect = pygame.Rect(300, 550, 400, 70)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return
        
        # Dessiner fond
        screen.fill(bg_color)
        
        # Effet de brillance (rectangles semi-transparents)
        overlay = pygame.Surface((1000, 700))
        overlay.set_alpha(30)
        overlay.fill(main_color)
        screen.blit(overlay, (0, 0))
        
        # Titre principal
        title_surface = title_font.render(title_text, True, main_color)
        title_rect = title_surface.get_rect(center=(500, 150))
        # Ombre du texte
        shadow = title_font.render(title_text, True, BLACK)
        screen.blit(shadow, (title_rect.x + 5, title_rect.y + 5))
        screen.blit(title_surface, title_rect)
        
        # Nom du gagnant
        winner_text = subtitle_font.render(f"{winner_name} l'emporte !", True, WHITE)
        winner_rect = winner_text.get_rect(center=(500, 250))
        screen.blit(winner_text, winner_rect)
        
        # XP gagnés (seulement si victoire)
        if is_player_winner:
            xp_text = info_font.render("+100 XP", True, GOLD)
            xp_rect = xp_text.get_rect(center=(500, 320))
            screen.blit(xp_text, xp_rect)
            
            # Nouvelle capture ?
            if is_new_capture:
                capture_text = info_font.render("✨ Nouvelle capture Pokédex ! ✨", True, GOLD)
                capture_rect = capture_text.get_rect(center=(500, 380))
                screen.blit(capture_text, capture_rect)
        
        # Bouton retour
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BLUE, button_rect, border_radius=15)
        else:
            pygame.draw.rect(screen, (50, 100, 200), button_rect, border_radius=15)
        
        pygame.draw.rect(screen, WHITE, button_rect, 4, border_radius=15)
        
        button_text = button_font.render("RETOUR AU MENU", True, WHITE)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)
        
        # Instructions
        hint = info_font.render("(Appuyez sur ENTRÉE ou cliquez)", True, BLUE)
        hint_rect = hint.get_rect(center=(500, 650))
        screen.blit(hint, hint_rect)
        
        pygame.display.flip()
        clock.tick(60)
