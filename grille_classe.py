# coding=utf-8

import random
import os
import pygame
import HUD
import batiment_classe
import unite_classe

CONST_BACK_VIDE = 0
CONST_BACK_FLEUR = 1
CONST_BACK_OBS_VIDE = 2
CONST_BACK_OBS_LAVA = 3

CONST_FRONT_VIDE = 0
CONST_FRONT_ROUTE = 1
CONST_FRONT_FORET = 2
CONST_FRONT_ROCHER = 3
CONST_FRONT_BUCHES = 4
CONST_FRONT_TRONC = 5

CONST_FRONT_BAT = 9

CONST_UNIT_VIDE = 0
CONST_UNIT_USED = 1

class Grille:

	def __init__(self,rows,cols,count,screen,hud):
		self.selectX = 5
		self.selectY = 3
		self.selectR = 0
		self.hud = hud
		self.rows = rows
		self.cols = cols
		self.tile_size = 50
		self.routes = list()
		self.batiments = list()
		self.units = list()
		self.screen = screen
		self.generer_nb_grille(count)
		self.turn=0
		self.images = {}
		self.images['test'] = pygame.image.load("images/test.png")
		self.images['sprites'] = pygame.image.load("images/sprites.png")

		self.images['selector'] = self.images['sprites'].subsurface((370,250,20,20))

		self.images['back'] = {}
		self.images['back'][CONST_BACK_VIDE] = self.images['sprites'].subsurface((70,130,50,50))
		self.images['back'][CONST_BACK_FLEUR] = self.images['sprites'].subsurface((10,130,50,50))
		self.images['back'][CONST_BACK_OBS_VIDE] = self.images['sprites'].subsurface((190,130,50,50))
		self.images['back'][CONST_BACK_OBS_LAVA] = self.images['sprites'].subsurface((130,130,50,50))

		self.images['front'] = {}
		self.images['front'][CONST_FRONT_ROUTE] = self.images['test']
		self.images['front'][CONST_FRONT_ROCHER] = self.images['sprites'].subsurface((190,190,50,50))
		self.images['front'][CONST_FRONT_BUCHES] = self.images['sprites'].subsurface((10,190,50,50))
		self.images['front'][CONST_FRONT_TRONC] = self.images['sprites'].subsurface((70,190,50,50))
		self.images['front'][CONST_FRONT_FORET] = self.images['sprites'].subsurface((130,190,50,50))

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
		for i in range(len(self.grille)):
			for j in range(len(self.grille[0])):
				# Dessin de l'arrière plan
				self.screen.blit(self.images['back'][self.grille[i][j]['background']],[i*taille,j*taille])

				# Dessin de l'avant plan
				if self.grille[i][j]['front'] == CONST_FRONT_BAT:
					self.grille[i][j]['item'].draw(self.screen.subsurface((i*taille,j*taille,taille,taille)))
				elif self.grille[i][j]['front'] == CONST_FRONT_ROUTE:
					self.screen.blit(self.images['routes'][self.grille[i][j]['orientation']],[i*taille,j*taille])
				elif self.grille[i][j]['front'] != CONST_FRONT_VIDE:
					self.screen.blit(self.images['front'][self.grille[i][j]['front']],[i*taille,j*taille])

				# Dessin des unités
				if self.grille[i][j]['unit'] != CONST_UNIT_VIDE:
					self.grille[i][j]['item'].draw(self.screen.subsurface((i*taille,j*taille,taille,taille)))

				# Dessin de la séléction
				if self.hud.getMode() == 'towers' and i == self.selectX and j == self.selectY:
					if (self.turn/15)%2==0:
						pygame.draw.rect(self.screen,(45,106,229),pygame.Rect(i*taille,j*taille,taille-1,taille-1),2)
					else:
						pygame.draw.rect(self.screen,(45,106,229),pygame.Rect(i*taille,j*taille,taille,taille),1)
		if self.hud.getMode()=='units':
			self.screen.blit(self.images['selector'],(0,self.routes[self.selectR][0]['y']*50+15))

	def creer_grille(self,x,y):
		grille = list()
		for i in range(x):
			ligne = list()
			grille.append(ligne)
			for i in range(y):
				alea = random.randrange(6)
				if alea == 0:
					ligne.append({'background':CONST_BACK_FLEUR, 'front':CONST_FRONT_VIDE, 'orientation':0, 'unit': CONST_UNIT_VIDE, 'item': None})
				else:
					ligne.append({'background':CONST_BACK_VIDE, 'front':CONST_FRONT_VIDE, 'orientation':0, 'unit': CONST_UNIT_VIDE, 'item': None})
		return grille

	def generer_route(self,grilleTemp,id_route,cols,rows):
		inf = 1
		sup = len(grilleTemp[0])-1
		construc = True
		y = random.randrange(inf,sup)
		x,choix = 0,0
		orion = [0]
		route = []
		while construc:
			route.append({'x':x,'y':y})
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
						grilleTemp[c['x']][c['y']]['orientation'] = 0
					elif orion[ind] == 1:
						grilleTemp[c['x']][c['y']]['orientation'] = 4
					elif orion[ind] == 2:
						grilleTemp[c['x']][c['y']]['orientation'] = 2
				elif orion[ind+1] == 1:
					if orion[ind] == 0:
						grilleTemp[c['x']][c['y']]['orientation'] = 3
					elif orion[ind] == 1:
						grilleTemp[c['x']][c['y']]['orientation'] = 1
				elif orion[ind+1] == 2:
					if orion[ind] == 0:
						grilleTemp[c['x']][c['y']]['orientation'] = 5
					elif orion[ind] == 2:
						grilleTemp[c['x']][c['y']]['orientation'] = 1
			except IndexError:
				pass
		self.routes.append(route)
		for ind in range(len(self.routes[id_route])):
			self.routes[id_route][ind]['y'] += id_route*rows

	def generer_nb_grille(self,nb):
		x = self.cols
		y = self.rows
		y/=nb
		self.grille = self.creer_grille(x,y)
		self.generer_route(self.grille,0,x,y)
		for i in range(1,nb):
			grilleTemp = self.creer_grille(x,y)
			self.generer_route(grilleTemp,i,x,y)
			self.grille = fusion_grille(self.grille,grilleTemp)
		self.generer_obstacles()
		self.generer_mal()

	def generer_obstacles(self):
		for i in range(len(self.grille)/2):
			for j in range(len(self.grille[0])):
				alea = random.randrange(7)
				if alea == 1 and self.grille[i][j]['front'] == CONST_FRONT_VIDE:
					alea = random.randrange(30)
					if alea >= 0 and alea <=10:
						self.grille[i][j]['front'] = CONST_FRONT_BUCHES
					elif alea >= 11 and alea <=13:
						self.grille[i][j]['front'] = CONST_FRONT_TRONC
					elif alea >= 14 and alea <=29:
						self.grille[i][j]['front'] = CONST_FRONT_FORET
		for i in range(len(self.grille)):
			for j in range(len(self.grille[0])):
				alea = random.randrange(12)
				if alea == 1 and self.grille[i][j]['front'] == CONST_FRONT_VIDE:
					alea = random.randrange(10)
					if alea >= 0 and alea <=5:
						self.grille[i][j]['front'] = CONST_FRONT_ROCHER


	def generer_mal(self):
		for i in range(len(self.grille)/2,len(self.grille)):
			for j in range(len(self.grille[0])):
				alea = random.randrange(4)
				if alea == 0 and self.grille[i][j]['front'] == CONST_FRONT_VIDE:
					self.grille[i][j]['background'] = CONST_BACK_OBS_LAVA
				else:
					self.grille[i][j]['background'] = CONST_BACK_OBS_VIDE


	def selectLeft(self):
		if self.hud.getMode() == 'towers':
			self.selectX-=1
			if self.selectX<0:
				self.selectX = self.cols-1
		else:
			self.selectR-=1
			if self.selectR<0:
				self.selectR = len(self.routes)-1
	def selectRight(self):
		if self.hud.getMode() == 'towers':
			self.selectX+=1
			if self.selectX>=self.cols:
				self.selectX = 0
		else:
			self.selectR+=1
			if self.selectR>=len(self.routes):
				self.selectR = 0
	def selectUp(self):
		if self.hud.getMode() == 'towers':
			self.selectY-=1
			if self.selectY<0:
				self.selectY = self.rows-1
		else:
			self.selectR-=1
			if self.selectR<0:
				self.selectR = len(self.routes)-1
	def selectDown(self):
		if self.hud.getMode() == 'towers':
			self.selectY+=1
			if self.selectY>=self.rows:
				self.selectY = 0
		else:
			self.selectR+=1
			if self.selectR>=len(self.routes):
				self.selectR = 0

	def canUse(self):
		if self.hud.getMode() == 'towers':
			return self.grille[self.selectX][self.selectY]['front'] == CONST_FRONT_VIDE and self.selectX<=self.cols/2
		else:
			return self.grille[self.routes[self.selectR][0]['x']][self.routes[self.selectR][0]['y']]['unit'] == CONST_UNIT_VIDE

	def canBuild(self,pos):
		return self.grille[pos['x']][pos['y']]['front'] == CONST_FRONT_VIDE and pos['x']<self.cols/2

	def canSpawn(self,road):
		return self.grille[road[0]['x']][road[0]['y']]['unit'] == CONST_UNIT_VIDE

	def place(self,item):
		if item.__class__.__name__ == 'Batiment':
			if self.canBuild(item.getPos()):
				self.grille[self.selectX][self.selectY]['front'] = CONST_FRONT_BAT
				self.grille[self.selectX][self.selectY]['item'] = item
				self.batiments.append(item)
				return True
			else:
				return False
		else:
			if self.canSpawn(item.getRoute()):
				self.grille[self.routes[self.selectR][0]['x']][self.routes[self.selectR][0]['y']]['unit'] = CONST_UNIT_USED
				self.grille[self.routes[self.selectR][0]['x']][self.routes[self.selectR][0]['y']]['item'] = item
				self.units.append(item)
				return True
			else:
				return False

	def getSelected(self):
		return {'x': self.selectX, 'y': self.selectY}

	def getGrille(self):
		return self.grille

	def getRoute(self):
		return self.routes[self.selectR]

	def play(self):
		for val in self.batiments:
			val.play()
		for val in self.units:
			val.play()



	def fin_route(self,x,y,nb):
		route = self.routes[nb]
		if route[len(route)-1]["x"] == x and route[len(route)-1]["y"] == y:
			return True
		else:
			return False

	def debut_route(self,x,y,nb):
		route = self.routes[nb]
		if route[0]["x"] == x and route[0]["y"] == y:
			return True
		else:
			return False

	def route_vide(self,x,y,nb):
		if self.grille[coor["x"]][coor["y"]]["unit"] == CONST_UNIT_USED:
			return Fasle
		else:
			return True
	""" # Ancienne méthode pour faire avancer les unitées
	def avancer_unit(self):
		nb_route = 0
		#deplacement gentil
		for route in self.routes:
			i  = len(route)-1
			while i >= 0:
				if not self.debut_route(route[i]["x"],route[i]["y"],nb_route):
					if self.grille[route[i]["x"]][route[i]["y"]]["unit"] != CONST_UNIT_USED and self.grille[route[i-1]["x"]][route[i-1]["y"]]["unit"] == CONST_UNIT_USED:
						if self.grille[route[i-1]["x"]][route[i-1]["y"]]["item"].getEquipe() ==0:
							self.grille[route[i]["x"]][route[i]["y"]]["unit"] = CONST_UNIT_USED
							self.grille[route[i-1]["x"]][route[i-1]["y"]]["unit"] = CONST_UNIT_VIDE
							self.grille[route[i]["x"]][route[i]["y"]]["item"] = self.grille[route[i-1]["x"]][route[i-1]["y"]]["item"]
							self.grille[route[i-1]["x"]][route[i-1]["y"]]["item"] = None
				i-=1
			nb_route+=1

		#deplacement mechant
		nb_route = 0
		for route in self.routes:
			i  = 0
			while i <= len(route)-1:
				if not self.fin_route(route[i]["x"],route[i]["y"],nb_route):
					if self.grille[route[i]["x"]][route[i]["y"]]["unit"] != CONST_UNIT_USED and self.grille[route[i+1]["x"]][route[i+1]["y"]]["unit"] == CONST_UNIT_USED:
						if self.grille[route[i+1]["x"]][route[i+1]["y"]]["item"].getEquipe() ==1:
							self.grille[route[i]["x"]][route[i]["y"]]["unit"] = CONST_UNIT_USED
							self.grille[route[i+1]["x"]][route[i+1]["y"]]["unit"] = CONST_UNIT_VIDE
							self.grille[route[i]["x"]][route[i]["y"]]["item"] = self.grille[route[i-1]["x"]][route[i-1]["y"]]["item"]
							self.grille[route[i+1]["x"]][route[i+1]["y"]]["item"] = None
				i+=1
			nb_route+=1

	def combat_unit(self):
		nb_route = 0
		#deplacement gentil
		for route in self.routes:
			i  = 0
			while i <= len(route)-1:
				if self.grille[route[i]["x"]][route[i]["y"]]["unit"] == CONST_UNIT_USED:			#Si la case est occupe
					if self.debut_route(route[i]["x"],route[i]["y"],nb_route):							#Si c'est un debut de route
						if self.grille[route[i]["x"]][route[i]["y"]]["item"].getEquipe() ==1:				#Si c'est un ennemi
							############ ATTAQUE DE MINAS
					elif self.fin_route(route[i]["x"],route[i]["y"],nb_route):							#Sinon si c'est en fin de route
						if self.grille[route[i]["x"]][route[i]["y"]]["item"].getEquipe() ==0:				#Si c'est un allie
							############ ATTAQUE DE L'OEIL
					else:																				#Sinon (case ordinaire)
						if self.grille[route[i+1]["x"]][route[i+1]["y"]]["unit"] == CONST_UNIT_USED:		#Si ya une unite en face
							if self.grille[route[i+1]["x"]][route[i+1]["y"]]["item"].getEquipe() ==1:			#Si c'est un ennemi
							############ ATTAQUE ENTRE LES DEUX


				i+
			nb_route+=1
	"""
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
