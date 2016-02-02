import pygame

class Batiment:

		def __init__(self, id_tour,equipe, nom, attPhy, attMag, distanceAtt, prix):
			self.id_tour = id_tour
			self.equipe = equipe
			self.nom = nom
			self.attPhy = attPhy
			self.attMag = attMag
			self.distanceAtt = distanceAtt
			self.prix = prix

			self.image = pygame.image.load("images/sprites.jpg").subsurface((self.id_tour*60+10,70-self.equipe*60,50,50))

		def draw(screen):
			screen.blit(self.image,(0,0))


		#Getter et Setter de merde

		#Setter id_tour
		def setId_tour(id_tour):
			self.id_tour = id_tour

		#Setter Equipe
		def setEquipe(equipe):
			self.equipe = equipe

		#Setter nom
		def setNom(nom):
			self.nom = nom

		#Setter attPhy
		def setAttPhy(attPhy):
			self.attPhy = attPhy

		#Setter attMag
		def setAttMag(attMag):
			self.attMag = attMag

		#Setter distanceAtt
		def setDistanceAtt(distanceAtt):
			self.distanceAtt = distanceAtt

		#Setter prix
		def setprix(prix):
			self.prix = prix

		#Getter id_tour
		def getId_tour():
			return self.id_tour

		#Getter equipe
		def getEquipe():
			return self.equipe

		#Getter nom
		def getNom():
			return self.nom

		#Getter attPhy
		def getAttPhy():
			return self.attPhy

		#Getter attMag
		def getAttMag():
			return self.attMag

		#Getter distanceAtt
		def getDistanceAtt():
			return self.distanceAtt

		#Getter prix
		def getprix():
			return self.prix
