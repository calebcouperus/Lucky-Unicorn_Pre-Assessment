"""Component 3 (random tokens) v3
format currency
Ensures odds favour the  house - 10% chance of Unicorn and 30% chance for each of Zebra, Donkey, and horse"""

import random

tokens = ["Unicorn",
          "Horse", "Donkey", "Zebra",
          "Horse", "Donkey", "Zebra",
          "Horse", "Donkey", "Zebra"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE

# testing loop to generate 100 tokens
for item in range(100):
    token = random.choice(tokens)

    # adjust balance
    if token == "Unicorn":
        balance += 4
    elif token == "Donkey":
        balance -= 1
    else:
        balance -= .50

    # output
    print(f"Starting balance = ${STARTING_BALANCE:.2f}")
    print(f"Final balance = ${balance:.2f}")
