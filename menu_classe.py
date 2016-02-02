# coding=utf-8
import pygame
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
		pygame.display.set_caption("Dagobert - Menu")
		self.clock = pygame.time.Clock()
		#pygame.display.update()

		self.background_image = pygame.image.load("images/back.jpg")

		# -------- Main Program Loop -----------
		done = False
		while not done:
			# --- Main event loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 'QUIT'
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.selectPrev()
					elif event.key == pygame.K_RIGHT:
						self.selectNext()
					elif event.key == pygame.K_RETURN:
						if self.selected==1:
							print('Credits')
						else:
							done = True

        	# --- Game logic should go here
			self.screen.fill((75,75,75))
			self.screen.blit(self.background_image, (0,0))
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
		text = pygame.font.Font("alagard.ttf",50)
		m = text.render("Dagobert",True,(255,255,255))
		j = text.render("Jouer",True,(255,255,255))
		c = text.render("Credit",True,(255,255,255))
		q = text.render("Quitter",True,(255,255,255))

		#Position de hauteur
		jouer_y_off=0
		quit_y_off=0
		credit_y_off=0
		if self.selected==0:
			jouer_y_off=20
		elif self.selected==1:
			credit_y_off=20
		elif self.selected==2:
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
