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
		if color == 'b':
			self.board[position[1]][position[0]] = 'B'
		else:
			self.board[position[1]][position[0]] = 'W'

	def remove_group(self, stones_position):
		for stone_position in stones_position:
			self.board[stone_position[1]][stone_position[0]] = '.'

	def __str__(self): # Méthode temporaire, à supprimer lors de la mise en place de l'interface graphique
		""" Affiche le contenu de l'attribut board, représentant le plateau de jeu """
		printed_board = ""
		for line in self.board:
			for chara in line:
				printed_board += " " + chara
			printed_board += "\n"
		return printed_board
