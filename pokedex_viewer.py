# pokedex_viewer.py
"""
Interface de visualisation du Pokédex - affiche tous les Pokémon capturés
"""

import pygame
import sys
from pokedex_manager import pokedex_manager

def show_pokedex():
    """
    Affiche l'interface du Pokédex avec tous les Pokémon capturés
    """
    pygame.init()
    WIDTH, HEIGHT = 1000, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pokédex")
    clock = pygame.time.Clock()
    
    # Couleurs
    BG_COLOR = (20, 25, 40)
    PANEL_COLOR = (40, 50, 70)
    WHITE = (245, 245, 255)
    GOLD = (255, 215, 0)
    BLUE = (120, 190, 255)
    BORDER_COLOR = (100, 130, 190)
    TEXT_COLOR = (230, 230, 240)
    
    # Fonts
    title_font = pygame.font.SysFont("arial", 48, bold=True)
    subtitle_font = pygame.font.SysFont("arial", 32, bold=True)
    normal_font = pygame.font.SysFont("consolas", 24)
    small_font = pygame.font.SysFont("consolas", 20)
    
    # Charger Pokédex
    captured = pokedex_manager.get_all_captured()
    pokemon_list = list(captured.items())
    
    # Scroll
    scroll_offset = 0
    max_visible = 5
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    return
                if event.key == pygame.K_UP:
                    scroll_offset = max(0, scroll_offset - 1)
                if event.key == pygame.K_DOWN:
                    scroll_offset = min(len(pokemon_list) - max_visible, scroll_offset + 1)
            
            # Scroll avec molette
            if event.type == pygame.MOUSEWHEEL:
                scroll_offset -= event.y
                scroll_offset = max(0, min(len(pokemon_list) - max_visible, scroll_offset))
            
            # Clic sur bouton retour
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button = pygame.Rect(350, 620, 300, 60)
                if back_button.collidepoint(event.pos):
                    return
        
        # Dessiner
        screen.fill(BG_COLOR)
        
        # Titre
        title = title_font.render("📖 POKÉDEX", True, GOLD)
        title_rect = title.get_rect(center=(WIDTH // 2, 50))
        screen.blit(title, title_rect)
        
        # Statistiques
        total_captured = len(captured)
        stats_text = subtitle_font.render(f"Pokémon capturés : {total_captured}", True, BLUE)
        stats_rect = stats_text.get_rect(center=(WIDTH // 2, 110))
        screen.blit(stats_text, stats_rect)
        
        if not pokemon_list:
            # Aucun Pokémon capturé
            empty_text = normal_font.render("Aucun Pokémon capturé pour le moment...", True, TEXT_COLOR)
            empty_rect = empty_text.get_rect(center=(WIDTH // 2, 300))
            screen.blit(empty_text, empty_rect)
            
            hint = small_font.render("Gagnez des combats pour remplir votre Pokédex !", True, BLUE)
            hint_rect = hint.get_rect(center=(WIDTH // 2, 350))
            screen.blit(hint, hint_rect)
        else:
            # Afficher les Pokémon
            y_start = 160
            visible_pokemon = pokemon_list[scroll_offset:scroll_offset + max_visible]
            
            for i, (name, data) in enumerate(visible_pokemon):
                y = y_start + i * 90
                rect = pygame.Rect(50, y, 900, 80)
                
                # Panel
                pygame.draw.rect(screen, PANEL_COLOR, rect, border_radius=10)
                pygame.draw.rect(screen, BORDER_COLOR, rect, 3, border_radius=10)
                
                # Nom
                name_text = normal_font.render(f"🔸 {data['nom']}", True, GOLD)
                screen.blit(name_text, (rect.left + 20, y + 10))
                
                # Type
                type_text = small_font.render(f"Type: {data['type']}", True, BLUE)
                screen.blit(type_text, (rect.left + 20, y + 40))
                
                # Stats
                stats = small_font.render(f"ATK:{data['power']}  DEF:{data['defense']}  HP:{data['max_life']}", True, TEXT_COLOR)
                screen.blit(stats, (rect.left + 250, y + 40))
                
                # Combats gagnés
                defeats = small_font.render(f"Défaites: {data['times_defeated']}", True, WHITE)
                screen.blit(defeats, (rect.left + 650, y + 40))
                
                # XP total
                xp = small_font.render(f"XP: {data['total_xp_gained']}", True, GOLD)
                screen.blit(xp, (rect.left + 800, y + 40))
            
            # Indicateur de scroll
            if len(pokemon_list) > max_visible:
                scroll_info = small_font.render(f"↕ {scroll_offset + 1}-{min(scroll_offset + max_visible, len(pokemon_list))} / {len(pokemon_list)}", True, BLUE)
                screen.blit(scroll_info, (WIDTH - 150, 160))
        
        # Bouton retour
        back_button = pygame.Rect(350, 620, 300, 60)
        mouse_pos = pygame.mouse.get_pos()
        
        if back_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (100, 150, 255), back_button, border_radius=12)
        else:
            pygame.draw.rect(screen, (50, 100, 200), back_button, border_radius=12)
        
        pygame.draw.rect(screen, WHITE, back_button, 3, border_radius=12)
        
        back_text = subtitle_font.render("RETOUR", True, WHITE)
        back_rect = back_text.get_rect(center=back_button.center)
        screen.blit(back_text, back_rect)
        
        pygame.display.flip()
        clock.tick(60)
