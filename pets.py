# This file contains the definition of the Pet class and associated methods.

class Pet(object):
    """Represents a pet.
    
    An instance of this class contains the data to describe a pet: Its age, its
    sadness, its value, what types of food it can eat, and its needs. It also
    contains methods which grow it, check if it dies or changes dimension,
    etc., return a list of cards a player must draw. """

    def __init__(self, name, needs_list, price_list, diet, age=2):
    	"""Initialize the pet.
	
	Expects a string name, a list of needs and a list of prices, both
	full-length and in order with respect to the age of the pet. Diet
	should be a string - omnivore, carnivore, or herbivore. Age should be
	an integer between 2 and the length of the needs & price lists."""
    	self.name = name
	self.needs_list = needs_list
	self.price_list = price_list
	self.age = age

	diet_cases = {
			'omnivore': [True, True],
			'carnivore': [True, False],
			'herbivore': [False, True],
	}

	[self.carnivore, self.herbivore] = diet_cases.get(diet.lower())

    def growUp(self):
    	"""docstring for growUp"""
    	pass
