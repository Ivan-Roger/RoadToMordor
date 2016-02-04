# coding=utf-8

import pygame

class InGameMenu:
	def __init__(self,screenP):
		self.screen = screenP
		self.font = pygame.font.Font("alagard.ttf",50)
		self.selected = 0


	def draw(self):
		#Creation des texte
		j = self.font.render("Reprendre",True,(255,255,255))
		r = self.font.render("Regles",True,(255,255,255))
		q = self.font.render("Abandonner",True,(255,255,255))

		#Position de hauteur
		j_y_off=0
		r_y_off=0
		q_y_off=0
		if self.selected==0:
			j_y_off=20
		elif self.selected==1:
			r_y_off=20
		elif self.selected==2:
			q_y_off=20

		# Fond de l'interface du haut
		pygame.draw.rect(self.screen,(200,200,200),(0,0,self.screen.get_rect().width,50),0)

		# Nom du Jeu
		text = self.font.render("Road to Mordor",True,(75,75,75))
		self.screen.blit(text, [(self.screen.get_rect().width/2)-(text.get_rect().width/2), 0])

		self.screen.blit(j,(self.screen.get_rect().centerx-(j.get_rect().centerx)-300,500-j_y_off))
		self.screen.blit(r,(self.screen.get_rect().centerx-(r.get_rect().centerx),500-r_y_off))
		self.screen.blit(q,(self.screen.get_rect().centerx-(q.get_rect().centerx)+300,500-q_y_off))

	def getSelected(self):
		return self.selected

	def switchSelected(self):
		self.selected+=1
		if self.selected>=3:
			self.selected=0

	def selectPrev(self):
		self.selected-=1
		if self.selected<0:
			self.selected=2
