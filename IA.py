import random
import os
import pygame
import Grille
import joueur_classe

class IA:

	def __init__(self,grille):
		self.joueur = joueur_classe.Joueur("IA", "orc", 1)
		self.grille = grille

	def play(self):
		self.tour_IA()

	def generer_homme(self):


	def nb_tour(self):
		nb = 0
		for i in range((len(self.grille)/2)+1,len(self.grille)):
			for j in range(len(self.grille[0])):
				if (self.grille[i][j] >= CONST_FRONT_TOWER_IA_1 and self.grille[i][j] <= CONST_FRONT_TOWER_IA_6):
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
		self.grille[temp_i][temp_j]['item'] = batiment_classe.Batiment(0,0,"Tour IA")
		# Faire payer l'IA
		#joueur.payer(self.grille[temp_i][temp_j]['batiment'].getPrix())


	def tour_IA(self,grille):
		alea = random.randrange(100)
		if(Grille.nb_tour <= 5):
			if (alea < 50):
				Grille.generer_homme()
			else:
				Grille.generer_tour()
		if(Grille.nb_tour <= 10 and Grille.nb_tour > 5 ):
			if (alea < 60):
				Grille.generer_homme()
			elif( alea > 89 ):
				Grille.generer_upgrade()
			else:
				Grille.generer_tour()
		if(Grille.nb_tour <= 15 and Grille.nb_tour > 10 ):
			if (alea < 60):
				Grille.generer_homme()
			elif( alea > 79 ):
				Grille.generer_upgrade()
			else:
				Grille.generer_tour
		if(Grille.nb_tour <= 25 and Grille.nb_tour > 15 ):
			if (alea < 70):
				Grille.generer_homme()
			elif( alea > 79 ):
				Grille.generer_upgrade()
			else:
				Grille.generer_tour
		if(Grille.nb_tour > 25 ):
			if (alea < 60):
				Grille.generer_homme()
			else:
				Grille.generer_upgrade()
