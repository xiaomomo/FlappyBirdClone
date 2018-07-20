import sys
import pygame
from pygame.locals import *
import random

screenWidth = 288
screenHeight = 512

pygame.init()
pygame.display.set_caption('Flappy Bird')

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeight))
backgroundImage = pygame.image.load('../assets/sprites/background-day.png').convert()
playerListImage = [pygame.image.load('../assets/sprites/redbird-upflap.png').convert_alpha(),
                   pygame.image.load('../assets/sprites/redbird-midflap.png').convert_alpha(),
                   pygame.image.load('../assets/sprites/redbird-downflap.png').convert_alpha()]
baseImage = pygame.image.load('../assets/sprites/base.png')
pipeListImage = [pygame.transform.rotate(pygame.image.load('../assets/sprites/pipe-red.png').convert_alpha(), 180),
                 pygame.image.load('../assets/sprites/pipe-red.png').convert_alpha()]
wing_sounds = pygame.mixer.Sound('../assets/audio/wing.ogg')
die_sounds = pygame.mixer.Sound('../assets/audio/die.ogg')
playerX = int(screenWidth * 0.2)
playerY = int((screenHeight - playerListImage[0].get_height()) / 2)
basex = 0
basey = int(screenHeight * 0.78)
baseShift = baseImage.get_width() - backgroundImage.get_width()
playerIndex = 0
playerVelY = -9  # player's velocity along Y, default same as playerFlapped
playerMaxVelY = 10  # max vel along Y, max descend speed
playerAccY = 1  # players downward accleration
playerFlapAcc = -9  # players speed on flapping
playerFlapped = False  #

# 管道用两组position渲染，每组四对
pipFirstPositionList = []
initPipX = screenWidth + 100
pipXDistance = 140


def getRandomPipY():
    return random.randrange(-250, -100)


def checkCrash(playerY):
    return playerY > screenHeight-baseImage.get_height()


for index in range(0, 20):
    x = initPipX + index * pipXDistance
    y = getRandomPipY()
    pipFirstPositionList.append([[x, y], [x, y + 450]])

while True:
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

    isCrash = checkCrash(playerY)
    if isCrash:
        die_sounds.play()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

    screen.blit(backgroundImage, (0, 0))
    playerIndex = (playerIndex + 1) % 3
    screen.blit(playerListImage[playerIndex], (playerX, playerY))

    for pipPosition in pipFirstPositionList:
        pipPosition[0][0] = pipPosition[0][0] - 2
        pipPosition[1][0] = pipPosition[1][0] - 2
        screen.blit(pipeListImage[0], (pipPosition[0][0], pipPosition[0][1]))
        screen.blit(pipeListImage[1], (pipPosition[1][0], pipPosition[1][1]))

    basex = -((-basex + 2) % baseShift)
    screen.blit(baseImage, (basex, basey))

    pygame.display.update()
    fpsClock.tick(60)
