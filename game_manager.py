import pygame


class WindowException(Exception):
    def __str__(self):
        return "The window must be a multiple of the size"


class GameManager:
    def __init__(
            self,
            window_height: int,
            window_width: int,
            tile_size: int,
            window_title: str,

    ):
        pygame.init()
        self.set_window_size(window_height, window_width, tile_size)
        self.game_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(window_title)

    def set_window_size(self, height: int, width: int, tile_size: int):
        if height//tile_size and width//tile_size:
            self.width = width
            self.height = height
            self.size = (width, height)
        else:
            raise WindowException
