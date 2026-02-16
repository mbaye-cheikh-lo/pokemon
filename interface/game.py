import pygame
from screen import Screen
from map import Map

class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.map = Map(self.screen)
        self.running = True

    def run(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.get_display().fill((0, 0, 0))

            self.map.update()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
