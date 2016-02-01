import pygame

class UserInterface:
	""" Classe pour l'interface utilisateur """

	def __init__(self,screenP):
		self.screen = screenP

	def draw(self):
		screenRect = self.screen.get_rect()
		pygame.draw.rect(self.screen,(200,200,200),(0,0,screenRect[2],50),0)
