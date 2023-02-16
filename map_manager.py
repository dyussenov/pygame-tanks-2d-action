import pygame
from textures_manager import TextureLoader
from game_manager import GameManager


class Map:
    def __init__(self, textures: TextureLoader, window: GameManager):
        self.textures = textures
        self.window = window
        self.map_surface = pygame.Surface(window.size)

    def draw(self):
        pass
