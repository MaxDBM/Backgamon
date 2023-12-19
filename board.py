# Board Class
# Stores the board state and provides methods to manipulate it
class Board:
	# class variables
	# Store how many pieces are in each location
	blackPieceLocations = [0 for _ in range(24)]
	whitePieceLocations = [0 for _ in range(24)]

	# How many pieces are in the jail
	blackJail = 0
	whiteJail = 0

	# Dice number
	dice = (1, 1)

	# Store who's turn it is
	isBlackTurn = False

	# constructor
	def __init__(self):
		# Set up the board
		self.whitePieceLocations[0] = 2
		self.whitePieceLocations[11] = 5
		self.whitePieceLocations[16] = 3
		self.whitePieceLocations[18] = 5
		self.blackPieceLocations[5] = 5
		self.blackPieceLocations[7] = 3
		self.blackPieceLocations[12] = 5
		self.blackPieceLocations[23] = 2

	# methods

	# set the self.dice touple to two random numbers between 1 and 6
	def rollDice(self):
		# TODO: implement dice rolling

		
		return # nothing

	# print the board
	def printBoard(self):
		print("Black: ", end="")
		for i in range(24):
			print(self.blackPieceLocations[i], end=" ")
		print("\nWhite: ", end="")
		for i in range(24):
			print(self.whitePieceLocations[i], end=" ")
		print("\n")
