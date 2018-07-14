import sys
import pygame
from pygame.locals import *

screenWidth = 288
screenHeight = 512

pygame.init()
pygame.display.set_caption('Flappy Bird')

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeight))

background = pygame.image.load('../assets/sprites/background-day.png').convert()
player = pygame.image.load('../assets/sprites/redbird-upflap.png').convert_alpha()

playerX = int(screenWidth * 0.2)
playerY = int((screenHeight - player.get_height()) / 2)

while True:
    screen.blit(background, (0, 0))
    screen.blit(player, (playerX, playerY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            playerY = playerY - 20

    pygame.display.update()
    fpsClock.tick(60)
