import pygame
import Grille

class UserInterface:
	""" Classe pour l'interface utilisateur """
	def __init__(self,screenP, joueur1, joueur2):
		self.selected = 0
		self.balance = 500
		self.screen = screenP
		self.joueur1 = joueur1
		self.joueur2 = joueur2
		self.images = {}
		self.images['test'] = pygame.image.load("images/test.png")
		self.images['coinsSprites'] = pygame.image.load("images/coin.png")
		self.images['coins'] = {}
		self.images['coins'][0] = self.images['coinsSprites'].subsurface((7,7,50,50))
		self.images['coins'][1] = self.images['coinsSprites'].subsurface((61,7,50,50))
		self.images['coins'][2] = self.images['coinsSprites'].subsurface((114,7,50,50))
		self.images['coins'][3] = self.images['coinsSprites'].subsurface((168,7,50,50))
		self.images['coins'][4] = self.images['coinsSprites'].subsurface((221,7,50,50))
		self.images['coins'][5] = self.images['coinsSprites'].subsurface((274,7,50,50))
		self.images['coins'][6] = self.images['coinsSprites'].subsurface((327,7,50,50))
		self.images['coins'][7] = self.images['coinsSprites'].subsurface((381,7,50,50))
		self.images['sprites'] = pygame.image.load("images/sprites.png")
		self.images['towers'] = {}
		self.images['towers'][0] = self.images['sprites'].subsurface((10,70,50,50))
		self.images['towers'][1] = self.images['sprites'].subsurface((70,70,50,50))
		self.images['towers'][2] = self.images['sprites'].subsurface((130,70,50,50))
		self.images['towers'][3] = self.images['sprites'].subsurface((190,70,50,50))
		self.images['towers'][4] = self.images['test']
		self.images['towers'][5] = self.images['test']
		self.turn = 0

	def draw(self):
		self.turn+=1
		screenRect = self.screen.get_rect()
		# Fond de l'interface du haut
		pygame.draw.rect(self.screen,(200,200,200),(0,0,screenRect[2],50),0)

		# Contour barre de vie
		pygame.draw.rect(self.screen,(225,50,50),(10,10,200,30),1)
		# Barre de vie
		pygame.draw.rect(self.screen,(225,100,100),(10,10,-2*self.lifePercent,30),0)
		# Texte du % de vie
		text = pygame.font.SysFont('Calibiri', 25, False, False).render(str(self.lifePercent)+"%",True,(25,25,25))
		self.screen.blit(text, [95, 15])

		# Image pieces
		self.screen.blit(self.images['coins'][(self.turn/5)%8],(240,0))

		# Nombre de pieces
		text = pygame.font.SysFont('Calibiri', 40, False, False).render(str(self.balance),True,(25,25,25))
		self.screen.blit(text, [325, 10])

		# Barre de selection
		pygame.draw.rect(self.screen,(200,200,200),(200,screenRect[3]-60,800,60),0)
		for i in range(0,6):
			x_pos = (i*50)+225+(i*50)
			y_off = 5 if i == self.selected else 0
			self.screen.blit(self.images['towers'][i],(x_pos,screenRect[3]-(50+y_off)))

	def selectNext(self):
		self.selected+=1
		if self.selected>=6:
			self.selected=0

	def selectPrev(self):
		self.selected-=1
		if self.selected<0:
			self.selected=5

	def getSelected(self):
		return self.selected+10

	def setLife(self,value):
		self.lifePercent = value

	def getLife(self):
		return self.lifePercent

	def setBalance(self,value):
		self.balance = value

	def getBalance(self):
		return self.balance

	def removeLife(self,value):
		self.lifePercent-=value
		if self.lifePercent < 0:
			self.lifePercent = 0
