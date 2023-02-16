import pygame
import json


class TextureLoader:
    def __init__(self, file_path: str, textures_path: str):
        self.file_path = file_path
        self.textures_path = textures_path

    def load_from_json(self):
        with open(self.file_path, "r") as file:
            json_data = json.load(file)
            print(json_data)
            for attr, value in json_data.items():
                self.__setattr__(attr, pygame.image.load(self.textures_path + value))

    def load_from_csv(self):
        pass