import pygame


class Batiment:
	tours = [
		{'attPhy': 5, 'attMag': 0, 'distanceAtt': 1, 'prix': 5},
		{'attPhy': 5, 'attMag': 0, 'distanceAtt': 1, 'prix': 10},
		{'attPhy': 5, 'attMag': 0, 'distanceAtt': 1, 'prix': 20},
		{'attPhy': 5, 'attMag': 0, 'distanceAtt': 1, 'prix': 50},
		{'attPhy': 5, 'attMag': 0, 'distanceAtt': 1, 'prix': 75},
		{'attPhy': 5, 'attMag': 0, 'distanceAtt': 1, 'prix': 100}
	]

	def __init__(self, id_tour, equipe, nom):
		self.id_tour = id_tour
		self.equipe = equipe
		self.nom = nom
		self.attPhy = Batiment.tours[id_tour]['attPhy']
		self.attMag = Batiment.tours[id_tour]['attMag']
		self.distanceAtt = Batiment.tours[id_tour]['distanceAtt']
		self.prix = Batiment.tours[id_tour]['prix']
		self.niveau = 0

		sprites = pygame.image.load("images/sprites.png")
		self.image_tour = sprites.subsurface((self.id_tour*60+10,10+self.equipe*60,50,50))
		self.image_niveau = sprites.subsurface((370,10+self.equipe*20,10,10))

	def draw(self,screen):
		screen.blit(self.image_tour,(0,0))
		for i in range(self.niveau):
			screen.blit(self.image_niveau,(20*i,40))



	#Getter et Setter de merde

	#Setter id_tour
	def setId_tour(self,id_tour):
		self.id_tour = id_tour

	#Setter Equipe
	def setEquipe(self,equipe):
		self.equipe = equipe

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
