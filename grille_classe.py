import random
import os
import pygame
import batiment_classe

CONST_BACK_VIDE = 0
CONST_BACK_FLEUR = 1

CONST_FRONT_VIDE = 0
CONST_FRONT_ROUTE = 1
CONST_FRONT_FORET = 2
CONST_FRONT_ROCHER = 3
CONST_FRONT_BUCHES = 4
CONST_FRONT_TRONC = 5

CONST_FRONT_BAT = 9

"""
CONST_FRONT_TOWER_1 = 10
CONST_FRONT_TOWER_2 = 11
CONST_FRONT_TOWER_3 = 12
CONST_FRONT_TOWER_4 = 13
CONST_FRONT_TOWER_5 = 14
CONST_FRONT_TOWER_6 = 15

CONST_FRONT_TOWER_IA_1 = 20
CONST_FRONT_TOWER_IA_2 = 21
CONST_FRONT_TOWER_IA_3 = 22
CONST_FRONT_TOWER_IA_4 = 23
CONST_FRONT_TOWER_IA_5 = 24
CONST_FRONT_TOWER_IA_6 = 25
"""

def creer_grille(x,y):
	grille = list()
	for i in range(x):
		ligne = list()
		grille.append(ligne)
		for i in range(y):
			alea = random.randrange(6)
			if alea == 0:
				ligne.append({'background':CONST_BACK_FLEUR,'front':CONST_FRONT_VIDE, 'orientation':0})
			else:
				ligne.append({'background':CONST_BACK_VIDE,'front':CONST_FRONT_VIDE, 'orientation':0})
	return grille

def generer_route(grilleTemp):
	inf = 1
	sup = len(grilleTemp[0])-1
	construc = True
	y = random.randrange(inf,sup)
	x,choix = 0,0
	orion = [0]
	route = []
	while construc:
		route.append([x,y])
		grilleTemp[x][y]['front'] = CONST_FRONT_ROUTE
		alea = random.randrange(3)
		if alea == 0: #Tout droit
			x+=1
			choix = 0
			orion.append(0)
		elif alea == 1: #En bas
			if y < len(grilleTemp[0])-2 and grilleTemp[x-1][y+1]['front'] != CONST_FRONT_ROUTE and choix != 2:#Si la route peut encore descendre
				y+=1
				choix =1
				orion.append(1)
			else: #Si l'aleatoire a decider de descendre alors que c'est pas possible, on avance
				x+=1
				orion.append(0)
		elif alea == 2: #En haut
			if y > 1 and grilleTemp[x-1][y-1]['front'] != CONST_FRONT_ROUTE and choix != 1: #Si la route peut encore monter
				y-=1
				choix =2
				orion.append(2)
			else: #Si l'aleatoire a decider de monter alors que c'est pas possible, on avance
				x+=1
				orion.append(0)
		if x == len(grilleTemp):
			construc = False

	for ind,c in enumerate(route):
		try:
			if orion[ind+1] ==0:
				if orion[ind] == 0:
					grilleTemp[c[0]][c[1]]['orientation'] = 0
				elif orion[ind] == 1:
					grilleTemp[c[0]][c[1]]['orientation'] = 4
				elif orion[ind] == 2:
					grilleTemp[c[0]][c[1]]['orientation'] = 2
			elif orion[ind+1] == 1:
				if orion[ind] == 0:
					grilleTemp[c[0]][c[1]]['orientation'] = 3
				elif orion[ind] == 1:
					grilleTemp[c[0]][c[1]]['orientation'] = 1
			elif orion[ind+1] == 2:
				if orion[ind] == 0:
					grilleTemp[c[0]][c[1]]['orientation'] = 5
				elif orion[ind] == 2:
					grilleTemp[c[0]][c[1]]['orientation'] = 1
		except IndexError:
			pass


