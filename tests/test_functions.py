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
group3 = [(4, 2), (5, 2)]
group4 = [(3, 3), (3, 4)]

group1_b = Group(game, 'b', group1)
group2_b = Group(game, 'b', group2)
group1_w = Group(game, 'w', group3)
group2_w = Group(game, 'w', group4)

groups = set()
groups.update([group1_b, group2_b, group1_w, group2_w])

for group in groups:
	for stone in group.stones:
		game.add_stone(group.color, stone)


def test_point_is_empty():
	assert point_is_empty((5, 4)) == False
	assert point_is_empty((3, 4)) == False
	assert point_is_empty((1, 1)) == True
	assert point_is_empty((5, 6)) == True

def test_examine_adjacent_points():
	assert examine_adjacent_points('b', (4, 5)) == [(4, 4), (5, 5), (4, 6)]
	assert examine_adjacent_points('b', (6, 4)) == [(5, 4)]
	assert examine_adjacent_points('w', (4, 3)) == [(4, 2), (3, 3)]
	assert examine_adjacent_points('.', (6, 4)) == [(6, 3), (7, 4), (6, 5)]
	assert examine_adjacent_points('.', (8, 0)) == [(8, 1), (7, 0)]
	assert examine_adjacent_points('.', (4, 3)) == []

def test_has_liberties():
	assert has_liberties((4, 3)) == False
	assert has_liberties((4, 5)) == True
	assert has_liberties((6, 6)) == True

def test_has_groups():
	assert has_groups('b', (4, 3)) == {group1_b}
	assert has_groups('b', (4, 5)) == {group1_b, group2_b}
	assert has_groups('b', (6, 4)) == {group1_b}
	assert has_groups('w', (4, 3)) == {group1_w, group2_w}
	assert has_groups('w', (4, 5)) == {}
