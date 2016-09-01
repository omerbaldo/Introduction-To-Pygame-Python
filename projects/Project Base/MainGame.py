'''
Steps:
    1) import (pygame, sys, locals, objects you want to use)
    2) init pygame
    3) create screen, background image, load image on screen
    4)
'''







import pygame               # imports all modules from pygame
import sys                  # system means file manipulation stuff
from pygame.locals import * # idk
from Player import Player   # import     player class
from Enemy import Enemy     # import the enemy class

pygame.init()               # intitialize pygame modules

'''
Next we create a graphical window with a call to
pygame.display.set_mode(). This represents images
as surface objects. The display.set_mode creates a
new surface object that represents the actual displayed
graphics. The screen shojuld be the same size of the
background image
'''
screen = pygame.display.set_mode((640, 480)) # how big it looks

'''
Alpha in computer graphics, is the proces of combining
an image with a background to create the apperance of
transparency.

Py Game Supports: JPG, PNG, TGA, & GIF
'''
background = pygame.image.load("images/background.png").convert_alpha();



'''
blit draws one image onto another

bit(source, desitination)
destination is a paair of coordinates
which is the upper left corner of the image
'''
screen.blit(background, (0, 0))            # draws background at origin

pygame.display.set_caption('Game Base')    # makes a captian of the window
font = pygame.font.SysFont(None, 36,True,True)       # creates a font object
'''
SysFont(name, size, boolean bold, boolean italic)
'''

player = Player() # Creates a player object
enemy = Enemy(500,100)

enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)


# Grouping sprites
all_group = pygame.sprite.Group()
all_group.add(player)
all_group.add(enemy)


main_clock = pygame.time.Clock()

direction = -1  # 0 is right, 1 is left

# Print out a score
score = 0
font = pygame.font.SysFont(None, 36)

# need to create a score rectange and draw text on it
score_text = font.render('Score: %s' %(score), 1, (0, 0, 0))
score_rect = score_text.get_rect()
score_rect.topleft = (50, 50)


# state for menu, game, gameover ect.

state = 0

while True:
    # check for events
    for event in pygame.event.get(): # these are signals sent from pygame
        if event.type == QUIT:       # if signal is quit, then exit
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()  # returns keys input

    if state == 0:
        '''
        Look at http://www.pygame.org/docs/ref/key.html for key names
        Common ones:
             K_RIGHT, K_LEFT, K_UP, K_DOWN, K_a, K_w ,
        '''
        if keys[K_a]:
            direction = 1
        elif keys[K_d]:
            direction = 0
        else:
            direction = -1

        '''
        The clock keeps track of how much frames per second
        the program is allowed to go. This program is not
        allowed to go past 60 frames a second
        '''
        main_clock.tick(60)

        # Check if enemy collides with the player
        '''
        spritecollide() finds sprites in a group that intersect another sprite
        spritecollide(sprite, group, dokill, collided = None)
        dokill, if set to true, removes collided sprites from group
           this method returns a list contains all sprites in a group
            that intersect with another sprite
        '''
        collide_list = pygame.sprite.spritecollide(player, enemy_group, False, collided = None)
        if len(collide_list) > 0:
            player.subtract_lives()  # loose one life
            for enemy in collide_list:
                enemy.collision()    # call the collision method

        '''
        spritecollide() finds sprites in a group that intersect another sprite
        spritecollide(sprite, group, dokill, collided = None)
        dokill, if set to true, removes collided sprites from group
           this method returns a list contains all sprites in a group
           that intersect with another sprite
        '''

        # print out the score
        score += 10
        score_text = font.render('Score: %s' % (score), 1, (0, 0, 0))
        screen.blit(background, (0, 0))     # update the background
        screen.blit(score_text, score_rect) # put score text on score rectange

        player.update(direction) # call the player object with input
        enemy.update()

        all_group.clear(screen, background)
        all_group.draw(screen)

        if player.get_lives() <= 0:
            state = 1


    elif state == 1:
        if keys[K_RETURN]:
            score = 0
            player.set_lives(3)
            state = 0
        instructions = font.render('Press Enter to play again.', 1, (0, 0, 0))
        instructions_rect = score_rect
        screen.blit(background, (0, 0))
        screen.blit(instructions, instructions_rect)

    pygame.display.update()