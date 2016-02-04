# coding=utf-8

import pygame

class Regles:
	def __init__(self,screen):
		self.screen = screen
		self.font = pygame.font.Font("alagard.ttf",20)
		self.fontTitle = pygame.font.Font("alagard.ttf",50)
		self.rules = open('regles.txt')
		self.textes = list()
		for line in self.rules:
			line = line.replace('\n','')
			self.textes.append(self.font.render(line,True,(200,200,200)))
			
	def stop(self):
		self.rules.close()

	def draw(self):
		# Fond de l'interface du haut
		pygame.draw.rect(self.screen,(200,200,200),(0,0,self.screen.get_rect().width,50),0)

		# Nom du Jeu
		text = self.fontTitle.render("Road to Mordor",True,(75,75,75))
		self.screen.blit(text, [(self.screen.get_rect().width/2)-(text.get_rect().width/2), 0])

		for ind in range(len(self.textes)):
			val = self.textes[ind]
			self.screen.blit(val,(self.screen.get_rect().centerx-val.get_rect().centerx,80+ind*25))
