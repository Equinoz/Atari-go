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

	def add_stone(self):
		GAME.add_stone('b', (7, 6))
		GAME.add_stone('w', (7, 2))
		assert GAME.board[7] == ['.', '.', 'W', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.']

	def remove_group(self):
		stones_position = list((6, 6), (6, 7), (7, 6), (8, 5), (8, 6))
		GAME.remove_group(stones_position)
		assert GAME.board[6] == ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
		assert GAME.board[7] == ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
		assert GAME.board[8] == ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
