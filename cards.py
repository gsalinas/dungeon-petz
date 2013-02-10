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
    
    def __repr__(self):
            """Define the string representation of a Card object."""

            return self.color + " " + self.symbol

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

    def drawCard(self):
        """Return a card from the deck, reshuffling if needed."""
        if not self.draw_pile:
            self.shuffleDeck()

        return self.draw_pile.pop(0)

class DeckGroup(object):
    """A group of several decks. Manages discard color and piles."""

    def __init__(self):
        """Initialize the deck group.
        
        For now the default decks are set up and those defaults are part of
        this class description."""
        
        redDist = [("Anger",12),("Play",4),("Hunger",3),("Poop",3),("Sickness",2)]
        greenDist = [("Hunger",16),("Poop",10),("Anger",4),("Sickness",2)]
        yellowDist = [("Play",12),("Magic",4),("Hunger",2),("Poop",2),("Sickness",4)]
        purpleDist = [("Magic",12),("Play",4),("Anger",4),("Sickness",4)]
        blueDist = [("Potion",5)]

        self.red_deck = Deck("Red",redDist)
        self.green_deck = Deck("Green",greenDist)
        self.yellow_deck = Deck("Yellow",yellowDist)
        self.purple_deck = Deck("Purple",purpleDist)
        self.blue_deck = Deck("Blue",blueDist)
        
        self.test_string = "Test String"
        self.deck_dict = {
                "Red": self.red_deck,
                "Green": self.green_deck,
                "Yellow": self.yellow_deck,
                "Purple": self.purple_deck,
                "Blue": self.blue_deck,
        }

    def drawCard(self, color):
        """Return a card from the deck of the given color."""
        return self.deck_dict.get(color).drawCard()

    def drawSeveralCards(self, needs_list):
        """Return a list of cards of the appropriate colors."""
        return_list = []

        for color in needs_list:
            return_list.append(self.drawCard(color))

        return return_list

    def discardCards(self, cards_list):
        """Discard the cards in the provided list to the appropriate decks.
        
        Origin of the cards to be discarded is responsible for removing
        references to them from player hands, etc."""
        for card in cards_list:
            deck = self.deck_dict.get(card.color)
            deck.discard_pile.append(card)
