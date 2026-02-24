import pygame
from pokedex import *

show_pokedex()

p1 = get_pokemon("Pikachu")
p2 = get_pokemon("Salameche")

print(p1.name, "VS", p2.name)