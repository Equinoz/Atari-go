#!/usr/bin/python3.6
# -*- coding:Utf-8 -*-

import pygame
from pygame.locals import *

from constants import *
from game import Game
from group import Group
from functions import *

def display_border():
	window.blit(background, (0, 0))

	for y in range(65, INTERVAL * (BOARD_SIZE + 1), INTERVAL):
		pygame.draw.line(window, (0,0,0), (BORDER, y), (BORDER + GRID_WIDTH, y), LINE_WIDTH)
	for x in range(BORDER, INTERVAL * (BOARD_SIZE + 1), INTERVAL):
		pygame.draw.line(window, (0,0,0), (x, BORDER), (x, BORDER + GRID_WIDTH), LINE_WIDTH)

	for hoshi in HOSHIS:
		x = hoshi[0] * INTERVAL + BORDER
		y = hoshi[1] * INTERVAL + BORDER
		pygame.draw.circle(window, (0,0,0), (x,y), 3 * LINE_WIDTH)

	text_area = font.render(text, 1, (50,60,25))
	text_pos = text_area.get_rect(centerx=window.get_width()/2, centery=window.get_height()-70)
	window.blit(text_area, text_pos)

	for group in groups:
		image_path = "images/stone_{}_{}.png".format(group.color, group.state)
		stone_image = pygame.image.load(image_path).convert_alpha()
		for stone in group.stones:
			x, y = stone
			window.blit(stone_image, (stone[0] * INTERVAL + BORDER - STONE_WIDTH / 2, stone[1] * INTERVAL + BORDER - STONE_WIDTH / 2))

	pygame.display.flip()

game_running = True

while game_running:
	match_running = True
	player = 'b'
	opponent = 'w'
	game = Game(13)
	groups = set()
	text = "Au tour de noir"

	pygame.init()
	window = pygame.display.set_mode((BOARD_WIDTH, BOARD_WIDTH + 100))
	pygame.display.set_caption(TITLE)
	background = pygame.image.load("images/background.jpeg").convert()
	font = pygame.font.Font("font/ABeeZee-Regular.otf", 50)

	while match_running:
		pygame.time.Clock().tick(30)
		display_border()

		for event in pygame.event.get():
			if event.type == QUIT:
				game_running = match_running = False
			elif event.type == MOUSEBUTTONUP:
				x = round((event.pos[0]-BORDER)/INTERVAL)
				y = round((event.pos[1]-BORDER)/INTERVAL)
				position = (x, y)
				if (x > -1 and x < BOARD_SIZE) and (y > -1 and y < BOARD_SIZE):
					# Si la case sélectionnée est vide on détermine les groupes alliés et adverses et la présence ou non de libertés
					if point_is_empty(game, position):
						associate_groups = has_groups(game, groups, player, position)
						opponent_groups = has_groups(game, groups, opponent, position)
						liberties = has_liberties(game, position)

						# On vérifie que le coup est autorisé selon les règles de capture
						if liberties or not_in_atari(associate_groups) or in_atari(opponent_groups):
							# Listing des pierres composant le groupe et suppression éventuelle des groupes obsolètes
							stones = [position]
							for group in associate_groups:
								stones.extend(group.stones)
								groups.remove(group)
							game.add_stone(player, position)

							# On met à jour les groupes adjacents adverses pour vérifier si certains ont été capturés. Si oui ils sont supprimés et le joueur gagne
							for group in opponent_groups:
								group.update_state(game)
								if group.state == 0:
									game.remove_group(group.stones)
									groups.remove(group)
									match_running = False

							# On crée le nouveau groupe avec la liste éventuelle des pierres qui appartenaient aux groupes adjacents alliés 
							groups.add(Group(game, player, stones))

							# Changement de joueur
							player, opponent = opponent, player
							if player == 'b':
								text = "Au tour de noir"
							else:
								text = "Au tour de blanc"

						else:
							text = "Suicide, coup interdit!"

					else:
						text = "Case déjà occupée!"

					# On met à jour les groupes
					if match_running:
						for group in groups:
							group.update_state(game)
					else:
						if opponent == 'w':
							winner = "blanc"
						else:
							winner = "noir"
						for group in groups:
							if group.color == player:
								group.state = 0
							else:
								group.state = 5
						text = "Victoire de {}!".format(winner)
						display_border()

	if game_running:
		pygame.time.wait(3000)
		text = "Cliquez pour rejouer"
		display_border()
		another_match = True
		while another_match:
			for event in pygame.event.get():
				if event.type == QUIT:
					game_running = another_match = False
				elif event.type == MOUSEBUTTONUP:
					another_match = False
