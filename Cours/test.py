import sys
import pygame
import os
sys.path.append('../')
import menu
import credit

if __name__ == '__main__':
	pygame.init()

	width = 1200
	height = 910

	size = width, height
	screen = pygame.display.set_mode(size)
	os.environ['SDL_VIDEO_CENTERED'] = '1'

	menu = menu.MenuInterface(screen)
	credit = credit.CreditInterface(screen)

	done = False
	# Boucle de jeu
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					menu.jouer_select()
				if event.key == pygame.K_RIGHT:
					menu.credit_select()
				if event.key == pygame.K_RETURN:
					if menu.selected == 1:
						print("Jeux !")
					elif menu.selected == 2:
						while not credit.fini or not done:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									done = True
								if event.type == pygame.KEYDOWN:
									if event.key == pygame.K_ESCAPE:
										done = True
							credit.draw()
							pygame.display.flip()
						menu.init()
						credit.init()
						done = False
					elif menu.selected == 0:
						menu.jouer_select()


		menu.draw()
		pygame.display.flip()
		pygame.time.Clock().tick(60)


else:
	if 1 == 2:
		pygame.init()

		width = 1200
		height = 910

		#os.environ['SDL_VIDEO_CENTERED'] = '1'
		size = width, height
		screen = pygame.display.set_mode(size)
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		clock = pygame.time.Clock()


		#print("textpos = {0}".format(textpos))

		done = False
		# Boucle de jeu
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True

			screen.fill((0,0,0))
			textpos[1]-=1
			screen.blit(a,textpos)
			textpos[1]-=200
			screen.blit(b,textpos)
			textpos[1]-=200
			screen.blit(c,textpos)
			textpos[1]-=200
			screen.blit(d,textpos)
			textpos[1]-=200
			screen.blit(e,textpos)
			textpos[1]-=200
			screen.blit(f,textpos)
			textpos[1]+=1000
			pygame.display.flip()
			clock.tick(60)
