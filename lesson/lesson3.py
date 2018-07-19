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

wall = pygame.image.load('../assets/sprites/base.png')

wing_sounds = pygame.mixer.Sound('../assets/audio/wing.ogg')

playerX = int(screenWidth * 0.2)
playerY = int((screenHeight - playerList[0].get_height()) / 2)

wallX = 0
basey = int(screenHeight * 0.78)
baseShift = wall.get_width() - background.get_width()

playerIndex = 0
playerVelY = -9  # player's velocity along Y, default same as playerFlapped
playerMaxVelY = 10  # max vel along Y, max descend speed
playerAccY = 1  # players downward accleration
playerFlapAcc = -9  # players speed on flapping
playerFlapped = False  #
while True:

    # playerY = playerY + 2
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            # 慢慢上升、慢慢下降
            wing_sounds.play()
            playerFlapped = True
            playerVelY = playerFlapAcc

    # player's movement
    if playerVelY < playerMaxVelY and not playerFlapped:
        playerVelY += playerAccY
    if playerFlapped:
        playerFlapped = False
    playerY += playerVelY

    screen.blit(background, (0, 0))

    playerIndex = (playerIndex + 1) % 3
    screen.blit(playerList[playerIndex], (playerX, playerY))

    wallX = -((-wallX + 2) % baseShift)
    print(wallX)
    screen.blit(wall, (wallX, basey))

    pygame.display.update()
    fpsClock.tick(60)
