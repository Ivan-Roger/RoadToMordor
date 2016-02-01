import random
import os
import pygame

CONST_ROUTE = 1
CONST_FORET = 2
CONST_ROCHER = 3

def creer_grille(x,y):
	grille = list()
	for i in range(x):
		ligne = list()
		grille.append(ligne)
		for i in range(y):
			ligne.append(0)
	return grille

def generer_route(grilleTemp):
	inf = 1
	sup = len(grilleTemp[0])-1
	construc = True
	y = random.randrange(inf,sup)
	x,choix = 0,0

	while construc:
		grilleTemp[x][y] = CONST_ROUTE
		alea = random.randrange(3)
		if alea == 0: #Tout droit
			x+=1
			choix = 0
		elif alea == 1: #En bas
			if y < len(grilleTemp[0])-2 and grilleTemp[x-1][y+1] != CONST_ROUTE and choix != 2:#Si la route peut encore descendre
				y+=1
				choix =1
			else: #Si l'aleatoire a decider de descendre alors que c'est pas possible, on avance
				x+=1
		elif alea == 2: #En haut
			if y > 1 and grilleTemp[x-1][y-1] != CONST_ROUTE and choix != 1: #Si la route peut encore monter
				y-=1
				choix =2
			else: #Si l'aleatoire a decider de monter alors que c'est pas possible, on avance
				x+=1
		if x == len(grilleTemp):
			construc = False

class Grille:

	def __init__(self,rows,cols,count,screen):
		self.rows = rows
		self.cols = cols
		self.tile_size = 50
		self.screen = screen
		self.generer_nb_grille(count)

	def draw(self):
		taille = self.tile_size
		# Ajoute notre images a la file des affichages prevus
		for i in range(len(self.grille)):
			for j in range(len(self.grille[0])):
				if self.grille[i][j] == CONST_ROUTE:
					pygame.draw.rect(self.screen,(255,255,255),[i*taille,j*taille,taille,taille],0)
				elif self.grille[i][j] == CONST_FORET:
					pygame.draw.rect(self.screen,(30,109,2),[i*taille,j*taille,taille,taille],0)
				elif self.grille[i][j] == CONST_ROCHER:
					pygame.draw.rect(self.screen,(109,109,109),[i*taille,j*taille,taille,taille],0)
					#screen.blit(background_image, [i*20,j*20])

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
		self.generer_rocher()

	def generer_foret(self):
		for i in range(len(self.grille)):
			for j in range(len(self.grille[0])):
				alea = random.randrange(10)
				if alea == 1 and self.grille[i][j] != CONST_ROUTE and self.grille[i][j] != CONST_ROCHER:
					self.grille[i][j] = CONST_FORET

	def generer_rocher(self):
		for i in range(len(self.grille)):
			for j in range(len(self.grille[0])):
				alea = random.randrange(17)
				if alea == 1 and self.grille[i][j] != CONST_ROUTE and self.grille[i][j] != CONST_FORET:
					self.grille[i][j] = CONST_ROCHER

# --- FIN de la classe Grille ---

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
			print("x = {0}, y = {1}".format(i,j))
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
