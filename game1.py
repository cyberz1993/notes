#small pygame project blocks with collision detection
import pygame, sys, time
from pygame.locals import *


white = (255, 255, 255)
red = (255, 0,0)
green = (0, 255, 0)
blue = (0, 0, 255 )
black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1000, 800))
screen.fill(white)
pygame.display.update()
pygame.key.set_repeat(1, 1)

locationx1 = 60
locationx2 = 120
locationy1 = 60
locationy2 = 60

while True:
    block1 = pygame.draw.line(screen, red, (locationx1, locationy1), (locationx2, locationy2), 60)
    block2 = pygame.draw.line(screen, blue, (800, 100), (860, 100), 60)
    pygame.display.update()
    time.sleep(0.01)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and (locationx2 not in range(800, 921) or locationy2 not in range(39, 161)):
                locationy1 += 1
                locationy2 += 1
            elif event.key == pygame.K_UP and (locationx2 not in range(800, 921) or locationy2 not in range(39, 161)):
                locationy1 -= 1
                locationy2 -= 1
            elif event.key == pygame.K_LEFT and (locationx2 not in range(800, 921) or locationy2 not in range(40, 160)):
                locationx1 -= 1
                locationx2 -= 1
            elif event.key == pygame.K_RIGHT and (locationx2 not in range(799, 860) or locationy2 not in range(39, 160)):
                locationx1 += 1
                locationx2 += 1
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
