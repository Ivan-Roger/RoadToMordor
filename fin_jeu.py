import pygame

class Fin:
	def __init__(self,screen):
		self.screen = screen
		self.font = pygame.font.Font("alagard.ttf",20)
		self.fontTitle = pygame.font.Font("alagard.ttf",50)
		self.background_image = pygame.image.load("images/back2.jpg")

		self.text_fonction = pygame.font.Font("alagard.ttf",200, bold=True)
		self.victoire = self.text_fonction.render("VICTOIRE",True,(255,255,255))
		self.defaite = self.text_fonction.render("DEFAITE",True,(255,255,255))
		self.vict = False

	def start(self,victoire):
		print('................')
		self.vict = victoire
		if victoire:
			print('victoire')
			self.music_victoire = pygame.mixer.music.load('Musique/theme_principal.mp3')
		else:
			print('defaite')
			self.music_defaite = pygame.mixer.music.load('Musique/defaite.mp3')
		print('!!!!!!!!!!!')
		pygame.mixer.music.play()
		pygame.mixer.music.set_volume(1.0)
		print('................')

	def stop(self):
		pygame.mixer.music.stop()
		pygame.mixer.music.set_volume(1.0)

	def draw(self):
		# Fond de l'interface du haut
		self.screen.blit(self.background_image, (0,0))
		pygame.draw.rect(self.screen,(200,200,200),(0,0,self.screen.get_rect().width,50),0)

		# Nom du Jeu
		text = self.fontTitle.render("Road to Mordor",True,(75,75,75))
		self.screen.blit(text, [(self.screen.get_rect().width/2)-(text.get_rect().width/2), 0])

		if self.vict:
			textpos = self.victoire.get_rect()
			textpos.centerx = self.screen.get_rect().centerx
			textpos[1] = 450
			self.screen.blit(self.victoire,textpos)
		else:
			textpos = self.defaite.get_rect()
			textpos.centerx = self.screen.get_rect().centerx
			textpos[1] = 450
			self.screen.blit(self.defaite,textpos)
