import pygame

class MenuInterface:

	def __init__(self,screenP):
		self.screen = screenP
		self.background_image = pygame.image.load("images/back.jpg")
		self.jouer_pos = 500
		self.credit_pos = 500
		self.selected = 0


	def draw(self):
		#Creation des texte
		text = pygame.font.Font("alagard.ttf",50)
		m = text.render("Dagobert",True,(255,255,255))
		j = text.render("Jouer",True,(255,255,255))
		c = text.render("Credit",True,(255,255,255))

		#Position de centre
		mpos = m.get_rect()
		mpos.centerx = self.screen.get_rect().centerx
		jpos = j.get_rect()
		jpos.centerx = self.screen.get_rect().centerx
		cpos = c.get_rect()
		cpos.centerx = self.screen.get_rect().centerx

		#Position de hauteur
		jpos[0]-=150
		jpos[1]=self.jouer_pos
		cpos[0]+=150
		cpos[1]=self.credit_pos

		#blit
		self.screen.blit(self.background_image, (0,0))
		self.screen.blit(m,mpos)
		self.screen.blit(j,jpos)
		self.screen.blit(c,cpos)

	def jouer_select(self):
		if self.selected == 0:
			self.jouer_pos-=20
		elif self.selected == 2:
			self.jouer_pos-=20
			self.credit_pos+=20
		self.selected = 1

	def credit_select(self):
		if self.selected == 0:
			self.credit_pos-=20
		elif self.selected == 1:
			self.jouer_pos+=20
			self.credit_pos-=20
		self.selected = 2

	def init(self):
		self.jouer_pos = 500
		self.credit_pos = 500
		self.selected = 0
