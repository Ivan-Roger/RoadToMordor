# coding=utf-8

import random
import os
import pygame
import grille_classe
import joueur_classe
import unite_classe
import batiment_classe

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


class IA:

	def __init__(self,grille,joueur):
		self.selectT = {}
		self.selectT['units'] = list()
		self.selectT['units'].append(0)
		self.selectT['units'].append(0)
		self.selectT['units'].append(0)
		self.selectT['units'].append(0)
		self.selectT['units'].append(0)
		self.selectT['units'].append(0)
		self.selectT['towers'] = list()
		self.selectT['towers'].append(0)
		self.selectT['towers'].append(0)
		self.selectT['towers'].append(0)
		self.selectT['towers'].append(0)
		self.selectT['towers'].append(0)
		self.selectT['towers'].append(0)
		self.joueur = joueur
		self.grille = grille.getGrille()
		self.grille_obj = grille
		self.routes = self.grille_obj.routes
		self.turn=0

	def play(self):
		self.turn+=1
		self.tick()
		#print("===================================\nArgent IA ava,t tour = {}".format(self.joueur.getArgent()))
		if self.turn%10==0:
			print('---------------------- TOUR IA ----------------------')
			self.tour_IA()
		#print("Argent IA apres tour = {}\n===================================".format(self.joueur.getArgent()))

	def tick(self):
		for i in range(6):
			if (self.selectT['towers'][i]>0):
				self.selectT['towers'][i]-=1
			if (self.selectT['units'][i]>0):
				self.selectT['units'][i]-=1

	def get_IA_soldat_route(self,nb_route):
		IA = []
		route = self.routes[nb_route]
		i  = 0
		while i <= len(route)-1:
			if self.grille[route[i]["x"]][route[i]["y"]]["unit"] == CONST_UNIT_USED:
				if self.grille[route[i]["x"]][route[i]["y"]]["item"].getEquipe() == 0:
					IA.append(self.grille[route[i]["x"]][route[i]["y"]]["item"])
			i+=1
		return IA

	def get_humain_soldat_route(self,nb_route):
		humain = []
		route = self.routes[nb_route]
		i  = 0
		while i <= len(route)-1:
			if self.grille[route[i]["x"]][route[i]["y"]]["unit"] == CONST_UNIT_USED:
				if self.grille[route[i]["x"]][route[i]["y"]]["item"].getEquipe() == 1:
					humain.append(self.grille[route[i]["x"]][route[i]["y"]]["item"])
			i+=1
		return humain

	def get_humain_tour_route(self,nb_route):
		tours = []
		coord = []
		route = self.routes[nb_route]
		i  = 0
		while i <= len(route)-1:
			x = route[i]["x"]
			y = route[i]["y"]
			j = x-1
			k = y-1
			while (j <= x + 1):
				k = y - 1
				while (k <= y + 1):
					try:
						if self.grille[j][k]['front'] == CONST_FRONT_BAT:
							if self.grille[j][k]['item'].getEquipe() == 1 and [j,k] not in coord:
								t = self.grille[j][k]['item']
								tours.append(t)
								coord.append([t.getPos()["x"],t.getPos()["y"]])
					except IndexError:
						continue
					finally:
						k+=1
				j+=1


			i+=1
		return tours

	def get_IA_tour_route(self,nb_route):
		tours = []
		coord = []
		route = self.routes[nb_route]
		i  = 0
		while i <= len(route)-1:
			x = route[i]["x"]
			y = route[i]["y"]
			j = x-1
			k = y-1
			while (j <= x + 1):
				k = y - 1
				while (k <= y + 1):
					try:
						if self.grille[j][k]['front'] == CONST_FRONT_BAT:
							if self.grille[j][k]['item'].getEquipe() == 0 and [j,k] not in coord:
								t = self.grille[j][k]['item']
								tours.append(t)
								coord.append([t.getPos()["x"],t.getPos()["y"]])
					except IndexError:
						continue
					finally:
						k+=1
				j+=1


			i+=1
		return tours

	def nb_route_autour(self,radius,x,y):
		nb = 0
		i = x - radius
		while (i <= x + radius):
			j = y - radius
			while (j <= y + radius):
				try:
					if self.grille[i][j]['front'] == CONST_FRONT_ROUTE:
						nb+=1
				except IndexError:
					continue
				finally:
					j+=1
			i+=1
		return nb


	def generer_tour(self,choix_route,choix_tour):
		temp_i, temp_j, max1, nbcase = 0,0,0,0
		nb_route = (len(self.routes)+1)
		if self.grille_obj.rows%nb_route != 0:
			s = self.grille_obj.rows-((self.grille_obj.rows/len(self.grille))+(self.grille_obj.rows%len(self.grille)))
			f = self.grille_obj.rows
		else:
			s = (self.grille_obj.rows/nb_route)*choix_route
			f = (self.grille_obj.rows/nb_route)*(choix_route+1)-1

		for i in range((len(self.grille)/2)+1,len(self.grille)-1):
			for j in range(s,f):
				if self.grille[i][j]['front'] == CONST_FRONT_VIDE:
					nbcase = self.nb_route_autour(1,i,j)
					if (nbcase > max1):
						max1 = nbcase
						temp_i = i
						temp_j = j

		if self.grille_obj.canBuild({'x':temp_i,'y':temp_j},self.joueur.getEquipe()) and self.selectT['towers'][choix_tour]==0:
			tour = self.joueur.createBuild(choix_tour,self.grille_obj,{'x':temp_i,'y':temp_j})
			if not tour == False:
				self.grille_obj.place(tour)
				self.selectT['towers'][choix_tour] = 100
				print("==================================== TOUR Génerée")
				return True
			else:
				return False
		else:
			return False

	def generer_homme(self,choix_route,choix_unit):
		if self.grille_obj.canSpawn(self.routes[choix_route],self.joueur.getEquipe()) and self.selectT['units'][choix_unit]==0:
			homme = self.joueur.createUnit(choix_unit,self.grille_obj,self.routes[choix_route])
			if not homme == False:
				self.grille_obj.place(homme)
				self.selectT['units'][choix_unit] = 100
				print("==================================== SOLDAT Géneré")
				return True
			else:
				return False
		else:
			return False

	def stats_joueurs_route(self,nb_route):
		allies = self.get_humain_soldat_route(nb_route)
		ennemis = self.get_IA_soldat_route(nb_route)
		route = self.grille[nb_route]
		attaquePhy = 0
		attaqueMag = 0
		defensePhy = 0
		defenseMag = 0
		totalVie = 0
		stats = []
		stats.append([])
		for unit in ennemis:
			totalVie+=unit.getVie()
			attaquePhy+=unit.getAttPhy()
			attaqueMag+=unit.getAttMag()
			defensePhy+=unit.getResPhy()
			defenseMag+=unit.getResMag()
		stats[0].append(totalVie)
		stats[0].append(attaquePhy)
		stats[0].append(attaqueMag)
		stats[0].append(defensePhy)
		stats[0].append(defenseMag)

		stats.append([])
		attaquePhy = 0
		attaqueMag = 0
		defensePhy = 0
		defenseMag = 0
		totalVie = 0
		for unit in allies:
			totalVie+=unit.getVie()
			attaquePhy+=unit.getAttPhy()
			attaqueMag+=unit.getAttMag()
			defensePhy+=unit.getResPhy()
			defenseMag+=unit.getResMag()
		stats[1].append(totalVie)
		stats[1].append(attaquePhy)
		stats[1].append(attaqueMag)
		stats[1].append(defensePhy)
		stats[1].append(defenseMag)
		return stats

	def stats_tour_route(self,nb_route):
		allies = self.get_humain_tour_route(nb_route)
		ennemis = self.get_IA_tour_route(nb_route)
		route = self.grille[nb_route]
		attaquePhy=0
		attaqueMag=0
		stats = []
		stats.append([])
		for unit in ennemis:
			attaquePhy+=unit.getAttPhy()
			attaqueMag+=unit.getAttMag()
		stats[0].append(attaquePhy)
		stats[0].append(attaqueMag)

		stats.append([])
		attaquePhy=0
		attaqueMag=0
		for unit in allies:
			attaquePhy+=unit.getAttPhy()
			attaqueMag+=unit.getAttMag()
		stats[1].append(attaquePhy)
		stats[1].append(attaqueMag)
		return stats

	def generer_tour_pos(self,x,y,choix_tour):
		if self.grille_obj.canBuild({'x':x,'y':y},self.joueur.getEquipe()) and self.selectT['towers'][choix_tour]==0:
			tour = self.joueur.createBuild(choix_tour,self.grille_obj,{'x':x,'y':y})
			if not tour == False:
				self.grille_obj.place(tour)
				self.selectT['towers'][choix_tour] = 100
				print("==================================== TOUR Génerée")
				return True
			else:
				return False
		else:
			return False

	def tour_IA(self):
		actRestant = 2
		argent = self.joueur.getArgent()
		if argent >=5:
			calcul_units = []
			calcul_tours = []
			nb_routes = len(self.routes)
			for i in range(nb_routes):
				calcul_units.append(self.stats_joueurs_route(i))
			for i in range(nb_routes):
				calcul_tours.append(self.stats_tour_route(i))

			#L'IA essaye de supprimer les menaces immediate
			for route in self.routes:
				x = route[len(route)-1]["x"]
				y = route[len(route)-1]["y"]
				if self.grille[x][y]["unit"] == CONST_UNIT_USED and actRestant>0:
					if self.grille[x][y]["item"].getEquipe() == 1:
						if self.grille[x][y+1]["front"]== CONST_FRONT_VIDE:
							if self.generer_tour_pos(x,y+1,1) :
								actRestant -= 1
							elif self.generer_tour_pos(x,y+1,0) :
								actRestant -= 1
						elif self.grille[x][y-1]["front"] == CONST_FRONT_VIDE:
							if self.generer_tour_pos(x,y-1,1) :
								 actRestant -= 1
 							elif self.generer_tour_pos(x,y-1,0) :
 								actRestant -= 1
						elif self.grille[x-1][y+1]["front"] == CONST_FRONT_VIDE:
							if self.generer_tour_pos(x+1,y+1,1) :
								 actRestant -= 1
 							elif self.generer_tour_pos(x+1,y+1,0) :
 								actRestant -= 1
						elif self.grille[x-1][y-1]["front"] == CONST_FRONT_VIDE:
							if self.generer_tour_pos(x+1,y-1,1) :
								 actRestant -= 1
 							elif self.generer_tour_pos(x+1,y-1,0) :
 								actRestant -= 1
						elif self.grille[x-1][y]["front"] == CONST_FRONT_VIDE:
							if self.generer_tour_pos(x+1,y,1) :
								 actRestant -= 1
 							elif self.generer_tour_pos(x+1,y,0) :
 								actRestant -= 1

			#L'IA essaye de contrer d'abord les attaques
			for i in range(nb_routes):
				if calcul_units[i][1][0] >= calcul_tours[i][0][0]*2+calcul_tours[i][0][1]*2+calcul_units[i][0][1]+calcul_units[i][0][2]:
					#envoyer unit ou construire tours
					alea = random.randrange(5)
					if alea !=0:
						encore = True
						while encore and actRestant>0 and self.joueur.getArgent() > (argent/4)*3 and self.stats_joueurs_route(i)[1][0] >= self.stats_tour_route(i)[0][0]*2+self.stats_tour_route(i)[0][1]+self.stats_joueurs_route(i)[0][1]+self.stats_joueurs_route(i)[0][2]:
							alea2 = random.randrange(20)
							if alea2 >=9 :
								encore = self.generer_tour(i,0)
								if encore: actRestant -= 1
							elif alea2 <9 and alea2 >= 3:
								encore = self.generer_tour(i,1)
								if encore: actRestant -= 1
							elif alea2 <3 :
								encore = self.generer_tour(i,2)
								if encore: actRestant -= 1
					else:
						encore = True
						while encore and actRestant>0 and self.joueur.getArgent() > (argent/4)*2 and self.stats_joueurs_route(i)[1][0] >= self.stats_tour_route(i)[0][0]*2+self.stats_tour_route(i)[0][1]+self.stats_joueurs_route(i)[0][1]+self.stats_joueurs_route(i)[0][2]:
							alea2 = random.randrange(20)
							if alea2 >=9 :
								encore = self.generer_homme(i,0)
								if encore: actRestant -= 1
							elif alea2 <9 and alea2 >= 3:
								encore = self.generer_homme(i,1)
								if encore: actRestant -= 1
							elif alea2 <3 :
								encore = self.generer_homme(i,2)
								if encore: actRestant -= 1

			#Puis avec les ressources qui lui reste elle attaque
			min_vie = 150000
			min_tours = 150000
			choix_attaque_unit = -1
			choix_attaque_tour = -1

			for i in range(nb_routes):
				if min_vie != min(min_vie,calcul_units[i][1][0]):
					min_vie = min(min_vie,calcul_units[i][1][0])
					choix_attaque_unit = i
				if min_tours != min(min_tours,calcul_tours[i][1][0]+calcul_tours[i][1][1]):
					min_tours = min(min_tours,calcul_tours[i][1][0]+calcul_tours[i][1][1])
					choix_attaque_tour = i

			encore = True
			while encore and actRestant>0 and self.joueur.getArgent() > (argent/10):
				alea2 = random.randrange(20)
				if alea2 >=9 :
					encore = self.generer_homme(choix_attaque_tour,0)
					if encore: actRestant -= 1
				elif alea2 <9 and alea2 >= 3:
					encore = self.generer_homme(choix_attaque_tour,1)
					if encore: actRestant -= 1
				elif alea2 <3 :
					encore = self.generer_homme(choix_attaque_tour,2)
					if encore: actRestant -= 1
