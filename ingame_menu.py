# coding=utf-8

import pygame

class InGameMenu:
	def __init__(self,screenP):
		self.screen = screenP
		self.jouer_pos = 500
		self.regles_pos = 500
		self.credit_pos = 500
		self.selected = 0


	def draw(self):
		#Creation des texte
		text = pygame.font.Font("alagard.ttf",50)
		m = text.render("Dagobert",True,(255,255,255))
		j = text.render("Jouer",True,(255,255,255))
		r = text.render("Règles",True,(255,255,255))
		c = text.render("Credit",True,(255,255,255))

		#Position de centre
		mpos = m.get_rect()
		mpos.centerx = self.screen.get_rect().centerx
		jpos = j.get_rect()
		jpos.centerx = self.screen.get_rect().centerx
		rpos = r.get_rect()
		rpos.centerx = self.screen.get_rect().centerx
		cpos = c.get_rect()
		cpos.centerx = self.screen.get_rect().centerx

		#Position de hauteur
		jouer_y_off=0
		regles_y_off=0
		credit_y_off=0
		if self.selected==0:
			jouer_y_off=20
		elif self.selected==1:
			regles_y_off=20
		elif self.selected==2:
			credit_y_off=20

		#blit
		self.screen.blit(m,(self.screen.get_rect().centerx,50))
		self.screen.blit(j,(self.screen.get_rect().centerx-150,500-jouer_y_off))
		self.screen.blit(r,(self.screen.get_rect().centerx,500-jouer_y_off))
		self.screen.blit(c,(self.screen.get_rect().centerx+150,500-jouer_y_off))

	def switchSelected(self):
		self.selected+=1
		if self.selected>=3:
			self.selected=0
