# starting scores

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('-----------------------')
print('Harry Potter House Quiz')
print('-----------------------')

# question 1
print('Q1) Do you like Dawn or Dusk?')
print('1) Dawn')
print('2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print('please type an answer in the correct number format :)')

# question 2
print('Q2) When I’m dead, I want people to remember me as...')
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin +=2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('please type an answer in the correct number format :)')

# question 3
print('Q3) Which kind of instrument most pleases your ear?')
print('1) The Violin')
print('2) The Trumpet')
print('3) The Piano')
print('4) The Drum')
answer = int(input('Enter answer (1-4): '))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print('please type an answer in the correct number format :)')

print('Final Scores')

print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

# calculates which house has the highest number of points

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)
print('Your House Is...')

if gryffindor == most_points:
  print('🦁 Gryffindor!')
elif ravenclaw == most_points:
  print('🦅 Ravenclaw!')
elif hufflepuff == most_points:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')