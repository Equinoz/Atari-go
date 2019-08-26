class Game:
	"""	Reçoit un entier 'n' et initialise une nouvelle partie avec un plateau de dimensions n x n
	Attributs: "size" indiquant la dimension du plateau et "board" étant une liste de listes figurant les pierres noires, blanches et les intersections encore libres
	Méthodes: "add_stone" reçoit un char et un tuple et ajoute une pierre sur le board et "remove_group" supprime une liste de pierres selon leurs coordonnées
 	
	"""
	def __init__(self, size):
		self.size = size
		# On initialise le nouveau board composé uniquement d'intersections vides dans un premier temps
		self.board = [['.'] * self.size for i in range(self.size)]
				
	def add_stone(self, color, position):
		self.board[position[1]][position[0]] = color.upper()

	def remove_group(self, stones_position):
		for point in stones_position:
			self.board[point[1]][point[0]] = '.'

	def __str__(self): # Méthode temporaire, à supprimer lors de la mise en place de l'interface graphique
		""" Affiche le contenu de l'attribut board, représentant le plateau de jeu """
		return "\n".join(" ".join(point for point in row) for row in self.board)
