#!/usr/bin/python3

class Animal:

	def __init__(self, name, species, age):

		self.name = name
		self.species = species
		self.age = age

	def __testInput(self, prop, value):
		"""
		Test function for data types
		"""
		if type(value) is not str:
			raise TypeError("species must be an str")

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__name = value

	@property
	def species(self):
		return self.__species

	@species.setter
	def species(self, value):
		if value != "Aquatic" and value != "Terrestrial":
			raise ValueError("Only availables species: Aquatic or Terrestrial")

		self.__species = value

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, value):
		if not isinstance(value, int):
			raise TypeError("species must be an int")
		if value <= 0:
			raise ValueError("age must be > 0")
		
		self.__age = value

	def tell(self):
		'''Tell my details.'''
		print('Name:"{}" Specie:"{}" Age:"{}"'.format(self.name, self.species, self.age))

	def move(self):
		if self.__species == "Aquatic":
			print(f"{self.__name} is {self.__species} and it's swimming!")
		if self.__species == "Terrestrial":
			print(f"{self.__name} is {self.__species} and it's running!")

	def show(self):
		print(f"My name is {self.__name}")

	
	def sound(self):
		if self.__species == "Aquatic":
			print(" Glu Glu!!")
		if self.__species == "Terrestrial":
			print("Tacatas tacatas Tacatas")


class Aquatic(Animal):
	'''Specie type Aquitic.'''

	def __init__(self, name, species, age = 300):
		Animal.__init__(self, name, species, age)

		print('(Initialized Aquitic Animal: {})'.format(self.name))

	def tell(self):
		Animal.tell(self)

class Terrestrial(Animal):
	'''Specie type Terrestrial.'''

	def __init__(self, name, species = "Terrestrial", age = 1000):
		Animal.__init__(self, name, species, age)
		print('(Initialized Terrestrial Animal: {})'.format(self.name))

	def tell(self):
		Animal.tell(self)

"""Objects of the class"""
Starfish = Aquatic('Estrellita', "Aquatic", 30000)
Rabbit = Terrestrial('Alicia', "Terrestrial", 70000)
Seal = Aquatic("Foquita", "Aquatic", 124)
Goat = Terrestrial("Cabrita", "Terrestrial", 247)

# prints a blank line
print()

Rabbit.show()
Rabbit.move()
Rabbit.sound()
print()

Starfish.show()
Starfish.move()
Starfish.sound()
print()

Seal.show()
Seal.move()
Seal.sound()
print()

Goat.show()
Goat.move()
Goat.sound()
print()

members = [Starfish, Rabbit, Seal, Goat]
for member in members:
    # Works for both Teachers and Students
    member.tell()