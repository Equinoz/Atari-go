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

print("Ok")
# Initialisation d'un plateau et de groupes pour tester les fonctions
game = Game(9)
group1 = [(5, 3), (4, 4), (5, 4), (5, 5)]
group2 = [(3, 6), (4, 6)]
group3 = [(7, 8), (8, 8)]
group4 = [(4, 2), (5, 2)]
group5 = [(3, 3), (3, 4)]
group6 = [(7, 7), (8, 7)]

groups_b = [group1, group2, group3]
groups_w = [group4, group5, group6]

for group in groups_b:
	for stone in group:
		game.add_stone('b', stone)

for group in groups_w:
	for stone in group:
		game.add_stone('w', stone)

group1_b = Group(game, 'b', group1)
group2_b = Group(game, 'b', group2)
group3_b = Group(game, 'b', group3)
group1_w = Group(game, 'w', group4)
group2_w = Group(game, 'w', group5)
group3_w = Group(game, 'w', group6)

groups = set()
groups.update([group1_b, group2_b, group3_b, group1_w, group2_w, group3_w])

print(game)

# Vérificateur de groupes
for index, group in enumerate(groups):
	print("Groupe {}: couleur: {}, pierres: {}, libertées: {}, état: {}".format(index, group.color, group.stones, group.liberties, group.state))
