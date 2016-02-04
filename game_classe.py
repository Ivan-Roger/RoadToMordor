# coding=utf-8

import pygame
import grille_classe
import unite_classe
import joueur_classe
import ig_menu_classe
import regles_classe
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
		pygame.display.set_caption("Road to Mordor")
		self.clock = pygame.time.Clock()

		self.joueur = joueur_classe.Joueur("Player 1","humain",1)
		self.joueurIA = joueur_classe.Joueur("Computer","orc",0)
		self.hud = HUD.UserInterface(self.screen,self.joueur,self.joueurIA)
		self.grille = grille_classe.Grille(16,20,3,self.screen.subsurface((200,50,1000,800)),self.hud)
		self.ig_menu = ig_menu_classe.InGameMenu(self.screen)
		self.rules = regles_classe.Regles(self.screen)
		turn=0
		done = False
		show_regles = False
		# -------- Main Program Loop -----------
		keys_pressed = dict()
		pygame.event.Event(pygame.USEREVENT,{'key':0,'unicode':''})
		while not done:
			turn+=1
        	# --- Main event loop
			for event in pygame.event.get():
                #print('EVENT ', pygame.event.event_name(event.type))
				if event.type == pygame.QUIT:
					print('Ending game ... and QUIT !')
					return False
				elif event.type == pygame.KEYDOWN:
                    # Create KEYPRESS events
					keys_pressed[event.key] = {'key': event.key, 'unicode': event.unicode}
					if len(keys_pressed)>0:
						pygame.time.set_timer(pygame.USEREVENT,150)
					if self.paused:
						if event.key == pygame.K_RETURN:
							res_m = self.ig_menu.getSelected()
							if res_m == 1:
								show_regles=True
							elif res_m == 2:
								self.paused=False
								print('Ending game ...')
								return True
							else:
								self.paused=False
						elif event.key == pygame.K_ESCAPE:
							if show_regles:
								show_regles=False
							else:
								self.paused=False
						else:
							self.ig_menu.switchSelected()
					else:
	                    # Handle KEYDOWN
						#print('keydown',event.unicode)
						if event.unicode == 'd':
							self.hud.selectNext()
						elif event.unicode == 'q': # Q sur un Azerty
							self.hud.selectPrev()
						elif event.unicode == 'a': # A sur un Azerty
							self.hud.switchMode()
						elif event.unicode == '-':
							print('- HEY !')
						elif event.key == pygame.K_ESCAPE:
							self.paused = True
							# Effet temporaire, a terme cela ouvre
							#   le menu ingame qui permet ensuite de quitter
						elif event.key == pygame.K_UP:
							self.grille.selectUp()
						elif event.key == pygame.K_DOWN:
							self.grille.selectDown()
						elif event.key == pygame.K_LEFT:
							self.grille.selectLeft()
						elif event.key == pygame.K_RIGHT:
							self.grille.selectRight()
						elif event.key == pygame.K_RETURN:
							if self.hud.canUse():
								if self.hud.getMode()=='towers':
									if self.grille.canBuild(self.grille.getSelected()):
										tour = self.joueur.createBuild(self.hud.getSelected(),self.grille.getGrille(),self.grille.getSelected())
										if tour == False:
											self.hud.showMessage("Argent insufisant ...",70)
											print('Argent insufisant')
										else:
											self.grille.place(tour)
											self.hud.use()
									else:
										self.hud.showMessage("Placement impossible !",70)
										print('Placement impossible')
								else:
									if self.grille.canSpawn(self.grille.getRoute()):
										unit = self.joueur.createUnit(self.hud.getSelected(),self.grille.getGrille(),self.grille.getRoute(),0)
										if unit == False:
											self.hud.showMessage("Argent insufisant ...",70)
											print('Argent insufisant')
										else:
											self.grille.place(unit)
											self.hud.use()
									else:
										self.hud.showMessage("Placement impossible !",70)
										print('Placement impossible')
							else:
								self.hud.showMessage("Cooldown en cours.",70)
								print('Cooldown en cours')
				elif event.type == pygame.KEYUP:
					# Create KEYPRESS events
					keys_pressed.pop(event.key)
					if len(keys_pressed)<=0:
						pygame.time.set_timer(pygame.USEREVENT,0)
				elif event.type == pygame.USEREVENT:
					for key,item in keys_pressed.iteritems():
						if key == pygame.K_UP:
							self.grille.selectUp()
						elif key == pygame.K_DOWN:
							self.grille.selectDown()
						elif key == pygame.K_LEFT:
							self.grille.selectLeft()
						elif key == pygame.K_RIGHT:
							self.grille.selectRight()
			# --- Game logic should go here
			#pygame.display.update()
			self.screen.fill((75,75,75))
			if not self.paused:
				self.grille.draw()
				self.hud.draw()
				if turn%10==0:
					self.grille.play()
			else:
				if show_regles:
					self.rules.draw()
				else:
					self.ig_menu.draw()

			# --- Go ahead and update the screen with what we've drawn.
			pygame.display.flip()

			# --- Limit to 60 frames per second
			self.clock.tick(60)

		# Close the window and quit.
		pygame.quit()

		print('Ending game ...')

		return True
