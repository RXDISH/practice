import random

def play():
    user = input("What's your choice?'rock' for rock, 'paper' for paper, 'scissors' for scissors\n")
    computer = random.choice(['rock','paper','scissors'])

    if user == computer:
      return 'tie womp womp'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You Win!'

    return 'You Lost!'

def is_win(player, opponent):
   # return true if player wins
   # r > s, s > p, p > r
   if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
     return True
   
print(play())