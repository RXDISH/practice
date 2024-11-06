import random

my_numbers = 0
winning_numbers = 0

# 'x' just leaves the variable blank
my_numbers = [random.randint(1,69) for x in range(5)]
winning_numbers = [random.randint(1,69) for x in range(5)]

# adds new numbers to same list
my_numbers.append(random.randint(1,26))
winning_numbers.append(random.randint(1,26))

print('My Numbers:', my_numbers)
print('Winning Numbers:', winning_numbers)