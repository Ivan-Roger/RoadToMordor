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
		q = self.font.render("Quitter",True,(255,255,255))

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

		#blit
		self.screen.blit(j,(self.screen.get_rect().centerx-(j.get_rect().width/2)-250,500-j_y_off))
		self.screen.blit(r,(self.screen.get_rect().centerx-(r.get_rect().width/2),500-r_y_off))
		self.screen.blit(q,(self.screen.get_rect().centerx-(q.get_rect().width/2)+250,500-q_y_off))

	def getSelected(self):
		return self.selected

	def switchSelected(self):
		self.selected+=1
		if self.selected>=3:
			self.selected=0
