import pygame

class MyShip:

    def __init__(self):
        self.image = pygame.image.load("s.png").convert_alpha()
        self.rect = self.image.get_rect(center=(200,200))