""" Ce fichier contient les tests de la classe Game """

import sys

sys.path[:0] = ["../"]
from game import Game

class TestGame:
	GAME = Game(13)
	GAME.board[2] = ['.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', 'W', '.', '.']
	GAME.board[3] = ['.', '.', 'B', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '.']
	GAME.board[6] = ['.', '.', '.', '.', '.', '.', 'B', 'B', '.', '.', '.', '.', '.']
	GAME.board[8] = ['.', '.', '.', '.', '.', 'B', 'B', '.', '.', '.', '.', '.', '.']
	GAME.board[9] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.']
	GAME.board[10] = ['.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
	GAME.board[11] = ['.', '.', '.', '.', '.', 'W', '.', '.', 'W', '.', '.', '.', '.']

	def test_add_stone(self):
		self.GAME.add_stone('b', (6, 7))
		self.GAME.add_stone('w', (2, 7))
		assert self.GAME.board[7] == ['.', '.', 'W', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.']

	def test_remove_group(self):
		stones_position = [(6, 6), (7, 6), (6, 7), (5, 8), (6, 8)]
		self.GAME.remove_group(stones_position)
		assert self.GAME.board[6] == ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
		assert self.GAME.board[7] == ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
		assert self.GAME.board[8] == ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
