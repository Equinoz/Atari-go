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

print("\n")
print(game)

while game_running:
	valid_move = False
	while not valid_move:
		x = y = -1
		while (x < 0 or x >= game.size) or (y < 0 or y >= game.size):
			print("\nAu tour du joueur {}:\n".format(player))
			x = int(input("x = "))
			y = int(input("y = "))
		position = x, y

		if point_is_empty(game, position):
			adjacent_groups = has_groups(game, groups, player, position)
			liberties = has_liberties(game, position)

			if not adjacent_groups and liberties:
				stone = [position]
				groups.add(Group(game, player, stone))
				valid_move = True

			elif adjacent_groups and (not_in_atari(adjacent_groups) or liberties):
				stones = [position]
				for group in adjacent_groups:
					stones.extend(group.stones)
					groups.remove(group)
				groups.add(Group(game, player, stones))
				valid_move = True

			else:
				print("Suicide, coup interdit!\n")

		else:
			print("Cette case est déjà occupée par une autre pierre\n")

	for group in groups:
		if group.state == 0:
			game.remove_group(group.stones)
			print("Le joueur {} a gagné!".format(player))
			game_running = False

	print(game)

	# Vérificateur de groupes
	print("\n")
	for index, group in enumerate(groups):
		print("Groupe {}: couleur: {}, pierres: {}, libertées: {}, état: {}".format(index + 1, group.color, group.stones, group.liberties, group.state))
	print("\n")

	if player == 'b':
		player = 'w'
	else:
		player = 'b'
