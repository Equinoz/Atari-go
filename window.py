import pygame
from pygame.locals import *

from constants import *

class Window:
	""" Initialise une nouvelle fenêtre avec les constantes données dans le fichier "constants.py"
		Attributs: "window" la fenêtre à afficher, "background" l'image de fond et "font" la police utilisée pour le texte
		Méthode: "display" reçoit un set de groupes et un string pour rafraîchir la fenêtre

	"""
	def __init__(self):
		pygame.init()
		self.window = pygame.display.set_mode((BOARD_WIDTH, BOARD_WIDTH+100))
		pygame.display.set_caption(TITLE)
		self.background = pygame.image.load("images/background.jpeg").convert()
		self.font = pygame.font.Font("font/ABeeZee-Regular.otf", 50)

	def display(self, groups, text):
		# Mise en place du fond
		self.window.blit(self.background, (0,0))

		# Dessin des lignes du goban
		for y in range(BORDER, INTERVAL * (BOARD_SIZE+1), INTERVAL):
			pygame.draw.line(self.window, (0,0,0), (BORDER,y), (BORDER+GRID_WIDTH,y), LINE_WIDTH)
		for x in range(BORDER, INTERVAL * (BOARD_SIZE+1), INTERVAL):
			pygame.draw.line(self.window, (0,0,0), (x,BORDER), (x,BORDER+GRID_WIDTH), LINE_WIDTH)

		# Dessin des hoshis
		for hoshi in HOSHIS:
			x = hoshi[0] * INTERVAL + BORDER
			y = hoshi[1] * INTERVAL + BORDER
			pygame.draw.circle(self.window, (0,0,0), (x,y), LINE_WIDTH * 3)

		# Affichage du texte
		text_area = self.font.render(text, 1, (50,60,25))
		text_pos = text_area.get_rect(centerx=self.window.get_width()/2, centery=self.window.get_height()-70)
		self.window.blit(text_area, text_pos)

		# Affichage des pierres selon l'état de santé de leur groupe
		for group in groups:
			image_path = "images/stone_{}_{}.png".format(group.color, group.state)
			stone_image = pygame.image.load(image_path).convert_alpha()
			for stone in group.stones:
				x, y = stone
				self.window.blit(stone_image, (x*INTERVAL+BORDER-STONE_WIDTH/2, y*INTERVAL+BORDER-STONE_WIDTH/2))

		# Rafraîchissement de la fenêtre
		pygame.display.flip()
