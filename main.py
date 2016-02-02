"""
	Dagobert Main file
"""

import pygame
import Grille
import joueur_classe
import os
import HUD

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 1400
screen_height = 910
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode([screen_width, screen_height])
grille = Grille.Grille(20,16,1,screen.subsurface((100,50,1000,800)))

pygame.display.set_caption("Dagobert (the Game) !")
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
joueur = joueur_classe.Joueur("Player 1","humain",1)
joueurIA = joueur_classe.Joueur("Computer","orc",0)
clock = pygame.time.Clock()
hud = HUD.UserInterface(screen,joueur,joueurIA)

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				hud.selectNext()
			elif event.key == pygame.K_q:
				hud.selectPrev()
			elif event.key == pygame.K_UP:
				grille.selectUp()
			elif event.key == pygame.K_DOWN:
				grille.selectDown()
			elif event.key == pygame.K_LEFT:
				grille.selectLeft()
			elif event.key == pygame.K_RIGHT:
				grille.selectRight()
			elif event.key == pygame.K_RETURN:
				if not grille.build(hud.getSelected()):
					print('Construction impossible sur un obstacle')
	# --- Game logic should go here
	screen.fill((75,75,75))
	grille.draw()
	hud.draw()

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
