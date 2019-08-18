from game import Game
from group import Group

game = Game(9)
print(game)
game.add_stone('b', (0, 0))
game.add_stone('w', (2, 8))
game.add_stone('w', (2, 7))
game.add_stone('w', (2, 6))
game.add_stone('w', (3, 8))
print(game)
group = [(2, 8), (2, 7), (2, 6), (3, 8)]
game.remove_group(group)
print(game)
print("***************")
stones = [(6, 6), (7, 6), (8, 6), (6, 7), (6, 8)]
for stone in stones:
	game.add_stone('b', stone)
game.add_stone('w', (5, 6))
game.add_stone('w', (5, 7))
game.add_stone('w', (7, 7))
game.add_stone('w', (7, 8))
game.add_stone('w', (8, 7))
game.add_stone('w', (5, 8))
groupe1 = Group(game, 'b', stones)
print(game)
print(groupe1.state)
