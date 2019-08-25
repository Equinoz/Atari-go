""" Fichier de fonctions d'Atari-go """

def point_is_empty(game, position):
	""" Vérifie que l'intersection passée en paramètre est vide
	Reçoit une partie, un tuple de coordonnées et renvoie un booléen

	"""
	if game.board[position[1]][position[0]] == '.':
		return True
	else:
		return False

def examine_adjacent_points(game, character, position):
	""" Vérifie la présence d'un type d'élément donné sur les intersections adjacentes
	Reçoit une partie, un caractère, un tuple de coordonnées et renvoie une liste de tuples de coordonnées

	"""
	x, y = position
	character = character.upper()
	points = []
	# On vérifie que la pierre ne se situe pas sur un bord pour tester la case adjacente concernée
	if y > 0 and game.board[y-1][x] == character:
		points.append((x, y-1))
	if x < game.size - 1 and game.board[y][x+1] == character:
		points.append((x+1, y))
	if y < game.size - 1 and game.board[y+1][x] == character:
		points.append((x, y+1))
	if x > 0 and game.board[y][x-1] == character:
		points.append((x-1, y))
	return points

def has_liberties(game, position):
	""" Vérifie la présence de libertés pour une position donnée
	Reçoit une partie, un tuple de coordonnées et renvoie un booléen

	"""
	liberties = examine_adjacent_points(game, '.', position)
	if len(liberties) > 0:
		return True
	else:
		return False

def has_groups(game, groups, color, position):
	""" Vérifie la présence de groupes adjacents à une position donnée
	Reçoit une partie, une couleur, un tuple de coordonnées et renvoie un set de groupes

	"""
	stones = examine_adjacent_points(game, color, position)
	adjacent_groups = set()
	for stone in stones:
		for group in groups:
			if stone in group.stones:
				adjacent_groups.add(group)
	return adjacent_groups

def in_atari(groups):
	""" Vérifie dans un set donné si au moins un groupe est en atari
	Reçoit un set de groupes et renvoie un booléen

	"""
	for group in groups:
		if group.state == 1:
			return True
	return False

def not_in_atari(groups):
	""" Vérifie dans un set donné si au moins un groupe n'est pas en atari
	Reçoit un set de groupes et renvoie un booléen

	"""
	for group in groups:
		if group.state > 1:
			return True
	return False
