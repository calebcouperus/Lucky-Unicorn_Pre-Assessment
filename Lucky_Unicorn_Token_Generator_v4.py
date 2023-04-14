"""Component 3 (random tokens) v4
Calculate percentages to ensure the odds favour the house
5% unicorns, 30% donkeys, and the remaining 65% horses/Zebras
"""

import random


STARTING_BALANCE = 100
balance = STARTING_BALANCE

# testing loop to generate 100 tokens
for item in range(10):
    number = random.randint(1, 100)

    # adjust balance
    # if the number is between 1 and 5
    # user gets a unicorn (add $4 to balance)
    if 1 <= number <= 5:
        token = "Unicorn"
        balance += 4

    elif 6 <= number <= 36:
        token = 'Donkey'
        balance -= 1

    else:
        if number % 2 == 0:
            token = 'Zebra'
            balance -= 0.5

        else:
            token = 'Horse'
            balance -= 0.5

    # output
    print(f'Token: {token}, Balance: ${balance:.2f}')

print()
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance}")
