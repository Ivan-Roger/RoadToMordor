import random
import os
import pygame

CONST_BACK_VIDE = 0
CONST_BACK_FLEUR = 1

CONST_FRONT_VIDE = 0
CONST_FRONT_ROUTE = 1
CONST_FRONT_FORET = 2
CONST_FRONT_ROCHER = 3
CONST_FRONT_BUCHES = 4
CONST_FRONT_TRONC = 5
CONST_FRONT_TOWER_1 = 10
CONST_FRONT_TOWER_2 = 11
CONST_FRONT_TOWER_3 = 12
CONST_FRONT_TOWER_4 = 13
CONST_FRONT_TOWER_5 = 14
CONST_FRONT_TOWER_6 = 15

def creer_grille(x,y):
	grille = list()
	for i in range(x):
		ligne = list()
		grille.append(ligne)
		for i in range(y):
			alea = random.randrange(6)
			if alea == 0:
				ligne.append({'background':CONST_BACK_FLEUR,'front':CONST_FRONT_VIDE})
			else:
				ligne.append({'background':CONST_BACK_VIDE,'front':CONST_FRONT_VIDE})
	return grille

def generer_route(grilleTemp):
	inf = 1
	sup = len(grilleTemp[0])-1
	construc = True
	y = random.randrange(inf,sup)
	x,choix = 0,0

	while construc:
		grilleTemp[x][y]['front'] = CONST_FRONT_ROUTE
		alea = random.randrange(3)
		if alea == 0: #Tout droit
			x+=1
			choix = 0
		elif alea == 1: #En bas
			if y < len(grilleTemp[0])-2 and grilleTemp[x-1][y+1]['front'] != CONST_FRONT_ROUTE and choix != 2:#Si la route peut encore descendre
				y+=1
				choix =1
			else: #Si l'aleatoire a decider de descendre alors que c'est pas possible, on avance
				x+=1
		elif alea == 2: #En haut
			if y > 1 and grilleTemp[x-1][y-1]['front'] != CONST_FRONT_ROUTE and choix != 1: #Si la route peut encore monter
				y-=1
				choix =2
			else: #Si l'aleatoire a decider de monter alors que c'est pas possible, on avance
				x+=1
		if x == len(grilleTemp):
			construc = False

class Grille:

	def __init__(self,rows,cols,count,screen):
		self.selectX = 5
		self.selectY = 3
		self.rows = rows
		self.cols = cols
		self.tile_size = 50
		self.screen = screen
		self.generer_nb_grille(count)
		self.images = {}
		self.images['test'] = pygame.image.load("images/test.png")
		self.images['sprites'] = pygame.image.load("images/sprites.png")
		self.images['herbe'] = {}
		self.images['herbe'][CONST_BACK_VIDE] = self.images['sprites'].subsurface((70,130,50,50))
		self.images['herbe'][CONST_BACK_FLEUR] = self.images['sprites'].subsurface((10,130,50,50))
		self.images['construc'] = {}
		self.images['construc'][CONST_FRONT_ROUTE] = self.images['test']
		self.images['construc'][CONST_FRONT_ROCHER] = self.images['test']
		self.images['construc'][CONST_FRONT_BUCHES] = self.images['sprites'].subsurface((10,190,50,50))
		self.images['construc'][CONST_FRONT_TRONC] = self.images['sprites'].subsurface((70,190,50,50))
		self.images['construc'][CONST_FRONT_FORET] = self.images['sprites'].subsurface((130,190,50,50))
		self.images['construc'][CONST_FRONT_TOWER_1] = self.images['sprites'].subsurface((10,70,50,50))
		self.images['construc'][CONST_FRONT_TOWER_2] = self.images['sprites'].subsurface((70,70,50,50))
		self.images['construc'][CONST_FRONT_TOWER_3] = self.images['sprites'].subsurface((130,70,50,50))
		self.images['construc'][CONST_FRONT_TOWER_4] = self.images['sprites'].subsurface((190,70,50,50))
		self.images['construc'][CONST_FRONT_TOWER_5] = self.images['test']
		self.images['construc'][CONST_FRONT_TOWER_6] = self.images['test']
		self.turn=0

	def draw(self):
		self.turn+=1
		taille = self.tile_size
		# Ajoute notre images a la file des affichages prevus
		for i in range(len(self.grille)):
			for j in range(len(self.grille[0])):
				self.screen.blit(self.images['herbe'][self.grille[i][j]['background']],[i*taille,j*taille])
				if self.grille[i][j]['front'] != CONST_FRONT_VIDE:
					self.screen.blit(self.images['construc'][self.grille[i][j]['front']],[i*taille,j*taille])
				if i == self.selectX and j == self.selectY:
					pygame.draw.rect(self.screen,(200,25,25),(i*taille,j*taille,taille,taille),2+(self.turn/15)%2)

	def generer_nb_grille(self,nb):
		x = self.rows
		y = self.cols
		y/=nb
		self.grille = creer_grille(x,y)
		generer_route(self.grille)
		for i in range(nb-1):
			grilleTemp = creer_grille(x,y)
			generer_route(grilleTemp)
			self.grille = fusion_grille(grilleTemp,self.grille)
		self.generer_foret()
		self.generer_obstacles()

	def generer_foret(self):
		for i in range(len(self.grille)):
			for j in range(len(self.grille[0])):
				alea = random.randrange(10)
				if alea == 1 and self.grille[i][j]['front'] == CONST_FRONT_VIDE:
					self.grille[i][j]['front'] = CONST_FRONT_FORET

	def generer_obstacles(self):
		for i in range(len(self.grille)):
			for j in range(len(self.grille[0])):
				alea = random.randrange(17)
				if alea == 1 and self.grille[i][j]['front'] == CONST_FRONT_VIDE:
					alea = random.randrange(20)
					if alea >= 0 and alea <=5:
						self.grille[i][j]['front'] = CONST_FRONT_ROCHER
					elif alea >= 6 and alea <=10:
						self.grille[i][j]['front'] = CONST_FRONT_BUCHES
					elif alea >= 11 and alea <=13:
						self.grille[i][j]['front'] = CONST_FRONT_TRONC

	def selectLeft(self):
		self.selectX-=1
		if self.selectX<0:
			self.selectX = self.rows-1
	def selectRight(self):
		self.selectX+=1
		if self.selectX>=self.rows:
			self.selectX = 0
	def selectUp(self):
		self.selectY-=1
		if self.selectY<0:
			self.selectY = self.cols-1
	def selectDown(self):
		self.selectY+=1
		if self.selectY>=self.cols:
			self.selectY = 0

	def build(self,batiment):
		if self.grille[self.selectX][self.selectY]['front'] == CONST_FRONT_VIDE:
			self.grille[self.selectX][self.selectY]['front'] = batiment
			return True
		else:
			return False

