from functions import examine_adjacent_points

class Group:
	""" Reçoit une partie "game", une couleur et une liste de coordonnées de pierres et initialise un groupe de pierres
	Attributs: "color" la couleur du groupe, "stones" la liste des coordonnées des pierres le composant et "state" un indice de 0 à 5 indiquant la bonne santé du groupe
	Méthode: "update_state" qui mets à jour l'indice "state" de 0 à 4

	"""
	def __init__(self, game, color, stones):
		self.color = color
		self.stones = stones
		self.state = 5
		# On met à jour le plateau de jeu en ajoutant la nouvelle pierre, dont les coordonnées sont dans le premier tuple de "stones"
		game.add_stone(self.color, self.stones[0])

	def update_state(self, game):
		""" Mets à jour l'attribut "state" du groupe
		Reçoit une partie "game"
		Définition des différents états du groupe:
		4: au moins deux fois plus de libertés que de pierres composant le groupe
		3: entre deux fois et une fois plus de libertés que de pierres composant le groupe
		2: moins de libertés que de pierres composant le groupe
		1: plus qu'une seule liberté (groupe en atari)
		0: groupe capturé

		"""
		# Utilisation d'un set pour recenser les cases adjacentes vides en évitant les doublons
		free_points = set()
		for stone in self.stones:
			adjacent_liberties = examine_adjacent_points(game, '.', stone)
			for liberty in adjacent_liberties:
				free_points.add(liberty)
		liberties = len(free_points)

		# Mise à jour de l'attribut state
		ratio = liberties / len(self.stones)
		if ratio > 2:
			self.state = 4
		elif ratio >= 1 and ratio <= 2:
			self.state = 3
		elif ratio < 1:
			self.state = 2
		if liberties < 2:
			self.state = liberties
