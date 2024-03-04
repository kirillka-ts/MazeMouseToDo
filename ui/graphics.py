import pygame

import settings
from ui import screen

Image = pygame.Surface
flip = pygame.display.flip


def fill(color):
    screen.fill(color)


# принимает размеры картинки в координатах лабиринта
def load_image(path, size=(1, 1)):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (size[0] * settings.tile_size[0], size[1] * settings.tile_size[1]))


# клиенты будут передавать координаты лабиринта
def draw_image(image, x, y):
    """Здесь нужен pygame blit с пересчетом на settings.tile_size"""
    pass


# клиенты будут передавать координаты лабиринта
def draw_circle(color, x, y, r):
    #print("Здесь нужен pygame draw.circle с пересчетом на settings.tile_size")
    pass

