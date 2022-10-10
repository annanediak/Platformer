import pygame
import time

print("""

  SONIC    SONIC    SONIC    SONIC    SONIC
   THE      THE      THE      THE      THE
HEDGEHOG HEDGEHOG HEDGEHOG HEDGEHOG HEDGEHOG

""")

width = 500
height = 500
pygame.init()
win = pygame.display.set_mode((width, height))

xPlayer = 250
yPlayer = 150
pside = 25

acc = 1000
vel = 0
jumpVel = -400
h_vel = 1242.5

score = 0

start_time = time.time()
run = True
while run:
    print(xPlayer)
    diff = time.time()-start_time
    print(diff)
    start_time = time.time()

    onGround = False
    yPlayer += vel * diff
    vel += acc * diff
    if yPlayer >= 240:
        yPlayer = 240
        vel = 0
        onGround = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if onGround:
                    vel = jumpVel
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xPlayer -= h_vel * diff 
    if keys[pygame.K_RIGHT]:
        xPlayer += h_vel * diff 

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (xPlayer, yPlayer, pside, pside))
    pygame.draw.rect(win, (65, 169, 76), (-5, 265, 510, 500))
    pygame.display.update()

    time.sleep(0.02 - (time.time() - start_time))
