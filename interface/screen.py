import pygame

class Screen:
    def __init__(self):
        self.display=pygame.display.set_mode((960,640))
        pygame.display.set_caption("Pokemon")
        self.clock=pygame.time.Clock()
        self.framerate=60

    def update(self):
        self.display.fill((0,0,0))
        pygame.display.flip()
        self.clock.tick(self.framerate)

    def get_size(self):
        return self.display.get_size()
    def get_display(self):
        return self.display