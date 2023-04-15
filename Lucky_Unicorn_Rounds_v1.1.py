"""Component 4 - Game mechanics and looping v1.1
Based on token generator v4 but hardwired to give donkey
Gives user feedback about rounds played and maintains balance
Test amount set to $5
Updated v1 to work"""

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

    # Output
    print(f"Round {rounds_played}.\n"
          f"Token: {token}\n"
          f"Balance: ${balance:.2f}\n")

    # breaks loop if out balance = 0
    if balance == 0:
        print("Sorry you ran out of money")
        break

    # Asking to play again
    play_again = input("Do you want to play another round\n"
                       "<enter> to play again or 'X' to exit\n"
                       ">>>").upper()

# Output
print()
print(f"Thankyou for playing\n"
      f"You started with ${TEST_AMOUNT:.2f}\n"
      f"and you leave with ${balance:.2f}\n"
      f"Goodbye")
