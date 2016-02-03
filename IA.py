import random
import os
import pygame
import Grille
import joueur_classe

class IA:

	def __init__(self):
		self.joueur = joueur_classe.Joueur("IA", "orc", 1)


	def play(self):
		

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