class Grille:

	def __init__(self,rows,cols,count,screen):
		self.selectX = 5
		self.selectY = 3
		self.rows = rows
		self.cols = cols
		self.tile_size = 50
		self.screen = screen
		self.generer_nb_grille(count)
		self.turn=0

		self.images = {}
		self.images['test'] = pygame.image.load("images/test.png")
		self.images['sprites'] = pygame.image.load("images/sprites.png")

		self.images['herbe'] = {}
		self.images['herbe'][CONST_BACK_VIDE] = self.images['sprites'].subsurface((70,130,50,50))
		self.images['herbe'][CONST_BACK_FLEUR] = self.images['sprites'].subsurface((10,130,50,50))

		self.images['construc'] = {}
		self.images['construc'][CONST_FRONT_ROUTE] = self.images['test']
		self.images['construc'][CONST_FRONT_ROCHER] = self.images['sprites'].subsurface((190,190,50,50))
		self.images['construc'][CONST_FRONT_BUCHES] = self.images['sprites'].subsurface((10,190,50,50))
		self.images['construc'][CONST_FRONT_TRONC] = self.images['sprites'].subsurface((70,190,50,50))
		self.images['construc'][CONST_FRONT_FORET] = self.images['sprites'].subsurface((130,190,50,50))

		self.images['routes'] = {}
		self.images['routes'][0] = self.images['sprites'].subsurface((10+60*0,250,50,50))
		self.images['routes'][1] = self.images['sprites'].subsurface((10+60*1,250,50,50))
		self.images['routes'][2] = self.images['sprites'].subsurface((10+60*2,250,50,50))
		self.images['routes'][3] = self.images['sprites'].subsurface((10+60*3,250,50,50))
		self.images['routes'][4] = self.images['sprites'].subsurface((10+60*4,250,50,50))
		self.images['routes'][5] = self.images['sprites'].subsurface((10+60*5,250,50,50))

	def draw(self):
		self.turn+=1
		taille = self.tile_size
		# Ajoute notre images a la file des affichages prevus
		for i in range(len(self.grille)):
			for j in range(len(self.grille[0])):
				self.screen.blit(self.images['herbe'][self.grille[i][j]['background']],[i*taille,j*taille])

				if self.grille[i][j]['front'] == CONST_FRONT_BAT:
					self.grille[i][j]['batiment'].draw(self.screen.subsurface((i*taille,j*taille,taille,taille)))
				elif self.grille[i][j]['front'] == CONST_FRONT_ROUTE:
					self.screen.blit(self.images['routes'][self.grille[i][j]['orientation']],[i*taille,j*taille])
				elif self.grille[i][j]['front'] != CONST_FRONT_VIDE:
					self.screen.blit(self.images['construc'][self.grille[i][j]['front']],[i*taille,j*taille])

				if i == self.selectX and j == self.selectY:
					if (self.turn/15)%2==0:
						pygame.draw.rect(self.screen,(45,106,229),pygame.Rect(i*taille,j*taille,taille-1,taille-1),2)
					else:
						pygame.draw.rect(self.screen,(45,106,229),pygame.Rect(i*taille,j*taille,taille,taille),1)

	def generer_nb_grille(self,nb):
		x = self.cols
		y = self.rows
		y/=nb
		self.grille = creer_grille(x,y)
		generer_route(self.grille)
		for i in range(nb-1):
			grilleTemp = creer_grille(x,y)
			generer_route(grilleTemp)
			self.grille = fusion_grille(grilleTemp,self.grille)
		self.generer_foret()
		self.generer_obstacles()
		for i in range(10):
			self.generer_tour()

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
			self.selectX = self.cols-1
	def selectRight(self):
		self.selectX+=1
		if self.selectX>=self.cols:
			self.selectX = 0
	def selectUp(self):
		self.selectY-=1
		if self.selectY<0:
			self.selectY = self.rows-1
	def selectDown(self):
		self.selectY+=1
		if self.selectY>=self.rows:
			self.selectY = 0

	def canBuild(self):
		return self.grille[self.selectX][self.selectY]['front'] == CONST_FRONT_VIDE and self.selectX<=self.cols/2

	def build(self,tour):
		if self.canBuild():
			self.grille[self.selectX][self.selectY]['front'] = CONST_FRONT_BAT
			self.grille[self.selectX][self.selectY]['batiment'] = tour
			return True
		else:
			return False

	# IA function ------------

	def nb_tour(self):
		nb = 0
		for i in range((len(self.grille)/2)+1,len(self.grille)):
			for j in range(len(self.grille[0])):
				if (self.grille[i][j] == CONST_FRONT_TOWER_IA_1 or self.grille[i][j] == CONST_FRONT_TOWER_IA_2 or self.grille[i][j] == CONST_FRONT_TOWER_IA_3 or self.grille[i][j] == CONST_FRONT_TOWER_IA_4 or self.grille[i][j] == CONST_FRONT_TOWER_IA_5 or self.grille[i][j] == CONST_FRONT_TOWER_IA_6):
					nb+=1
		return nb

	def nb_case_autour(self,radius,x,y):
		nb = 0
		i = x - radius
		while (i <= x + radius):
			j = y - radius
			while (j <= y + radius):
				#print("case en cours : {2},{3}  case de base : {0},{1}".format(i,j,x,y))
				try:
					if self.grille[i][j]['front'] == CONST_FRONT_ROUTE:
						nb+=1
				except IndexError:
					continue
				finally:
					j+=1
			i+=1
		return nb

	def generer_tour(self):
		temp_i, temp_j, max1, nbcase = 0,0,0,0
		for i in range((len(self.grille)/2)+1,len(self.grille)):
			for j in range(len(self.grille[0])):
				if self.grille[i][j]['front'] == CONST_FRONT_VIDE:
					nbcase = self.nb_case_autour(1,i,j)
					if (nbcase > max1):
						max1 = nbcase
						temp_i = i
						temp_j = j
				#print("i: {0} j:{1} nb {2} max {3}".format(i,j,nbcase,max1))
		self.grille[temp_i][temp_j]['front'] = CONST_FRONT_BAT
		self.grille[temp_i][temp_j]['batiment'] = batiment_classe.Batiment(0,0,"Tour IA")
		# Faire payer l'IA
		#joueur.payer(self.grille[temp_i][temp_j]['batiment'].getPrix())
# --- FIN de la classe Grille ---

# Autres ------------

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
