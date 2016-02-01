import sys
import pygame
import os

pygame.init()

#os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# Boucle de jeu
while 1:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    	    sys.exit()
