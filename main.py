import pygame
import time

from classes import *
from levels import levels

width = 500
height = 500
pygame.init()
win = pygame.display.set_mode((width, height))

acc = 1000
vel = 0
jumpVel = -400
h_vel = 200 

level = 0

player_rect = Rect(levels[level].start_y,
                   levels[level].start_y + 25,
                   levels[level].start_x,
                   levels[level].start_x + 25,
                   (255, 0, 0))

start_time = time.time()
run = True
while run:
    diff = time.time() - start_time
    start_time = time.time()

    player_rect.move_down(vel * diff)
    vel += acc * diff

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.move_right(-h_vel * diff)
    if keys[pygame.K_RIGHT]:
        player_rect.move_right(h_vel * diff)

    player_status, on_ground, abuntahead = levels[level].update_player(player_rect)
    if player_status == 1:
        level += 1
        if level == len(levels):
            print("Congrats! You beat the game!")
            break
    elif player_status == 2:
        print("You hit lava. Try not to do that.")
    elif player_status == 3:
        print("You got cRuShEd and mUsHeD to death.")
    if player_status != 0:
        player_rect = Rect(levels[level].start_y,
                           levels[level].start_y + 25,
                           levels[level].start_x,
                           levels[level].start_x + 25,
                           (255, 0, 0))

    if on_ground and vel > 0:
        vel = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if on_ground:
                    vel = jumpVel
    if abuntahead and vel < 0:
        vel = 0

    if player_rect.right <= 0 or player_rect.left >= 500:
        player_rect = Rect(levels[level].start_y,
                           levels[level].start_y + 25,
                           levels[level].start_x,
                           levels[level].start_x + 25,
                           (255, 0, 0))

    win.fill((0, 0, 0))
    levels[level].draw(win)
    player_rect.draw(win)
    pygame.display.update()

    time.sleep(0.02 - (time.time() - start_time))

