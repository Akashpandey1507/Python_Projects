
import random as r

while True:
# Where "r" = Random
    Guessing_Number = int(input('Enter the Your Number: '))
    Random_Number = r.randrange(1,101)

    if Guessing_Number > Random_Number:
        print('The Guessing Number is too High')
        break
    elif Guessing_Number < Random_Number:
        print('The Guessing Number is too Low')
        break
    else:
        print(f'You are win because the Guessing Number: {Guessing_Number} and Random Number: {Random_Number} are matching.')
        break