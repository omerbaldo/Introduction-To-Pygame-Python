
#The final example code below.

import pygame
import random
import math
import sys
from ship import MyShip
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 640))
font = pygame.font.SysFont(None, 36)

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))

screen.fill((255, 255, 255))

ship = MyShip()

ship_image_list = []

initial_rotation = 0

for x in range (0, 8):
    temp_image = pygame.transform.rotate(ship.image, initial_rotation)
    initial_rotation += 45
    ship_image_list.append(temp_image)

speed_one_dir = 15
speed = [speed_one_dir, speed_one_dir]
rot_image = 4
x_pos = 200
y_pos = 200

#Could you figure out the speed directions?
def check_rotation():
    global speed
    global rot_image
    if rot_image is 0:
        speed = [speed_one_dir, -speed_one_dir]
    elif rot_image is 7:
        speed = [speed_one_dir, 0]
    elif rot_image is 6:
        speed = [speed_one_dir, speed_one_dir]
    elif rot_image is 5:
        speed = [0, speed_one_dir]
    elif rot_image is 4:
        speed = [-speed_one_dir, speed_one_dir]
    elif rot_image is 3:
        speed = [-speed_one_dir, 0]
    elif rot_image is 2:
        speed = [-speed_one_dir, -speed_one_dir]
    elif rot_image is 1:
        speed = [0, -speed_one_dir]

ship.image = ship_image_list[rot_image]
main_clock = pygame.time.Clock()
timer = 0

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        x_pos += speed[0]
        y_pos += speed[1]
    timer += main_clock.tick(50)
    if timer > 30:
        if keys[K_a]:
            if rot_image < 7:
                rot_image += 1
            else:
                rot_image = 0
        if keys[K_d]:
            if rot_image > 0:
                rot_image -= 1
            else:
                rot_image = 7
        timer = 0

    check_rotation()
    ship.image = ship_image_list[rot_image]
    ship.rect = ship_image_list[rot_image].get_rect(center=(x_pos, y_pos))

    main_clock.tick(50)
    screen.fill((255, 255, 255))
    screen.blit(ship.image, ship.rect.topleft)
    pygame.display.update()