import sys
import pygame
from pygame.locals import *

screenWidth = 288
screenHeight = 512

pygame.init()
pygame.display.set_caption('Flappy Bird')

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeight))

playerImageList = ['../assets/sprites/redbird-upflap.png',
                   '../assets/sprites/redbird-midflap.png',
                   '../assets/sprites/redbird-downflap.png', ]

background = pygame.image.load('../assets/sprites/background-day.png').convert()

playerList = [pygame.image.load(playerImageList[0]).convert_alpha(),
              pygame.image.load(playerImageList[1]).convert_alpha(),
              pygame.image.load(playerImageList[2]).convert_alpha()]

playerX = int(screenWidth * 0.2)
playerY = int((screenHeight - playerList[0].get_height()) / 2)

loopTime = 0
playerIndex = 0
while True:
    screen.blit(background, (0, 0))

    # if (loopTime + 1) % 5 == 0:
    #     playerIndex = (playerIndex + 1) % 3
    playerIndex = (playerIndex + 1) % 3

    screen.blit(playerList[playerIndex], (playerX, playerY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            playerY = playerY - 20

    pygame.display.update()
    fpsClock.tick(60)
    # loopTime = loopTime + 1
    loopTime = (loopTime + 1) % 30
