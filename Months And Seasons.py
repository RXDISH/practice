month = int(input('Please enter the month (1-12): '))

if month == range(1, 4):
  print ('Winter')
elif month == range(4, 7):
  print ('Spring')
elif month == range(7, 10):
  print ('Summer')
elif month == range(10, 13):
  print ('Autumn')
else:
  print('That number is invalid, just like you for trying to break my code <3')
