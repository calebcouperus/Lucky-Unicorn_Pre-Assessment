"""Component 4 - Game mechanics and looping v1
Based on token generator v4 but hardwired to give donkey
Gives user feedback about rounds played and maintains balance
Test amount set to $5"""


import random

# Main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# Testing loop to generate 5 tokens
while play_again != "X":
    rounds_played += 1  # keep track of rounds
    number = random.randint(6, 36)  # Only gives donkey

    # adjust balance
    # if the number is between 1 and 5
    # User gets unicorn add $4 to balance
    if 1 <= number <= 5:
        token = "Unicorn"
        balance += 4

    # If the number between 6 and 36
    # User gets donkey (Subtract $1 from balance)
    elif 6 <= number <= 36:
        token = "Donkey"
        balance -= 1

    # In all other cases token must be a horse or zebra
    # Subtract $0.50 from balance in either case
    else:
        # If number is even, set token to zebra
        if number % 2 == 0:
            token = "Zebra"
            balance -= 0.5

        # Otherwise set token to horse
        else:
            token = "Horse"
            balance -= 0.5
