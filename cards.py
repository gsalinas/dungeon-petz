# This file contains the defintion of the Card and Deck classes and associated
# methods.
import random

class Card(object):
	"""Represents a Dungeon Petz card.

	An instance of this class is a single card from one of the Need decks.
	A card has attributes for its color, its primary symbol, and its
	secondary symbol if any."""

	# Also contains whatever I decide I need to make advanced cards work.

	def __init__(self, color, symbol, secondary_symbol=None):
		"""Initialize the card.
		
		Expects a string for card color, a string for card symbol, and
		an optional string for a secondary card symbol."""

		self.color = color
		self.symbol = symbol
		
		if secondary_symbol != None:
			self.has_secondary = True
			self.secondary_symbol = secondary_symbol
		else:
			self.has_secondary = False

class Deck(object):
	"""Represents a Needs deck of a particular color.

	An instance of this class is a single deck of a particular color. Other
	parts of the code can draw cards from a deck and discard cards to a
	deck, and it will automatically shuffle itself as needed."""

	def __init__(self, color, distribution):
		"""Initialize the deck.
		
		Expects a string for the deck color and a list of string /
		number pairs for the symbol distribution."""

		self.color = color
		self.draw_pile = []
		self.discard_pile = []

		for x in distribution:
			symbol = x[0]
			number = x[1]

			for i in range(number):
				new_card = Card(self.color, symbol)
				self.draw_pile.append(new_card)

		self.shuffleDeck()

	def shuffleDeck(self):
		"""Add the discard pile back to the deck and reshuffle."""
		self.draw_pile.extend(self.discard_pile)
		self.discard_pile[:] = []
		random.shuffle(self.draw_pile)

