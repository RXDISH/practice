player = ''
computer = ''
import random

print('--------------------')
print('Rock, Paper,Scissors')
print('--------------------')

print('1) ✊')
print('2) ✋')
print('3) ✌️')

player = int(input('Select a number: '))

computer = (random.randint(1,3))
# r > s / s > p / p > r

if computer == 1:
    print('CPU chose: ✊')
elif computer == 2:
    print('CPU chose: ✋')
else:
    print('CPU chose: ✌️')

if player == 1:
    print('You chose: ✊')
elif player == 2:
    print('You chose: ✋')
else:
    print('You chose: ✌️')


if (player == 1 and computer == 3) or (player == 3 and computer == 2) or (player == 2 and computer == 1):
    print('You won!')
elif player == computer:
    print('You tied!')
else:
    print('The CPU won!')