""" Ce fichier contient les tests du module "functions" """

import sys

sys.path[:0] = ["../"]
from game import Game
from group import Group
from functions import *

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

# Initialisation du plateau
for group in groups_b:
	for stone in group:
		game.add_stone('b', stone)

for group in groups_w:
	for stone in group:
		game.add_stone('w', stone)

# Initialisation des groupes
group1_b = Group(game, 'b', group1)
group2_b = Group(game, 'b', group2)
group3_b = Group(game, 'b', group3)
group1_w = Group(game, 'w', group4)
group2_w = Group(game, 'w', group5)
group3_w = Group(game, 'w', group6)

groups = set()
groups.update([group1_b, group2_b, group3_b, group1_w, group2_w, group3_w])
for group in groups:
	group.update_state(game)


def test_point_is_empty():
	assert point_is_empty(game, (5, 4)) == False
	assert point_is_empty(game, (3, 4)) == False
	assert point_is_empty(game, (1, 1)) == True
	assert point_is_empty(game, (5, 6)) == True

def test_examine_adjacent_points():
	assert examine_adjacent_points(game, 'b', (4, 5)) == [(4, 4), (5, 5), (4, 6)]
	assert examine_adjacent_points(game, 'b', (6, 4)) == [(5, 4)]
	assert examine_adjacent_points(game, 'w', (4, 3)) == [(4, 2), (3, 3)]
	assert examine_adjacent_points(game, '.', (6, 4)) == [(6, 3), (7, 4), (6, 5)]
	assert examine_adjacent_points(game, '.', (8, 0)) == [(8, 1), (7, 0)]
	assert examine_adjacent_points(game, '.', (4, 3)) == []

def test_has_liberties():
	assert has_liberties(game, (4, 3)) == False
	assert has_liberties(game, (4, 5)) == True
	assert has_liberties(game, (6, 6)) == True

def test_has_groups():
	assert has_groups(game, groups, 'b', (4, 3)) == {group1_b}
	assert has_groups(game, groups, 'b', (4, 5)) == {group1_b, group2_b}
	assert has_groups(game, groups, 'b', (6, 4)) == {group1_b}
	assert has_groups(game, groups, 'w', (4, 3)) == {group1_w, group2_w}
	assert has_groups(game, groups, 'w', (4, 5)) == set()

def test_in_atari():
	assert in_atari({group3_b}) == True
	assert in_atari({group1_b, group2_b, group3_b}) == True
	assert in_atari({group2_w, group3_w}) == False

def test_not_in_atari():
	assert not_in_atari({group3_b}) == False
	assert not_in_atari({group1_b, group2_b, group3_b}) == True
	assert not_in_atari({group2_w, group3_w}) == True
