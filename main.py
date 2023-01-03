import pygame
import time

class Rect:
    def __init__(self, top, bottom, left, right, color):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.color = color
    
    def move_down(self, shift):
        self.top += shift
        self.bottom += shift

    def move_right(self, offset):
        self.left += offset
        self.right += offset

    def intersects(self, other):
        return (self.left < other.right and self.right > other.left and
                self.top > other.bottom and self.bottom < other.top)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.left, self.top,
                self.right - self.left, self.bottom - self.top))


width = 500
height = 500
pygame.init()
win = pygame.display.set_mode((width, height))

player_rect = Rect(150, 175, 250, 275, (0, 0, 255))

acc = 1000
vel = 0
jumpVel = -400
h_vel = 400 

level = 0

start_time = time.time()
run = True
while run:
    diff = time.time() - start_time
    print(diff)
    start_time = time.time()

    onGround = False
    player_rect.move_down(vel * diff)
    vel += acc * diff
    if player_rect.bottom >= 240:
        player_rect.move_down(240 - player_rect.bottom)
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
        player_rect.move_right(-h_vel * diff)
    if keys[pygame.K_RIGHT]:
        player_rect.move_right(h_vel * diff)

    win.fill((0, 0, 0))
    player_rect.draw(win)
    pygame.draw.rect(win, (65, 169, 76), (-5, 240, 510, 500))
    pygame.display.update()

    time.sleep(0.02 - (time.time() - start_time))

