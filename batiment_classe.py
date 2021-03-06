# coding=utf-8

import pygame
import grille_classe

class Batiment:
	stats = [
		{'name': "Tour de garde", 'attPhy': 5, 'attMag': 0, 'attAbs': 0, 'distanceAtt': 1, 'nbCibles': 1, 'prix': 5},
		{'name': "Tour de mages", 'attPhy': 0, 'attMag': 7, 'attAbs': 0, 'distanceAtt': 1, 'nbCibles': 1, 'prix': 10},
		{'name': "Garnison d archers", 'attPhy': 10, 'attMag': 0, 'attAbs': 0, 'distanceAtt': 1, 'nbCibles': 3, 'prix': 20},
		{'name': "Monolithe d invocation", 'attPhy': 0, 'attMag': 15, 'attAbs': 0, 'distanceAtt': 1, 'nbCibles': 3, 'prix': 50},
		{'name': "Cannon longue distance", 'attPhy': 3, 'attMag': 0, 'attAbs': 0, 'distanceAtt': 2, 'nbCibles': 5, 'prix': 75},
		{'name': "Vigie avancee", 'attPhy': 0, 'attMag': 2, 'attAbs': 1, 'distanceAtt': 2, 'nbCibles': 5, 'prix': 100}
	]

	def __init__(self, id_tour, equipe, nom, grille, pos):
		self.pos = pos
		self.grille = grille
		self.id_tour = id_tour
		self.equipe = equipe
		self.nom = nom
		self.attPhy = self.stats[id_tour]['attPhy']
		self.attMag = self.stats[id_tour]['attMag']
		self.attAbs = self.stats[id_tour]['attAbs']
		self.distanceAtt = self.stats[id_tour]['distanceAtt']
		self.nbCibles = self.stats[id_tour]['nbCibles']
		self.prix = self.stats[id_tour]['prix']
		self.niveau = 0

		sprites = pygame.image.load("images/sprites.png")
		self.image_tour = sprites.subsurface((self.id_tour*60+10,10+self.equipe*60,50,50))
		self.image_niveau = sprites.subsurface((370,10+self.equipe*20,10,10))

	def draw(self,screen):
		screen.blit(self.image_tour,(0,0))
		for i in range(self.niveau):
			screen.blit(self.image_niveau,(20*i,40))

	#Getter et Setter de merde

	#Setter nom
	def setNom(self,nom):
		self.nom = nom

	#Setter attPhy
	def setAttPhy(self,attPhy):
		self.attPhy = attPhy

	#Setter attMag
	def setAttMag(self,attMag):
		self.attMag = attMag

	#Setter distanceAtt
	def setDistanceAtt(self,distanceAtt):
		self.distanceAtt = distanceAtt

	#Setter prix
	def setPrix(self,prix):
		self.prix = prix

	#Getter id_tour
	def getId_tour(self):
		return self.id_tour

	#Getter equipe
	def getEquipe(self):
		return self.equipe

	#Getter nom
	def getNom(self):
		return self.nom

	#Getter attPhy
	def getAttPhy(self):
		return self.attPhy

	#Getter attMag
	def getAttMag(self):
		return self.attMag

	#Getter distanceAtt
	def getDistanceAtt(self):
		return self.distanceAtt

	#Getter prix
	def getPrix(self):
		return self.prix

	def getPos(self):
		return self.pos

	def play(self):
		#print('{} - Joue !'.format(self.nom))
		cibleRestantes=self.nbCibles
		#r_x = range(self.pos['x']-self.distanceAtt,2*self.distanceAtt+1)
		for i in range(self.pos['x']-self.distanceAtt,self.pos['x']+self.distanceAtt+1):
			for j in range(self.pos['y']-self.distanceAtt,self.pos['y']+self.distanceAtt+1):
				try:
					if cibleRestantes>0 and self.grille.getGrille()[i][j]['front']==grille_classe.CONST_FRONT_ROUTE and self.grille.getGrille()[i][j]['unit']!=grille_classe.CONST_UNIT_VIDE and self.grille.getGrille()[i][j]['item'].getEquipe()!=self.equipe:
						cibleRestantes-=1
						self.grille.getGrille()[i][j]['item'].subirDegats({'Phy':self.attPhy,'Mag':self.attMag,'Abs':self.attAbs})
				except IndexError:
					pass
