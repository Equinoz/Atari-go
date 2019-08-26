#!/usr/bin/python3.6
# -*- coding:Utf-8 -*-

""" Interface console temporaire pour tester les fonctionnalitées du programme """

from game import Game
from group import Group
from functions import *

game_running = True
game = Game(13)
groups = set()
player = 'b'
opponent = 'w'

print("\n")
print(game)

while game_running:
	valid_move = False
	while not valid_move:
		# On vérifie que les coordonnées saisies soient cohérentes avec la taille du plateau
		x = y = -1
		while (x < 0 or x >= game.size) or (y < 0 or y >= game.size):
			print("\nAu tour du joueur {}:\n".format(player))
			x = int(input("x = "))
			y = int(input("y = "))
		position = x, y

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
						game_running = False

				# On crée le nouveau groupe avec la liste éventuelle des pierres qui appartenaient aux groupes adjacents alliés 
				groups.add(Group(game, player, stones))
				valid_move = True

			else:
				print("Suicide, coup interdit!\n")

		else:
			print("Cette case est déjà occupée par une autre pierre\n")

	# Changement de joueur
	player, opponent = opponent, player

	# On met à jour les groupes et on les affiche
	for group in groups:
		group.update_state(game)
	print(game)

	# Vérificateur de groupes
	print("\n")
	for index, group in enumerate(groups):
		print("Groupe {}: couleur: {}, pierres: {}, état: {}".format(index + 1, group.color, group.stones, group.state))
	print("\n")

print("Le joueur {} a gagné!".format(opponent))
