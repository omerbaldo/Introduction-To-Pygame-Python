import pygame

class Enemy(pygame.sprite.Sprite): # inherits from this class

    def __init__(self, x, y): #initialization, takes itsself as an arguement
        super().__init__()
        self.image = pygame.image.load("images/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y)) # this is where the enemy will be initialized

    def update(self):
        self.rect.y += 5
        if self.rect.y >= 480: # makes the enemy wrap around the screen when they hit the bottom
            self.rect.y = 0

    def collision(self): # go back to the top
        self.rect.y = 0