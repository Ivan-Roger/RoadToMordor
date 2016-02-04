"""
	Dagobert Main file
"""
import pygame
import game_classe
import menu_classe

# -------- Main Program -----------
menu = menu_classe.Menu();
game = game_classe.Game();

done = False

print('Initialized ! Launching ...')
while not done:
	res_m = menu.launch()
	print(res_m)
	if res_m == 'QUIT':
		done = True
	elif res_m == 'PLAY':
		done = not game.launch()
		print(done)
