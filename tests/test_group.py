""" Ce fichier contient les tests de la classe Group """

import sys

sys.path[:0] = ["../"]
from group import Group
from game import Game

class TestGroup:
	# Initialisation de la partie et du groupe pour pouvoir en tester les attributs
	stones_position = [(0, 5), (1, 5), (1, 6), (0, 7), (1, 7)]
	GAME = Game(13)
	for stone in stones_position:
		GAME.add_stone('b', stone)
	# Pierres supplémentaires pour simuler une partie
	GAME.add_stone('b', (2, 8))
	GAME.add_stone('w', (0, 4))
	GAME.add_stone('w', (1, 4))
	GAME.add_stone('w', (2, 6))
	GAME.add_stone('w', (2, 7))
	GROUP = Group(GAME, 'b', stones_position)

	def test_update_state(self):
		self.GROUP.update_state(self.GAME)
		assert self.GROUP.state == 2
