from functions import examine_adjacent_points

class Group:
	""" Reçoit une partie "game", une couleur et une liste de coordonnées de pierres et initialise un groupe de pierres
	Attributs: "game" la partie où se constituent les groupes, "color" la couleur du groupe, "stones" la liste des coordonnées des pierres le composant, "liberties" le nombre de libertés dont le groupe dispose et "state" un indice de 0 à 5 indiquant la bonne santé du groupe
	Méthodes: "count_liberties" méthode privée permettant de compter le nombre de libertés du groupe et "evaluate_state" méthode privée qui détermine l'indice de 0 à 5

	"""
	def __init__(self, game, color, stones):
		self.game = game
		self.color = color
		self.stones = stones
		# On met à jour le plateau de jeu en ajoutant la nouvelle pierre, dont les coordonnées sont dans le premier tuple de "stones"
		self.game.add_stone(self.color, self.stones[0])
		self.liberties = self.__count_liberties()
		self.state = self.__evaluate_state()

	def __count_liberties(self):
		# Utilisation d'un set pour recenser les cases adjacentes vides en évitant les doublons
		free_points = set()
		for stone in self.stones:
			adjacent_liberties = examine_adjacent_points(self.game, '.', stone)
			for liberty in adjacent_liberties:
				free_points.add(liberty)
		return len(free_points)

	def __evaluate_state(self):
		""" Définition des différents états du groupe
				4: au moins deux fois plus de libertés que de pierres composant le groupe
				3: entre deux fois et une fois plus de libertés que de pierres composant le groupe
				2: moins de libertés que de pierres composant le groupe
				1: plus qu'une seule liberté (groupe en atari)
				0: groupe capturé

		"""
		if self.liberties == 0:
			return 0
		elif self.liberties == 1:
			return 1
		ratio = self.liberties / len(self.stones)
		if ratio < 1:
			return 2
		if ratio >= 1 and ratio <= 2:
			return 3
		if ratio > 2:
			return 4
