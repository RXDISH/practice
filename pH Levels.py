import random
pH = (random.randint(0,14))

if pH > 7:
  print("Basic")
elif pH < 7:
  print("Acidic")
else:
  print("Neutral")