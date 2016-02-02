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
		self.niveauUnite = dict(barbare=1, archer=1, magicien=1, chevalier=1, paladin=1, soigneur=1)
		# self.niveauTour = dict()
		self.prixAmeliorationUnite = dict(bar1a2=10, bar2a3=10, arc1a2=10, arc2a3=10, mag1a2=10, mag2a3=10, che1a2=10, che2a3=10, pal1a2=10, pal2a3=10, soi1a2=10, soi2a3=10)
		# self.prixAmeliorationTour = dict()

############### Creation des unites

	# Creer et retourne un objet barbare
	def creationBarbare(self):
		if race == 'humain':
			nom = 'Barbare'
		else:
			nom = 'Guerrier Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet archer
	def creationArcher(self):
		if race == 'humain':
			nom = 'Archer'
		else:
			nom = 'Archer Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet magicien
	def creationMagicien(self):
		if race == 'humain':
			nom = 'Magicien'
		else:
			nom = 'Magicien Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet chevalier
	def creationChevalier(self):
		if race == 'humain':
			nom = 'Chevalier'
		else:
			nom = 'Cavalier Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet paladin
	def creationPaladin(self):
		if race == 'humain':
			nom = 'Paladin'
		else:
			nom = 'Paladin Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)

	# Creer et retourne un objet soigneur
	def creationSoigneur(self):
		if race == 'humain':
			nom = 'Pretre'
		else:
			nom = 'Pretre Orc'
		return Unite(nom, self.equipe, 30, 10, 0, 0, 2, 0, 5)


	############### Amelioration des unites de niveau 1 a 2

	# Ameliore un objet barbare au niveau 2
	def ameliorationBarbare1a2(self, unite):
		if unite.getNom() == 'barbare':
			unite.setVie(unite.getVie() + 15)
			unite.setAttPhy(unite.getAttPhy() + 0)
			unite.setAttMag(unite.getAttMag() + 0)
			unite.setResPhy(unite.getResPhy() + 0)
			unite.setResMag(unite.getResMag() + 0)
			unite.setPrix(unite.getPrix() + 0)

	# Ameliore un objet archer au niveau 2
	def ameliorationArcher1a2(self, unite):
		if unite.getNom() == 'archer':
			unite.setVie(unite.getVie() + 0)
			unite.setAttPhy(unite.getAttPhy() + 0)
			unite.setAttMag(unite.getAttMag() + 0)
			unite.setResPhy(unite.getResPhy() + 0)
			unite.setResMag(unite.getResMag() + 0)
			unite.setPrix(unite.getPrix() + 0)

	# Ameliore un objet magicien au niveau 2
	def ameliorationMagicien1a2(self, unite):
		if unite.getNom() == 'magicien':
			unite.setVie(unite.getVie() + 0)
			unite.setAttPhy(unite.getAttPhy() + 0)
			unite.setAttMag(unite.getAttMag() + 0)
			unite.setResPhy(unite.getResPhy() + 0)
			unite.setResMag(unite.getResMag() + 0)
			unite.setPrix(unite.getPrix() + 0)

	# Ameliore un objet chevalier au niveau 2
	def ameliorationChevalier1a2(self, unite):
		if unite.getNom() == 'chevalier':
			unite.setVie(unite.getVie() + 0)
			unite.setAttPhy(unite.getAttPhy() + 0)
			unite.setAttMag(unite.getAttMag() + 0)
			unite.setResPhy(unite.getResPhy() + 0)
			unite.setResMag(unite.getResMag() + 0)
			unite.setPrix(unite.getPrix() + 0)

	# Ameliore un objet paladin au niveau 2
	def ameliorationPaladin1a2(self, unite):
		if unite.getNom() == 'paladin':
			unite.setVie(unite.getVie() + 0)
			unite.setAttPhy(unite.getAttPhy() + 0)
			unite.setAttMag(unite.getAttMag() + 0)
			unite.setResPhy(unite.getResPhy() + 0)
			unite.setResMag(unite.getResMag() + 0)
			unite.setPrix(unite.getPrix() + 0)

	# Ameliore un objet soigneur au niveau 2
	def ameliorationSoigneur1a2(self, unite):
		if unite.getNom() == 'soigneur':
			unite.setVie(unite.getVie() + 0)
			unite.setAttPhy(unite.getAttPhy() + 0)
			unite.setAttMag(unite.getAttMag() + 0)
			unite.setResPhy(unite.getResPhy() + 0)
			unite.setResMag(unite.getResMag() + 0)
			unite.setPrix(unite.getPrix() + 0)
