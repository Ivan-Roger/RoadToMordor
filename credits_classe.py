import pygame

class Credits:

	def __init__(self,screenP):
		self.screen = screenP
		self.background_image = pygame.image.load("images/back.jpg")
		self.pos = 1001
		self.fini = False


	def draw(self):
		#Creation des texte
		text_nom = pygame.font.Font("alagard.ttf",50, bold=True)
		text_fonction = pygame.font.Font("alagard.ttf",70, bold=True)
		florian = text_nom.render("Florian INARD",True,(255,255,255))
		ivan = text_nom.render("Ivan ROGER",True,(255,255,255))
		mathias = text_nom.render("Mathias NOVEL",True,(255,255,255))
		matthieu = text_nom.render("Matthieu VIVIER",True,(255,255,255))
		maxime = text_nom.render("Maxime GERMAIN",True,(255,255,255))
		hugo = text_nom.render("Hugo VERONESE",True,(255,255,255))
		son = text_fonction.render("Bruitage et Musique",True,(255,255,255))
		graphique = text_fonction.render("Graphique",True,(255,255,255))
		code = text_fonction.render("Code",True,(255,255,255))

		#Position de centre
		florianpos = florian.get_rect()
		florianpos.centerx = self.screen.get_rect().centerx
		ivanpos = ivan.get_rect()
		ivanpos.centerx = self.screen.get_rect().centerx
		mathiaspos = mathias.get_rect()
		mathiaspos.centerx = self.screen.get_rect().centerx
		matthieupos = matthieu.get_rect()
		matthieupos.centerx = self.screen.get_rect().centerx
		maximepos = maxime.get_rect()
		maximepos.centerx = self.screen.get_rect().centerx
		hugopos = hugo.get_rect()
		hugopos.centerx = self.screen.get_rect().centerx
		sonpos = son.get_rect()
		sonpos.centerx = self.screen.get_rect().centerx
		graphiquepos = graphique.get_rect()
		graphiquepos.centerx = self.screen.get_rect().centerx
		codepos = code.get_rect()
		codepos.centerx = self.screen.get_rect().centerx

		#Position de hauteur
		if self.pos < -1100:
			self.fini = True

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

		#blit
		self.screen.blit(self.background_image, (0,0))
		self.screen.blit(son,sonpos)
		self.screen.blit(matthieu,matthieupos)
		self.screen.blit(graphique,graphiquepos)
		self.screen.blit(hugo,hugopos)
		self.screen.blit(code,codepos)
		self.screen.blit(florian,florianpos)
		self.screen.blit(ivan,ivanpos)
		self.screen.blit(mathias,mathiaspos)
		self.screen.blit(maxime,maximepos)

	def init(self):
		self.pos = 1001
		self.fini = False
