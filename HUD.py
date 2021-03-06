# coding=utf-8

import pygame
import grille_classe
import batiment_classe
import unite_classe

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
		self.messages = list()
		self.fontSmall = pygame.font.Font('alagard.ttf', 15)
		self.font = pygame.font.Font('alagard.ttf', 25)
		self.fontBig = pygame.font.Font('alagard.ttf', 40)
		self.fontTitle = pygame.font.Font('alagard.ttf', 50)
		self.images = {}
		self.images['test'] = pygame.image.load("images/test.png")
		self.images['sprites'] = pygame.image.load("images/sprites.png")

		self.images['mur'] = self.images['sprites'].subsurface((520,310,5,50))
		self.images['herbe'] = self.images['sprites'].subsurface((70,130,50,50))
		self.images['terre'] = self.images['sprites'].subsurface((190,130,50,50))

		self.images['chateau'] = {}
		self.images['chateau'][0] = self.images['sprites'].subsurface((600,10,200,290))
		self.images['chateau'][1] = self.images['sprites'].subsurface((390,10,200,290))

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
		self.images['units'][0] = self.images['sprites'].subsurface((10,430,50,50))
		self.images['units'][1] = self.images['sprites'].subsurface((70,430,50,50))
		self.images['units'][2] = self.images['sprites'].subsurface((130,430,50,50))
		self.images['units'][3] = self.images['sprites'].subsurface((190,430,50,50))
		self.images['units'][4] = self.images['sprites'].subsurface((250,430,50,50))
		self.images['units'][5] = self.images['sprites'].subsurface((310,430,50,50))

		self.selectT = {}
		self.selectT['towers'] = {}
		self.selectT['towers'][0] = 0
		self.selectT['towers'][1] = 0
		self.selectT['towers'][2] = 0
		self.selectT['towers'][3] = 0
		self.selectT['towers'][4] = 0
		self.selectT['towers'][5] = 0

		self.selectT['units'] = {}
		self.selectT['units'][0] = 0
		self.selectT['units'][1] = 0
		self.selectT['units'][2] = 0
		self.selectT['units'][3] = 0
		self.selectT['units'][4] = 0
		self.selectT['units'][5] = 0

	def draw(self):
		self.turn+=1
		self.tick()
		screenRect = self.screen.get_rect()
		# Fond de l'interface du haut
		pygame.draw.rect(self.screen,(200,200,200),(0,0,screenRect[2],50),0)

		# Contour barre de vie
		pygame.draw.rect(self.screen,(25,59,128),(10,10,200,30),1)
		# Barre de vie
		pygame.draw.rect(self.screen,(45,106,229),(10,10,2*self.joueur1.getVieChateauPourcent(),30),0)
		# Texte du % de vie
		text = self.font.render(str(self.joueur1.getVieChateauPourcent())+"%",True,(25,25,25))
		self.screen.blit(text, [95, 15])

		# Contour barre de vie
		pygame.draw.rect(self.screen,(149,0,0),(1400,10,-200,30),1)
		# Barre de vie
		pygame.draw.rect(self.screen,(193,46,26),(1400,10,-2*self.joueur2.getVieChateauPourcent(),30),0)
		# Texte du % de vie
		text = self.font.render(str(self.joueur2.getVieChateauPourcent())+"%",True,(25,25,25))
		self.screen.blit(text, [1280, 15])

		# Nom du Jeu
		text = self.fontTitle.render("Road to Mordor",True,(75,75,75))
		self.screen.blit(text, [(self.screen.get_rect().width/2)-(text.get_rect().width/2), 0])

		# Image pieces
		self.screen.blit(self.images['coins'][(self.turn/5)%8],(210,0))

		# Nombre de pieces
		text = self.fontBig.render(str(self.joueur1.getArgent()),True,(25,25,25))
		self.screen.blit(text, [260, 10])

		# Chateau gauche
		for i in range(4):
			for j in range(16):
				self.screen.blit(self.images['herbe'],(50*i,50+50*j))
		for y in range(16):
				self.screen.blit(self.images['mur'],(200,50+50*y))
		self.screen.blit(self.images['chateau'][0],(0,50+400-self.images['chateau'][0].get_rect().centery))
		# Chateau droit
		for i in range(4):
			for j in range(16):
				self.screen.blit(self.images['terre'],(1210+50*i,50+50*j))
		for y in range(16):
				self.screen.blit(self.images['mur'],(1205,50+50*y))
		self.screen.blit(self.images['chateau'][1],(1210,50+400-self.images['chateau'][1].get_rect().centery))

		# Affichage des messages
		ind=0
		for val in self.messages:
			self.screen.blit(self.fontSmall.render(val['msg'],True,(0,0,0)),(10,80+ind*15))
			val['time']-=1
			if val['time'] == 0:
				self.messages.remove(val)
			ind+=1

		# Barre de selection
		pygame.draw.rect(self.screen,(200,200,200),(0,screenRect[3]-60,screenRect[2],60),0)
		for i in range(0,6):
			x_pos = (i*50)+225+(i*50)
			y_off = 5 if i == self.selected else 0
			if i == self.selected:
				if (self.turn/15)%2==0:
					pygame.draw.rect(self.screen,(25,59,128),(x_pos,screenRect[3]-(y_off),60,5),0)
				else:
					pygame.draw.rect(self.screen,(45,106,229),(x_pos,screenRect[3]-(y_off),60,5),0)
			self.screen.blit(self.images[self.mode][i],(x_pos,screenRect[3]-(50+y_off)))
			h_val = self.selectT[self.mode][i]/2
			pygame.draw.rect(self.screen,(45,106,229),(x_pos+55,screenRect[3]-y_off,5,-h_val),0)

		# Infos sur la séléction
		if self.mode=='towers':
			name = batiment_classe.Batiment.stats[self.selected]['name']
			prix = batiment_classe.Batiment.stats[self.selected]['prix']
			attPhy = batiment_classe.Batiment.stats[self.selected]['attPhy']
			attMag = batiment_classe.Batiment.stats[self.selected]['attMag']
			attAbs = batiment_classe.Batiment.stats[self.selected]['attAbs']
			nbCibles = batiment_classe.Batiment.stats[self.selected]['nbCibles']
			distanceAtt = batiment_classe.Batiment.stats[self.selected]['distanceAtt']
			details=''
			if attPhy>0:
				details += ( " / " if len(details)>0 else "" )
				details += "Phy "+str(attPhy)
			if attMag>0:
				details += ( " / " if len(details)>0 else "" )
				details += "Mag "+str(attMag)
			if attAbs>0:
				details += ( " / " if len(details)>0 else "" )
				details += "Abs "+str(attAbs)
			details+= " / Rad "+str(distanceAtt)
			details+= " / Nb "+str(nbCibles)
		else:
			name = unite_classe.Unite.stats[self.selected]['name']
			prix = unite_classe.Unite.stats[self.selected]['prix']
			attPhy = unite_classe.Unite.stats[self.selected]['attPhy']
			attMag = unite_classe.Unite.stats[self.selected]['attMag']
			distanceAtt = unite_classe.Unite.stats[self.selected]['distanceAtt']
			details=''
			if attPhy>0:
				details += ( " / " if len(details)>0 else "" )
				details += "Phy "+str(attPhy)
			if attMag>0:
				details += ( " / " if len(details)>0 else "" )
				details += "Mag "+str(attMag)
			details+= " / Rad "+str(distanceAtt)
		self.screen.blit(self.font.render(name,True,(25,25,25)),(875,855))
		self.screen.blit(self.fontSmall.render("Cout : "+str(prix),True,(50,50,50)),(875,880))
		self.screen.blit(self.fontSmall.render(details,True,(50,50,50)),(875,895))

	def tick(self):
		for i in range(6):
			if (self.selectT['towers'][i]>0):
				self.selectT['towers'][i]-=1
			if (self.selectT['units'][i]>0):
				self.selectT['units'][i]-=1

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

	def showMessage(self,message,time):
		self.messages.append({'msg': message, 'time': time})

	def getMode(self):
		return self.mode

	def canUse(self):
		return self.selectT[self.mode][self.selected]==0

	def getSelected(self):
		return self.selected

	def use(self):
		if self.canUse():
			self.selectT[self.mode][self.selected] = 100
			return True
		else:
			return False
