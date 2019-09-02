#!/usr/bin/python3.6
# -*- coding:Utf-8 -*-

import pygame
from pygame.locals import *

from constants import *
from window import *
from game import Game
from group import Group
from functions import *

def main():
	""" Fonction principale """
	# Boucle principale
	game_running = True
	while game_running:
		# Initialisation d'une nouvelle partie
		game = Game(BOARD_SIZE)
		groups = set()
		player = 'b'
		opponent = 'w'
		text = "Au tour de noir"
		window = Window()
		window.display(groups, text)

		# Boucle de jeu principale
		match_running = True
		while match_running:
			pygame.time.Clock().tick(30)

			for event in pygame.event.get():
				if event.type == QUIT:
					game_running = match_running = False

				elif event.type == MOUSEBUTTONUP:
					x = round((event.pos[0]-BORDER)/INTERVAL)
					y = round((event.pos[1]-BORDER)/INTERVAL)
					position = (x, y)

					# L'emplacement cliqué doit être dans la zone du goban
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

								# Si la partie a encore cours on met à jour les groupes...
								if match_running:
									for group in groups:
										group.update_state(game)

									# ... et on change de joueur
									player, opponent = opponent, player
									text = "Au tour de noir" if player == 'b' else "Au tour de blanc"

								# Si la partie est finie on détermine le vainqueur et on met le statut des groupes à jour
								else:
									winner = "blanc" if player == 'w' else "noir"
									text = "Victoire de {}!".format(winner)
									for group in groups:
										if group.color == player:
											group.state = 5
										else:
											group.state = 0

							else:
								text = "Suicide, coup interdit!"

						else:
							text = "Case déjà occupée!"

						# Quoiqu'il en soit on rafraîchit la fenêtre
						window.display(groups, text)

		# Si la partie est finie mais que le script n'a pas été interrompu...
		if game_running:
			text = "Cliquez pour rejouer"
			pygame.time.wait(3000)
			window.display(groups, text)

			# ... on propose une nouvelle partie
			other_match = True
			while other_match:
				pygame.time.Clock().tick(30)
				for event in pygame.event.get():
					if event.type == QUIT:
						game_running = other_match = False
					elif event.type == MOUSEBUTTONUP or event.type == KEYDOWN:
						other_match = False

main()
