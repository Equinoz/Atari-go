class Game:
	"""	Reçoit un entier 'n' et initialise une nouvelle partie avec un plateau de dimensions n x n
	Attributs: "size" indiquant la dimension du plateau et "board" étant une liste de listes figurant les pierres noires, blanches et les intersections encore libres
	Méthodes: "add_stone" ajoute une pierre sur le board et "remove_group" supprime une liste de pierres selon leurs coordonnées
 	
	"""
	def __init__(self, size):
		self.size = size

	def add_stone(self, color, position):
		pass

	def remove_group(self, stones_position):
		pass

	def __str__(self): # Méthode temporaire, à supprimer lors de la mise en place de l'interface graphique
		pass
