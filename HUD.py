import pygame
import Grille

class UserInterface:
	""" Classe pour l'interface utilisateur """
	def __init__(self,screenP, joueur1, joueur2):
		self.selected = 0
		self.balance = 500
		self.screen = screenP
		self.turn = 0
		self.mode = 'towers'
		self.joueur1 = joueur1
		self.joueur2 = joueur2
		self.images = {}
		self.images['test'] = pygame.image.load("images/test.png")
		self.images['sprites'] = pygame.image.load("images/sprites.png")
		self.images['coinsSprites'] = pygame.image.load("images/coin.png")

		self.images['coins'] = {}
		self.images['coins'][0] = self.images['sprites'].subsurface((10,310,50,50))
		self.images['coins'][1] = self.images['sprites'].subsurface((70,310,50,50))
		self.images['coins'][2] = self.images['sprites'].subsurface((130,310,50,50))
		self.images['coins'][3] = self.images['sprites'].subsurface((190,310,50,50))
		self.images['coins'][4] = self.images['sprites'].subsurface((250,310,50,50))
		self.images['coins'][5] = self.images['sprites'].subsurface((310,310,50,50))
		self.images['coins'][6] = self.images['sprites'].subsurface((370,310,50,50))
		self.images['coins'][7] = self.images['sprites'].subsurface((430,310,50,50))

		self.images['towers'] = {}
		self.images['towers'][0] = self.images['sprites'].subsurface((10,70,50,50))
		self.images['towers'][1] = self.images['sprites'].subsurface((70,70,50,50))
		self.images['towers'][2] = self.images['sprites'].subsurface((130,70,50,50))
		self.images['towers'][3] = self.images['sprites'].subsurface((190,70,50,50))
		self.images['towers'][4] = self.images['sprites'].subsurface((250,70,50,50))
		self.images['towers'][5] = self.images['sprites'].subsurface((310,70,50,50))

		self.images['units'] = {}
		self.images['units'][0] = self.images['test']
		self.images['units'][1] = self.images['test']
		self.images['units'][2] = self.images['test']
		self.images['units'][3] = self.images['test']
		self.images['units'][4] = self.images['test']
		self.images['units'][5] = self.images['test']
		#self.lifePercent = 62

	def draw(self):
		self.turn+=1
		screenRect = self.screen.get_rect()
		# Fond de l'interface du haut
		pygame.draw.rect(self.screen,(200,200,200),(0,0,screenRect[2],50),0)

		# Contour barre de vie
		pygame.draw.rect(self.screen,(25,59,128),(10,10,200,30),1)
		# Barre de vie
		pygame.draw.rect(self.screen,(45,106,229),(10,10,2*self.joueur1.getVieChateauPourcent(),30),0)
		# Texte du % de vie
		text = pygame.font.Font('alagard.ttf', 25).render(str(self.joueur1.getVieChateauPourcent())+"%",True,(25,25,25))
		self.screen.blit(text, [95, 15])

		# Contour barre de vie
		pygame.draw.rect(self.screen,(149,0,0),(1190,10,-200,30),1)
		# Barre de vie
		pygame.draw.rect(self.screen,(193,46,26),(1190,10,-2*self.joueur2.getVieChateauPourcent(),30),0)
		# Texte du % de vie
		text = pygame.font.Font('alagard.ttf', 25).render(str(self.joueur2.getVieChateauPourcent())+"%",True,(25,25,25))
		self.screen.blit(text, [1070, 15])

		# Image pieces
		self.screen.blit(self.images['coins'][(self.turn/5)%8],(240,0))

		# Nombre de pieces
		text = pygame.font.Font('alagard.ttf', 40).render(str(self.joueur1.getArgent()),True,(25,25,25))
		self.screen.blit(text, [290, 10])

		# Barre de selection
		pygame.draw.rect(self.screen,(200,200,200),(0,screenRect[3]-60,screenRect[2],60),0)
		for i in range(0,6):
			x_pos = (i*50)+225+(i*50)
			y_off = 5 if i == self.selected else 0
			self.screen.blit(self.images[self.mode][i],(x_pos,screenRect[3]-(50+y_off)))

	def selectNext(self):
		self.selected+=1
		if self.selected>=6:
			self.selected=0

	def selectPrev(self):
		self.selected-=1
		if self.selected<0:
			self.selected=5

	def switchMode(self):
		if self.mode=='towers':
			self.mode='units'
		else:
			self.mode='towers'

	def getMode(self):
		return self.mode

	def getSelected(self):
		return self.selected

	def removeLife(self,value):
		self.lifePercent-=value
		if self.lifePercent < 0:
			self.lifePercent = 0
