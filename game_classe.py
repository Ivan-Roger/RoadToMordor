# coding=utf-8

import pygame
import grille_classe
import joueur_classe
import os
import HUD

class Game:
    def __init__(self):
        self.paused=False

        # Set the width and height of the screen [width, height]
        self.screen_width = 1400
        self.screen_height = 910
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    def launch(self):
        print('Launching game ...')

        pygame.init()
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        pygame.display.set_caption("Dagobert - Jeu")
        self.clock = pygame.time.Clock()

        self.grille = grille_classe.Grille(16,20,1,self.screen.subsurface((200,50,1000,800)))
        self.joueur = joueur_classe.Joueur("Player 1","humain",1)
        self.joueurIA = joueur_classe.Joueur("Computer","orc",0)
        self.hud = HUD.UserInterface(self.screen,self.joueur,self.joueurIA)

        done = False
        # -------- Main Program Loop -----------
        while not done:
        	# --- Main event loop
        	for event in pygame.event.get():
        		if event.type == pygame.QUIT:
        			done = True
        		elif event.type == pygame.KEYDOWN:
        			if event.unicode == 'd':
        				self.hud.selectNext()
        			elif event.unicode == 'q':
        				self.hud.selectPrev()
        			elif event.unicode == 'a':
        				self.hud.switchMode()
        			elif event.key == pygame.K_ESCAPE:
        				print('MENU')
        			elif event.key == pygame.K_RETURN:
        				if self.hud.getMode()=='towers':
        					if not self.grille.use(self.hud.getSelected(),self.joueur):
        						print('Construction impossible')
        				else:
        					print('Pas tout de suite.')
                elif event.type == pygame.KEYPRESS:
                    if event.key == pygame.K_UP:
        				self.grille.selectUp()
        			elif event.key == pygame.K_DOWN:
        				self.grille.selectDown()
        			elif event.key == pygame.K_LEFT:
        				self.grille.selectLeft()
        			elif event.key == pygame.K_RIGHT:
        				self.grille.selectRight()
        	# --- Game logic should go here
        	self.screen.fill((75,75,75))
        	self.grille.draw()
        	self.hud.draw()

        	# --- Go ahead and update the screen with what we've drawn.
        	pygame.display.flip()

        	# --- Limit to 60 frames per second
        	self.clock.tick(60)

        # Close the window and quit.
        pygame.quit()

        print('Ending game ...')

        return True
