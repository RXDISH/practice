from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

radius = 0

random_planet = ch(planets)

if random_planet == 'Mercury':
  radius = 2440
elif random_planet == 'Venus':
  radius = 6052
elif random_planet == 'Earth':
  radius = 6371
elif random_planet == 'Mars':
  radius = 3390
elif random_planet == 'Saturn':
  radius = 58232
else:
  print('Oops! An error occoured.')

planet_area = 4 * pi * radius * radius

print(f'Area of {random_planet}: {planet_area} sq mi')