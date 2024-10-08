# entering a PIN demo

print('BANK OF CODEX')

pin = int(input('Please enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Please enter yout PIN again: '))

if pin == 1234:
  print('PIN accepted!')