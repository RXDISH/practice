class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

print(vars(bobs_burgers))


class City: 
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

nyc = City('New York City', 'New York', 8000000, 'Catacombs, Museum')

print(vars(nyc))