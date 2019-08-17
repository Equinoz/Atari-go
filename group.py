class Group:
	""" Reçoit une partie "game", une couleur et une liste de coordonnées de pierres et initialise un groupe de pierres
	Attributs: "game" la partie où se constituent les groupes, "color" la couleur du groupe, "stones" la liste des coordonnées des pierres le composant, "liberties" le nombre de libertés dont le groupe dispose et "state" un indice de 0 à 5 indiquant la bonne santé du groupe
	Méthodes: "count_liberties" méthode privée permettant de compter le nombre de libertés du groupe et "evaluate_state" méthode privée qui détermine l'indice de 0 à 5

	"""
	def __init__(self, game, color, stones):
		self.game = game
		self.color = color
		self.stones = stones
		self.liberties = self.__count_liberties()
		self.state = self.__evaluate_state()

	def __count_liberties(self):
		# self.game, self.stones...
		pass

	def __evaluate_state(self):
		""" Définition des différents états du groupe
				5: pas de contact avec les pierres adverses
				4: au moins deux fois plus de libertés que de pierres composant le groupe
				3: entre deux fois et une fois plus de libertés que de pierres composant le groupe
				2: moins de libertés que de pierres composant le groupe
				1: plus qu'une seule liberté (groupe en atari)
				0: groupe capturé

		"""
		pass
