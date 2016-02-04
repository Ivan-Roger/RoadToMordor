# coding=utf-8

import unite_classe
import batiment_classe

class Joueur():

	def __init__(self, nom, race, equipe):

		# Nom du joueur
		self.nom = nom
		# Vie maximum du chateau
		self.vieChateauMax = 1000
		# Vie du chateau du joueur
		self.vieChateau = self.vieChateauMax
		# Argent du joueur
		self.argent = 100
		# Race du joueur
		self.race = race
		# Equipe du joueur (0 = IA)
		self.equipe = equipe
		# Sprites de la race
		self.sprite = 0

############ Getter

	# Retourne le nom du joueur
	def getNom (self):
		return self.nom

	# Retourne le nombre de point de vies du chateau
	def getVieChateau (self):
		return self.vieChateau

	def getVieChateauPourcent (self):
		compt = int((float(self.vieChateau)/float(self.vieChateauMax))*100.0)
		if self.vieChateau>0 and compt==0:
			compt=1
		return compt

	# Retourne l'argent d'un joueur
	def getArgent (self):
		return self.argent

	# Retourne la race d'un joueur
	def getRace (self):
		return self.race

	# Retourne l'equipe d'un joueur
	def getEquipe (self):
		return self.equipe

	# Retourne les sprites d'un joueur (associes a la race)
	def getSprite (self):
		return self.sprite

############ Setter

	# Modifie le nombre de point de vies du chateau
	def setVieChateau (self, vieChateau):
		self.vieChateau = vieChateau

	# Modifie l'argent d'un joueur
	def setArgent (self, argent):
		self.argent = argent

	# Modifie les sprites d'un joueur (associes a la race)
	def setSprite (self, sprite):
		self.sprite = sprite

	def payerArgent(self, montant):
		# Verifier que le joueur a assez d'argent
		if (self.getArgent()-montant)<0:
			return False
		self.setArgent(self.getArgent() - montant)
		return True

	def recevoirArgent (self, montant):
		# Verifier que le joueur a assez d'argent
		self.setArgent(self.getArgent() + montant)

	def subirDegats(self,value):
		self.vieChateau-=value
		if self.vieChateau<0:
			self.vieChateau = 0

############### Creation des unites

	# Creer et retourne un objet barbare
	def createUnit(self, id_unit, grille, route):
		if self.equipe==0:
			routePos = len(route)-1
		else:
			routePos = 0
		if self.payerArgent(unite_classe.Unite.stats[id_unit]['prix']):
			nom = ''
			if id_unit == 0:
				if self.race == 'humain':
					nom = 'Barbare'
				else:
					nom = 'Guerrier Orc'
			elif id_unit == 1:
				if self.race == 'humain':
					nom = 'Archer'
				else:
					nom = 'Archer Orc'
			elif id_unit == 2:
				if self.race == 'humain':
					nom = 'Magicien'
				else:
					nom = 'Shaman Orc'
			elif id_unit == 3:
				if self.race == 'humain':
					nom = 'Chevalier'
				else:
					nom = 'Cavalier Orc'
			elif id_unit == 4:
				if self.race == 'humain':
					nom = 'Paladin'
				else:
					nom = 'Paladin Orc'
			elif id_unit == 5:
				if self.race == 'humain':
					nom = 'Pretre'
				else:
					nom = 'Pretre Orc'
			return unite_classe.Unite(id_unit, nom, self.equipe, grille, route, routePos)
		else:
			return False

############### Creation des batiments

	# Creer et retourne un objet batiment
	def createBuild(self,id_bat,grille,pos):
		if self.payerArgent(batiment_classe.Batiment.stats[id_bat]['prix']):
			nom = ''
			if id_bat == 0:
				if self.race == 'humain':
					nom = 'Tour'
				else:
					nom = 'Tour Orc'
			elif id_bat == 1:
				if self.race == 'humain':
					nom = 'Tour'
				else:
					nom = 'Tour Orc'
			elif id_bat == 2:
				if self.race == 'humain':
					nom = 'Tour'
				else:
					nom = 'Tour Orc'
			elif id_bat == 3:
				if self.race == 'humain':
					nom = 'Tour'
				else:
					nom = 'Tour Orc'
			elif id_bat == 4:
				if self.race == 'humain':
					nom = 'Tour'
				else:
					nom = 'Tour Orc'
			elif id_bat == 5:
				if self.race == 'humain':
					nom = 'Tour'
				else:
					nom = 'Tour Orc'
			return batiment_classe.Batiment(id_bat, self.equipe, nom, grille, pos)
		else:
			return False
