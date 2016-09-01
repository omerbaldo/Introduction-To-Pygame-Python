import pygame

class Player(pygame.sprite.Sprite): # inherits from this class

    def __init__(self):#initialization, takes itsself as an arguement
        super().__init__()
        # these three lines create lives rect and image
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(300, 380)) # init x and y
        self.lives = 3

    def update(self, direction):
        if direction == 1:
            self.rect.x -= 5
        elif direction == 0:
            self.rect.x += 5

    def subtract_lives(self):
        if self.lives > 0:
            self.lives -= 1

    def get_lives(self):
        return self.lives

    def set_lives(self, lives_count):
        self.lives = lives_count