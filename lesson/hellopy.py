import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode([500, 400])
basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render('Hello world!', True, (0, 0, 255))

windowSurface.blit(text, (20, 20))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