# --- FIN de la classe Grille ---

# IA function ------------

def nb_case_autour_1(x,y):
	nb = 0
	i = x - 1
	j = y - 1
	while (i <= x + 1 ):
		j = 0
		while (j <= y + 1):
			if grilleTemp[i][j]['front'] == CONST_FRONT_ROUTE:
				nb+=1
			j+=1
		i+=1
	return res

def nb_case_autour_2(x,y):
	nb = 0
	i = x - 2
	j = y - 2
	while (i <= x + 2 ):
		j = 0
		while (j <= y + 2):
			if grilleTemp[i][j]['front'] == CONST_FRONT_ROUTE:
				nb+=1
			j+=1
		i+=1
	return res

def nb_case_autour_3(x,y):
	nb = 0
	i = x - 3
	j = y - 3
	while (i <= x + 3 ):
		j = 0
		while (j <= y + 3):
			if grilleTemp[i][j]['front'] == CONST_FRONT_ROUTE:
				nb+=1
			j+=1
		i+=1
	return res

# Autres ------------
def contenu_grille(grille):
	for i in range(len(grille)):
		for j in range(len(grille[i])):
			print("Aux coordonnees {0},{1} : {2}".format(i,j,grille[i][j]))

def choix_nb_grille(x,y): #il faudrait essayer d'arranger la mochete de boucle for en bas de la fonction
	continuer = True
	while continuer:
		try:
			nb = int(input("Combien voulez-vous de chemin ? (1,2 ou 3)"))
			if nb not in (1,2,3):
				print("Entre 1 et 3 connard !")
			else :
				continuer = False
		except NameError:
			print("Walah c'est pas un nombre gros mongole !")
	return generer_nb_grille(x,y,nb)



def fusion_grille(grille1,grille2):
	res = []
	for i in range(len(grille1)):
		ligne = []
		res.append(ligne)
		for j in range(len(grille1[0])+len(grille2[0])):
			#print("x = {0}, y = {1}".format(i,j))
			if j <= len(grille1[0])-1:
				ligne.append(grille1[i][j])
			else:
				ligne.append(grille2[i][j-len(grille1[0])])

	return res


def afficher_map(grille,taille):
	# Init modules pygames
	pygame.init()

	# Affiche la fenetre
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	size = width, height = len(grille)*taille,len(grille[0])*taille
	screen = pygame.display.set_mode(size)



	# Game loop
	while 1:
	    for event in pygame.event.get():
	    	if event.type == pygame.QUIT:
	    		sys.exit()

		screen.fill((0,0,0))
		# Ajoute notre images a la file des affichages prevus
		for i in range(len(grille)):
			for j in range(len(grille[0])):
				if grille[i][j] == CONST_ROUTE:
					pygame.draw.rect(screen,(255,255,255),[i*taille,j*taille,taille,taille],0)
				elif grille[i][j] == CONST_FORET:
					pygame.draw.rect(screen,(30,109,2),[i*taille,j*taille,taille,taille],0)
				elif grille[i][j] == CONST_ROCHER:
					pygame.draw.rect(screen,(109,109,109),[i*taille,j*taille,taille,taille],0)
					#screen.blit(background_image, [i*20,j*20])

	    # Affiche toute la liste FIFO (ici que notre image de fond)
	    pygame.display.flip()
