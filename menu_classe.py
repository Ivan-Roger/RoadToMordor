# coding=utf-8

import pygame
import credits_classe
import os

class Menu:
	def __init__(self):

		# Set the width and height of the screen [width, height]
		self.screen_width = 900
		self.screen_height = 500
		os.environ['SDL_VIDEO_CENTERED'] = '1'


		self.selected = 0

	def launch(self):
		print('Launching menu ...')

		pygame.init()
		self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
		pygame.display.set_caption("Road to Mordor")
		DagobertIcon = pygame.Surface((64,64))
		text = pygame.font.Font("alagard.ttf",64)
		DagobertIcon.fill((0,0,0))
		DagobertIcon.convert()
		DagobertIcon.blit(text.render("D",True,(0,255,255)),(12,4))
		pygame.display.set_icon(DagobertIcon)
		self.clock = pygame.time.Clock()
		#pygame.display.update()

		self.credits = credits_classe.Credits(self.screen)
		self.background_image = pygame.image.load("images/back.jpg")

		# -------- Main Program Loop -----------
		showCredits = False
		credits_finis = True
		done = False
		while not done:
			# --- Main event loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 'QUIT'
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						if credits_finis:
							self.selectPrev()
					elif event.key == pygame.K_RIGHT:
						if credits_finis:
							self.selectNext()
					elif event.key == pygame.K_ESCAPE:
						if self.selected==1:
							credits_finis = True
					elif event.key == pygame.K_RETURN:
						if credits_finis:
							if self.selected==1:
								showCredits = True
								credits_finis = False
								self.credits.reset()
							else:
								done = True

        	# --- Game logic should go here
			self.screen.fill((75,75,75))
			self.screen.blit(self.background_image, (0,0))
			if showCredits and not credits_finis:
				credits_finis = self.credits.draw()
			else:
				self.draw()
			# --- Go ahead and update the screen with what we've drawn.
			pygame.display.flip()
			# --- Limit to 10 frames per second
        	self.clock.tick(10)

		# Close the window and quit.
		pygame.quit()

		print('Ending menu ...')

		return ['PLAY','ERROR','QUIT'][self.selected]

	def draw(self):
		#Creation des texte
		textS = pygame.font.Font("alagard.ttf",40)
		text = pygame.font.Font("alagard.ttf",50)
		m = text.render("Road to Mordor",True,(255,255,255))
		j = textS.render("Jouer",True,(180,180,180))
		c = textS.render("Credit",True,(180,180,180))
		q = textS.render("Quitter",True,(180,180,180))

		#Position de hauteur
		jouer_y_off=0
		quit_y_off=0
		credit_y_off=0
		if self.selected==0:
			j = text.render("Jouer",True,(255,255,255))
			jouer_y_off=20
		elif self.selected==1:
			c = text.render("Credit",True,(255,255,255))
			credit_y_off=20
		elif self.selected==2:
			q = text.render("Quitter",True,(255,255,255))
			quit_y_off=20

		self.screen.blit(m,(self.screen.get_rect().centerx-(m.get_rect().width/2),50))
		self.screen.blit(j,(self.screen.get_rect().centerx-(j.get_rect().width/2)-250, 250-jouer_y_off))
		self.screen.blit(c,(self.screen.get_rect().centerx-(c.get_rect().width/2), 250-credit_y_off))
		self.screen.blit(q,(self.screen.get_rect().centerx-(q.get_rect().width/2)+250, 250-quit_y_off))

	def selectPrev(self):
		self.selected-=1
		if self.selected<0:
			self.selected=2

	def selectNext(self):
		self.selected+=1
		if self.selected>=3:
			self.selected=0
