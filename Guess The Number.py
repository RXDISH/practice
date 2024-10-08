tries = 0

guess = 0

print(tries,'of 5 tries used')

while guess != 6 and tries < 5:
  guess = int(input('Guess the number: '))
  tries = tries + 1
  print(tries,'of 5 tries used')

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')