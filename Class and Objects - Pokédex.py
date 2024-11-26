class pokemon: 
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught


  def display_pokemon(self):
    print('Entry Number : ' + str(self.entry)) # if a number is written str() must be written around it
    print('Name : ' + self.name)
    print('Type : ' + self.types)
    print('Description : ' + self.description)
    print(self.name + ' ' + self.is_caught)
  
  def speak(self):
    print(self.name + ' ' + self.name + ' ' + ':D')

pikachu = pokemon(25, 'Pikachu', 'Electric', 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', 'has already been caught!')
bulbasaur = pokemon(1, 'Bulbasaur', 'Grass', 'A small, mainly turquoise amphibian Pokémon with red eyes and a green bulb on its back. It is based on a frog/toad, with the bulb resembling a plant bulb that grows into a flower as it evolves.', 'has already been caught!')
greeninja = pokemon(658, 'Greeninja', 'Water + Dark', 'Greninja evolves from Frogadier at level 36.', 'has not been caught!')

pikachu.display_pokemon()
pikachu.speak()

bulbasaur.display_pokemon()
bulbasaur.speak()

greeninja.display_pokemon()
greeninja.speak()