# This file contains the definition of the Pet class and associated methods.

class Pet(object):
    """Represents a pet.
    
    An instance of this class contains the data to describe a pet: Its age, its
    sadness, its value, what types of food it can eat, and its needs. It also
    contains methods which grow it, check if it dies or changes dimension,
    etc., return a list of cards a player must draw. """

    def __init__(self, name, needs_list, diet, age=2):
    	"""Initialize the pet.
	
	Expects a string name, a list of needs,	full-length and in order with
	respect to the age of the pet. Diet should be a string - omnivore,
	carnivore, or herbivore. Age should be	an integer between 2 and the
	length of the needs & price lists. Defaults to age 2 if age is omitted.
	Defaults to standard pricing and aging, but if these are set to other
	values nothing should break."""
        
	# Default pricing based on pet diet.
        carnivore_pricing = [0,0,0,3,4,5,6]
	herbivore_pricing = [0,0,0,2,3,4,5]
	omnivore_pricing = [0,0,0,1,2,3,4]
	
	# Default pet aging.
	self.aging_chart = [0,0,2,2,1,1,1,0]

        # Assign basic attributes.
    	self.name = name
	self.needs_list = needs_list
	self.age = age
	self.misery = 0
	self.mutations = 0

        # Create a diet dictionary.
	diet_cases = {
			'Omnivore': [True, True, omnivore_pricing],
			'Carnivore': [True, False, carnivore_pricing],
			'Herbivore': [False, True, herbivore_pricing],
	}

        # Set carnivore and herbivore flags.
	[self.carnivore, self.herbivore] = diet_cases.get(diet)

        # Set pricing based on diet defaults.
	self.pricing_chart = diet_cases.get(diet)[-1]

    def growUp(self, i=None):
    	"""Age the pet according to its growth chart or the passed argument.
	
	If no arguments are given, ages the pet according to its growth chart.
	If an argument is given, ages the pet that many steps instead."""

	if i = None:
		i = self.aging_chart[self.age]
	
	self.age += i

    def currentNeeds(self):
    	"""Return a list of card types this pet needs based on its age."""
    	
	return self.needs_list[:self.age]

    def checkStatus(self):
    	"""Check if the pet dies due to mutation or misery."""
	goes_away = False

	if self.mutations > 1:
		goes_away = True
	
	if self.misery > self.age:
		goes_away = True
	
	return goes_away

