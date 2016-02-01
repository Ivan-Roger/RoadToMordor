import sys
import pygame
import os

pygame.init()

width = 1200
height = 910

#os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height
screen = pygame.display.set_mode(size)
os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = pygame.time.Clock()


text = pygame.font.SysFont("Arial",50)
t = text.render("TEST",True,(255,255,255))

x = width/2
y = height
done = False
# Boucle de jeu
while not done:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    	    done = True
	print 'g'
	screen.fill((0,0,0))
	y-=1
	screen.blit(t,(x,y))
	pygame.display.flip()
	clock.tick(60)
