# coding=utf-8

import pygame

class Credits:
	def __init__(self,screenP):
		self.screen = screenP
		self.background_image = pygame.image.load("images/back.jpg")
		self.reset()

		self.text_nom = pygame.font.Font("alagard.ttf",50, bold=True)
		self.text_fonction = pygame.font.Font("alagard.ttf",70, bold=True)
		self.text_ressource = pygame.font.Font("alagard.ttf",30, bold=True)
		self.florian = self.text_nom.render("Florian INARD",True,(255,255,255))
		self.ivan = self.text_nom.render("Ivan ROGER",True,(255,255,255))
		self.mathias = self.text_nom.render("Mathias NOVEL",True,(255,255,255))
		self.matthieu = self.text_nom.render("Matthieu VIVIER",True,(255,255,255))
		self.maxime = self.text_nom.render("Maxime GERMAIN",True,(255,255,255))
		self.hugo = self.text_nom.render("Hugo VERONESE",True,(255,255,255))
		self.son = self.text_fonction.render("Bruitages et Musiques",True,(255,255,255))

		self.son_1 = self.text_ressource.render("Theme en jeu : \"Evenstar\" de boopbeepbeepboop ",True,(255,255,255))
		self.sprite_1 = self.text_ressource.render("Certains sprites de Heroes of Might and Magic 2",True,(255,255,255))
		self.trailer_1 = self.text_ressource.render("Utilisation des images de la trilogie",True,(255,255,255))
		self.image_1 = self.text_ressource.render("Image de fond : Wallhaven",True,(255,255,255))

		self.graphique = self.text_fonction.render("Graphique",True,(255,255,255))
		self.code = self.text_fonction.render("Code",True,(255,255,255))
		self.ressources = self.text_fonction.render("Ressources",True,(255,255,255))

	def draw(self):
		#Position de centre
		florianpos = self.florian.get_rect()
		florianpos.centerx = self.screen.get_rect().centerx
		ivanpos = self.ivan.get_rect()
		ivanpos.centerx = self.screen.get_rect().centerx
		mathiaspos = self.mathias.get_rect()
		mathiaspos.centerx = self.screen.get_rect().centerx
		matthieupos = self.matthieu.get_rect()
		matthieupos.centerx = self.screen.get_rect().centerx
		maximepos = self.maxime.get_rect()
		maximepos.centerx = self.screen.get_rect().centerx
		hugopos = self.hugo.get_rect()
		hugopos.centerx = self.screen.get_rect().centerx
		sonpos = self.son.get_rect()
		sonpos.centerx = self.screen.get_rect().centerx
		graphiquepos = self.graphique.get_rect()
		graphiquepos.centerx = self.screen.get_rect().centerx

		codepos = self.code.get_rect()
		codepos.centerx = self.screen.get_rect().centerx

		ressourcespos = self.ressources.get_rect()
		ressourcespos.centerx = self.screen.get_rect().centerx

		son_1pos = self.son_1.get_rect()
		son_1pos.centerx = self.screen.get_rect().centerx
		sprite_1pos = self.sprite_1.get_rect()
		sprite_1pos.centerx = self.screen.get_rect().centerx
		trailer_1pos = self.trailer_1.get_rect()
		trailer_1pos.centerx = self.screen.get_rect().centerx
		image_1pos = self.image_1.get_rect()
		image_1pos.centerx = self.screen.get_rect().centerx

		#Position de hauteur
		self.fini = (self.pos<-1700)

		self.pos-=1
		sonpos[1]+=self.pos
		matthieupos[1]+=self.pos+100

		graphiquepos[1]+=self.pos+300
		hugopos[1]+=self.pos+400

		codepos[1]+=self.pos+600
		florianpos[1]+=self.pos+700
		ivanpos[1]+=self.pos+800
		mathiaspos[1]+=self.pos+900
		maximepos[1]+=self.pos+1000

		ressourcespos[1]+=self.pos+1200
		son_1pos[1]+=self.pos+1300
		sprite_1pos[1]+=self.pos+1375
		trailer_1pos[1]+=self.pos+1450
		image_1pos[1]+= self.pos+1525

		#blit
		self.screen.blit(self.background_image, (0,0))
		self.screen.blit(self.son,sonpos)
		self.screen.blit(self.matthieu,matthieupos)
		self.screen.blit(self.graphique,graphiquepos)
		self.screen.blit(self.hugo,hugopos)
		self.screen.blit(self.code,codepos)
		self.screen.blit(self.florian,florianpos)
		self.screen.blit(self.ivan,ivanpos)
		self.screen.blit(self.mathias,mathiaspos)
		self.screen.blit(self.maxime,maximepos)
		self.screen.blit(self.ressources,ressourcespos)
		self.screen.blit(self.son_1,son_1pos)
		self.screen.blit(self.sprite_1,sprite_1pos)
		self.screen.blit(self.trailer_1,trailer_1pos)
		self.screen.blit(self.image_1,image_1pos)

		return self.fini

	def reset(self):
		self.pos = 500
		self.fini = False
