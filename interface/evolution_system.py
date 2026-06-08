# evolution_system.py
"""
Système d'évolution des Pokémon
"""

import pygame
import math
import random

EVOLUTION_DATA = {
    "Salameche": {
        "evolves_to": "Reptincel",
        "level": 16,
        "battles": 1,
        "type": "Feu",
        "power": 64,
        "defense": 58,
        "life": 120
    },
    "Reptincel": {
        "evolves_to": "Dracaufeu",
        "level": 36,
        "battles": 1,
        "type": "Feu",
        "power": 84,
        "defense": 78,
        "life": 156
    },
    "Carapuce": {
        "evolves_to": "Carabaffe",
        "level": 16,
        "battles": 1,
        "type": "Eau",
        "power": 63,
        "defense": 80,
        "life": 118
    },
    "Carabaffe": {
        "evolves_to": "Tortank",
        "level": 36,
        "battles": 1,
        "type": "Eau",
        "power": 83,
        "defense": 100,
        "life": 158
    },
    "Bulbizarre": {
        "evolves_to": "Herbizarre",
        "level": 16,
        "battles": 1,
        "type": "Plante",
        "power": 62,
        "defense": 63,
        "life": 120
    },
    "Herbizarre": {
        "evolves_to": "Florizarre",
        "level": 36,
        "battles": 1,
        "type": "Plante",
        "power": 82,
        "defense": 83,
        "life": 160
    },
    "Pikachu": {
        "evolves_to": "Raichu",
        "level": 20,
        "battles": 1,
        "type": "Electrik",
        "power": 90,
        "defense": 55,
        "life": 120
    }
}

# Sprite IDs for face and back sprites of evolved forms
EVOLUTION_SPRITE_IDS = {
    "Reptincel": "5",
    "Dracaufeu": "6",
    "Carabaffe": "8",
    "Tortank": "9",
    "Herbizarre": "2",
    "Florizarre": "3",
    "Raichu": "26",
}


def _make_silhouette(sprite):
    """Returns a white silhouette of the sprite, preserving per-pixel alpha."""
    sil = sprite.copy()
    sil.fill((255, 255, 255, 0), special_flags=pygame.BLEND_RGBA_MAX)
    return sil


