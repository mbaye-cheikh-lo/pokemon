# victory_screen.py
"""
Écran de victoire/défaite avec feedback visuel amélioré
"""

import pygame
import sys
import math

def show_victory_screen(screen, winner_name, is_player_winner, is_new_capture=False):
    """
    Affiche un écran de victoire ou de défaite avec animations
    
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
    DARK_GREEN = (20, 100, 20)
    RED = (220, 40, 40)
    DARK_RED = (100, 20, 20)
    GOLD = (255, 215, 0)
    BLUE = (100, 150, 255)
    LIGHT_GOLD = (255, 235, 100)
    
    # Fonts
    title_font = pygame.font.SysFont("arial", 90, bold=True)
    subtitle_font = pygame.font.SysFont("arial", 45, bold=True)
    button_font = pygame.font.SysFont("arial", 38, bold=True)
    info_font = pygame.font.SysFont("arial", 32)
    small_font = pygame.font.SysFont("arial", 24)
    
    # Couleur de fond selon victoire/défaite
    if is_player_winner:
        bg_color = DARK_GREEN
        main_color = GREEN
        accent_color = LIGHT_GOLD
        title_text = "🎉 VICTOIRE ! 🎉"
        subtitle = f"{winner_name} a gagné le combat !"
    else:
        bg_color = DARK_RED
        main_color = RED
        accent_color = (255, 100, 100)
        title_text = "💔 DÉFAITE 💔"
        subtitle = f"{winner_name} vous a battu..."
    
    # Bouton retour au menu
    button_rect = pygame.Rect(250, 550, 500, 80)
    
    clock = pygame.time.Clock()
    running = True
    frame = 0
    
    # Animation d'entrée
    animation_duration = 30  # frames
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Ne pas quitter brutalement, retourner au menu
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return
        
        frame += 1
        
        # Animation d'entrée
        progress = min(1.0, frame / animation_duration)
        ease_progress = 1 - math.pow(1 - progress, 3)  # Ease out cubic
        
        # Dessiner fond avec dégradé
        screen.fill(bg_color)
        
        # Effet de brillance pulsante
        pulse = abs(math.sin(frame * 0.05)) * 40 + 20
        overlay = pygame.Surface((1000, 700))
        overlay.set_alpha(int(pulse))
        overlay.fill(main_color)
        screen.blit(overlay, (0, 0))
        
        # Particules décoratives (étoiles pour victoire)
        if is_player_winner and frame > animation_duration:
            for i in range(15):
                star_frame = (frame + i * 10) % 200
                x = 100 + (i * 60) % 800
                y = 50 + ((star_frame + i * 30) % 600)
                size = 3 + (i % 3)
                alpha = int(abs(math.sin(star_frame * 0.1)) * 200)
                star_surf = pygame.Surface((size * 2, size * 2))
                star_surf.set_alpha(alpha)
                star_surf.fill(GOLD)
                screen.blit(star_surf, (x, y))
        
        # Titre principal avec animation
        title_y = 150 - int((1 - ease_progress) * 100)
        title_surface = title_font.render(title_text, True, main_color)
        title_rect = title_surface.get_rect(center=(500, title_y))
        
        # Ombre du texte plus prononcée
        for offset in [(3, 3), (4, 4), (5, 5)]:
            shadow = title_font.render(title_text, True, BLACK)
            shadow.set_alpha(50)
            screen.blit(shadow, (title_rect.x + offset[0], title_rect.y + offset[1]))
        
        screen.blit(title_surface, title_rect)
        
        # Ligne décorative sous le titre
        if progress > 0.5:
            line_width = int(300 * ((progress - 0.5) * 2))
            pygame.draw.line(screen, accent_color, 
                           (500 - line_width//2, title_y + 60),
                           (500 + line_width//2, title_y + 60), 4)
        
        # Sous-titre avec fade-in
        if progress > 0.3:
            subtitle_alpha = min(255, int((progress - 0.3) * 365))
            subtitle_surface = subtitle_font.render(subtitle, True, WHITE)
            subtitle_surface.set_alpha(subtitle_alpha)
            subtitle_rect = subtitle_surface.get_rect(center=(500, 270))
            screen.blit(subtitle_surface, subtitle_rect)
        
        # Panneau d'informations
        if is_player_winner and progress > 0.6:
            info_alpha = min(255, int((progress - 0.6) * 637))
            
            # Rectangle d'information
            info_rect = pygame.Rect(200, 340, 600, 160)
            info_surface = pygame.Surface((600, 160))
            info_surface.set_alpha(200)
            info_surface.fill((30, 30, 50))
            screen.blit(info_surface, info_rect.topleft)
            pygame.draw.rect(screen, accent_color, info_rect, 3, border_radius=15)
            
            # XP gagnés avec effet brillant
            xp_text = info_font.render("💎 +100 XP gagnés", True, GOLD)
            xp_text.set_alpha(info_alpha)
            xp_rect = xp_text.get_rect(center=(500, 380))
            screen.blit(xp_text, xp_rect)
            
            # Nouvelle capture ?
            if is_new_capture:
                capture_text = info_font.render("✨ Nouveau Pokémon capturé !", True, LIGHT_GOLD)
                capture_text.set_alpha(info_alpha)
                capture_rect = capture_text.get_rect(center=(500, 430))
                screen.blit(capture_text, capture_rect)
                
                # Badge "NEW"
                badge_rect = pygame.Rect(650, 420, 70, 30)
                pygame.draw.rect(screen, RED, badge_rect, border_radius=8)
                pygame.draw.rect(screen, GOLD, badge_rect, 2, border_radius=8)
                badge_text = small_font.render("NEW!", True, WHITE)
                badge_text_rect = badge_text.get_rect(center=badge_rect.center)
                screen.blit(badge_text, badge_text_rect)
            else:
                already_text = small_font.render("(Déjà dans le Pokédex)", True, (150, 150, 150))
                already_text.set_alpha(info_alpha)
                already_rect = already_text.get_rect(center=(500, 440))
                screen.blit(already_text, already_rect)
        
        # Bouton retour avec effet hover animé
        mouse_pos = pygame.mouse.get_pos()
        is_hover = button_rect.collidepoint(mouse_pos)
        
        if progress > 0.8:
            button_alpha = min(255, int((progress - 0.8) * 1275))
            
            # Effet de pulsation sur hover
            scale = 1.05 if is_hover else 1.0
            hover_offset = int((1 - scale) * button_rect.width / 2)
            draw_rect = button_rect.inflate(int(button_rect.width * (scale - 1)), 
                                           int(button_rect.height * (scale - 1)))
            
            # Ombre du bouton
            shadow_rect = draw_rect.move(5, 5)
            shadow_surf = pygame.Surface((draw_rect.width, draw_rect.height))
            shadow_surf.set_alpha(100)
            shadow_surf.fill(BLACK)
            screen.blit(shadow_surf, shadow_rect.topleft)
            
            # Bouton principal
            button_color = BLUE if is_hover else (50, 100, 200)
            button_surf = pygame.Surface((draw_rect.width, draw_rect.height))
            button_surf.set_alpha(button_alpha)
            button_surf.fill(button_color)
            screen.blit(button_surf, draw_rect.topleft)
            
            pygame.draw.rect(screen, WHITE, draw_rect, 4, border_radius=15)
            
            button_text = button_font.render("⬅ RETOUR AU MENU", True, WHITE)
            button_text.set_alpha(button_alpha)
            button_text_rect = button_text.get_rect(center=draw_rect.center)
            screen.blit(button_text, button_text_rect)
        
        # Instructions clignotantes
        if frame > animation_duration:
            hint_alpha = int(abs(math.sin(frame * 0.08)) * 150 + 105)
            hint = small_font.render("Appuyez sur ENTRÉE, ESPACE ou cliquez", True, (180, 180, 220))
            hint.set_alpha(hint_alpha)
            hint_rect = hint.get_rect(center=(500, 665))
            screen.blit(hint, hint_rect)
        
        pygame.display.flip()
        clock.tick(60)
