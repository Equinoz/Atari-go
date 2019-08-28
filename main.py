#!/usr/bin/python3.6
# -*- coding:Utf-8 -*-

import pygame
from pygame.locals import *

game_running = True

STONE_WIDTH = 40
BOARD_SIZE = 13
HOSHIS = [(3,3), (9,3), (6,6), (3,9), (9,9)]
BORDER = 65
LINE_WIDTH = 2
TITRE = "Atari-go"

INTERVAL = STONE_WIDTH + 4
GRID_WIDTH = INTERVAL * (BOARD_SIZE - 1)
BOARD_WIDTH = GRID_WIDTH + BORDER * 2

pygame.init()
window = pygame.display.set_mode((BOARD_WIDTH, BOARD_WIDTH + 100))
pygame.display.set_caption(TITRE)
background = pygame.image.load("images/background.jpeg").convert()
font = pygame.font.Font("font/ABeeZee-Regular.otf", 50)
texte = "Au tour de noir"

while game_running:
	pygame.time.Clock().tick(30)
	window.blit(background, (0, 0))

	for y in range(65, INTERVAL * (BOARD_SIZE + 1), INTERVAL):
		pygame.draw.line(window, (0,0,0), (BORDER, y), (BORDER + GRID_WIDTH, y), LINE_WIDTH)
	for x in range(BORDER, INTERVAL * (BOARD_SIZE + 1), INTERVAL):
		pygame.draw.line(window, (0,0,0), (x, BORDER), (x, BORDER + GRID_WIDTH), LINE_WIDTH)

	for hoshi in HOSHIS:
		x = hoshi[0] * INTERVAL + BORDER
		y = hoshi[1] * INTERVAL + BORDER
		pygame.draw.circle(window, (0,0,0), (x,y), 3 * LINE_WIDTH)

	text = font.render(texte, 1, (50,60,25))
	textpos = text.get_rect(centerx=window.get_width()/2, centery=window.get_height()-70)
	window.blit(text, textpos)

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == QUIT:
			game_running = False
		elif event.type == MOUSEBUTTONUP:
			clic_x = event.pos[0]
			clic_y = event.pos[1]
			x = round((clic_x-BORDER)/INTERVAL)
			y = round((clic_y-BORDER)/INTERVAL)
			if (x > -1 and x < BOARD_SIZE) and (y > -1 and y < BOARD_SIZE):
				texte = "x: {}, y: {}; case: {},{}".format(clic_x, clic_y, x, y)
