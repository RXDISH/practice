# user inputs height and credits
height = int(input('How tall are you?(cm):'))
credits = int(input('How many credits do you have?:'))

# correct height and credits
if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
# incorrect height and correct credits
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
# correct height and incorrect credits
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("Get tall and rich bozo")