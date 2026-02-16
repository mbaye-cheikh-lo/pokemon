import pygame
import pytmx
import pyscroll
import os
from screen import Screen


class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None

        self.switch_map("map0")

    def switch_map(self, map_name: str):
        base_path = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(base_path, "assets", "map", f"{map_name}.tmx")

        print("Chargement de :", path)

        self.tmx_data = pytmx.load_pygame(path)
        map_data = pyscroll.data.TiledMapData(self.tmx_data)

        self.map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data,
            self.screen.get_size()
        )

        self.map_layer.zoom = 1

        self.group = pyscroll.PyscrollGroup(
            map_layer=self.map_layer,
            default_layer=1
        )

        map_width = self.tmx_data.width * self.tmx_data.tilewidth
        map_height = self.tmx_data.height * self.tmx_data.tileheight

        self.group.center((map_width // 2, map_height // 2))

    def update(self):
        self.group.draw(self.screen.get_display())
