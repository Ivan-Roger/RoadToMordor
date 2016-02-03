# coding=utf-8
import pygame

############# Classe mere des unites
class Unite:
	stats = [
		{'vie': 30, 'attPhy': 10, 'attMag': 0, 'distanceAtt': 1, 'resPhy': 2, 'resMag': 0, 'prix': 5},
		{'vie': 30, 'attPhy': 10, 'attMag': 0, 'distanceAtt': 1, 'resPhy': 2, 'resMag': 0, 'prix': 10},
		{'vie': 30, 'attPhy': 10, 'attMag': 0, 'distanceAtt': 1, 'resPhy': 2, 'resMag': 0, 'prix': 20},
		{'vie': 30, 'attPhy': 10, 'attMag': 0, 'distanceAtt': 1, 'resPhy': 2, 'resMag': 0, 'prix': 50},
		{'vie': 30, 'attPhy': 10, 'attMag': 0, 'distanceAtt': 1, 'resPhy': 2, 'resMag': 0, 'prix': 75},
		{'vie': 30, 'attPhy': 10, 'attMag': 0, 'distanceAtt': 1, 'resPhy': 2, 'resMag': 0, 'prix': 100}
	]

	def __init__(self,id_unit, nom, equipe):

		############# Caracteristiques du personnage

		# Nom de l'unite
		self.id_unit = id_unit
		# Nom de l'unite
		self.nom = nom
		# Equipe de l'unite
		self.equipe = equipe
		# Points de vie de l'unite
		self.vie = self.stats[id_unit]['vie']
		# Degats physique
		self.attPhy = self.stats[id_unit]['attPhy']
		# Degats magique
		self.attMag = self.stats[id_unit]['attMag']
		# Distance d'attaque (0 = corps a corps)
		self.distanceAtt = self.stats[id_unit]['distanceAtt']
		# Resistance au degats physique
		self.resPhy = self.stats[id_unit]['resPhy']
		# Resistance au degats magique
		self.resMag = self.stats[id_unit]['resMag']
		# Vitesse de mouvement (1 = vitesse de base)
		self.vitesse = 1
		# Prix de l'unite
		self.prix = self.stats[id_unit]['prix']

		# Joueur auquel il appartient (0 pour l'IA)
		self.equipe = 0

		# Etat du personnage : Attaque, Marche ou Mort
		self.etat = 0
		# Sprite associe a l'etat
		self.sprite = 0

		sprites = pygame.image.load("images/sprites.png")
		self.image_unit = sprites.subsurface((self.id_unit*60+10,370+self.equipe*60,50,50))


	def draw(self,screen):
		screen.blit(self.image_unit,(0,0))


############# Setter

	# Modifie l'id d'une unite
	def setEtat (self, id_unit):
		self.id_unit = id_unit

	# Modifie le sprite courant d'une unite
	def setSprite (self, sprite):
		self.sprite = sprite

	# Modifie la vie d'une unite
	def setVie (self, vie):
		self.vie = vie

	# Modifie l'attaque physique d'une unite
	def setAttPhy (self, attPhy):
		self.attPhy = attPhy

	# Modifie l'attaque magique d'une unite
	def setAttMag (self, attMag):
		self.attMag = attMag

	# Modifie la resistance physique d'une unite
	def setResPhy (self, resPhy):
		self.resPhy = resPhy

	# Modifie la resistance magique d'une unite
	def setResMag (self, resMag):
		self.resMag = resMag

	# Modifie la vitesse d'une unite
	def setVitesse (self,vitesse):
		self.vitesse = vitesse

	# Modifie l'equipe a laquelle appartient une unite
	def setEquipe (self,vitesse):
		self.equipe = equipe

	# Modifie le prix d'une unite
	def setPrix (self,prix):
		self.prix = prix

############# Getter

	# Retourne le nom de l'unite
	def getNom (self):
		return self.nom

	# Retourne l'equipe de  l'unite
	def getEquipe (self):
		return self.equipe

	# Retourne l'etat d'une unite
	def getEtat (self):
		return self.etat

	# Retourne la vie d'une unite
	def getVie (self):
		return self.vie

	# Retourne l'attaque physique d'une unite
	def getAttPhy (self):
		return self.attPhy

	# Retourne l'attaque magique d'une unite
	def getAttMag (self):
		return self.attMag

	# Retourne la resistance physique d'une unite
	def getResPhy (self):
		return self.resPhy

	# Retourne la resistance magique d'une unite
	def getResMag (self):
		return self.resMag

	# Retourne la vitesse d'une unite
	def getVitesse (self):
		return self.vitesse

	# Retourne le prix d'une unite
	def getPrix (self):
		return self.prix

############# Attaque et Dégats

	def subirDegats(self,degats,type_d):
		print('{} - Vie après dégats : {}'.format(self.nom,self.vie))
		if type_d=='Mag':
			self.vie-=(degats-self.resMag)
		elif type_d=='Phy':
			self.vie-=(degats-self.resPhy)
		elif type_d=='Abs':
			self.vie-=degats
		if self.vie<0:
			self.vie=0
			self = None
