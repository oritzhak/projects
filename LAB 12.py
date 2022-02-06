from random import randint
from time import sleep
print('''Welcome! This is Lotto Game!!!
Instructions
***each game cost 3$   ****************
***Insert how much money do you have***
****On each round, random 6 numbers****
*** If you guess the winner's numbers
number 6 = won 1000$
number 5 = won 500$
number 4 = won 100$
number 3 = won 50$
number 2 = won 25$
number 1 = won 10$
GOOD LUCK AND HAVE FUN!!!!
''')
sleep(3)
pot = int(input('how much money do you have?\n'))
turns = pot // 3
pot = pot - (turns*3)
print(f'\n.......you have {turns} turns!!!!!!!!')
sleep(2)


for i in range(turns):
    sleep(2)
    print('\n.......rolling 6 random numbers.........')
    numbers = []
    while len(numbers) < 6:
        n = randint(1, 37)
        if n in numbers:
            continue
        else:
            numbers.append(n)
    print(numbers)
    if 6 in numbers:          # you can only check one number no more
        pot += 1000
        print('you won 1000$')
    elif 5 in numbers:
        pot += 500
        print('you won 500$')
    elif 4 in numbers:
        pot += 100
        print('you won 100$')
    elif 3 in numbers:
        pot += 50
        print('you won 50$')
    elif 2 in numbers:
        pot += 25
        print('you won 25$')
    elif 1 in numbers:
        pot += 10
        print('you won 10$')
    else:
        print('you lost')
sleep(3)
print(f'your pot is {pot}$')



