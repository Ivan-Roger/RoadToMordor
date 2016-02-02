from unite_classe import *

class Joueur():

	def __init__(self, nom, race, equipe):

		# Nom du joueur
		self.nom = nom
		# Vie du chateau du joueur
		self.vieChateau = 1000
		# Argent du joueur
		self.argent = 100
		# Race du joueur
		self.race = race
		# Equipe du joueur (0 = IA)
		self.equipe = equipe
		# Sprites de la race
		self.sprite = 0

############ Listes des niveaux et des prix d'amelioration
		# Niveau des unites du joueur presentent sur le joueur
		self.niveauUnite = dict(Barbare=1, Archer=1, Magicien=1, Chevalier=1, Paladin=1, Pretre=1)
		# self.niveauTour = dict()
		self.prixAmeliorationUnite = dict(bar1a2=10, bar2a3=10, arc1a2=10, arc2a3=10, mag1a2=10, mag2a3=10, che1a2=10, che2a3=10, pal1a2=10, pal2a3=10, pre1a2=10, pre2a3=10)
		# self.prixAmeliorationTour = dict()

############ Getter

	# Retourne le nom du joueur
	def getNom (self):
		return self.nom

	# Retourne le nombre de point de vies du chateau
	def getVieChateau (self):
		return self.vieChateau

	# Retourne l'argent d'un joueur
	def getArgent (self):
		return self.argent

	# Retourne la race d'un joueur
	def getRace (self):
		return self.race

	# Retourne l'equipe d'un joueur
	def getEquipe (self):
		return self.equipe

	# Retourne les sprites d'un joueur (associés à la race)
	def getSprite (self):
		return self.sprite

############ Setter

	# Modifie le nombre de point de vies du chateau
	def setVieChateau (self, vieChateau):
		return self.vieChateau

	# Modifie l'argent d'un joueur
	def setArgent (self, argent):
		return self.argent

	# Modifie les sprites d'un joueur (associés à la race)
	def setSprite (self, sprite):
		return self.sprite


	def payer (self, montant):
		# Vérifier que le joueur a assez d'argent
		self.setArgent(self.getArgent - montant)

	def recevoir (self, montant):
		# Vérifier que le joueur a assez d'argent
		self.setArgent(self.getArgent + montant)

############### Creation des unites

	# Creer et retourne un objet barbare
	def creationBarbare(self):
		if self.race == 'humain':
			nom = 'Barbare'
		else:
			nom = 'Guerrier Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet archer
	def creationArcher(self):
		if self.race == 'humain':
			nom = 'Archer'
		else:
			nom = 'Archer Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet magicien
	def creationMagicien(self):
		if self.race == 'humain':
			nom = 'Magicien'
		else:
			nom = 'Magicien Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet chevalier
	def creationChevalier(self):
		if self.race == 'humain':
			nom = 'Chevalier'
		else:
			nom = 'Cavalier Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet paladin
	def creationPaladin(self):
		if self.race == 'humain':
			nom = 'Paladin'
		else:
			nom = 'Paladin Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet soigneur
	def creationPretre(self):
		if self.race == 'humain':
			nom = 'Pretre'
		else:
			nom = 'Pretre Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)


############### Amelioration des unites d'un niveau'

	# Ameliore un objet barbare d'un niveau
	def ameliorationBarbare(self, unite):
		if unite.getNom() == 'Barbare' or unite.getNom() == 'Guerrier Orc':
			if self.niveauUnite['Barbare'] == 1:
				payer(self.prixAmeliorationUnite['bar1a2'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Barbare'] = 2
			if self.niveauUnite['Barbare'] == 2:
				payer(self.prixAmeliorationUnite['bar2a3'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Barbare'] = 3


	# Ameliore un objet archer d'un niveau
	def ameliorationArcher(self, unite):
		if unite.getNom() == 'Archer' or unite.getNom() == 'Archer Orc':
			if self.niveauUnite['Archer'] == 1:
				payer(self.prixAmeliorationUnite['arc1a2'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Archer'] = 2
			if self.niveauUnite['Archer'] == 2:
				payer(self.prixAmeliorationUnite['arc2a3'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Archer'] = 3

	# Ameliore un objet magicien d'un niveau
	def ameliorationMagicien(self, unite):
		if unite.getNom() == 'Magicien' or unite.getNom() == 'Magicien Orc':
			if self.niveauUnite['Magicien'] == 1:
				payer(self.prixAmeliorationUnite['mag1a2'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Magicien'] = 2
			if self.niveauUnite['Magicien'] == 2:
				payer(self.prixAmeliorationUnite['mag2a3'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Magicien'] = 3

	# Ameliore un objet chevalier d'un niveau
	def ameliorationChevalier(self, unite):
		if unite.getNom() == 'Chevalier' or unite.getNom() == 'Cavalier Orc':
			if self.niveauUnite['Chevalier'] == 1:
				payer(self.prixAmeliorationUnite['che1a2'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Chevalier'] = 2
			if self.niveauUnite['Chevalier'] == 2:
				payer(self.prixAmeliorationUnite['che2a3'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Chevalier'] = 3

	# Ameliore un objet paladin d'un niveau
	def ameliorationPaladin(self, unite):
		if unite.getNom() == 'Paladin' or unite.getNom() == 'Paladin Orc':
			if self.niveauUnite['Paladin'] == 1:
				payer(self.prixAmeliorationUnite['pal1a2'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Paladin'] = 2
			if self.niveauUnite['Paladin'] == 2:
				payer(self.prixAmeliorationUnite['pal2a3'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Paladin'] = 3

	# Ameliore un objet pretre d'un niveau
	def ameliorationPretre(self, unite):
		if unite.getNom() == 'Pretre' or unite.getNom() == 'Pretre Orc':
			if self.niveauUnite['Pretre'] == 1:
				payer(self.prixAmeliorationUnite['pre1a2'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0)
				self.niveauUnite['Pretre'] = 2
			if self.niveauUnite['Pretre'] == 2:
				payer(self.prixAmeliorationUnite['pre2a3'])
				unite.setVie(unite.getVie() + 15)
				unite.setAttPhy(unite.getAttPhy() + 0)
				unite.setAttMag(unite.getAttMag() + 0)
				unite.setResPhy(unite.getResPhy() + 0)
				unite.setResMag(unite.getResMag() + 0)
				unite.setPrix(unite.getPrix() + 0))
				self.niveauUnite['Pretre'] = 3
