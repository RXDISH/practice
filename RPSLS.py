player = ''
computer = ''
import random

print('------------------------------------')
print('------------------------------------')
print('Rock, Paper, Scissors, Lizard, Spock')
print('------------------------------------')
print('------------------------------------')

print('The Rules Are...')
print('----------------------------------------------------------------------')

print('Scissors cut Paper - Paper covers Rock - Rock crushes Lizard -')
print('Lizard poisons Spock - Spock smashes Scissors - Scissors beat Lizard -')
print('Lizard eats Paper - Paper disproves Spock - Spock vaporizes Rock -')
print('Rock breaks Scissors')

print('----------------------------------------------------------------------')
print('----------------------------------------------------------------------')

print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')
print('-------------------------------------------------------------------------------')
print('If you chose a number outside of this list you will given one randomly from 1-5')
print('-------------------------------------------------------------------------------')

player = int(input('Select a number: '))

computer = (random.randint(1,5))

# r > s / s > p / p > r / r > l / l > sp / sp > s / s > l / l > p / p > sp / sp > r

if computer == 1:
    print('CPU chose: ✊')
elif computer == 2:
    print('CPU chose: ✋')
elif computer == 3:
    print('CPU chose: ✌️')
elif computer == 4:
    print('CPU chose: 🦎')
else:
    print('CPU chose: 🖖')

if player == 1:
    print('You chose: ✊')
elif player == 2:
    print('You chose: ✋')
elif player:
    print('You chose: ✌️')
elif player == 4:
    print('You chose: 🦎')
else:
    print('You chose: 🖖')

# r > s / s > p / p > r / r > l / l > sp / sp > s / s > l / l > p / p > sp / sp > r

if (player == 1 and computer == 3) or (player == 3 and computer == 2) or (player == 2 and computer == 1) or (player == 1 and computer == 4) or (player == 4 and computer == 5) or (player == 5 and computer == 3) or (player == 3 and computer == 4) or (player == 4 and computer == 2) or (player == 2 and computer == 5) or (player == 5 and computer == 1):
    print('You won!')
elif player == computer:
    print('You tied!')
else:
    print('The CPU won!')