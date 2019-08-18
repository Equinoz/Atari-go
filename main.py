from game import Game
from group import Group
from functions import *

game = Game(13)

stones = [('b', (1, 1)), ('b', (0, 2)), ('b', (3, 4)), ('w', (0, 4)), ('w', (0, 5)), ('w', (4, 6)), ('w', (7, 2)), ('w', (5, 3))]
for stone in stones:
	game.add_stone(stone[0], stone[1])
print(game)
print("*******************")

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
groups.add(group1_b)
groups.add(group2_b)
groups.add(group1_w)
groups.add(group2_w)

for group in groups:
	for stone in group.stones:
		game.add_stone(group.color, stone)
print(game)
