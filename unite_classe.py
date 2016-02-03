############# Classe mere des unites
class Unite:

	def __init__(self,id_unit, nom, equipe, vie, attPhy, attMag, distanceAtt, resPhy, resMag, prix):

############# Caracteristiques du personnage

		# Nom de l'unite
		self.id_unit = id_unit
		# Nom de l'unite
		self.nom = nom
		# Equipe de l'unite
		self.equipe = equipe
		# Points de vie de l'unite
		self.vie = vie
		# Degats physique
		self.attPhy = attPhy
		# Degats magique
		self.attMag = attMag
		# Distance d'attaque (0 = corps a corps)
		self.distanceAtt = distanceAtt
		# Resistance au degats physique
		self.resPhy = resPhy
		# Resistance au degats magique
		self.resMag = resMag
		# Vitesse de mouvement (1 = vitesse de base)
		self.vitesse = 1
		# Prix de l'unite
		self.prix = prix

		# Joueur auquel il appartient (0 pour l'IA)
		self.equipe = 0

		# Etat du personnage : Attaque, Marche ou Mort
		self.etat = 0
		# Sprite associe a l'etat
		self.sprite = 0

		sprites = pygame.image.load("images/guignol.png")
		self.image_unit = sprites.subsurface((self.id_unit*60+10,10+self.equipe*60,50,50))


	def draw(self,screen):
		screen.blit(self.image_unit,(0,0))


############# Setter

	# Modifie l'id d'une unite
	def setEtat (self, id_unit):
		self.id_unit = id_unit

	# Modifie l'etat d'une unite
	def setEtat (self, etat):
		self.etat = etat

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
		return self.id_unit

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