class EvolutionSystem:
    def __init__(self):
        self.battle_count = {}
        self.evolved_roster = {}  # {base_name: {"key": new_name, "data": [...], "sprite_id": "..."}}

    def can_evolve(self, pokemon, current_level=1):
        if pokemon.nom not in EVOLUTION_DATA:
            return None

        evolution_info = EVOLUTION_DATA[pokemon.nom]

        if pokemon.nom not in self.battle_count:
            self.battle_count[pokemon.nom] = 0
        self.battle_count[pokemon.nom] += 1

        battles_done = self.battle_count[pokemon.nom]
        required_battles = evolution_info["battles"]
        required_level = evolution_info["level"]

        if current_level >= required_level or battles_done >= required_battles:
            return evolution_info

        return None

    def evolve_pokemon(self, pokemon, evolution_data):
        from pokemon import Pokemon

        new_name = evolution_data["evolves_to"]

        evolved = Pokemon(
            nom=new_name,
            attack_name="Attaque évoluée",
            life=evolution_data["life"],
            type_=evolution_data["type"],
            defense=evolution_data["defense"],
            power2=evolution_data["power"],
            image=pokemon.image,
            xp=pokemon.xp + 200,
            imgback=pokemon.imgback
        )

        # Set the correct back sprite for the evolved form
        if new_name in EVOLUTION_SPRITE_IDS:
            sid = EVOLUTION_SPRITE_IDS[new_name]
            evolved.sprite_dos = f"assets/spritePokemonDos_PokeAPI/{sid}_{new_name.lower()}_dos.png"
        elif hasattr(pokemon, 'sprite_dos'):
            evolved.sprite_dos = pokemon.sprite_dos

        # Register in session roster so selection screen shows the evolved form
        sprite_id = EVOLUTION_SPRITE_IDS.get(new_name, "1")
        self.evolved_roster[pokemon.nom] = {
            "key": new_name,
            "data": [new_name, evolution_data["type"], evolution_data["power"], evolution_data["defense"], evolution_data["life"]],
            "sprite_id": sprite_id,
        }

        return evolved

    def show_evolution_screen(self, screen, old_name, new_name, old_sprite_path=None):
        """Cinematic evolution animation: flash → white burst → reveal → congratulations."""
        WHITE        = (255, 255, 255)
        YELLOW       = (255, 220, 30)
        PURPLE       = (160, 60, 255)
        LIGHT_PURPLE = (210, 140, 255)

        font_big   = pygame.font.SysFont("arial", 58, bold=True)
        font_med   = pygame.font.SysFont("arial", 40, bold=True)
        font_small = pygame.font.SysFont("arial", 26)

        clock = pygame.time.Clock()

        # Load old Pokemon back sprite
        old_sprite = None
        if old_sprite_path:
            try:
                old_sprite = pygame.image.load(old_sprite_path).convert_alpha()
                old_sprite = pygame.transform.scale(old_sprite, (200, 200))
            except Exception:
                pass

        # Load new Pokemon face sprite
        new_sprite = None
        if new_name in EVOLUTION_SPRITE_IDS:
            sid  = EVOLUTION_SPRITE_IDS[new_name]
            path = f"assets/spritePokemonFace_PokeAPI/{sid}_{new_name.lower()}_face.png"
            try:
                new_sprite = pygame.image.load(path).convert_alpha()
                new_sprite = pygame.transform.scale(new_sprite, (200, 200))
            except Exception:
                pass

        old_sil = _make_silhouette(old_sprite) if old_sprite else None

        # Particles that burst from center during reveal
        particles = [
            {
                "x":     500 + random.randint(-40, 40),
                "y":     300 + random.randint(-40, 40),
                "vx":    math.cos(random.uniform(0, 2 * math.pi)) * random.uniform(2, 7),
                "vy":    math.sin(random.uniform(0, 2 * math.pi)) * random.uniform(2, 7) - 2,
                "size":  random.randint(2, 7),
                "color": random.choice([YELLOW, WHITE, LIGHT_PURPLE, (255, 180, 50)]),
            }
            for _ in range(50)
        ]

        PHASE1 = 90    # Flash / silhouette flicker
        PHASE2 = 120   # Full white burst
        PHASE3 = 180   # New Pokemon reveal
        TOTAL  = 450   # Congratulations (skippable)

        frame   = 0
        running = True

        try:
            pygame.mixer.music.load("assets/song_and_sound/Champion Battle - Pokémon Red_Blue_Yellow Soundtrack.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.15)
        except Exception:
            pass

        while running and frame < TOTAL:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if frame >= PHASE3:
                    if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_ESCAPE):
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        running = False

            # ── Phase 1: Flashing silhouette ──────────────────────────────
            if frame < PHASE1:
                screen.fill((10, 5, 20))

                # Expanding purple aura
                aura_r     = 110 + int(frame * 0.9)
                aura_alpha = int(abs(math.sin(frame * 0.2)) * 100 + 40)
                aura_surf  = pygame.Surface((aura_r * 2, aura_r * 2), pygame.SRCALPHA)
                pygame.draw.ellipse(aura_surf, (*PURPLE, aura_alpha), (0, 0, aura_r * 2, aura_r * 2))
                screen.blit(aura_surf, (500 - aura_r, 300 - aura_r))

                # Flash speed increases over time (classic Gen 1 effect)
                flash_speed = max(2, 18 - frame // 5)
                show_white  = (frame // flash_speed) % 2 == 0

                if old_sprite and old_sil:
                    sprite_to_show = old_sil if show_white else old_sprite
                    screen.blit(sprite_to_show, sprite_to_show.get_rect(center=(500, 300)))

                t_alpha = min(255, frame * 5)
                t = font_med.render(f"{old_name} évolue !", True, YELLOW)
                t.set_alpha(t_alpha)
                screen.blit(t, t.get_rect(center=(500, 540)))

            # ── Phase 2: White burst ──────────────────────────────────────
            elif frame < PHASE2:
                p = (frame - PHASE1) / (PHASE2 - PHASE1)
                screen.fill((10, 5, 20))
                w = pygame.Surface((1000, 700))
                w.fill(WHITE)
                w.set_alpha(int(p * 255))
                screen.blit(w, (0, 0))

            # ── Phase 3: New Pokemon grows from the light ─────────────────
            elif frame < PHASE3:
                p    = (frame - PHASE2) / (PHASE3 - PHASE2)
                bg_v = int((1 - p) * 245)
                screen.fill((bg_v, bg_v, bg_v))

                if new_sprite:
                    scale  = 0.3 + p * 0.7
                    sw, sh = int(200 * scale), int(200 * scale)
                    scaled = pygame.transform.scale(new_sprite, (sw, sh))
                    scaled.set_alpha(min(255, int(p * 400)))
                    screen.blit(scaled, scaled.get_rect(center=(500, 300)))

                # Particles burst outward
                for pt in particles:
                    pt["x"] += pt["vx"]
                    pt["y"] += pt["vy"]
                    pt["vy"] += 0.15
                    a    = max(0, int(p * 220))
                    star = pygame.Surface((pt["size"] * 2, pt["size"] * 2), pygame.SRCALPHA)
                    pygame.draw.circle(star, (*pt["color"], a), (pt["size"], pt["size"]), pt["size"])
                    screen.blit(star, (int(pt["x"] - pt["size"]), int(pt["y"] - pt["size"])))

            # ── Phase 4: Congratulations ──────────────────────────────────
            else:
                p = (frame - PHASE3) / (TOTAL - PHASE3)
                screen.fill((10, 5, 20))

                # Pulsing golden glow behind new sprite
                glow_alpha = int(abs(math.sin(frame * 0.08)) * 80 + 40)
                glow = pygame.Surface((280, 280), pygame.SRCALPHA)
                pygame.draw.ellipse(glow, (*YELLOW, glow_alpha), (0, 0, 280, 280))
                screen.blit(glow, (360, 160))

                if new_sprite:
                    pulse    = 1.0 + math.sin(frame * 0.12) * 0.04
                    pw, ph   = int(200 * pulse), int(200 * pulse)
                    pulsed   = pygame.transform.scale(new_sprite, (pw, ph))
                    screen.blit(pulsed, pulsed.get_rect(center=(500, 280)))

                # Particles slowly fade out
                for pt in particles:
                    pt["x"] += pt["vx"] * 0.2
                    pt["y"] += pt["vy"] * 0.2
                    a    = max(0, int((1 - p) * 180))
                    star = pygame.Surface((pt["size"] * 2, pt["size"] * 2), pygame.SRCALPHA)
                    pygame.draw.circle(star, (*pt["color"], a), (pt["size"], pt["size"]), pt["size"])
                    screen.blit(star, (int(pt["x"] - pt["size"]), int(pt["y"] - pt["size"])))

                t_alpha = min(255, int(p * 400))

                cong = font_big.render("Félicitations !", True, YELLOW)
                cong.set_alpha(t_alpha)
                screen.blit(cong, cong.get_rect(center=(500, 470)))

                evo = font_med.render(f"{old_name}  →  {new_name}", True, LIGHT_PURPLE)
                evo.set_alpha(t_alpha)
                screen.blit(evo, evo.get_rect(center=(500, 540)))

                if p > 0.4:
                    blink = int(abs(math.sin(frame * 0.1)) * 150 + 80)
                    hint  = font_small.render("Appuyez sur ESPACE pour continuer", True, (180, 180, 220))
                    hint.set_alpha(blink)
                    screen.blit(hint, hint.get_rect(center=(500, 640)))

            pygame.display.flip()
            clock.tick(60)
            frame += 1

    def reset_battle_count(self, pokemon_name):
        if pokemon_name in self.battle_count:
            self.battle_count[pokemon_name] = 0

    def get_battle_count(self, pokemon_name):
        return self.battle_count.get(pokemon_name, 0)

    def get_evolution_progress(self, pokemon_name):
        if pokemon_name not in EVOLUTION_DATA:
            return None
        required = EVOLUTION_DATA[pokemon_name]["battles"]
        current  = self.battle_count.get(pokemon_name, 0)
        return min(100, int((current / required) * 100))


evolution_system = EvolutionSystem()
