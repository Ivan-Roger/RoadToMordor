"""
	Dagobert Main file
"""

import pygame
import Grille
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
screen_width = 1200
screen_height = 910
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode([screen_width, screen_height])
grille = Grille.Grille(20,16,3,screen.subsurface((50,100,1000,800)))

pygame.display.set_caption("Dagobert (the Game) !")
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
hud = HUD.UserInterface(screen)

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				hud.selectNext()
			elif event.key == pygame.K_LEFT:
				hud.selectPrev()
			elif event.key == pygame.K_UP:
				hud.setLife(100)
			elif event.key == pygame.K_DOWN:
				hud.removeLife(5)
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
