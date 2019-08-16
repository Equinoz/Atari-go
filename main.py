from game import Game

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
